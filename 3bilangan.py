bilangan_pertama=int(input("masukan bilangan :"))
bilangan_kedua=int(input("masukan bilangan :"))
bilangan_ketiga=int(input("masukan bilangan :"))

if bilangan_pertama > bilangan_kedua and bilangan_ketiga > bilangan_kedua:
    print(f"bilangan {bilangan_kedua} lebih kecil dari angka {bilangan_pertama} dan {bilangan_ketiga}")
elif bilangan_kedua > bilangan_pertama and bilangan_ketiga > bilangan_pertama:
    print(f"bilangan {bilangan_pertama} lebih kecil dari angka {bilangan_kedua} dan {bilangan_ketiga}")
elif bilangan_pertama > bilangan_ketiga and bilangan_kedua > bilangan_ketiga:
    print(f"bilangan {bilangan_ketiga} lebih kecil dari angka {bilangan_pertama} dan {bilangan_kedua}")
else:
    ("bilangan yang anda masukan sama")