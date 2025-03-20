# 1'den 100'e kadar olan asal sayıları ekrana yazdıran program

print("* 1'den 100'e kadar olan asal sayılar (for döngüsü):")
for sayi in range(2, 101):
    asal = True
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print(sayi, end=" ")

print("\n\n* 1'den 100'e kadar olan asal sayılar (while döngüsü):")
sayi = 2
while sayi <= 100:
    asal = True
    bolen = 2
    while bolen < sayi:
        if sayi % bolen == 0:
            asal = False
            break
        bolen += 1
    if asal:
        print(sayi, end=" ")
    sayi += 1
