from ib_insync import *
from numpy import *
import yfinance as yf
import pandas as pd 

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=11)

#Stock contract and ticker.
contract = Stock('AMD', 'SMART', 'USD')
stock = yf.Ticker('AMD')

#vars
nextOperation = True #True = buy, False = sell
#Buys the asset if its price decreased by more than the threshold.
dipThreshold = - 5
#Buys the asset if its price increased by more than the threshold.
upTrendThreshold = 10
#Sells the asset if its price has increased above the threshold since bought.
profitThreshold = 5
#Failsafe to stop major loses.
stopLossThreshold = 10
#Returns current price
stockCurrentPrice = stock.info["regularMarketPrice"]
#last 30 days historical price.
stockHistorical = stock.history(period='7d', interval='1d')
#High and Low average historical price.
openMean = stockHistorical['Open'].mean()
closeMean = stockHistorical['Close'].mean()
#Average of high and low historical price.
averageMean = (openMean+closeMean)/2
#Info to place buy order.
buyOrder = LimitOrder('BUY', 1, (stockCurrentPrice + dipThreshold)) #!!PUT MORE INFO!!
#Info to place sell order.
sellOrder = LimitOrder('SELL', 1, 5) #!!PUT MORE INFO!!
#Returns account Balance as a string.
accountBalanceString = ib.accountSummary()
for a in accountBalanceString:
	if a.tag=="CashBalance":
		accountBalanceString = (a.value)
#Converts accountBalanceString to a double.
accountBalance = double(accountBalanceString)
#funcs
def placeBuyOrder():
    print #!!EXAMPLE!!
def placeSellOrder():
    print #!!EXAMPLE!!

print(10 + dipThreshold)