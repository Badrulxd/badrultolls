import os, json, uuid
from rich.console import Console
from rich.panel import Panel
from Penyimpanan.FolderSC.instagram import Instagram

console = Console()
DB_FILE = "lisensi.json"
DEVICE_FILE = "device.id"


# ===================================
# DEVICE ID PERMANEN
# ===================================
def get_device_id():
    # jika sudah ada file device.id -> pakai yang tersimpan
    if os.path.exists(DEVICE_FILE):
        return open(DEVICE_FILE).read().strip()

    # jika belum ada -> buat baru & simpan
    dev = str(uuid.uuid4()).replace("-", "")
    open(DEVICE_FILE, "w").write(dev)
    return dev


# ===================================
# DATABASE HANDLER
# ===================================
def load_db():
    if not os.path.exists(DB_FILE):
        json.dump({}, open(DB_FILE, "w"))
    return json.load(open(DB_FILE))


def save_db(data):
    json.dump(data, open(DB_FILE, "w"), indent=4)


# ===================================
# CEK LISENSI
# ===================================
def cek_lisensi():
    db = load_db()
    dev = get_device_id()

    if dev not in db:
        return None
    return db[dev]


# ===================================
# INPUT API KEY
# ===================================
def input_api_key():
    os.system("clear")
    console.print(Panel("[cyan]MASUKKAN API KEY[/cyan]", width=60))

    api = input("\nAPI KEY: ")

    if api.strip() == "":
        print("API Key kosong!")
        input("Enter...")
        return

    dev = get_device_id()

    lisensi_data = {
        "api_key": api,
        "created": "Today",
        "expired": "Unlimited",
        "sisa": "Unlimited"
    }

    db = load_db()
    db[dev] = lisensi_data
    save_db(db)

    console.print(Panel("[green]API KEY BERHASIL DISIMPAN[/green]", width=60))
    input("Enter...")


# ===================================
# MASUK TOOLS INSTAGRAM
# ===================================
def masuk_ig():
    lis = cek_lisensi()

    if lis is None:
        console.print(Panel("[red]Belum ada lisensi![/red]\nMasukkan API key dulu.", width=60))
        input("Enter...")
        return

    try:
        Instagram().Chek_Cookies(
            lis["created"],
            lis["expired"],
            lis["sisa"]
        )
    except Exception as e:
        console.print(Panel(f"[red]{e}[/red]", width=60))
        input("Enter...")


# ===================================
# BELI LISENSI
# ===================================
def beli_lisensi():
    os.system("clear")
    console.print(Panel("[green]BELI LISENSI[/green]", width=60))

    print("""
1. 1 Bulan  - 100.000
2. 2 Minggu - 50.000
3. 1 Minggu - 30.000
0. Kembali
""")

    pilih = input("Pilih: ")

    paket = {
        "1": "1 Bulan",
        "2": "2 Minggu",
        "3": "1 Minggu"
    }

    if pilih not in paket:
        return

    dev = get_device_id()

    pesan = f"LISENSI BARU\nPaket: {paket[pilih]}\nDevice ID: {dev}"

    os.system(f"termux-open-url 'https://wa.me/6289516701746?text={pesan}'")
    input("Mengalihkan ke WhatsApp...\nEnter...")


# ===================================
# MENU UTAMA
# ===================================
def main_menu():
    while True:
        os.system("clear")
        console.print(Panel("[cyan]BADRUL STORE – LICENSE SYSTEM[/cyan]", width=60))

        print("""
1. Beli Lisensi
2. Masukkan API Key
3. Masuk Tools Instagram
0. Keluar
""")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            beli_lisensi()
        elif pilih == "2":
            input_api_key()
        elif pilih == "3":
            masuk_ig()
        else:
            exit()


main_menu()
