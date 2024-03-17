bilangan_pertama=int(input("masukan bilangan :"))
bilangan_kedua=int(input("masukan bilangan :"))

if bilangan_pertama > bilangan_kedua:
    print(f"bilangan {bilangan_pertama} lebih besar dari bilangan {bilangan_kedua}")
elif bilangan_kedua > bilangan_pertama:
    print(f"bilangan {bilangan_kedua} lebih besar dari bilangan {bilangan_pertama}")
else:
    print(f"bilangan {bilangan_pertama} sama besar dengan bilangan {bilangan_kedua}")

