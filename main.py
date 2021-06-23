#!/usr/bin/env python
import uvicorn
import argparse

from core.config import api_config
from core.api.controller import create_app


def start_mode():
    app = create_app()
    uvicorn.run(app, host=api_config.HOST, port=api_config.PORT)


if __name__ == '__main__':
    # options
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start',
                        help='start app',
                        action='store_true')
    args = parser.parse_args()

    if args.start:
        start_mode()
