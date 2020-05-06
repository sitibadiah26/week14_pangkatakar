import math
from lib.imajiner import Imajiner

class Akar(Imajiner):

    def __init__(self, name) :
        super().__init__(name)
        self.nilai2 = 0
        self.nilai_akar = 0

    def hitung(self, nilai2):
        self.nilai2 = nilai2

        if self.cek_nilai():
            self.print_eks()
        else:
            self.nilai_akar=math.sqrt(self.nilai2)

    def cek_nilai (self):
        return True if self.nilai2 < 0 else False

    def print_eks(self):
        print("Nilai kurang dari 0: {}".format(self.nilai2))

    def hasil(self, index):
        print("Nomor {} hasil {} dua nya adalah bernilai {} maka {}".format(index+1, self.nama, self.nilai_akar, self.cek_keterangan(self.nilai_akar)))

    def cek_keterangan(self, hasil):
        if hasil < 0:
            return "imajiner"
        elif hasil > 0:
            return "tidak imajiner"
        else :
            return "nol"

    def __repr__(self):
        return "Angka {}".format(self.nilai2)
