# Sekuensial
def percakapan_awal():
    print('Ibu berkata, "Pergi ke toko"')
    print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
    print('Ibu menjawab, "Beli satu botol susu"')
    print("Maka Budi berangkat ke toko")
    print("Dan mulai berbelanja")


# Percabangan
def belanja_susu_dan_telur(jumlah_botel_susu, jumlah_telur):
    print(f"Jumlah botol susu {jumlah_botel_susu} botol")
    print(f"Jumlah telur {jumlah_telur} butir")

    if jumlah_botel_susu > 0:
        print("Budi mengecek harganya, dan ternyata uangnya cukup")
        if jumlah_telur == 0:
            print("Budi membeli 1 botol susu")
        else:
            print("Budi membeli 6 botol susu")
    else:
        print("Budi tidak jadi membeli 1 botol susu")


# Hasil akhir
def hasil_belanja():
    print("Budi pulang ke rumah")
    print("Menyampaikan hasilnya kepada ibu")


# Jalankan fungsi secara langsung
percakapan_awal()
jumlah_botel_susu = 173
jumlah_telur = 1587
belanja_susu_dan_telur(jumlah_botel_susu, jumlah_telur)
hasil_belanja()
