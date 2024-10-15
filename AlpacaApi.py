from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from dotenv import load_dotenv
import os
import json
load_dotenv()

# Api key setup
ALPACA_API_KEY = os.environ['ALPACA_API_KEY']
ALPACA_API_SECRET_KEY = os.environ['ALPACA_API_SECRET_KEY']

trading_client = TradingClient(ALPACA_API_KEY, ALPACA_API_SECRET_KEY, paper=True)

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))



# class alpaca_api:
    # Get live market news
    # Get live stock price
    # Get historical stock data
    # Get stock data like P/E ratio
    # Get account status

# https://biztoc.com/