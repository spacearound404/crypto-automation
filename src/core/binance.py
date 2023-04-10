import re
import time
import json
import ccxt
import random
from config import *
from termcolor import cprint
from ccxt.base.errors import InvalidAddress, InvalidOrder, ExchangeError


def binance_withdraw(address_wallet, amount_to_withdraw, symbol_to_withdraw, network, api_key, secret):
    amount = 0.0
    account_binance = ccxt.binance({
        'apiKey': api_key,
        'secret': secret,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

    try:
        account_binance.withdraw(
            code=symbol_to_withdraw,
            amount=amount_to_withdraw,
            address=address_wallet,
            tag=None,
            params={
                "network": network
            }
        )
        cprint(f">>> Успешно | {address_wallet} | {amount_to_withdraw}", "green")
    except ExchangeError as error:
        cprint(f">>> Неудачно | {address_wallet} | ошибка : {error}", "red")