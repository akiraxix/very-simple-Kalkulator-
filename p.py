# Pembukaan
print("| Welcome user |".center(39, "="))
nama_user = input("Nama lu sapa? (iseng aja)XD ")
while nama_user == "":
    nama_user = input("Masukkin yang bener dongg!! :\n")

# Mulai program kalkulator
while True:
    print(f"| Yooo hallo {nama_user}, selamat menghitung 😹 |".center(50, "="))
    
    # Input simbol operasi
    input_simbol = input(f"""Silahkan masukkan operasi hitung berikut: 
( + | - | * | / | % | // )\n(Pilih salah satu aja ya {nama_user}): """)

    if input_simbol in ["+", "-", "*", "/", "%", "//"]:
        # Input angka
        try:
            angka1 = float(input("Silahkan masukkan angka pertama: "))
            angka2 = float(input("Silahkan masukkan angka kedua: "))
        except ValueError:
            print("Harus masukkan angka yang valid!")
            continue

        # Proses operasi
        if input_simbol == "+":
            hasil = angka1 + angka2
        elif input_simbol == "-":
            hasil = angka1 - angka2
        elif input_simbol == "*":
            hasil = angka1 * angka2
        elif input_simbol == "/":
            if angka2 == 0:
                print("Gak bisa bagi dengan nol yaa 😅")
                continue
            hasil = angka1 / angka2
        elif input_simbol == "%":
            hasil = angka1 % angka2
        elif input_simbol == "//":
            if angka2 == 0:
                print("Gak bisa floor divide dengan nol yaa 😅")
                continue
            hasil = angka1 // angka2

        print(f"Hasil dari {angka1} {input_simbol} {angka2} adalah: {hasil}\n")

    else:
        print("Simbol yang kamu masukin salah, coba lagi yaa...\n")

    # Tanya lanjut atau tidak
    lanjut = input("Mau hitung lagi? (y/n): ").lower()
    if lanjut != "y":
        print(f"Okay {nama_user}, sampai jumpa lagi yaa! 👋")
        break
