# 1’den 100’e kadar sadece çift sayıları ekrana yazdırma (for)
print("*1'den 100'e kadar olan çift sayılar (for ile):")
for i in range(2, 101, 2):
    print(i)

# 1’den 100’e kadar sadece çift sayıları ekrana yazdırma (while)
print("\n*1'den 100'e kadar olan çift sayılar (while ile):")
sayi = 2
while sayi <= 100:
    print(sayi)
    sayi += 2
