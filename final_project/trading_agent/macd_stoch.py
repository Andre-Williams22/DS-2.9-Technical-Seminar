
import requests
import os
import json
import pandas as pd
import alpaca_trade_api as tradeapi
import time
from datetime import datetime

#Alpaca Trade API 
#change this based on the path on your local machine
endpoint = "https://data.alpaca.markets/v1"
headers = json.loads(open("account.json",'r').read())
api = tradeapi.REST(headers["APCA-API-KEY-ID"], headers["APCA-API-SECRET-KEY"], base_url='https://paper-api.alpaca.markets')
max_pos = 10000 #max position size for each ticker
stoch_signal = {}

## get account info
account = api.get_account()

# google sheets stock api 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build 
from google.auth.transport.requests import Request
from googleapiclient import discovery
from google.oauth2.service_account import Credentials

# Google Sheets Authentication 
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

def hist_data(symbols, timeframe="15Min", limit=200, start="", end="", after="", until=""):
    """
    returns historical bar data for a string of symbols separated by comma
    symbols should be in a string format separated by comma e.g. symbols = "MSFT,AMZN,GOOG"
    """
    df_data = {}
    bar_url = endpoint + "/bars/{}".format(timeframe)
    params = {"symbols" : symbols,
              "limit" : limit,
              "start" : start,
              "end" : end,
              "after" : after,
              "until" : until}
    r = requests.get(bar_url, headers = headers, params = params)
    json_dump = r.json()
    for symbol in json_dump:
        temp = pd.DataFrame(json_dump[symbol])
        temp.rename({"t":"time","o":"open","h":"high","l":"low","c":"close","v":"volume"},axis=1, inplace=True)
        temp["time"] = pd.to_datetime(temp["time"], unit="s")
        temp.set_index("time",inplace=True)
        temp.index = temp.index.tz_localize("UTC").tz_convert("America/Indiana/Petersburg")
        temp.between_time('09:31', '16:00')
        df_data[symbol] = temp
    return df_data


def grabs_daily_volatile_stocks():
    '''grabs daily most volatile stocks and puts them in a list'''
    tickers = []

    client = gspread.authorize(creds)

    # Open the spreadhseet and grabs first sheet
    sheet = client.open("Daily_Volatile_Stocks").sheet1 #worksheet('Sheet1')   
    # Get a list of all records
    data = sheet.get_all_records() 
    # grab specific row 
    row = sheet.row_values(3)
    # grab tickers column 
    stocks = sheet.col_values(2)
    
    for ticker in stocks:
        
        tickers.append(ticker)
        tickers.append(',')
        
    tickers = tickers[2:-1]
    # tickers = tickers[-1]
    string = "".join(str(x) for x in tickers)
    
    return string


def MACD(df_dict, a=12 ,b=26, c=9):
    """function to calculate MACD
       typical values a(fast moving average) = 12; 
                      b(slow moving average) =26; 
                      c(signal line ma window) =9"""
    for df in df_dict:
        df_dict[df]["ma_fast"] = df_dict[df]["close"].ewm(span=a, min_periods=a).mean()
        df_dict[df]["ma_slow"] = df_dict[df]["close"].ewm(span=b, min_periods=b).mean()
        df_dict[df]["macd"] = df_dict[df]["ma_fast"] - df_dict[df]["ma_slow"]
        df_dict[df]["signal"] = df_dict[df]["macd"].ewm(span=c, min_periods=c).mean()
        df_dict[df].drop(["ma_fast","ma_slow"], axis=1, inplace=True)

def stochastic(df_dict, lookback=14, k=3, d=3):
    """function to calculate Stochastic Oscillator
       lookback = lookback period
       k and d = moving average window for %K and %D"""
    for df in df_dict:
        df_dict[df]["HH"] = df_dict[df]["high"].rolling(lookback).max()
        df_dict[df]["LL"] = df_dict[df]["low"].rolling(lookback).min()
        df_dict[df]["%K"] = (100 * (df_dict[df]["close"] - df_dict[df]["LL"])/(df_dict[df]["HH"]-df_dict[df]["LL"])).rolling(k).mean()
        df_dict[df]["%D"] = df_dict[df]["%K"].rolling(d).mean()
        df_dict[df].drop(["HH","LL"], axis=1, inplace=True)

def trade(tickers):
    '''makes the actual trades '''
    global stoch_signal

    historicalData = hist_data(tickers,"15Min")
    MACD(historicalData)
    stochastic(historicalData)
    positions = api.list_positions()
    
    for ticker in tickers.split(","):
        print(ticker)
        historicalData[ticker].dropna(inplace=True)
        existing_pos = False
        
        if historicalData[ticker]["%K"][-1] < 20:
            stoch_signal[ticker] = "oversold"
        elif historicalData[ticker]["%K"][-1] > 80:
            stoch_signal[ticker] = "overbought"
        
        for position in positions:
            if len(positions) > 0:
                if position.symbol == ticker and position.qty !=0:
                    print("existing position of {} stocks in {}...skipping".format(position.qty, ticker))
                    existing_pos = True
        
        if historicalData[ticker]["macd"].iloc[-1]> historicalData[ticker]["signal"].iloc[-1] and \
            historicalData[ticker]["macd"].iloc[-2]< historicalData[ticker]["signal"].iloc[-2] and \
            stoch_signal[ticker]=="oversold" and existing_pos == False:
                api.submit_order(ticker, max(1,int(max_pos/historicalData[ticker]["close"].iloc[-1])), "buy", "market", "ioc")
                print("bought {} stocks in {}".format(int(max_pos/historicalData[ticker]["close"].iloc[-1]),ticker))
                time.sleep(2)
                try:
                    filled_qty = api.get_position(ticker).qty
                    time.sleep(1)
                    api.submit_order(ticker, int(filled_qty), "sell", "trailing_stop", "day", trail_percent = "1.5")
                except Exception as e:
                    print(ticker, e)
    

if __name__ == '__main__':
    
    
    aapl_asset = api.get_asset('AAPL')
    if aapl_asset.tradable:
        print('We can trade AAPL.')
        
    tickers = grabs_daily_volatile_stocks()
        
    for ticker in tickers.split(','):
        stoch_signal[ticker] = ""

    # Check if the market is open now.
    clock = api.get_clock()
    # print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

    if clock.is_open:
        starttime = time.time()
        timeout = starttime + 60*60*7
        while time.time() <= timeout:
            print("starting iteration at {}".format(time.strftime("%Y-%m-%d %H:%M:%S")))
            trade(tickers)
            time.sleep(900 - ((time.time() - starttime) % 900)) 
        
    # else:
        
    #     print('market is closed')
    # print(stoch_signal)
    
    print(datetime.today().strftime('%Y-%m-%d'))
    
    open_orders_list = api.list_orders(status='open')
    # print(open_orders_list)
    
    api.close_all_positions()
    
    print('Balance ',account.equity)
    
    balance_change = float(account.equity) - float(account.last_equity)
    
    print('Daily Balance Change ',balance_change )
    
    print('Money available to make trades: ',account.buying_power)
    api.close_all_positions()
    
    
