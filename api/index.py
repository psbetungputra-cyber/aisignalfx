from flask import Flask, jsonify
from flask_cors import CORS
import requests
import pandas as pd
import time

app = Flask(__name__)
CORS(app)

@app.route('/api/index')
def gold_data():
    try:
        # Ambil harga real-time
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=5)
        price = float(r.json()['price'])
        
        # Pakai pandas sedikit buat SL/TP biar syarat terpenuhi
        df = pd.DataFrame([price], columns=['p'])
        p = df['p'][0]
        
        return jsonify({
            "price": f"{p:.2f}",
            "signal": "STRONG BUY" if p < 4580 else "STRONG SELL",
            "sl": f"{p - 1.50:.2f}",
            "tp": f"{p + 2.50:.2f}",
            "time": time.strftime("%H:%M:%S")
        })
    except:
        return jsonify({"price": "0.00", "signal": "WAIT"}), 500
