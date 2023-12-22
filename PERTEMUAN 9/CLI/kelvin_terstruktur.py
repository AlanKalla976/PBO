print("Konversi Suhu Kelvin")
def get_celcius (suhu): 
    C = ( float(suhu)) - 273
    return C

def get_fahrenheit (suhu):
    R = (9/5 * float(suhu)) +32
    return R

def get_reamur(suhu):
    K = (4/5 * float(suhu)) -273
    return K

# Entry
suhu = input("Masukkan suhu dalam Kelvin:")

# rumus
F = get_celcius (suhu)
R = get_fahrenheit (suhu)
K = get_reamur (suhu)