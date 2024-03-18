a= int(input("Masukkan angka: "))

if a > 0 and  a %2 == 0:
    print(f"{a} bilangan Positif & Genap")
elif a > 0 and a %2 == 1:
    print(f"{a} bilangan Positif & Ganjil")
elif a < 0 and a %2 == 0:
    print(f"{a} bilangan Negatif & Genap")
elif a < 0 and a %1 == 0:
    print(f"{a} bilangan Negatif & Ganjil")
else:
    print (f"{a} bilangan Netral")