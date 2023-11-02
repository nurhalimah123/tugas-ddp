# 1. buatkan program python dgn list dengan nilai (kodekendaraan, namakendaraan, CCkendaraan, Warnakendaraan)
kendaraan = ["1", "Beat", "125cc", "Silver"]
print(kendaraan)

# 2. dari list nomor 1 silahkan di tambahkan : diakhir tambahkan (harga dan jumlah roda, disisipkan setelah namakendaraan, merk, dan jeniskendaraan)
kendaraan.append('18,5 juta')
kendaraan.append('roda dua')
kendaraan.insert(2,"Honda")
kendaraan.insert(3,"Motor")
print(kendaraan)

# 3. buat program python dgn match case untuk menghitung luas bangun datar :
ket = '''menghitung luas bangun datar, masukkan pilihan : 
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
'''
print(ket)

pilihan = (input("masukkan pilihan : "))
match pilihan:
    case "1":
        print("menghitung luas persegi")
        sisi = int(input("masukan sisi: "))
        luas = sisi * sisi
        print("luas dari persegi dengan sisi", sisi, "adalah", luas)
    case "2":
        print("menghitung luas lingkaran")
        jari = int(input("masukan jari-jari: "))
        luas = 3.14 * jari * jari
        print("luas dari lingkaran dengan jari", jari, "adalah", luas)
    case "3":
        print("menghitung luas segitiga")
        alas = int(input("masukan alas: "))
        tinggi = int(input("masukan tinggi: "))
        luas = alas * tinggi * 0.5
        print("luas dari segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luas)
    case _:
        print("input tidak valid")