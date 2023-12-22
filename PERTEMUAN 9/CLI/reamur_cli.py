print("Konversi Suhu Reamur")

# entry
suhu= float(input("masukkan suhu dalam Reamur:"))

#rumus
F = (9/4 *  (suhu)) + 32
C = (5/4 *  (suhu))
K = 5/4 * suhu + 273

#output
print(suhu, " Reamur sama dengan ")
print(str(F) + " Fahrenheit ")
print(str(C) + " Celcius ")
print(str(K) + " kelvin ")