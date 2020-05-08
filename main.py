from lib.pangkat import Pangkat
from lib.akar import Akar

if __name__=="__main__":

    nilai1 = [1,5,7]
    nilai2 = [81,9,0]

    print("MENGHITUNG PERPANGKATAN DAN PERAKARAN\n")

    for i in range(len(nilai1)):

        pangkat=Pangkat("Pangkat")
        pangkat.hitung(nilai1[i])
        print(pangkat)
        pangkat.hasil(i)

        akar=Akar("Akar")
        akar.hitung(nilai2[i])
        print(akar)
        akar.hasil(i)
        
        print("\n")
                   
