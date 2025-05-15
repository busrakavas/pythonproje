#HASTA TC VE İSİM GİRİŞİ İLE YENİ HASTA KAYDI YAPAN
#BÖLÜMLERİNE GÖRE KAYITLI DOKTORLARDAN RANDEVU OLUŞTURAN
#OLUŞTURULAN RANDEVUNUN İPTALİNİ YAPAN BİR BASİT HASTANE OTOMASYONUDUR.

#ADMİN GİRİŞİ İÇİN 3 HAK VERİLMEKTE VE HATALI GİRİŞ SONUCUNDA OTOMASYONDAN ÇIKILIR
def admingiris():
    admin_kullanici_adi="admin"
    admin_sifre="123"
    hak=3
    while hak>0:
        kullanici_adi=input("Kullanıcı adı giriniz:")
        sifre=input("Şifre giriniz")

        if kullanici_adi==admin_kullanici_adi and sifre==admin_sifre:
            print("Giriş başarılı")
            return True
        else:
            hak-=1
            print("Hatalı giriş")
    print("Program sonlandırılıyor")
    return False
if not admingiris():
    exit()


class Kisi:
    def __init__(self, tc, isim):
        self.tc = tc
        self.isim = isim

class Hasta(Kisi):
    def __init__(self, tc, isim):
        super().__init__(tc, isim)

class Doktor:
    def __init__(self, isim, bolum):
        self.isim = isim
        self.bolum = bolum

class Randevu:
    def __init__(self, hasta, doktor, tarih):
        self.hasta = hasta
        self.doktor = doktor
        self.tarih = tarih

#DOKTORLAR BÖLÜMLERİNE GÖRE TANIMLANIR

bolumler = {
    "Dahiliye" : [Doktor("Ahmet S.","Dahiliye"),
                          Doktor("Selen K.","Dahiliye")],
            "Kardiyoloji": [Doktor("Elif Ş.","Kardiyoloji"),
                            Doktor("Karsu T.","Kardiyoloji")],
            "Göz Hastalıkları":[Doktor("Tamer K.","Göz Hastalıkları"),
                                Doktor("Ayşe U.","Göz Hastalıkları")],
            "Ortopedi": [Doktor("Necati A.",  "Ortopedi"),
                         Doktor("Ahmet G.",  "Ortopedi")],
            "Nöroloji": [Doktor("Canan Y.",  "Nöroloji"),
                         Doktor("Bahadır K.", "Nöroloji")],
            "Dermatoloji": [Doktor("Selma E.K.", "Dermatoloji"),
                            Doktor("Murat Z.", "Dermatoloji")],
            "Psikiyatri": [Doktor("Ecem M.", "Psikiyatri"),
                           Doktor("Serdar H.",  "Psikiyatri")],
            "Genel Cerrahi": [Doktor("Kenan S.", "Genel Cerrahi"),
                           Doktor("Canan T.", "Genel Cerrahi")]

}
hastalar = []
randevular = []

#HASTA KAYIT İLE HASTALAR LİSTESİNE EKLEME YAPILIR
def hasta_kayit():
    tc = input("Hasta TC: ")
    isim = input("Hasta Adı Soyadı: ")
    yeni_hasta = Hasta(tc, isim)
    hastalar.append(yeni_hasta)
    print(f"{isim} adlı hasta kaydedilmiştir.")

def hasta_listele():
    if not hastalar:
        print("Kayıtlı hasta bulunmamaktadır.")
        return
    print("\n Kayıtlı Hastalar:")
    sira=1
    for h in hastalar:
        print(f"{sira}. TC:{h.tc}, İsim-Soyisim:{h.isim}"),
        sira+=1



def doktorlari_listele():
    for bolum in bolumler:
        print(f"\n{bolum}:")
        for doktor in bolumler[bolum]:
            print(f" - {doktor.isim}")

#RANDEVU OLUŞTURULURKEN HASTA TCSİ SORDURULUR, KAYITLI İSE DEVAM EDİLİR, DEĞİLSE UYARI VERİR.
def randevu_olustur():
    tc = input("Hasta TC: ")
    hasta = None
    for h in hastalar:
        if h.tc == tc:
            hasta = h
            break

    if hasta is None:
        print("Hasta bulunamadı. Önce hasta kaydı yapmalısınız.")
        return

    print("\nBölümler:")
    bolum_adlari = list(bolumler.keys())
    sira = 1
    for bolum in bolum_adlari:
        print(f"{sira}. {bolum}")
        sira += 1

    secim = int(input("Bölüm seçiniz (1-6): "))
    if secim < 1 or secim > len(bolum_adlari):
        print("Geçersiz seçim.")
        return

    secilen_bolum = bolum_adlari[secim - 1]

    print("\nDoktorlar:")
    doktor_listesi = bolumler[secilen_bolum]
    sira = 1
    for doktor in doktor_listesi:
        print(f"{sira}. {doktor.isim}")
        sira += 1

    dr_secim = int(input("Doktor seçiniz (1-2): "))
    if dr_secim < 1 or dr_secim > len(doktor_listesi):
        print("Geçersiz seçim.")
        return

    secilen_doktor = doktor_listesi[dr_secim - 1]
    tarih = input("Randevu tarihi (GG/AA/YYYY): ")

    yeni_randevu = Randevu(hasta, secilen_doktor, tarih)
    randevular.append(yeni_randevu)

    print("\n✅ Randevunuz Oluşturulmuştur")
    print(f"Hasta: {hasta.isim}")
    print(f"Doktor: {secilen_doktor.isim}")
    print(f"Bölüm: {secilen_doktor.bolum}")
    print(f"Tarih: {tarih}")

def randevu_iptal():
    tc = input("Randevusu iptal edilecek hastanın TC'sini giriniz: ")
    iptal_edilen = None
    for r in randevular:
        if r.hasta.tc == tc:
            iptal_edilen = r
            break

    if iptal_edilen:
        randevular.remove(iptal_edilen)
        print("Randevu iptal edilmiştir.")
    else:
        print("Bu TC'ye ait randevu bulunamadı.")

def menu():
    while True:
        print("\n----- HASTANE OTOMASYONUNA HOŞGELDİNİZ -----")
        print("1. Hasta Kaydı")
        print("2. Doktor Listesi")
        print("3. Randevu Oluştur")
        print("4. Randevu İptal")
        print("5. Hastaları Listele")
        print("6. Çıkış")

        secim = input("Seçiminiz: ")
        if secim == "1":
            hasta_kayit()
        elif secim == "2":
            doktorlari_listele()
        elif secim == "3":
            randevu_olustur()
        elif secim == "4":
            randevu_iptal()
        elif secim == "5":
            hasta_listele()
        elif secim == "6":
            print("Hastane otomasyonundan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

menu()
#BÜŞRA KAVAS