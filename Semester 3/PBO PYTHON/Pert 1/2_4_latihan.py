class anjing :
    def __init__(self, nama, umur, warna) :
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def menggonggong(self) :
        print ("guk..guk..")

    def info (self) :
        print("nama anjing =" + self.nama + ", umurnya =" +str(self.umur) + "tahun, warnanya = " + str(self.warna))

    def berlari(self) :
        print("cepat....Sekali")
    