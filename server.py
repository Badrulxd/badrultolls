from flask import Flask, request, jsonify
import json, os, datetime, uuid

app = Flask(__name__)
DB_FILE = "database.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    return json.load(open(DB_FILE))

def save_db(data):
    json.dump(data, open(DB_FILE, "w"), indent=4)

# ================================
# API CEK LISENSI
# ================================
@app.route("/check", methods=["POST"])
def api_check():
    data = request.json
    api_key = data.get("api_key")
    device  = data.get("device")

    db = load_db()

    if api_key not in db:
        return jsonify({"status": False, "msg": "API Key tidak terdaftar"})

    lic = db[api_key]

    # ===== CEK DEVICE =====
    if lic["device"] != device:
        return jsonify({"status": False, "msg": "Device tidak cocok!"})

    # ===== CEK EXPIRED =====
    if lic["expired"] != "unlimited":
        exp = datetime.datetime.strptime(lic["expired"], "%d-%m-%Y")
        if exp < datetime.datetime.now():
            return jsonify({"status": False, "msg": "Lisensi Expired!"})

    return jsonify({
        "status": True,
        "msg": "Lisensi Valid",
        "created": lic["created"],
        "expired": lic["expired"],
        "sisa": lic["sisa"]
    })

# ================================
# API GENERATE LISENSI
# ================================
@app.route("/generate", methods=["POST"])
def api_generate():
    paket = request.json.get("paket")
    device = request.json.get("device")

    api_key = str(uuid.uuid4()).replace("-", "")[:20]

    # durasi paket
    today = datetime.datetime.now()

    if paket == "1bulan":
        exp = today + datetime.timedelta(days=30)
        sisa = "30 Hari"
    elif paket == "2minggu":
        exp = today + datetime.timedelta(days=14)
        sisa = "14 Hari"
    elif paket == "1minggu":
        exp = today + datetime.timedelta(days=7)
        sisa = "7 Hari"
    else:
        return jsonify({"status": False, "msg": "Paket tidak ditemukan!"})

    db = load_db()
    db[api_key] = {
        "device" : device,
        "created": today.strftime("%d-%m-%Y"),
        "expired": exp.strftime("%d-%m-%Y"),
        "sisa"   : sisa
    }
    save_db(db)

    return jsonify({
        "status": True,
        "api_key": api_key,
        "expired": exp.strftime("%d-%m-%Y"),
        "sisa": sisa
    })

# ================================
# Run server
# ================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
