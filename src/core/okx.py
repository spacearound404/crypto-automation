import re
import time
import json
import ccxt
import random
import requests
from config import *
from termcolor import cprint
from ccxt.base.errors import InvalidAddress, InvalidOrder, ExchangeError


def okx_withdraw(address_wallet, amount_to_withdraw, fee, symbol_to_withdraw, network, api_key, secret, password, proxies):
    amount = 0.0
    account_okx = ccxt.okx({
        'apiKey': api_key,
        'secret': secret,
        'password': password,
        'proxies': proxies,
        'enableRateLimit': True,
        'options': {}
    })

    try:
        account_okx.withdraw(
            code=symbol_to_withdraw,
            amount=amount_to_withdraw,
            address=address_wallet,
            tag=None,
            params={
                'network': network,
                'chainName': network,
                'fee': fee,
                'password': password
            }
        )
        cprint(f">>> Успешно | {address_wallet} | {amount_to_withdraw}", "green")
    except ExchangeError as error:
        cprint(f">>> Неудачно | {address_wallet} | ошибка : {error}", "red")



