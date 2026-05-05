from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/api/index')
def gold():
    try:
        # Ambil harga asli dari Binance
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=5).json()
        p = float(r['price'])
        return jsonify({
            "price": f"{p:.2f}",
            "signal": "BUY" if p < 4580 else "SELL",
            "sl": f"{p - 1.50:.2f}",
            "tp": f"{p + 2.50:.2f}",
            "time": time.strftime("%H:%M:%S")
        })
    except:
        return jsonify({"price": "OFFLINE", "signal": "WAIT"}), 500
