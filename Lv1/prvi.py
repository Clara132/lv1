def total_euro(a, b):
    ukupno = a * b
    return ukupno

    
s = int(input("Unesite radne sate: "))
p = float(input("Unesite koliko ste plaćeni po radnom satu: "))

ukupno = total_euro(s, p)

print("Radni sati:",s,"h") 
print("Eura/h:", p)

print("Ukupno:",ukupno,"eura")