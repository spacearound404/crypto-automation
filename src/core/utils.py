import time
import json
import random
import decimal
import requests
from config import *
from web3 import Web3
from tqdm import tqdm
from decimal import Decimal
from termcolor import cprint
from tabulate import tabulate


def int_to_decimal(qty, decimal):
    return int(qty * int("".join(["1"] + ["0"] * decimal)))


def decimal_to_int(qty, decimal):
    return qty / int("".join((["1"] + ["0"] * decimal)))


def prices():
    currency_price = []
    response = requests.get(url=f'https://api.gateio.ws/api/v4/spot/tickers')
    currency_price.append(response.json())
    return currency_price


def price_token(currency_price, symbol):
    price = 0

    try:
        for currency in currency_price[0]:
            if currency['currency_pair'] == f'{symbol}_USDT':
                price = currency['last']

        if symbol in ['USDC', 'USDT', 'DAI', 'BUSD']:
            price = 1
    except Exception as e:
        pass
    return price


def check_balance(private_key, rpc_chain, symbol_chain, min_balance):
    try:
        web3 = Web3(Web3.HTTPProvider(rpc_chain))
        account = web3.eth.account.from_key(private_key)
        balance = web3.eth.get_balance(web3.to_checksum_address(account.address))

        humanReadable = web3.from_wei(balance, 'ether')

        try:
            # check price of token
            currency_price = prices()
            for currency in currency_price[0]:
                if currency['currency_pair'] == f'{symbol_chain}_USDT':
                    price_ = Decimal(currency['last'])
                    price = price_ + price_ * Decimal(0.2)
        except:
            price = 300

        gas = web3.eth.gas_price
        gasPrice = decimal_to_int(gas, 18)

        return round(Decimal(humanReadable) - Decimal(Decimal(gasPrice) * Decimal(price)) - Decimal(min_balance), 7)


    except Exception as error:
        # cprint(f'error : {error}', 'yellow')
        pass


def check_token_balance(private_key, rpc_chain, address_contract, min_balance):
    try:
        web3 = Web3(Web3.HTTPProvider(rpc_chain))
        account = web3.eth.account.from_key(private_key)
        wallet = account.address
        token_contract = web3.eth.contract(address=web3.to_checksum_address(address_contract), abi=ERC20_ABI)
        token_balance = token_contract.functions.balanceOf(web3.to_checksum_address(wallet)).call()

        token_decimal = token_contract.functions.decimals().call()

        humanReadable = decimal_to_int(token_balance, token_decimal)

        # cprint(f'\nbalance : {round(humanReadable, 5)} {symbol}', 'white')

        return round(Decimal(humanReadable) - Decimal(min_balance), 7)

    except Exception as error:
        # cprint(f'error : {error}', 'yellow')
        pass


def check_rpc(chain):
    for elem in RPCS:
        if elem['chain'] == chain:
            RPC = elem['rpc']
            chainId = elem['chain_id']
            scan = elem['scan']
            token = elem['token']

            return {
                'rpc': RPC, 'chain_id': chainId, 'scan': scan, 'token': token
            }

def get_abi(token_name):
    token_abi = {}

    with open(f'./abi/{token_name.lower()}.json', 'r') as file:
        token_abi = json.load(file)

    return token_abi


def distribute_funds(addresses, total_amount, min_amount, max_amount):
    """
    Функция распределения средств между адресами.
    :param addresses: Список адресов
    :param total_amount: Общее количество средств, которые нужно распределить
    :param min_amount: Минимальное значение средств для адреса
    :param max_amount: Максимальное значение средств для адреса
    :return: Словарь с распределенными суммами для каждого адреса
    """
    n = len(addresses)
    partial_totals = [0] * n
    for i in range(n - 1):
        partial_totals[i] = random.randint(min_amount, max_amount)
    partial_totals[n - 1] = total_amount - sum(partial_totals)

    if partial_totals[n - 1] < min_amount:
        return distribute_funds(addresses, total_amount, min_amount, max_amount)

    return dict(zip(addresses, partial_totals))