from flask import Flask, jsonify
from flask_cors import CORS
import requests
import pandas as pd
import time

app = Flask(__name__)
CORS(app)

def fetch_data():
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Mengambil data Gold (PAXG)
    url = "https://query1.finance.yahoo.com/v8/finance/chart/PAXG-USD?interval=1m&range=1d"
    try:
        r = requests.get(url, headers=headers, timeout=10).json()
        prices = r['chart']['result'][0]['indicators']['quote'][0]['close']
        return pd.Series(prices).ffill()
    except:
        return None

@app.route('/api/index')
def home():
    df = fetch_data()
    if df is None:
        return jsonify({"error": "Data Offline"})
    
    # Logika Hitung Harga & Signal
    last_price = df.iloc[-1] + 6.45
    ma = df.rolling(window=10).mean().iloc[-1] + 6.45
    
    signal = "STRONG BUY" if last_price > ma else "STRONG SELL"
    
    return jsonify({
        "price": f"{last_price:.2f}",
        "signal": signal,
        "sl": f"{(last_price - 1.2 if signal == 'STRONG BUY' else last_price + 1.2):.2f}",
        "tp": f"{(last_price + 2.5 if signal == 'STRONG BUY' else last_price - 2.5):.2f}",
        "time": time.strftime('%H:%M:%S')
    })

# Bagian ini wajib untuk Vercel
app = app

if __name__ == '__main__':
    app.run()
