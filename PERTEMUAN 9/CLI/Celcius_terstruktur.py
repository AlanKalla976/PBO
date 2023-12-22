print("Konversi Suhu Celcius")
def get_fahrenheit(suhu):
    F = (9/5 * float(suhu))
    return F
def get_Reamur(suhu):
    R = (4/5 * float(suhu))
    return R
def get_Kelvin(suhu):
    K =  float(suhu) + 273
    return K
# entry
suhu = input("masukkan suhu dalam celcius:")

#rumus
F = get_fahrenheit(suhu)
R = get_Reamur(suhu)
K = get_Kelvin(suhu)
