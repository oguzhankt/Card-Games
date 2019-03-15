from random import shuffle
import time


def deste_yarat():
    # Desteye daha sonra kart ekleyebilmek için örnek değer atar
    tur = ["Maça", "Kupa", "Sinek", "Karo"]
    deste = []

    for outer in tur:
        for inner in range(1, 14):
            deste.append({"tur": outer, "sayi": inner})

    shuffle(deste)
    return deste


def menu():

    cevap = 0  # While döngüsünün en az bir kere çalışması için

    while not((cevap == 1) or (cevap == 2) or (cevap == 3)):
        print("\nKart oyunlarına hoşgeldiniz :")
        print("1) Fal Bakma")
        print("2) Blackjack")
        print("3) Çıkış")
        cevap = int(input())

        if not((cevap == 1) or (cevap == 2) or (cevap == 3)):
            print("Hatalı seçenek girdiniz tekrar deneyiniz...")

    if cevap == 1:
        fal()
    elif cevap == 2:
        blackjack()
    else:
        cevap2 = "a"
        while not((cevap2.upper == "E") or (cevap2.upper == "H")):
            cevap2 = input("Çıkmak istediğinize eminmisiniz ? (E/H-e/h)")

            if cevap2 == "H" or cevap2 == "h":
                menu()
            elif cevap2 == "E" or cevap2 == "e":
                exit(0)
            else:
                print("Hatalı seçenek girdiniz tekrar deneyiniz...")


def fal():
    deste = deste_yarat()
    skor = 0  # Skorun kart çekerken sıfırlanmaması için burada tanımlanması gerekti
    input("Niyetinizi tuttunuz mu?")
    fal_say(deste, skor)


def kart_ekleme(deste, eklenecek_kartlar):
    # Eşlemeleri bitirdikten sonra kartları destenin altına ekler
    for i in range(len(eklenecek_kartlar)):
        deste.append(eklenecek_kartlar[i])
    return deste


def fal_kart_çek(deste, kart_sayisi, skor):
    ayrilan_kartlar = []  # Ortaya açılan kartları tutmak için bir liste

    for outer in range(kart_sayisi):
        for i in range(len(deste) - 1, len(deste) - 2, -1):
            input("Kart çekmek için ENTER a basınız")
            ayrilan_kartlar.append(deste[i])
            print(outer+1, ". Çekilen kart =", kart_isimlendirme(deste[i]))
        if deste[i]["sayi"] == outer + 1:
            print("Eşleşti saymaya yeniden başlanıyor\n*\n")

            # Puan kartını ayırmak için
            ayrilan_kartlar.remove(ayrilan_kartlar[outer])
            deste.remove(deste[i])

            deste = kart_ekleme(deste, ayrilan_kartlar)
            if outer + 1 > 10:
                skor += 10
            else:
                skor += outer + 1
            fal_say(deste,skor)
        else:
            deste.remove(deste[i])
    else:
        print("Eşleşme yok saymaya yeniden başlanıyor\n*\n")
        fal_say(deste,skor)
    return skor


def fal_say(deste, skor):

    if len(deste) >= 13:
        skor += fal_kart_çek(deste, 13, skor)
    elif 0 < len(deste) < 13:
        skor += fal_kart_çek(deste, len(deste), skor)
    else:
        print("Deste bitti....")
        print("Tuttuğunuz falın gerçekleşme ihtimali : %", skor)
        yeniden_sor()

51
def blackjack():
    deste = deste_yarat()
    dagitici_eli = []
    oyuncu_eli = []

    # Desteyi dağıtır
    for i in range(len(deste)-1, len(deste)-3, -1):
        dagitici_eli.append(deste[i])
        deste.remove(deste[i])

    for i in range(len(deste) - 1, len(deste) - 3, -1):
        oyuncu_eli.append(deste[i])
        deste.remove(deste[i])

    print("Dağıtıcının açık kartı :\n", kart_isimlendirme(dagitici_eli[0]))

    # Oyuncunun elini yazdrır
    print("Oyuncunun eli :")
    for i in range(len(oyuncu_eli)):
        print(kart_isimlendirme(oyuncu_eli[i]))

    print("Skorunuz : ", skor(oyuncu_eli))

    if "21" in skor(oyuncu_eli):
        print("Blackjack!!!")
        dagitici_oynat(dagitici_eli, deste)
    else:
        oyuncu_oynat(oyuncu_eli, deste)
        dagitici_oynat(dagitici_eli, deste)


    print("\nDağıtıcı skoru :", skor(dagitici_eli))
    print("Oyuncu skoru :", skor(oyuncu_eli))
    # Skorları karşılaştırır
    if int(skor(oyuncu_eli)[:2]) > int(skor(dagitici_eli)[:2]):
        print("Oyuncu KAZANDI!!!")
        yeniden_sor()
    elif int(skor(oyuncu_eli)[:2]) < int(skor(dagitici_eli)[:2]):
        print("Dağıtıcı KAZANDI!!!")
        yeniden_sor()
    else:
        print("İki tarafta eşit...")
        yeniden_sor()


