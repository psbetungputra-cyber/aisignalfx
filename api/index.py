from flask import Flask, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

@app.route('/api/ind')
@app.route('/api/index')
def get_gold_data():
    try:
        # Mengambil data harga emas real-time (PAXG/USDT)
        url = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
        res = requests.get(url).json()
        price = float(res['price'])
        
        # Logika Signal Sederhana
        signal = "STRONG BUY" if price < 4560 else "STRONG SELL"
        
        return jsonify({
            "price": f"{price:.2f}",
            "signal": signal,
            "sl": f"{price - 1.5:.2f}",
            "tp": f"{price + 2.5:.2f}",
            "time": time.strftime("%H:%M:%S")
        })
    except:
        return jsonify({"error": "Gagal ambil data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
