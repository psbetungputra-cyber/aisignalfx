from flask import Flask, jsonify
import requests
import pandas as pd
import time

app = Flask(__name__)

@app.route('/api/index')
def get_gold():
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=5).json()
        price = float(r['price'])
        
        # Pakai pandas yang tadi kamu bilang bagus
        df = pd.DataFrame([price], columns=['p'])
        p = df['p'][0]
        
        return jsonify({
            "price": f"{p:.2f}",
            "signal": "STRONG BUY" if p < 4585 else "STRONG SELL",
            "sl": f"{p - 1.50:.2f}",
            "tp": f"{p + 2.50:.2f}",
            "time": time.strftime("%H:%M:%S")
        })
    except:
        return jsonify({"price": "0.00", "signal": "WAIT"}), 500