def skor(kartlar):
    skor = 0
    as_varmi = False

    for i in range(len(kartlar)):
        if kartlar[i]["sayi"] == 1:
            as_varmi = True
            skor += 1
        elif kartlar[i]["sayi"] == 11 or kartlar[i]["sayi"] == 12 or kartlar[i]["sayi"] == 13:
            skor += 10
        else:
            skor += kartlar[i]["sayi"]

    if as_varmi:
        if skor > 21:
            skor_str = str(skor)
        else:
            skor_str = str(skor) + " yada " + str(skor + 10)
    else:
        skor_str = str(skor)

    return skor_str


def kart_isimlendirme(kart):
    kart_isim = ""

    # İlk olarak kartın ismini belirler
    if kart["sayi"] == 1:
        kart_isim = "As"
    elif kart["sayi"] == 11:
        kart_isim = "Joker"
    elif kart["sayi"] == 12:
        kart_isim = "Queen"
    elif kart["sayi"] == 13:
        kart_isim = "King"
    else:
        kart_isim += str(kart["sayi"])

    # Sonra kartın türünü ekler

    kart_str = kart["tur"] + " " + kart_isim
    return kart_str


def yeniden_sor():
    cevap = "a"
    while not((cevap.upper == "E") or (cevap.upper == "H")):
        cevap = input("Yeniden menuye donmek istemisiniz (E/H,e/h)?")

        if cevap == "e" or cevap == "E":
            menu()
        elif cevap == "h" or cevap == "H":
            exit(0)
        else:
            print("Hatalı seçenek girdiniz tekrar deneyiniz...")


def oyuncu_oynat(oyuncu_eli, deste):
    cevap = 0
    while cevap < 1 or cevap > 2 :
        cevap = int(input("Ne yapmak istersiniz :\n1)Kart çek\n2)Pas"))
        if cevap == 1:
            for i in range(len(deste) - 1, len(deste) - 2, -1):
                oyuncu_eli.append(deste[i])
                deste.remove(deste[i])

            # Oyuncunun elini yazdrır
            print("Oyuncunun eli :")
            for i in range(len(oyuncu_eli)):
                print(kart_isimlendirme(oyuncu_eli[i]))
            print("Skorunuz : ", skor(oyuncu_eli))
            if int(skor(oyuncu_eli)[:2]) > 21 :
                print("Battınız...")
                yeniden_sor()
            elif int(skor(oyuncu_eli)[:2]) == 21:
                print("21 yaptınız sıra dağıtıcıya geçiyor...")
                break
            # Tekrardan oyuncuya ne yapmak istediğini sorar
            else:
                oyuncu_oynat(oyuncu_eli, deste)
        elif cevap == 2:
            print("Sıra dağıtıcıya geçiyor...")
        else:
            print("Hatalı seçenek girdiniz tekrardan deneyiniz...")


def dagitici_oynat(dagitici_eli, deste):
    print("Dağıtıcı oynuyor...")
    time.sleep(2)
    # [:2] - dağıtıcının elinde as olsa bile string karşılaştırması yapılabilmesini sağlar
    if int(skor(dagitici_eli)[:2]) < 16:
        # Dağıtıcı skoru 16 dan kuçukse kart çeker
        for i in range(len(deste) - 1, len(deste) - 2, -1):
            dagitici_eli.append(deste[i])
            deste.remove(deste[i])
        print("Dağıtıcı kart çekti")
        if int(skor(dagitici_eli)[:2]) > 21:
            print("Dağıtıcı battı...")
            yeniden_sor()
        else:
            dagitici_oynat(dagitici_eli, deste)

    else:
        print("Dağıtıcı pas geçti")


menu()

