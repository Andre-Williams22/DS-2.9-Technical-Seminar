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

## 🚀 Getting Started

## Prerequisites
* python3.7

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
python3 trade.py
```
```bash
# Only train the model
python3 run_DRL.py
```

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
  <tr>
    <td align="center"><a href="https://github.com/liyaSileshi"><br /><sub><b>Liya Tilahun</b></sub></a><br /><a title="Code">👩🏽‍💻</a></td>
  </tr>
    <tr>
    <td align="center"><a href="#"><br /><sub><b>Jerome Schmidt</b></sub></a><br /><a title="Code">💻</a></td>
  </tr>
</table>
