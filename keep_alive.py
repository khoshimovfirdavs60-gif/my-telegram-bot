from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is live!"

def run():
    # Portni 5000 qilaylik, u odatda bo'sh bo'ladi
    app.run(host='0.0.0.0', port=5000)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()