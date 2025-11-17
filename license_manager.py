import json, datetime

class LicenseManager:
    def __init__(self, db="database.json"):
        self.db = db
        self.data = self.load_db()

    def load_db(self):
        return json.load(open(self.db, "r"))

    def save_db(self):
        json.dump(self.data, open(self.db, "w"), indent=4)

    def check_license(self, api_key):
        for user_id, info in self.data["users"].items():
            if info["api_key"] == api_key:
                return self.validate(info)
        return False, "API Key tidak terdaftar!"

    def validate(self, info):
        created = info["created"]
        expired  = info["expired"]

        if info["status"] != "active":
            return False, "Lisensi tidak aktif"

        if expired.lower() == "unlimited":
            sisa = "unlimited"
            return True, {"created": created, "expired": expired, "sisa": sisa}

        today = datetime.datetime.now().date()
        exp_date = datetime.datetime.strptime(expired, "%Y-%m-%d").date()

        if today > exp_date:
            return False, "Lisensi sudah expired!"

        sisa_hari = (exp_date - today).days

        return True, {
            "created": created,
            "expired": expired,
            "sisa": f"{sisa_hari} hari"
        }
