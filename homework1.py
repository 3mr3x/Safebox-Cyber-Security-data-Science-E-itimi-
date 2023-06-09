def kullanici_kayit():
    kullanici_bilgi = {}
    kullanici_adi = input("Kullanici adini giriniz: ")
    kullanici_sifre = input("Kullanici sifresini giriniz: ")

    kullanici_bilgi["kullanici_adi"] = kullanici_adi
    kullanici_bilgi["kullanici_sifre"] = kullanici_sifre

    with open("kullanici_bilgileri.txt", "a") as f:
        f.write(kullanici_bilgi["kullanici_adi"]+","+kullanici_bilgi["kullanici_sifre"]+"\n")

    print("Kullanici kayit edildi!")

def giris():
    kullanici_adi = input("Kullanici Adi: ")
    sifre = input("Şifre: ")

    with open("kullanici_bilgileri.txt", "r") as dosya:
        for satir in dosya:
            dosya_kullanici_adi, dosya_sifre = satir.strip().split(",")

            if kullanici_adi == dosya_kullanici_adi and sifre == dosya_sifre:
                print("Giriş yapildi")
                return

    print("Bilgiler yanliş")


while True:
    secim = int(input("1-Kayit, 2-Giris, 3-Cikis"))

    if secim == 1:
        kullanici_kayit()
    elif secim == 2:
        giris()
        pass
    elif secim == 3:
        print("Cikis yapiliyor.")
        break
    else:
        print("Yanlis secim yaptiniz!")
