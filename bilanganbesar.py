a = int (input("masukan nilai anda :"))
b = int (input("masukan nilai anda :"))
c = int (input("masukan nilai anda :"))


if a > b and a > c:
    print(f"bilangan {a} lebih besar dibanding {b} dan {c}")
elif b > a and b > c:
    print(f"bilangan {b} lebih besar dibanding {a} dan {c}")
elif c > a and c > b:
    print(f"bilangan {c} lebih besar dibanding {a} dan {b}")
elif a == b > c:
    print(f"bilangan {a} sama dengan {b} tapi lebih besar dari {c}")
elif a == c > b:
    print(f"bilangan {a} sama dengan {c} tapi lebih besar dari {b}")
elif b == c > a:
    print(f"bilangan {b} sama dengan {c} tapi lebih besar dari {a}")
else:
    print("ketiga bilangan sama besar")