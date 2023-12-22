print("Konversi Suhu Fahrenheit")

# entry
suhu= float(input("masukkan suhu dalam Fahrenheit:"))

#rumus
C = 5/9 *  ((suhu) - 32)
R = 4/9 *  ((suhu) - 32)
K = 5/9 * (suhu - 32) + 273

#output
print(suhu,   " Fahrenheit sama dengan ")
print(str(C) + " Celcius ")
print(str(R) + " Reamur ")
print(str(K) + " kelvin ")