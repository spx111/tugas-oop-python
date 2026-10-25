class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru

    def tembak(self):
        self.skor += 50
        print("*PEW! Katak menembakkan bola!*")

    def info_status(self):
        print("--- Status Katak Zuma ---")
        print(f"Warna Peluru : {self.warna_peluru}")
        print(f"Skor Saat Ini: {self.skor}")
        print(f"Status Aktif : {self.is_active}")
        print("-------------------------\n")


katak_player = KatakZuma("Biru")

print("Kondisi Awal:")
katak_player.info_status()

katak_player.ganti_warna("Merah")

katak_player.tembak()

print("Kondisi Setelah Ganti Warna dan Menembak:")
katak_player.info_status()