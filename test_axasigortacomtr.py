import requests


def test_checkpoint1():
    url = 'https://www.axasigorta.com.tr/'
    response = requests.get(url, verify=False)
    print(response.elapsed)
    assert response.status_code == 200



def test_checkpoint2():
    url = 'https://www.axasigorta.com.tr/acente-ara'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint3():
    url = 'https://www.axasigorta.com.tr/acente-basvurusu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint4():
    url = 'https://www.axasigorta.com.tr/anlasmali-kurumlar'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint5():
    url = 'https://www.axasigorta.com.tr/anlasmali-otomobil-servisleri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint6():
    url = 'https://www.axasigorta.com.tr/anlasmali-saglik-kurumlari'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint7():
    url = 'https://www.axasigorta.com.tr/arac-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint8():
    url = 'https://www.axasigorta.com.tr/arac-sigortasi/arti-trafik-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint9():
    url = 'https://www.axasigorta.com.tr/arac-sigortasi/buyuk-hasar-kasko-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint10():
    url = 'https://www.axasigorta.com.tr/arac-sigortasi/lacivert-kasko-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint11():
    url = 'https://www.axasigorta.com.tr/arac-sigortasi/maksimum-kasko-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint12():
    url = 'https://www.axasigorta.com.tr/arac-sigortasi/tutumlu-kasko-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint13():
    url = 'https://www.axasigorta.com.tr/arac-sigortasi/zorunlu-trafik-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint14():
    url = 'https://www.axasigorta.com.tr/axa-da-hayat'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint15():
    url = 'https://www.axasigorta.com.tr/axa-da-kariyer'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint16():
    url = 'https://www.axasigorta.com.tr/axa-dan-saglikta-bir-ilk-daha-axa-bagimsiz-yasam-hatti'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint17():
    url = 'https://www.axasigorta.com.tr/axa-doktor-danisma-hatti'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint18():
    url = 'https://www.axasigorta.com.tr/axa-go'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint19():
    url = 'https://www.axasigorta.com.tr/axawebonline/?ref=axasigorta'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint20():
    url = 'https://www.axasigorta.com.tr/AXAWebOnline/?returnUrl=http%3A%2F%2Fwww.axasigorta.com.tr%2FAXAWebOnline%2FHome%2FIndex'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint21():
    url = 'https://www.axasigorta.com.tr/aydinlatma-bildirimi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint22():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint23():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/2017de-dogru-fiyat-veren-kazanacak'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint24():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-10-kez-dunyanin-en-degerli-sigorta-markasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint25():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-7-yildir-dunyanin-en-iyi-sigorta-markasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint26():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-8-yildir-dunyanin-en-iyi-sigorta-markasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint27():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-9-2-milyar-dolar-marka-degeriyle--en-degerli-sigorta' \
          '-markasi '
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint28():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-acenteleri-google-premier-partners-projesi-ile-hizla-dijitallesiyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint29():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-acentelerini-dunya-dostu-acente-hareketine-davet-ediyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint30():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-acenteleri-telematik-teknolojisi-ile-gelistirilen-axa-go-icin-bulustu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint31():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-acenteleriyle-dijital-ortamda-bulusmaya-devam-ediyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint32():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-arastirma-fonu-ve-national-geographicten-daha-saglikli' \
          '-bir-gelecek-icin-isbirligi '
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint33():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-bir-ilk-tutumlu-saglik-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint34():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-bir-kez-daha-bloomberg-cinsiyet-esitligi-endeksinde'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint35():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-bkm-isbirligi-ile-islemler-artik-daha-guvenli'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint36():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-bolu-karabuk-bartin-zonguldak-ve-eregli-acenteleriyle-bulustu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint37():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axabottan-sorulara-aninda-yanit'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint38():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axaclub-avantajlar-dunyasi-axafitte'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint39():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axada-gorev-degisikligi-henri-de-castries-ceoluk-gorevini-thomas-buberle-devrediyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint40():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axadan-100-milyar-euro-gelir-axadan-rekor-gelir-axa-gelir-rekoru-kirdi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint41():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-dan-5-kisilik-grubunu-olusturan-herkese-sulale-indirimi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint42():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axadan-99-milyar-euro-gelir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint43():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-dan-covid-19-mucadelesine-destek'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint44():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-dan-dunya-dostu-sigortacilik'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint45():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-dan-filenin-sultanlarina-basari-primi-ve-olimpiyat-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint46():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axadan-kadinlara-yonelik-sigorta-ve-hizmetlere-destek'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint47():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axadan-kiymetini-kaybetmeden-bilenlere-yeni-reklam-kampanyasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint48():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-dan-saglik-sigortalilarinin-hayatini-kolaylastiracak-yepyeni-bir-hizmet'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint49():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axadan-seffaflik-damgasi-hasar-surecleri-anlik-ve-dijital-olarak-takip-edilecek'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint50():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-dan-sektorde-bir-ilk-sulale-indirimi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint51():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-dan-trafik-sigortasi-nda-bir-ay-bedava-kampanyasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint52():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axadan-turkiyede-bir-ilk-axa-go-ile-kisisellestirilmis-kasko-urunu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint53():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-dijital-asistan-ile-hizli-hasar-tespiti'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint54():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-dow-jones-surdurulebilirlik-endeksinde-yukseldi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint55():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-icin-sigorta-gelisime-hizmet-eden-bir-guc'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint56():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-iyi-yasam-icin-ayse-tolga-ile-anlasti'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint57():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-kadin-girisimcileri-destekliyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint58():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-mersindeki-acenteleriyle-bulustu-axa-sigortadan-guclu-bolge-stratejisi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint59():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axanin-milyonerler-kulubu-lizbonda-bulustu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint60():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sagligim-uygulamasinin-bir-elinde-alti-marifet'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint61():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-seyahat-saglik-sigortasi-bkm-express-ile-1-tl'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint62():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-125-yasinda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint63():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-2016da-3-6-milyar-tl-prim-uretimi-ile-16-buyudu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint64():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-2017-guclu-ve-surdurebilir-bir-performansla-tamamlandi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint65():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-2021-de-de-sigorta-4-0-ile-buyumeye-devam-edecek'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint66():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-3-kez-turkiyenin-en-etik-sirketi-secildi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint67():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-4-vizyonunu-acentelerine-anlatmak-icin-yolda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint68():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-acente-bulusmalari-cevrimici-olarak-devam-ediyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint69():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-aktif-yasam-dernegi-ve-www-turkiye-den-ortak-proje'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint70():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-a-milli-erkek-voleybol-takimina-ozel-mars'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint71():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-besinci-kez-turkiyenin-en-iyi-isverenlerinden-biri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint72():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-bir-kez-daha-turkiyenin-en-etik-sirketleri-arasinda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint73():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-bolge-mudurlugu-yeni-yerinde-hizmete-basladi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint74():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-calisanlar%C4%B1-icin-guvenle-calisabilecekleri-bir-ofis-ortami-hazirlaniyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint75():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-calisanlari-daha-iyi-yasam-hedefiyle-bir-arada'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint76():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-calisanlarinin-sagligina-da-onem-veriyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint77():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-ceosu-guillaume-lejeune--bolge-toplantilarinda-unlu-ekonomist-emre-alkini-agirladi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint78():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-dan-anlamli-mesaj-kadinlar-guldukce-hepimiz-gucluyuz'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint79():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-dan-axa-ile-evde-kal-canli-yayin-servisi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint80():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortadan-babalar-gunu-hediyesi-10-indirimli-tamamlayici-saglik-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint81():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-dan-bir-ay-bedava-kampanyasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint82():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-dan-calisanlarina-ozel-kendine-iyi-bak-programi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint83():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-dan-doktor-danisma-hatti-hizmeti'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint84():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-dan-gelecegin-voleybolcularina-egitim-bursu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint85():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortadan-kadin-girisimcilere-ozel-sigorta'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint86():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-dan-maksimum-kasko-ile-axa-go-avantaji'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint87():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortadan-telefon-kazasina-son-reklam-filmi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint88():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortada-ust-duzey-atama'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint89():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortada-ust-duzey-atama-firuz-iscan'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint90():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-david-kohen-koleksiyonu-ile-sigortacilik-tarihini-sergiliyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint91():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-dijital-asistan-ve-yerinde-cam-degisimi-hasar-aninda-musterilerinin-yaninda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint92():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-efeler-ligi-resmi-isim-sponsoru-oldu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint93():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-en-begenilen--sigorta-sirketi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint94():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-evdekibakicim-is-birligi-ile-ebeveynlere-destek-oluyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint95():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-gelecek-fakultesi-ilk-mezunlarini-verdi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint96():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-greenbox-teknolojisi-kullanarak-acenteleri-ile-bir-araya-geldi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint97():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-genclerle-birlikte-insanligin-gelisimi-icin-hareket-ediyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint98():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-guclu-bolge-stratejisini-denizlili-acenteleri-ile-paylasti'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint99():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-iklim-co-cozumleri-ile-musteri-memnuniyetini-arttiracak'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint100():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-hopili-ilk-ve-tek-sigorta-sirketi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint101():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-iklim-degisikligine-karsi-parametrik-urunlerle-koruyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint102():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-ile-evdekibakicim-online-servisi-benzersiz-bir-is-ortakligi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint103():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-insanligin-gelisimi-adina-insanlar-icin-onemli-olani-korumaya-devam-ediyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint104():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-itu-cekirdek-te-gelecegi-sekillendiren-girisimlere-destek-veriyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint105():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-kadinin-guclenmesi-prensipleri-weps-sozlesmesini-imzaladi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint106():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-kaskoda-mukemmel-sirket'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint107():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-kupa-voleyin-ana-sponsoru-oldu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint108():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortalilar-global-gucun-birer-parcasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint109():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-marka-spor-zirvesinde-basarili-sponsorluklarini-anlatti'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint110():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-musteri-anketinde-zirvede'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint111():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortanin-iyi-yasam-uygulamasi-axafit-yenilendi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint112():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortanin-mukemmel-kaskosuyla-tanisin'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint113():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortanin-pr-ajansi-sobraz-oldu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint114():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortanin-yeni-ceosu-yavuz-olken'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint115():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortanin-yeni-kampanyasi-sagligim-tamam-yayinda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint116():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-pandemide-de-ek-hizmetlerle-sigortalilarinin-yaninda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint117():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-renault-ve-dacia-araclarina-ozel-anlasmali-marka-kasko-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint118():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-sektorun-ilk-online-acente-toplantisi-ile-kesintisiz-iletisime-devam-ediyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint119():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-sel-ve-dolu-magdurlarinin-yaninda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint120():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-tum-salgin-hastaliklari-teminat-altina-aldi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint121():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-tum-yollar-iklim-krizine-cikiyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint122():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-ve-gurgen-oz-dert-varsa-derman-axada-bulustu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint123():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-ve-nissan-dan-niskasko-ile-araciniza-orijinal-koruma'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint124():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortaya-5-odul-daha'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint125():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-yarinin-musterisine-hazir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint126():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortaya-sagligim-tamam-sigortasi-ile-effie-odulu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint127():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortaya-stevie-awardsdan-tam-yedi-odul'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint128():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-yerinde-cam-degisimi-ve-ucretsiz-vale-cekici-hizmeti'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint129():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigortayla-sagliginizi-sansa-birakmayin'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint130():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-stratejik-yolculugunun-yeni-asamasini-uygulamak-uzere-yaptigi-ust-duzey-liderlik-degisikliklerini-duyurdu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint131():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-tamamlayici-saglik-sigortasinda-liderligini-surduruyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint132():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-telefon-kazasina-son-dedi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint133():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-ve-unicef-suriyeli-cocuklar-icin-elele'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint134():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axaya-yedinci-kez-insana-saygi-odulu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint135():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-xl-group-satin-aldi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint136():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-yine-turkiyenin-en-iyi-isvereni'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint137():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/doktorlara-soru-sormanin-en-kolay-yolu-axafit-te'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint138():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/en-yenilikci-ve-en-cok-tercih-edilen-sigorta-markasi-axa'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint139():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/finansal-sonuclar'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint140():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/gurgen-oz-ve-axa-sigortadan--mini-komedi-tadinda-filmler-gurgen-oz-yine-kahkahaya-bogacak'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint141():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/iklim-degisikligine-karsi-ormanlara-destek-axa-dan-tema-vakfina-25-bin-fidan-2'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint142():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/is-guvenligi-ile-ilgili-onlemler-ekonomik-kosullara-bagli-olmaksizin-alinmali'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint143():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/istanbulda-yasanan-afet-sigortali-olmanin-onemini-bir-kez-daha-gosterdi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200



