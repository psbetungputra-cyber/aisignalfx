from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/api/index')
def get_gold():
    try:
        # Ambil harga asli
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=10).json()
        p = float(r['price'])
        
        # Rumus manual (Tanpa Pandas biar enteng)
        return jsonify({
            "price": f"{p:.2f}",
            "signal": "STRONG BUY" if p < 4585 else "STRONG SELL",
            "sl": f"{p - 1.50:.2f}",
            "tp": f"{p + 2.50:.2f}",
            "time": time.strftime("%H:%M:%S")
        })
    except Exception as e:
        return jsonify({"price": "Error", "signal": "Wait"}), 500
