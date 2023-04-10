from config import *
from src.handler.okx import *
from src.handler.binance import *
from src.handler.bridges import *
from src.handler.transfer import *


def main():
    action_handler_mapping = {
        'okx-withdraw': okx_handler,
        'binance-withdraw': binance_handler,
        'orbiter-bridging': bridge_orbiter_handler,
        'mm-withdraw': transfer_tokens_handler
    }

    for action in ACTIONS:
        action_type = action['type']
        action_data = action['data']

        action_handler_mapping[action_type](action_data)


if __name__ == "__main__":
    main()


