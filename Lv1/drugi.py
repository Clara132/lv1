try:

    ocjena = float(input("Unesite ocjenu između intervala [0.0 i 1.0]: "))

    if ocjena < 0.0 or ocjena > 1.0:
        print("Ocjena nije unutar intervala [0.0 i 1.0]")
    elif ocjena >= 0.9:
        print("Vaša ocjena je A")
    elif ocjena >= 0.8:
        print("Vaša ocjena je B")
    elif ocjena >= 0.7:
        print("Vaša ocjena je C")
    elif ocjena >= 0.6:
        print("Vaša ocjena je D")
    else:
        print("Vaša ocjena je F")

except:
    print("Greška! Niste unijeli odgovarajuću ocjenu")
