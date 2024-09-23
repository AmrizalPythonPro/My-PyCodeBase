def tambah_agenda(agenda, agenda_baru):
    """Fungsi untuk menambahkan agenda baru ke daftar agenda."""
    agenda.append(agenda_baru)
    print("Agenda berhasil ditambahkan.\n")

def lihat_agenda(agenda):
    """Fungsi untuk menampilkan daftar agenda yang sudah dimasukkan."""
    if agenda:
        print("Daftar AgendaKU:")
        for index, item in enumerate(agenda, start=1):
            print(f'{index}. {item}')
    else:
        print("Belum ada agenda yang ditambahkan.")
    print()

def tampilkan_menu():
    """Fungsi untuk menampilkan menu utama."""
    print("AgendaKU")
    print("1. Menambah Agenda")
    print("2. Melihat Agenda")
    print("3. Keluar dari Program")
    print()

def main():
    agenda = []

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1, 2, atau 3): ")

        if pilihan == '1':
            agenda_baru = input("Masukkan agenda baru: ")
            tambah_agenda(agenda, agenda_baru)
        elif pilihan == '2':
            lihat_agenda(agenda)
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

# Memanggil fungsi main langsung
main()
