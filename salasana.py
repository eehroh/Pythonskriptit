import random

chars = "abcdefghijklmnopqrstuvwxyzåäö1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ.@!"

pasw = ""

pituus = input("Valitse salasanan pituus: ")
pituus = int(pituus)
for c in range(pituus):
    pasw += random.choice(chars)
print(pasw)