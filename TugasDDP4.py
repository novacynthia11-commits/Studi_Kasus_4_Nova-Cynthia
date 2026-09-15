print("=" * 30)
teks = "DATA BUKU-BUKU"
print (f"{teks:^30}")
print("=" * 30)

# Dictionory
buku = {
    "judul" : "Cantik Itu Luka",
    "penulis" : "Eka Kurniawan",
    "tahun_terbit" : "2002"
}

# Daftar Menu
while True :
    print("\n°‧ 𓆝 𓆟 𓆞 ·｡ DAFTAR MENU °‧ 𓆝 𓆟 𓆞 ·｡")
    print("1. Tampilkan Data Buku")
    print("2. Tambahkan Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("0. Keluar")
    print("𓆝 𓆟 𓆞 𓆝 𓆟" * 4)
    menu = input("Pilih menu : ")

# Pilihan 1
    if menu == "1" :
        print()
        print("Judul :", buku["judul"])
        print("Penulis :", buku["penulis"])
        print("Tahun Terbit :", buku["tahun_terbit"])

        # jika penerbit ditambahkan
        if "penerbit" in buku :
            print("Penerbit :",buku["penerbit"])

    elif menu == "2" :
        print()
        penerbit = input("Masukkan nama penerbit : ")
        buku["penerbit"] = penerbit
        print("\x1B[3mData Penerbit berhasil ditambahkan!\x1B[0m")

    elif menu == "3" :
        print()
        penulis_hanyar = input("Ubah nama penulis menjadi : ")
        buku["penulis"] = penulis_hanyar
        print("\x1B[3mData Penulis berhasil diubah!\x1B[0m")

    elif menu == "4" :
        print()
        if "penerbit" in buku :
            buku.pop("penerbit")
            print("\x1B[3mData Penerbit berhasil dihapus\x1B[0m")
        else:
            print("Data Penerbit belum ditambahkan.")
            continue

    elif menu == "0" :
        print()
        print("𓅰 𓅬 𓅭 𓅮 𓅯" * 4)
        akhir = "DATA BUKU TERBARU"
        print (f"{teks:^30}")
        print("Judul :", buku["judul"])
        print("Penulis :", buku["penulis"])
        print("Tahun Terbit :", buku["tahun_terbit"])
        
        # jika penerbit ditambahkan
        if "penerbit" in buku :
            print("Penerbit :",buku["penerbit"])
        print("𓅰 𓅬 𓅭 𓅮 𓅯" * 4)
        break
    
    else:
        print("Pilihan Tidak Tersedia ( ｡ •̀ ᴖ •́ ｡) ")
        continue