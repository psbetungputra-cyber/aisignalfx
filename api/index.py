from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/api/index')
def get_gold():
    try:
        # Ambil harga PAXG/USDT (Emas) real-time
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=5).json()
        price = float(r['price'])
        
        # Logika signal simpel (Sesuaikan sesukamu Mang)
        return jsonify({
            "price": f"{price:.2f}",
            "signal": "STRONG BUY" if price < 4590 else "STRONG SELL",
            "sl": f"{price - 1.50:.2f}",
            "tp": f"{price + 2.50:.2f}",
            "time": time.strftime("%H:%M:%S")
        })
    except:
        return jsonify({"price": "Error", "signal": "Wait"}), 500