def test_checkpoint144():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/musteriler-puanliyor-axa-sigorta-yayinliyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint145():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/sagligim-tamam-sigortasi-ile-sagligimiz-axa-sigorta-ya-emanet'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint146():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/sigortacilik-sektoru-ve-sanayi-4-0'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint147():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/sigorta-risk-teftislerinde-bir-ilk-axa-drone-kullaniyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint148():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/sigorta-sektorunun-en-itibarlisi-axa-sigorta'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint149():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/sinema-sektoru-axa-guvencesi-altinda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint150():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/tuketicilere-gore-sigorta-sektorunde-en-teknolojik-markasi-axa-sigorta'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint151():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/turkiye-axa-grubu-icin-onemli-bir-buyume-alani'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint152():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/turkiye-de-bir-ilk'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint153():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/turkiyenin-super-markalari-arasinda-yer-alan-tek-sigorta-sirketi-axa-sigorta'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint154():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/ust-uste-9-kez-dunyanin-bir-numarali-sigorta-markasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint155():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/yeni-babalara-4-hafta-izin'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint156():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=1'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint157():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=2'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint158():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=3'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint159():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=4'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint160():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=5'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint161():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=6'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint162():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=7'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint163():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=8'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint164():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=9'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint165():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=10'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint166():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=11'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint167():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=12'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint168():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=13'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint169():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=14'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint170():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=15'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint171():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=16'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint172():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=17'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint173():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=18'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint174():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=19'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint175():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=20'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint176():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=21'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint177():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=22'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint178():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri?sayfa=23'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint179():
    url = 'https://www.axasigorta.com.tr/bireysel-islemler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint180():
    url = 'https://www.axasigorta.com.tr/biz-kimiz/axa-global'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint181():
    url = 'https://www.axasigorta.com.tr/biz-kimiz/finansal-bilgiler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint182():
    url = 'https://www.axasigorta.com.tr/biz-kimiz/marka-amacimiz'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint183():
    url = 'https://www.axasigorta.com.tr/biz-kimiz/medya-odasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200
    assert response.elapsed


