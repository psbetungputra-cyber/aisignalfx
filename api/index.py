from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/api/index')
def get_data():
    try:
        res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT").json()
        p = float(res['price'])
        return jsonify({
            "price": f"{p:.2f}",
            "signal": "STRONG BUY" if p < 4565 else "STRONG SELL",
            "sl": f"{p - 2:.2f}",
            "tp": f"{p + 3:.2f}",
            "time": time.strftime("%H:%M:%S")
        })
    except:
        return jsonify({"price": "Error", "signal": "Wait"}), 500
