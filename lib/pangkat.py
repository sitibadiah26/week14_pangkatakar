from lib.imajiner import Imajiner

class Pangkat(Imajiner):

    def __init__(self, name) :
        super().__init__(name)
        self.nilai1 = 0
        self.nilai_pangkat = 0

    def hitung(self, nilai1):
        self.nilai1 = nilai1

        if self.cek_nilai():
            self.print_eks()
        else:
            self.nilai_pangkat=self.nilai1**2

    def cek_nilai (self):
        return True if self.nilai1 < 0 else False

    def print_eks(self):
        print("Nilai kurang dari 0: {}".format(self.nilai1))

    def hasil(self, index):
        print("Nomor {} hasil {} dua nya adalah {} ".format(index, self.nama, self.nilai_pangkat))

    def __repr__(self):
        return "Angka {}".format(self.nilai1)
