#!/usr/bin/env python
from fastapi.testclient import TestClient
import uvicorn
import argparse

from core.api.controller import create_app


def start_mode():
    app = create_app()
    uvicorn.run(app, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    # options
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start',
                        help='start app',
                        action='store_true')
    args = parser.parse_args()

    if args.start:
        start_mode()
