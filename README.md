# CoinbaseProCryptoBuyingBot
Script that will buy Bitcoin or any other Crypto on Coinbase Pro as soon as there is a Fiat balance available.

## Installation
Make sure pip and python3 is installed.
Install the needed requirements by doing:
```
pip install -r requirements.txt
```

## Configuration
Copy config.ini.example to config.ini.
Edit the config.ini file with your own API details, fiat and crypto currencies.
The configuration is set so the script will check every hour (3600 seconds).
Fee is set to 0.2% so there is always enough left to cover the fees.

## Running the script
Simply run:
```
python3 main.py
```
