class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(f"{self.nama} sedang berlari")

    def ambil_koin(self, jumlah):
        self.koin += jumlah
        print(f"Klinggg!! {self.nama} mengambil {jumlah} koin (total koin {self.koin})")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"Duar! {self.nama} menabrak kereta. GAME OVER")

    def info_player(self):
        print("\n=== STATUS KARAKTER ===")
        print(f"Nama         : {self.nama}")
        print(f"Skor         : {self.skor}")
        print(f"Jumlah Koin  : {self.koin}")
        print(f"Sedang Lari? : {self.is_running}")
        print("=======================\n")


player1 = KarakterSurfer("Jake")

player1.info_player()         
player1.berlari()             
player1.ambil_koin(10)        
player1.ambil_koin(15)        
player1.info_player()         
player1.tabrak_rintangan()    
player1.info_player()