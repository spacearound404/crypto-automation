# Crypto Automation
[![pypi: package](https://img.shields.io/badge/pypi-0.0.4-blue)](https://pypi.org/project/bufflogin/)
[![Python: versions](
https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)]()

Crypto Automation project contains several modules for interaction with crypto.

## Features

- binance: withdrawal from binance to wallets via api key;
- okx: withdrawal from okx to wallets via api key;
- transfer: withdrawal from wallets to other wallets (okx sub-accounts);
- bridge: bridge from any network to any network via Orbiter;
- support list of wallets for all actions;

## Requirements
- Python 3.x.x

## Setup
Setup project, follow these steps:
1. `pip install -r requirements.txt`
2. setup `config.py`
3. setup `actions.json`

### Setup `config.py`
| Param           |                                                               Desc                                                                |
|-----------------|:---------------------------------------------------------------------------------------------------------------------------------:|
| `ERC20_ABI_PATH`  |                                             path to ERC20 ABI json file (depricated)                                              |
| `ACTIONS_PATH`    |                                                    path to actions, json file                                                     |
| `RPCS`            |                                   RPC. To add a new network, follow the general json structure                                    |
| `ORBITER_AMOUNT`  | The code of the network to which Orbiter transfers. Make sure that the code is the same as those described on the Orbiter website | 

### Setup `actions.json`
You can combine these actions, building them into a chain of actions to automate the process. Use the templates below.

> ⚠️ **Warnning!!!**
>
> 1. Name of network corresponds to name of `chain` field in `RPCS` constant, in file `config.py`.
> 2. `token_contract` must be taken from scan site of your network/chain
> 3. `bridge_contract` must be taken from the Orbiter site (another bridge does not fit).
> 4. When using token name in Orbiter and when transfer token from wallet, you must first add ABI of that token to `abi` folder with name of that token, i.e. the name of token in your `actions.json` is the name of ABI file.
> 5. Note that amount specified for Orbiter is `amount` + `X` to compensate for gas in various networks, `X` can be viewed on Orbiter website.
> 6. Note that your API tokens for Binance and OKX, must have permission to withdraw funds.

### Binance templates
```json
  {
    "type": "binance-withdraw",
    "data": {
      "api_key": "",
      "secret": "",
      "token": "USDT",
      "amount": 10,
      "min_amount": 4,
      "max_amount": 10,
      "min_sleep": 3,
      "max_sleep": 6,
      "network": "MATIC",
      "addresses_path": "./data/binance.txt"
    }
  }
```

| Name | Description |
| --- | --- |
| `api_key` | API key from Binance account |
| `secret` | secret from Binance account |
| `token` | token name (see all tokens name from Binance site) |
| `amount` | token amount for withdraw (supported up to two decimal places) |
| `min_amount` | minimum value for generating a random value for withdraw to one wallet |
| `max_amount` | maximum value for generating a random value for withdraw to one wallet |
| `min_sleep` | minimum value for generating a random value for sleep between action |
| `max_sleep` | minimum value for generating a random value for sleep between action |
| `network` | network name from Binance site |
| `addresses_path` | path to file with list of addresses (each address must start on a new line) |

### OKX templates
```json
  {
    "type": "okx-withdraw",
    "data": {
      "min_sleep": 1,
      "max_sleep": 3,
      "api_key": "",
      "secret": "",
      "password": "",
      "token": "USDT",
      "amount": 10,
      "min_amount": 3,
      "max_amount": 10,
      "network": "MATIC",
      "min_fee": "1",
      "max_fee": "1",
      "addresses_path": "./data/okx.txt",
      "proxies": {
            "http": "",
            "https": ""
      }
    }
  }
```

| Name | Description                                                                        |
| --- |------------------------------------------------------------------------------------|
| api_key | API key from OKX account                                                           |
| secret | secret from OKX account                                                            |
| password | password from API key                                                              |
| token | token name (see all tokens name from OKX site)                                     |
| amount | token amount for withdraw (supported up to two decimal places)                     |
| min_amount | minimum value for generating a random value for withdraw to one wallet             |
| max_amount | maximum value for generating a random value for withdraw to one wallet             |
| min_sleep | minimum value for generating a random value for sleep between action               |
| max_sleep | minimum value for generating a random value for sleep between action               |
| network | network name from OKX site                                                         |
| addresses_path | path to file with list of addresses (each address must start on a new line)        |
| min_fee | minimum value for generating a random value for fee                                |
| max_fee | maximum value for generating a random value for fee                                |
| proxies | structure: `{"http": "http://host:port", "https": "http://user:password@host:port"}` |

### Metamask transfer templates
```json
  {
    "type": "mm-withdraw",
    "data": {
      "token": "USDT",
      "amount": 100,
      "min_amount": 10,
      "max_amount": 20,
      "min_sleep": 3,
      "max_sleep": 10,
      "network": "MATIC",
      "private_key": "",
      "token_contract": "0xc2132D05D31c914a87C6611C10748AEb04B58e8F",
      "addresses_path": "./data/transfer.txt"
    }
  }
```

| Name | Description |
| --- | --- |
| `token` | token name (see `/abi` folder) |
| `amount` | token amount for withdraw (supported up to two decimal places) |
| `min_amount` | minimum value for generating a random value for withdraw to one wallet |
| `max_amount` | maximum value for generating a random value for withdraw to one wallet |
| `min_sleep` | minimum value for generating a random value for sleep between action |
| `max_sleep` | minimum value for generating a random value for sleep between action |
| `network` | network name (see `config.py` and get network name from) |
| `private_key` | private key of wallet |
| `token_contract` | token address in network |
| `addresses_path` | path to file with list of addresses (each address must start on a new line) |

### Orbiter bridge templates
```json
  {
    "type": "orbiter-bridging",
    "data": {
      "private_keys_path": "./data/bridge.txt",
      "from_chain": "MATIC",
      "to_chain": "ARBITRUM",
      "amount": "20%",
      "min_sleep": 4,
      "max_sleep": 10,
      "token": "USDT",
      "token_contract": "0xc2132D05D31c914a87C6611C10748AEb04B58e8F",
      "bridge_contract": "0xd7aa9ba6caac7b0436c91396f22ca5a7f31664fc"
    }
  }
```

| Name | Description |
| --- | --- |
| `token` | token name (see `/abi` folder) |
| `amount` | token amount for withdraw in percentage (supported up to two decimal places). Example: `1%`, `15.6%`, `19,3 %` |
| `private_keys_path` | path to file with list of private keys from wallets (each pk must start on a new line) |
| `min_sleep` | minimum value for generating a random value for sleep between action |
| `max_sleep` | minimum value for generating a random value for sleep between action |
| `from_chain` | network name (see `config.py` and get network name from) |
| `to_chain` | network name (see `config.py` and get network name from) |
| `token_contract` | token address in network |
| `bridge_contract` | bridge contract address of Orbiter |

## Run
To run the project, use the command:

`python main.py`
