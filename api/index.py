<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>AI SIGNALFX</title>
    <style>
        body { background: #0b0e14; color: #e6edf3; font-family: 'Segoe UI', sans-serif; margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh; width: 100vw; overflow: hidden; }
        .container { background: #161b22; border: 1px solid #30363d; border-radius: 20px; padding: 40px 20px; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: space-around; align-items: center; box-sizing: border-box; }
        h1 { font-size: 1.8rem; color: #8b949e; margin: 0; text-transform: uppercase; letter-spacing: 4px; font-weight: bold; }
        .price { font-size: 5.5rem; font-weight: 900; margin: 10px 0; color: #58a6ff; text-shadow: 0 0 30px rgba(88,166,255,0.4); font-family: 'Courier New', monospace; }
        .signal-box { width: 90%; padding: 25px; border-radius: 15px; font-weight: 800; font-size: 2.2rem; text-align: center; transition: 0.5s; background: #30363d; box-shadow: inset 0 0 10px rgba(0,0,0,0.5); }
        .buy { background: #238636 !important; color: white; box-shadow: 0 0 30px rgba(35, 134, 54, 0.6); }
        .sell { background: #da3633 !important; color: white; box-shadow: 0 0 30px rgba(218, 54, 51, 0.6); }
        .details { width: 90%; display: flex; justify-content: space-between; border-top: 2px solid #30363d; padding-top: 25px; font-size: 1.2rem; font-weight: bold; }
        .time { color: #8b949e; font-size: 1.1rem; background: rgba(255,255,255,0.05); padding: 5px 15px; border-radius: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>AI SIGNALFX</h1>
        <div class="time" id="time">Menghubungkan...</div>
        <div class="price" id="price">...</div>
        <div id="signal" class="signal-box">SCANNING</div>
        <div class="details">
            <div>SL: <span id="sl" style="color: #ff7b72;">0</span></div>
            <div>TP: <span id="tp" style="color: #3fb950;">0</span></div>
        </div>
    </div>
    <script>
        async function getSignal() {
            try {
                // Mencoba ambil data dari API
                const r = await fetch('/api/index');
                if (!r.ok) throw new Error();
                const d = await r.json();
                
                document.getElementById('price').innerText = d.price || "0.00";
                document.getElementById('time').innerText = (d.time || "--:--") + " WIB";
                document.getElementById('sl').innerText = d.sl || "0";
                document.getElementById('tp').innerText = d.tp || "0";
                
                const s = document.getElementById('signal');
                s.innerText = d.signal || "SCANNING";
                
                if (String(d.signal).includes('BUY')) {
                    s.className = 'signal-box buy';
                } else if (String(d.signal).includes('SELL')) {
                    s.className = 'signal-box sell';
                }
            } catch (e) {
                document.getElementById('price').innerText = "RECONNECT";
                console.log("Koneksi gagal...");
            }
        }
        setInterval(getSignal, 2000);
        getSignal();
    </script>
</body>
</html>
