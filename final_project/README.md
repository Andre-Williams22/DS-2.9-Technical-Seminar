<p align="center">
<h1>Reinforcement Learning Trading Agent </h1>
<br>
<br>
A tool to automate trading and investing.

Built by: Andre Williams

[Presentation]()
</p>
<p align="center">
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>
<br>

## Project Description
The DRL Agent will be a culmination of several reinforcement learning strategies that learn to analyze, optimize, and execute a real-time trading strategy in the stock market by receiving a series of technical indicators and stock price data. The goal of the project is to successfully automate trading. Its potential value is not only automating trading but taking the human emotions and intuition out of the equation for making intelligent investment decisions. The data set will be from a combination of sources like Yahoo Finance, Alpaca, and Alpha Vantage. 

## Project Scope
This project is attainable within 6 weeks because it's simply a build up and continuation of other smaller projects I've worked on in the past. The learning curve, compute resources, and storage capacity has all been accounted for and will be a continual process as the project scales. 6 weeks is enough time in order to develop an MVP with an end-to-end pipeline.

## Data 
1. [Alpaca Real-Time Market Data](https://alpaca.markets/docs/api-documentation/api-v2/market-data/)
2. [Alpha Vantage Stock Data](https://www.alphavantage.co/documentation/)
3. [Finding most volatile stocks](https://towardsdatascience.com/find-the-highest-moving-hidden-stocks-of-the-day-with-python-aab0d7bfe5ff)


## Research Papers Summary

1. [Deep Reinforcement Learning (Automated Stock Trading)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3690996)
2. [Graph Convolutional Neural Networks](https://www.sciencedirect.com/science/article/abs/pii/S0020025520312342?dgcid=rss_sd_all)
3. [Multiple Stock Trading](https://towardsdatascience.com/finrl-for-quantitative-finance-tutorial-for-multiple-stock-trading-7b00763b7530)
4. [Parallel Stochastic RL Learning Environments](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3690996)
5. [Machine Learning Pipeline](https://ai.plainenglish.io/advances-in-financial-machine-learning-for-dummies-part-0-c08e169335f)
6. [Geometric Brownian Motion](https://towardsdatascience.com/simulating-stock-prices-in-python-using-geometric-brownian-motion-8dfd6e8c6b18)
7. [Monte Carlo Method Stock Simulator with GBM and Bootstrap Sampling](https://towardsdatascience.com/simulating-stock-prices-in-python-using-geometric-brownian-motion-8dfd6e8c6b18)

After extensive research, there appears to be a correlation with using reinforcement learning for handling probabilistic outcomes. Reinforcement learning heavily relies on a Markov Decision Process that helps determine that actions, states, and rewards. This methodology works with both a discrete and continuous time series. Applying reinforcement learning to stock market trend predictions is relevant because it can handle different variables that the stock market entails in a timely manner through its components. In addition to regular reinforcement learning, applying technical indicators and other information of stock data like news and volitility. Other statistical techniques have proven to be proficient in identifying patterns in that which seemed random like the stock market like geometric brownian motion. Brownian Motion was used by Einstein to support his thesis on subatomic particle in pollen moving around in a pattern, concluding that there's an acutal pattern within the randomness and that everything no matter how random has an underlying pattern with respect to its environment. Applying statistical models like GBM, MACD, RSI, and Bollingerbands can help the reinforcement agent to optimize its rewards which is maximizing profit from trades.

This project is simply an intelligent system that can buy and sell stocks using a predefined trading strategy. Once the script is called it will programmatically connect to a trading platform via an API to get access to real-time data. Then the algorithm will buy and sell as well as implement a stop loss. All of this will be done in a fixed amount of time that will end up being how long the script runs. I should also be able to log in to the brokers’ interface and view the algorithm take positions in the market in real-time.


## Project Goals / Implementation Plan
1. Find time series data for multiple stocks 
2. Scan stock markets to find most volatile stocks 
3. Send that data to a database/spreadsheet 
4. Grab that data  
5. Build a Reinforcement Learning Algorithm
6. Train/Test RL Agent on historical data
7. Connect algorithm with real-time data
8. Setup algorithm with a brokerage to take real positions in the market
9. Connect algorithm to a scheduler in GCP
10. Have the Algorithm trade everyday at Market Open and Close
11. Have algorithm send emails, informing me about it's positions
12. Make Money


## 🚀 Getting Started

## Prerequisites
* python3.7
* pip 


## 💻 Local Development

```bash
# clone the repo
git clone https://github.com/Andre-Williams22/DS-2.9-Technical-Seminar.git
```
```bash
# cd into the repo
cd final-project
```
```bash
# create a virtual environment 
python3.7 -m venv venv
```
```bash
# Activate virtual environment 
source venv/bin/activate
```
```bash
# Install the requirements
pip3 install -r requirements.txt
```

```bash
# cd into the program locally
cd trading_agent
```
```bash
# run the program
python3 run_DRL.py
```
```bash
# Only train the model
python3 trade.py
```

## 📝 License

By contributing, you agree that your contributions will be licensed under its MIT License.

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Credit and Acknowledgment

1. https://towardsdatascience.com/finrl-for-quantitative-finance-tutorial-for-multiple-stock-trading-7b00763b7530
1. [Finding most volatile stocks](https://towardsdatascience.com/find-the-highest-moving-hidden-stocks-of-the-day-with-python-aab0d7bfe5ff)


## Contributors

Anyone is welcome to contribute!

<table>
  <tr>
    <td align="center"><a href="https://github.com/Andre-Williams22"><br /><sub><b>Andre Williams</b></sub></a><br /><a href="https://github.com/Andre-Williams22/msconsole/commits?author=Andre-Williams22" title="Code">💻</a></td>
  </tr>
</table>
