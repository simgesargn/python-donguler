# Kullanıcının girdiği bir sayının faktöriyelini hesaplayan program

sayi = int(input("Lütfen bir sayı giriniz: "))

# For ile faktöriyel hesaplama
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i
print(f"{sayi}! = {faktoriyel} (for döngüsü)")

# While ile faktöriyel hesaplama
faktoriyel = 1
i = 1
while i <= sayi:
    faktoriyel *= i
    i += 1
print(f"{sayi}! = {faktoriyel} (while döngüsü)")

