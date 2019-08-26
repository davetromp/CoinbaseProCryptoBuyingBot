# CoinbaseProCryptoBuyingBot
This script will buy Bitcoin or any other Crypto on Coinbase Pro as soon as there is a Fiat balance available.

## Installation
Make sure pip and python3 is installed.
Install the needed requirements by doing:
```
pip install -r requirements.txt
```

## Configuration
Copy config.ini.example to config.ini.
```
cp config.ini.example config.ini
```
Edit the config.ini file with your own API details, fiat currency and cryptocurrency.
```
nano config.ini
```
The configuration is set so the script will check every hour (3600 seconds).
Fee is set to 0.25% so there is always enough left to cover the fees, but you can change it as you see fit.

### Withdraw option
There is the option to automatically withdraw to a wallet address once your crypto holdings reach a certain threshold. By default this option is switched off. You can switch it on by setting withdraw to True.
Also be sure to set the threshold. Default is 0.0.
Be sure to have transfers enabled in the permission settings of your API.

## Running the script
Simply run:
```
python3 main.py
```
