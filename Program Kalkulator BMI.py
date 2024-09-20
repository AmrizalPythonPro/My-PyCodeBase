print("SELAMAT DATANG DI PROGRAM KALKULATOR BMI\n")
while True:
    try:
        height = float(input("Masukan tinggi badan anda (cm) : ")) / 100
        weight = float(input("Masukan berat bdan anda (kg) : "))
        if height < 0 or weight < 0:
            print("\nInput harus berupa bilangan bulat positif. Silakan coba lagi")
            continue
        break
    except ValueError:
        print("\nInput tidak valid. Silakan masukkan bilangan bulat positif.")

bmi = weight / (height ** 2)
bottom_ideal_weight = 18.5 * (height ** 2)
top_ideal_weight = 25 * (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
elif bmi < 35:
    category = "Obese"
else:
    category = "Extreme Obese"

print("\n=============================================")
print(f"Hasil perhitungan BMI anda adalah {bmi:.2f}")
print(f"\nKategori BMI anda adalah {category}")
print(f"\nBerat badan ideal anda antara {bottom_ideal_weight:.2f} kg sampai {top_ideal_weight:.2f} kg")
print("\nTerima kasih telah menggunakan program ini")
print("==============================================")