def test_checkpoint184():
    url = 'https://www.axasigorta.com.tr/blog/10-soruda-tamamlayici-saglik-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint185():
    url = 'https://www.axasigorta.com.tr/blog/60-yas-saglik-sigortasi-detaylari-nelerdir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint186():
    url = 'https://www.axasigorta.com.tr/blog/7-maddede-bireysel-emeklilik-nedir-ne-degildir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint187():
    url = 'https://www.axasigorta.com.tr/blog/ailece-izleyebileceginiz-en-guzel-filmler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint188():
    url = 'https://www.axasigorta.com.tr/blog/aileniz-ile-geleneksel-yilbasi-eglenceleri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint189():
    url = 'https://www.axasigorta.com.tr/blog/arabanizla-uzun-yola-cikmadan-once-yapmaniz-gerekenler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint190():
    url = 'https://www.axasigorta.com.tr/blog/araciniza-kar-zinciri-nasil-takilir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint191():
    url = 'https://www.axasigorta.com.tr/blog/arac-muayenesi-rehberi-muayene-oncesi-ve-sonrasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint192():
    url = 'https://www.axasigorta.com.tr/blog/avrupada-ziyaret-etmeniz-gereken-sehirler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint193():
    url = 'https://www.axasigorta.com.tr/blog/bagisiklik-sistemizinizi-guclendirmek-icin-besin-onerileri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint194():
    url = 'https://www.axasigorta.com.tr/blog/binaniz-depreme-hazir-mi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint195():
    url = 'https://www.axasigorta.com.tr/blog/ciftciler-icin-devlet-destekli-tarim-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint196():
    url = 'https://www.axasigorta.com.tr/blog/cocugunuz-ergenlige-giriyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint197():
    url = 'https://www.axasigorta.com.tr/blog/cok-gec-olmasin-ev-yanginlarini-onlemenin-yollari'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint198():
    url = 'https://www.axasigorta.com.tr/blog/daha-hareketli-bir-hayat-mumkun'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint199():
    url = 'https://www.axasigorta.com.tr/blog/dask-hasar-tespiti-nasil-yapilir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint200():
    url = 'https://www.axasigorta.com.tr/blog/dask-ile-konut-sigortasinin-farklari-nelerdir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint201():
    url = 'https://www.axasigorta.com.tr/blog/dask-nedir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint202():
    url = 'https://www.axasigorta.com.tr/blog/dask-nedir-konut-sigortasindan-ne-farki-var'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint203():
    url = 'https://www.axasigorta.com.tr/blog/deprem-cantasi-hazirlarken-nelere-dikkat-edilmelidir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint204():
    url = 'https://www.axasigorta.com.tr/blog/dis-sagligi-semptomlar-ve-sebepleri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint205():
    url = 'https://www.axasigorta.com.tr/blog/dogal-afetlerin-yarattigi-hasari-dusunmeyin'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint206():
    url = 'https://www.axasigorta.com.tr/blog/dunya-icin-harekete-gec'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint207():
    url = 'https://www.axasigorta.com.tr/blog/en-guzel-kayak-merkezleri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint208():
    url = 'https://www.axasigorta.com.tr/blog/en-sik-gorulen-bahar-hastaliklari-ve-alinabilecek-onlemler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint209():
    url = 'https://www.axasigorta.com.tr/blog/evde-calisirken-verimliliginizi-artiracak-oneriler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint210():
    url = 'https://www.axasigorta.com.tr/blog/evde-ekmek-yapmak-isteyenlere-oneriler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint211():
    url = 'https://www.axasigorta.com.tr/blog/evde-kaliteli-zaman-gecirmek-icin-oneriler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint212():
    url = 'https://www.axasigorta.com.tr/blog/evden-calisirken-is-ve-yasam-dengesini-saglamak'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint70():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-a-milli-erkek-voleybol-takimina-ozel-mars'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint213():
    url = 'https://www.axasigorta.com.tr/blog/evde-spor-ve-egzersiz-yapmak'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint214():
    url = 'https://www.axasigorta.com.tr/blog/evdeyken-ev-islerini-duzenleme-rehberi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint215():
    url = 'https://www.axasigorta.com.tr/blog/evdeyken-ic-huzuru-yakalamak'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint216():
    url = 'https://www.axasigorta.com.tr/blog/evinizden-cikmadan-katilabileceginiz-online-etkinlikler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint217():
    url = 'https://www.axasigorta.com.tr/blog/ferdi-kaza-sigortasi-nedir-ne-ise-yarar'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint218():
    url = 'https://www.axasigorta.com.tr/blog/grip-asisi-ile-ilgili-bilmeniz-gerekenler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint219():
    url = 'https://www.axasigorta.com.tr/blog/gunes-hapini-duydunuz-mu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint220():
    url = 'https://www.axasigorta.com.tr/blog/hangi-mulklere-konut-sigortasi-yaptirilabilir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint221():
    url = 'https://www.axasigorta.com.tr/blog/hayati-iskalamadan-para-biriktirme-yontemleri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint222():
    url = 'https://www.axasigorta.com.tr/blog/ikinci-el-arac-alip-satarken-yapmaniz-gerekenler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint223():
    url = 'https://www.axasigorta.com.tr/blog/insurtech-nedir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint224():
    url = 'https://www.axasigorta.com.tr/blog/is-yerinize-sigorta-yaptirirken-dikkat-edilmesi-gereken-5-sey'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint83():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-dan-doktor-danisma-hatti-hizmeti'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint225():
    url = 'https://www.axasigorta.com.tr/blog/karbon-emisyonu-yakit-tuketimi-kuresel-isinma-iklim-degisimi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint226():
    url = 'https://www.axasigorta.com.tr/blog/kentsel-donusum-surecinde-bilinmesi-gerekenler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint227():
    url = 'https://www.axasigorta.com.tr/blog/kira-sozlesmesi-yaparken-dikkat-edilmesi-gerekenler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint228():
    url = 'https://www.axasigorta.com.tr/blog/kis-aylarinda-hastaliktan-korunmak-icin-ne-yapilmali'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint229():
    url = 'https://www.axasigorta.com.tr/blog/kisisel-finans-yonetiminde-en-sik-yapilan-6-hata'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint230():
    url = 'https://www.axasigorta.com.tr/blog/kis-mevsiminde-arac-surme-rehberi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint231():
    url = 'https://www.axasigorta.com.tr/blog/konut-sigortasinin-maliyetini-belirleyen-5-sey'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint232():
    url = 'https://www.axasigorta.com.tr/blog/kopek-sahiplenmek'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint233():
    url = 'https://www.axasigorta.com.tr/blog/korkunun-kokusu-var-midir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint234():
    url = 'https://www.axasigorta.com.tr/blog/minik-amsterdam-utrecht-hollanda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint235():
    url = 'https://www.axasigorta.com.tr/blog/neden-hayat-sigortasi-yaptirmalisiniz-riske-karsi-onlem'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint236():
    url = 'https://www.axasigorta.com.tr/blog/organik-gidalar-gercekten-daha-faydali-mi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint237():
    url = 'https://www.axasigorta.com.tr/blog/orta-yas-krizi-ile-nasil-mucadele-edersiniz'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint238():
    url = 'https://www.axasigorta.com.tr/blog/otobanda-arabaniz-bozulursa-ne-yapmalisiniz'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint239():
    url = 'https://www.axasigorta.com.tr/blog/ozel-saglik-sigortasi-yaptirdiginizda-hayatinizda-degisecek-5-sey'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint240():
    url = 'https://www.axasigorta.com.tr/blog/romada-yapmaniz-gereken-seyler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint241():
    url = 'https://www.axasigorta.com.tr/blog/saglikli-bir-yasam-icin-dikkat-etmeniz-gerekenler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint242():
    url = 'https://www.axasigorta.com.tr/blog/schengen-vizesi-almak-icin-yapmaniz-gerekenler-2019'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint243():
    url = 'https://www.axasigorta.com.tr/blog/sifir-kilometre-arac-yeni-arac-almak-arac-ruhsati-yeni-arac-icin-sigorta-zorunlu-trafik-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint244():
    url = 'https://www.axasigorta.com.tr/blog/sitede-yasamanin-avantajlari-ve-dezavantajlari'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint245():
    url = 'https://www.axasigorta.com.tr/blog/soya-proteinin-faydalari'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint246():
    url = 'https://www.axasigorta.com.tr/blog/subliminal-mesajlar-sizi-satin-almaya-tesvik-ediyor-mu'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint247():
    url = 'https://www.axasigorta.com.tr/blog/su-tasarrufu-yaparak-dunyayi-kurtarin'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint248():
    url = 'https://www.axasigorta.com.tr/blog/tamamlayici-saglik-sigortasi-nedir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint249():
    url = 'https://www.axasigorta.com.tr/blog/tamamlayici-saglik-sigortasi-nedir-neleri-kapsar'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint250():
    url = 'https://www.axasigorta.com.tr/blog/tamamlayici-saglik-sigortasi-vergi-indiriminden-kimler-faydalanabilir'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint251():
    url = 'https://www.axasigorta.com.tr/blog/toprak-anaya-saygi-ile-ciftcilere-duyurulur-tarim-sigortasi-yaptirin'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint252():
    url = 'https://www.axasigorta.com.tr/blog/trafik-kazalari-hakkinda-istatistikler-2018'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint253():
    url = 'https://www.axasigorta.com.tr/blog/trafik-sigortasindan-kaskoya-7-axa-arac-sigortasi-teklifi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint254():
    url = 'https://www.axasigorta.com.tr/blog/turkiyede-ilk-axa-cep-telefonu-sigortasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint255():
    url = 'https://www.axasigorta.com.tr/blog/tutumlu-ozel-saglik-sigortasi-neden-onemli'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint256():
    url = 'https://www.axasigorta.com.tr/blog/uzak-durmaniz-gereken-gida-katkilari'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint257():
    url = 'https://www.axasigorta.com.tr/blog/vizesiz-gidilebilecek-ulkeler-2019-ve-buralarda-yapabilecekleriniz'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint257():
    url = 'https://www.axasigorta.com.tr/blog/vizesiz-gidilebilecek-ulkeler-2019-ve-buralarda-yapabilecekleriniz'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint258():
    url = 'https://www.axasigorta.com.tr/blog/yemek-tutkunlarina-alabileceginiz-hediyeler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint259():
    url = 'https://www.axasigorta.com.tr/blog/yeni-bir-is-yeri-kurarken-dikkat-edilmesi-gerekenler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint120():
    url = 'https://www.axasigorta.com.tr/basin-bultenleri/axa-sigorta-tum-salgin-hastaliklari-teminat-altina-aldi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint260():
    url = 'https://www.axasigorta.com.tr/blog/yeni-nesil-hard-diskler-helyum-ile-calisiyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint261():
    url = 'https://www.axasigorta.com.tr/blog/yurt-disi-seyahat-saglik-sigortasi-ile-evden-uzakta-guvence'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint262():
    url = 'https://www.axasigorta.com.tr/blog/zorunlu-bes-hakkinda-yanlis-bilinenler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint263():
    url = 'https://www.axasigorta.com.tr/blog/zorunlu-trafik-sigortasi-ne-zaman-yapilmali'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint264():
    url = 'https://www.axasigorta.com.tr/blog/zorunlu-trafik-sigortasi-ve-kasko-farklar-neler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint265():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=1'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint266():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=2'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint267():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=3'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint268():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=4'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint269():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=5'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint270():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=6'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint271():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=7'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint272():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=8'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint273():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=9'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint274():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=10'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint275():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=11'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint276():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=12'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint277():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=13'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint278():
    url = 'https://www.axasigorta.com.tr/blog?sayfa=14'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint279():
    url = 'https://www.axasigorta.com.tr/CepOnline/'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint280():
    url = 'https://www.axasigorta.com.tr/DegerKaybi/HasarForm.aspx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint281():
    url = 'https://www.axasigorta.com.tr/degerlerimiz'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint282():
    url = 'https://www.axasigorta.com.tr/diger-urunler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200

