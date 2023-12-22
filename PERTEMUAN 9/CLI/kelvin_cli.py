print("Konversi Suhu Kelvin")

# entry
suhu= float(input("masukkan suhu dalam Kelvin:"))

#rumus
F =  9/5 * (suhu - 273) + 32
R =  4/5 * (suhu - 273)
C = suhu - 273

#output
print(suhu, " Kelvin sama dengan ")
print(str(F) + " Fahrenheit ")
print(str(R) + " Reamur ")
print(str(C) + " Celcius ")