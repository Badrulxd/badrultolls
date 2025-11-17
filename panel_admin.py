import os
import json
import uuid
import datetime
import webbrowser

ADMIN_WA = "+6289516701746"
DB_FILE = "license_db.json"

# ------------------- DATABASE -------------------
def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

# ------------------- GENERATOR KEY -------------------
def generate_key():
    return uuid.uuid4().hex[:25].upper()

# ------------------- MASA LISENSI -------------------
def add_days(amount):
    return (datetime.datetime.now() + datetime.timedelta(days=amount)).strftime("%Y-%m-%d")

# ------------------- MENU LISENSI -------------------
def beli_lisensi():
    os.system("clear")
    print("====== BADRUL STORE | LISENSI DEVICE ======")
    print("1. 1 Bulan | 100K")
    print("2. 2 Minggu | 50K")
    print("3. 1 Minggu | 30K")
    print("==========================================")
    pilih = input("Pilih paket: ")

    if pilih == "1":
        days = 30
        harga = 100000
    elif pilih == "2":
        days = 14
        harga = 50000
    elif pilih == "3":
        days = 7
        harga = 30000
    else:
        print("Pilihan tidak valid!")
        return

    key = generate_key()
    expired = add_days(days)

    db = load_db()
    db[key] = {
        "expired": expired,
        "device": None,
        "status": "active"
    }
    save_db(db)

    print(f"\nAPI Key Berhasil Dibuat!\nKey: {key}\nExpired: {expired}")

    # WA otomatis (klik kirim)
    text = f"Pembelian Lisensi\nKey: {key}\nExpired: {expired}\nHarga: {harga}"
    wa_url = f"https://wa.me/{ADMIN_WA.replace('+','')}?text={text.replace(' ','%20')}"
    webbrowser.open(wa_url)

# ------------------- CEK LISENSI -------------------
def cek_lisensi(key, device_id):
    db = load_db()

    if key not in db:
        return False, "Key tidak ditemukan!"

    info = db[key]

    # ikat device
    if info["device"] is None:
        info["device"] = device_id
        save_db(db)

    # tolak device lain
    if info["device"] != device_id:
        return False, "Key dipakai di device lain!"

    # cek expired
    if datetime.datetime.now().strftime("%Y-%m-%d") > info["expired"]:
        return False, "Lisensi Expired!"

    return True, "Lisensi Valid!"

# ------------------- RUN MENU ADMIN -------------------
if __name__ == "__main__":
    beli_lisensi()
