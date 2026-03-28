# Trading Bot (Binance Futures Testnet)

## Features
- MARKET & LIMIT orders
- BUY / SELL support
- CLI based input
- Logging & error handling

## Setup
pip install -r requirements.txt

Create .env file:
API_KEY=your_key
API_SECRET=your_secret
BASE_URL=https://testnet.binancefuture.com

## Run

Market order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000
