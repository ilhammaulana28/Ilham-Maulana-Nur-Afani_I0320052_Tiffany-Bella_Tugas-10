import matematika.geometri2D

def main():
    sisi = 5

    luas = matematika.geometri2D.luasBujursangkar(sisi)

    print('BUJUR SANGKAR')
    print('PANJANG SISI\t:', sisi)
    print('LUAS\t\t:', luas)

if __name__ == '__main__':
    main()