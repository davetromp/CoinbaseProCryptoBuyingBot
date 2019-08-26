#!/usr/bin/python3
# coding=utf-8

import datetime
from time import sleep
import configparser
import ccxt

config = configparser.ConfigParser()
config.read('config.ini')
secret = config['coinbasepro']['secret']
api_key = config['coinbasepro']['api_key']
password = config['coinbasepro']['password']
fiat = config['coinbasepro']['fiat']
crypto = config['coinbasepro']['crypto']
ticker = '{}/{}'.format(crypto, fiat)
fee = float(config['coinbasepro']['fee'])
delay = int(config['coinbasepro']['delay'])
withdraw = bool(config['coinbasepro']['withdraw'])
withdrawThreshold = float(config['coinbasepro']['withdrawThreshold'])
toAddress = config['coinbasepro']['toAddress']

coinbasepro = ccxt.coinbasepro({
    'apiKey': api_key,
    'secret': secret,
    'password': password
})

def main():
    try:
        while True:
            fiat_balance = float(coinbasepro.fetch_balance()[fiat]['free'])
            print("#####################")
            print(datetime.datetime.now())
            print("Current fiat ({}) balance is {}.".format(fiat, fiat_balance))
            if fiat_balance > 0:
                rate = float(coinbasepro.fetch_ticker(ticker)['ask'])
                ordersize = (fiat_balance / rate) * (1.0 - fee)
                print("Placing a market buy order.\nOrdersize: {}\nTicker: {}\nCurrent price: {}".format(ordersize, ticker, rate))
                try:
                    coinbasepro.create_market_buy_order(ticker, ordersize)
                except Exception as e:
                    print(e)
            crypto_balance = float(coinbasepro.fetch_balance()[crypto]['free'])
            if crypto_balance > withdrawThreshold and withdraw == True:
                print("Sending {} of {} to {}.".format(crypto_balance, crypto, toAddress))
                coinbasepro.withdraw(crypto, crypto_balance, toAddress, tag=None, params={})
            print("#####################")
            sleep(delay)
    except KeyboardInterrupt:
        print("\nCancelled by user")


if __name__ == '__main__':
    main()
