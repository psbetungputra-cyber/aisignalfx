from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/api/index')
def gold_data():
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=5)
        price = float(r.json()['price'])
        return jsonify({
            "price": f"{price:.2f}",
            "signal": "STRONG BUY" if price < 4575 else "STRONG SELL",
            "sl": f"{price - 1.50:.2f}",
            "tp": f"{price + 2.50:.2f}",
            "time": time.strftime("%H:%M:%S")
        })
    except:
        return jsonify({"price": "0.00", "signal": "ERROR"}), 500
