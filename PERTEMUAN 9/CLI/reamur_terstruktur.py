print("Konversi Suhu Reamur")
def get_celcius (suhu): 
    C = (9/4 * float(suhu)) + 32
    return C

def get_fahrenheit (suhu):
    R = (5/4 * float(suhu)) 
    return R

def get_kelvin(suhu):
    K = (5/4 * float(suhu)) -32 + 273
    return K

# Entry
suhu = input("Masukkan suhu dalam Reamur:")

# rumus
F = get_celcius (suhu)
R = get_fahrenheit (suhu)
K = get_kelvin (suhu)