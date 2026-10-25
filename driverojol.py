class DriverOjol:
    def __init__(self, nama):
        self.nama = nama
        self.saldo = 0
        self.is_online = False

    def masuk_online(self):
        self.is_online = True
        print(f"{self.nama} sekarang online dan siap menerima orderan.")

    def terima_order(self, tarif):
        if self.is_online:
            print(f"{self.nama} menerima orderan senilai {tarif}. Saldo sekarang: {self.saldo}")
        else:
            print(f"{self.nama} tidak bisa menerima orderan karena sedang offline.")

    def selesai_order(self, tarif):
        self.saldo += tarif
        print(f"Orderan selesai! {self.nama} mendapatkan uang Rp{tarif}.")

    def info_driver(self):
        print("\n=== STATUS DRIVER OJOL ===")
        print(f"Nama         : {self.nama}")
        print(f"Saldo        : {self.saldo}")
        print(f"Sedang Online? : {self.is_online}")
        print("==========================\n")

driver1 = DriverOjol("Budi")
driver1.info_driver()
driver1.masuk_online()
driver1.terima_order(50000)
driver1.selesai_order(50000)
driver1.info_driver()