print(40*"~")
print("SELAMAT DATANG DI KALKULATOR BANGUN RUANG")
print(40*"~")

#Input Pilihan Bangun Ruang
print("Masukkan pilihan bangun ruang :\n", "1. balok \n", "2. bola \n", "3. kerucut \n", "4. kubus \n", "5. Limas Segiempat \n", "6. Limas Segitiga \n", "7. Prisma Segitiga \n", "8. Tabung \n")
pilihan = input("Masukkan pilihan bangun ruang :")

# Input pilihan operator
print("Masukkan pilihan operator :\n", "a. Luas Permukaan \n", "b. Volume \n")
pilihan2 = input("Masukkan pilihan operator :")

# Operator bangun ruang
if pilihan == "1" and pilihan2 == "a":
    panjang = float(input("Masukkan panjang :"))
    lebar = float(input("Masukkan lebar :"))
    tinggi = float(input("Masukkan tinggi :"))
    luas_balok = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    print(f"Hasilnya adalah : {luas_balok} m^2")

elif pilihan == "1" and pilihan2 == "b":
    panjang = float(input("Masukkan panjang :"))
    lebar = float(input("Masukkan lebar :"))
    tinggi = float(input("Masukkan tinggi :"))
    volume_balok = panjang * lebar * tinggi
    print(f"Hasilnya adalah : {volume_balok} m^3")

elif pilihan == "2" and pilihan2 == "a":
    jari_jari = float(input("masukan jari-jari :"))
    pi = 3.14
    luas_bola = 4 * pi * (jari_jari ** 2)
    print(f"hasilnya adalah : {luas_bola} m^2")

elif pilihan == "2" and pilihan2 == "b":
    jari_jari = float(input("masukan jari-jari :"))
    pi = 3.14
    volume_bola = (4/3) * pi * (jari_jari ** 3)
    print(f"hasilnya adalah : {volume_bola} m^3")

elif pilihan == "3" and pilihan2 == "a":
    jari_jari = float(input("masukan jari-jari :"))
    tinggi = float(input("Masukkan tinggi :"))
    garis_pelukis = float(input("masukan garis pelukis :"))
    pi = 3.14
    luas_kerucut = pi * jari_jari * (jari_jari + garis_pelukis)
    print(f"hasilnya adalah : {luas_kerucut} m^2")

elif pilihan == "3" and pilihan2 == "b":
    jari_jari = float(input("masukan jari-jari :"))
    tinggi = float(input("Masukkan tinggi :"))
    garis_pelukis = float(input("masukan garis pelukis :"))
    pi = 3.14
    volume_kerucut = (1/3) * pi * (jari_jari ** 2) * tinggi
    print(f"hasilnya adalah : {volume_kerucut} m^3")

elif pilihan == "4" and pilihan2 == "a":
    sisi = float(input("masukan sisi :"))
    luas_kubus = 6 * (sisi ** 2)
    print(f"hasilnya adalah : {luas_kubus} m^2")

elif pilihan == "4" and pilihan2 == "b":
    sisi = float(input("masukan sisi :"))
    volume_kubus = sisi ** 3
    print(f"hasilnya adalah : {volume_kubus} m^3")

elif pilihan == "5" and pilihan2 == "a":
    sisi_alas = float(input("masukan sisi alas :"))
    tinggi_limas = float(input("masukan tinggi limas :"))
    tinggi_segitiga = float(input("masukan tinggi segitiga :"))
    luas_limas_segiempat = (sisi_alas ** 2) + 2 * sisi_alas * (tinggi_limas + tinggi_segitiga)
    print(f"hasilnya adalah : {luas_limas_segiempat} m^2")

elif pilihan == "5" and pilihan2 == "b":
    sisi_alas = float(input("masukan sisi alas :"))
    tinggi_limas = float(input("masukan tinggi limas :"))
    tinggi_segitiga = float(input("masukan tinggi segitiga :"))
    volume_limas_segiempat = (sisi_alas ** 2 * tinggi_limas) / 3
    print(f"hasilnya adalah : {volume_limas_segiempat} m^3")

elif pilihan == "6" and pilihan2 == "a":
    alas = float(input("masukan alas :"))
    tinggi_limas = float(input("masukan tinggi limas :"))
    tinggi_segitiga = float(input("masukan tinggi segitiga :"))
    luas_limas_segitiga = (alas * tinggi_limas) / 2 + 3 * (0.5 * alas * tinggi_segitiga)
    print(f"hasilnya adalah : {luas_limas_segitiga} m^2")

elif pilihan == "6" and pilihan2 == "b":
    alas = float(input("masukan alas :"))
    tinggi_limas = float(input("masukan tinggi limas :"))
    tinggi_segitiga = float(input("masukan tinggi segitiga :"))
    volume_limas_segitiga = (alas ** 2 * tinggi_segitiga) / 6
    print(f"hasilnya adalah : {volume_limas_segitiga} m^3")

elif pilihan == "7" and pilihan2 == "a":
    alas_segitiga = float(input("masukan alas segitiga :"))
    tinggi_segitiga = float(input("masukan tinggi segitiga :"))
    tinggi_prisma = float(input("masukan tinggi prisma :"))
    luas_prisma_segitiga = (alas_segitiga * tinggi_prisma) + 2 * (0.5 * alas_segitiga * tinggi_segitiga)
    print(f"hasilnya adalah : {luas_prisma_segitiga} m^2")

elif pilihan == "7" and pilihan2 == "b":
    alas_segitiga = float(input("masukan alas segitiga :"))
    tinggi_segitiga = float(input("masukan tinggi segitiga :"))
    tinggi_prisma = float(input("masukan tinggi prisma :"))
    volume_prisma_segitiga = 0.5 * alas_segitiga * tinggi_segitiga * tinggi_prisma
    print(f"hasilnya adalah : {volume_prisma_segitiga} m^3")

elif pilihan == "8" and pilihan2 == "a":
    jari_jari = float(input("masukan jari jari :"))
    tinggi = float(input("masukan tinggi :"))
    pi = 3.14
    luas_tabung = 2 * pi * jari_jari * (jari_jari + tinggi)
    print(f"hasilnya adalah : {luas_tabung} m^2")

elif pilihan == "8" and pilihan2 == "b":
    jari_jari = float(input("masukan jari jari :"))
    tinggi = float(input("masukan tinggi :"))
    pi = 3.14
    volume_tabung = pi * (jari_jari ** 2) * tinggi
    print(f"hasilnya adalah : {volume_tabung} m^3")

else :
    print("TIDAK ADA OPERATOR YANG DIPILIH")