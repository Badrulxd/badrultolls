import json, datetime
from device import get_device_id

class LicenseSystem:
    def __init__(self):
        self.db = "database/license.json"
        self.device = get_device_id()

    def load(self):
        return json.load(open(self.db))

    def save(self, data):
        json.dump(data, open(self.db, "w"), indent=4)

    def validate(self, key):
        data = self.load()

        if key not in data:
            return False, "Lisensi tidak ditemukan"

        lic = data[key]

        # Jika device kosong → daftarkan
        if lic["device"] is None:
            lic["device"] = self.device
            self.save(data)
        else:
            # Sudah terikat device lain
            if lic["device"] != self.device:
                return False, "Lisensi sudah digunakan di device lain"

        # Cek expired
        if lic["expired"] != "unlimited":
            exp = datetime.datetime.strptime(lic["expired"], "%Y-%m-%d")
            if datetime.datetime.now() > exp:
                return False, "Lisensi expired"

        return True, lic
        