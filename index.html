<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI SIGNALFX</title>
    <style>
        body { background: #0b0e14; color: #e6edf3; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .container { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 30px; width: 90%; max-width: 400px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        h1 { font-size: 1.2rem; color: #8b949e; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 2px; }
        .price { font-size: 3.5rem; font-weight: bold; margin: 10px 0; color: #58a6ff; text-shadow: 0 0 20px rgba(88,166,255,0.3); }
        .signal-box { padding: 15px; border-radius: 8px; font-weight: bold; font-size: 1.5rem; margin: 20px 0; transition: 0.3s; background: #30363d; }
        .buy { background: #238636 !important; color: white; box-shadow: 0 0 15px rgba(35, 134, 54, 0.4); }
        .sell { background: #da3633 !important; color: white; box-shadow: 0 0 15px rgba(218, 54, 51, 0.4); }
        .details { display: flex; justify-content: space-between; border-top: 1px solid #30363d; padding-top: 15px; font-size: 0.9rem; }
        .time { color: #8b949e; margin-bottom: 10px; font-size: 0.8rem; }
    </style>
</head>
<body>
    <div class="container">
        <h1>AI SIGNALFX</h1>
        <div class="time" id="time">Menghubungkan...</div>
        <div class="price" id="price">0.00</div>
        <div id="signal" class="signal-box">SCANNING</div>
        <div class="details">
            <div>SL: <span id="sl" style="color: #ff7b72;">0</span></div>
            <div>TP: <span id="tp" style="color: #3fb950;">0</span></div>
        </div>
    </div>
    <script>
        async function getSignal() {
            // Kita coba jalur /api/ind dulu, kalau gagal pindah ke /api/index
            const paths = ['/api/ind', '/api/index'];
            let success = false;

            for (let path of paths) {
                if (success) break;
                try {
                    const r = await fetch(path);
                    if (!r.ok) continue;
                    const d = await r.json();
                    
                    document.getElementById('price').innerText = d.price;
                    document.getElementById('time').innerText = d.time + " WIB";
                    document.getElementById('sl').innerText = d.sl || d.sl1 || "0";
                    document.getElementById('tp').innerText = d.tp || "0";
                    
                    const s = document.getElementById('signal');
                    s.innerText = d.signal;
                    
                    if (d.signal.toUpperCase().includes('BUY')) {
                        s.className = 'signal-box buy';
                    } else if (d.signal.toUpperCase().includes('SELL')) {
                        s.className = 'signal-box sell';
                    }
                    success = true;
                } catch (e) {
                    console.log("Gagal di jalur: " + path);
                }
            }
        }
        
        setInterval(getSignal, 2000);
        getSignal();
    </script>
</body>
</html>
