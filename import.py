import geometri2D

p = 10
l = 8

luas = geometri2D.luasPersegiPanjang(p, l)
kel = geometri2D.kelilingPersegiPanjang(p, l)

print('PERSEGI PANJANG')
print('PANJANG\t:', p)
print('LEBAR\t:', l)
print('LUAS\t:', luas)
print('KELILING\t:', kel)

jarijari = 3

luasling = geometri2D.luasLingkaran(jarijari)
kelling = geometri2D.kelilingLingkaran(jarijari)

print('\nLINGKARAN')
print('JARI - JARI\t:', jarijari)
print('LUAS\t:', luasling)
print('KELILING\t:', kelling)