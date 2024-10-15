def hitung_bmi(berat, tinggi):
    return berat / ((tinggi / 100) ** 2)

def interpretasi_bmi(bmi, jenis_kelamin):
    if jenis_kelamin.lower() == 'pria':
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Kelebihan berat badan"
        else:
            return "Obesitas"
    elif jenis_kelamin.lower() == 'wanita':
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 24:
            return "Normal"
        elif 24 <= bmi < 29:
            return "Kelebihan berat badan"
        else:
            return "Obesitas"
    else:
        return "Jenis kelamin tidak valid"

def main():
    print("Kalkulator Berat Badan Ideal")
    jenis_kelamin = input("Masukkan jenis kelamin (pria/wanita): ")
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (cm): "))

    bmi = hitung_bmi(berat, tinggi)
    kategori = interpretasi_bmi(bmi, jenis_kelamin)

    print(f"\nBMI Anda adalah: {bmi:.2f}")
    print(f"Kategori berat badan: {kategori}")

    if kategori == "Normal":
        print("Berat badan Anda sudah ideal!")
    else:
        if kategori == "Kurus":
            berat_ideal_min = 18.5 * ((tinggi / 100) ** 2)
            print(f"Untuk mencapai berat badan ideal, Anda perlu menambah berat badan minimal {berat_ideal_min - berat:.2f} kg")
        elif kategori in ["Kelebihan berat badan", "Obesitas"]:
            if jenis_kelamin.lower() == 'pria':
                berat_ideal_max = 25 * ((tinggi / 100) ** 2)
            else:
                berat_ideal_max = 24 * ((tinggi / 100) ** 2)
            print(f"Untuk mencapai berat badan ideal, Anda perlu menurunkan berat badan minimal {berat - berat_ideal_max:.2f} kg")

if __name__ == "__main__":
    main()