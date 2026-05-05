from flask import Flask, jsonify
import requests
import pandas as pd
import time

app = Flask(__name__)

# ... (kode fetch_data kamu tetap sama) ...

@app.route('/api/index')
def home():
    # ... (kode logika signal kamu tetap sama) ...
    return jsonify({
        "price": "2300.00", # Contoh
        "signal": "NEUTRAL",
        "time": time.strftime('%H:%M:%S')
    })

# TAMBAHKAN INI DI PALING BAWAH:
if __name__ == '__main__':
    app.run()
