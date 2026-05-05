<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>AI SIGNALFX</title>
    <style>
        body { background: #0b0e14; color: #e6edf3; font-family: sans-serif; margin: 0; height: 100vh; width: 100vw; display: flex; justify-content: center; align-items: center; overflow: hidden; }
        .container { background: #161b22; border: 2px solid #30363d; border-radius: 25px; width: 95%; height: 95%; display: flex; flex-direction: column; justify-content: space-around; align-items: center; box-sizing: border-box; padding: 20px; }
        h1 { font-size: 2rem; color: #8b949e; margin: 0; letter-spacing: 5px; }
        .price { font-size: 5rem; font-weight: bold; color: #58a6ff; text-shadow: 0 0 20px rgba(88,166,255,0.5); margin: 0; }
        .signal-box { width: 90%; padding: 30px 10px; border-radius: 20px; font-weight: 900; font-size: 2.5rem; text-align: center; background: #30363d; }
        .buy { background: #238636 !important; box-shadow: 0 0 30px #238636; }
        .sell { background: #da3633 !important; box-shadow: 0 0 30px #da3633; }
        .details { width: 85%; display: flex; justify-content: space-between; border-top: 2px solid #30363d; padding-top: 20px; font-size: 1.5rem; }
        .time { font-size: 1.2rem; color: #8b949e; }
    </style>
</head>
<body>
    <div class="container">
        <h1>AI SIGNALFX</h1>
        <div class="time" id="time">LOADING...</div>
        <div class="price" id="price">0.00</div>
        <div id="signal" class="signal-box">SCANNING</div>
        <div class="details">
            <div style="color: #ff7b72;">SL: <span id="sl">0</span></div>
            <div style="color: #3fb950;">TP: <span id="tp">0</span></div>
        </div>
    </div>
    <script>
        async function loadData() {
            try {
                const res = await fetch('/api/index');
                const d = await res.json();
                document.getElementById('price').innerText = d.price || "0.00";
                document.getElementById('time').innerText = (d.time || "--:--") + " WIB";
                document.getElementById('sl').innerText = d.sl || "0";
                document.getElementById('tp').innerText = d.tp || "0";
                const s = document.getElementById('signal');
                s.innerText = d.signal || "WAIT";
                s.className = 'signal-box ' + (String(d.signal).includes('BUY') ? 'buy' : 'sell');
            } catch (e) {
                document.getElementById('price').innerText = "CONNECTING";
            }
        }
        setInterval(loadData, 2000);
        loadData();
    </script>
</body>
</html>
