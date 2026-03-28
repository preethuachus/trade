import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger
import logging

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_side(args.side)
    validate_order_type(args.type)

    print("Order Summary:")
    print(vars(args))

  
    if args.type == "MARKET":
        result = place_market_order(args.symbol, args.side, args.quantity)
    else:
        if not args.price:
            raise ValueError("Price required for LIMIT order")
        result = place_limit_order(args.symbol, args.side, args.quantity, args.price)

   
    print("FULL RESPONSE:", result)

    
    if not result or "orderId" not in result:
        print("Order Failed:", result)
        logging.error(result)
    else:
        print("Order Success")
        print("Order ID:", result.get("orderId"))
        print("Status:", result.get("status"))
        print("Executed Qty:", result.get("executedQty"))
        print("Avg Price:", result.get("avgPrice"))

        logging.info(result)

except Exception as e:
    print("Error:", str(e))
    logging.error(str(e))