from flask import Flask, jsonify
import requests
import pandas as pd
import time

app = Flask(__name__)

@app.route('/api/index')
def get_gold():
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=10).json()
        price = float(r['price'])
        
        # SL dan TP sesuai selera kamu tadi
        return jsonify({
            "price": f"{price:.2f}",
            "signal": "STRONG BUY" if price < 4585 else "STRONG SELL",
            "sl": f"{price - 1.20:.2f}",
            "tp": f"{price + 2.50:.2f}",
            "time": time.strftime("%H:%M:%S")
        })
    except:
        return jsonify({"price": "0.00", "signal": "WAIT"}), 500
