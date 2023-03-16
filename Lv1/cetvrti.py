
fhand = open("2.txt")
brojac = 0
confidence = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        confidence += float(line.split(" ")[1])
        brojac += 1
print(float(confidence/brojac), "je srednja vrijednost")
