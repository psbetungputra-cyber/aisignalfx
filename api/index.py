from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/index')
def get_gold():
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=5).json()
        p = float(r['price'])
        return jsonify({
            "price": f"{p:.2f}",
            "signal": "BUY" if p < 4580 else "SELL",
            "sl": f"{p-2:.2f}",
            "tp": f"{p+2:.2f}",
            "time": "LIVE"
        })
    except:
        return jsonify({"error": "koneksi gagal"}), 500

# Penting: Baris ini jangan dihapus
if __name__ == "__main__":
    app.run()
