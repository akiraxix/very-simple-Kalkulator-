# Welcome User
print("| Welcome User! 😊 |".center(50, "="))

# Input nama user
nama_user = input("| Haloo! kenalan dulu yu, nama kamu siapa? |: ")
while nama_user == "" or nama_user == " ":
    nama_user = input("Masukkan nama kamu dengan benar!: ")
    
while True:
    print("\n" + f"| Halo {nama_user}! Selamat berhitung. |".center(50, "=") + "\n")

    # Input simbol
    print(f"""Halo {nama_user}! Silahkan masukkan simbol operasi Aritmatikanya! 
contoh: | + |, | - |, | * |, | / |, | % |, | // |""")
    simbol = input("Masukkan simbol: ")
    if simbol in ["+", "-", "*", "/", "%", "//"]:
        try:
            # input angka
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua  : "))
        except ValueError:
            print("Masukkan hanya angka! ")
            continue
            # proses hitung
        if simbol == "+":
            hasil = angka1 + angka2
        elif simbol == "-":
            hasil = angka1 - angka2
        elif simbol == "*":
            hasil = angka1 * angka2
        elif simbol == "/":
            if angka2 == 0:
                print("Jangan masukkan 0 pada angka 2 ya, nanti error!😊")
                continue
            hasil = angka1 / angka2
        elif simbol == "%":
            hasil = angka1 % angka2
        elif simbol == "//":
            hasil = angka1 // angka2

        # Hasil/output user
        print(f"Hasil dari {angka1} {simbol} {angka2} adalah: {hasil}" + "\n")

    else:
        print("Simbol yang kamu masukin salah!!")    
        continue

        # Lanjut atau ga?
    lanjut = input(f"Apakah kamu mau lanjut berhitung? [y/n]. ").lower()
    if lanjut == "y":
        continue
    else:
        print(f"Terimakasih {nama_user}, telah menggunakan jasa kami!!")
        
        
    break