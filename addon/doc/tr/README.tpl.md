# NVDA için basit zamanlayıcı ve kronometre ${addon_version}

NVDA'ya doğrudan zamanlayıcı ve kronometre işlevi sağlar.  

## İndirme:

[NVDA için Basit Zamanlayıcı ve Kronometre ${addon_version} Eklentisini İndirin](${addon_url}/releases/download/${addon_version}/${addon_name}-${addon_version}.nvda-addon)

## zamanlayıcı ve kronometre:

Zamanlayıcı belirtilen bir zamandan 0'a kadar geri saymaya başlar. 0'a ulaştığında biter ve bir alarm çalınır.  

Bir kronometre 0'dan saymaya başlar ve durdurulana kadar devam eder. Bu esnada, geçen süre görüntülenir.  

## Özellikler:

### Basit yapılandırma iletişim kutusu:

Basit bir yapılandırma iletişim kutusundan zamanlayıcı veya kronometre yapılandırılabilir.  

Farklı ilerleme izleme istemleri de aynı iletişim kutusundan yapılandırılabilir.  

#### Nasıl çalışır?

Eklenti ayarları iletişim kutusunu açmak için "NVDA için Zamanlayıcı Ayarları" alt menüsünü kullanın veya NVDA + Shift + t tuşlarına basın.
Alt menü, NVDA'nın "Araçlar" menüsünde bulunabilir.  

* Bir zamanlayıcı veya kronometre çalışıyorsa şunları yapabilirsiniz:
    * Yapılandırma iletişim kutusunun durum çubuğunu okuyarak ilerlemeyi izleyin.
    * Zamanlayıcıyı veya kronometreyi duraklatın, devam ettirin veya durdurun.
* Zamanlayıcı veya kronometre durursa şunları yapabilirsiniz:
    * Yürütme modunu ayarlayın (zamanlayıcı veya kronometre)
    * Zamanlayıcı için başlangıç ​​zamanı ve ayrıca gösterge (saniye, dakika veya saat) için kullanılan zaman birimini ayarlayın.
    * Zamanlayıcıyı veya kronometreyi başlatın.
* İstediğiniz zaman şunları yapabilirsiniz:
    * İlerlemenin sesle mi, bip sesiyle mi, her ikisi ile mi yoksa hiçbiriyle mi gösterileceğini seçin.

### NVDA komutlarından çalıştırın

Herhangi bir zamanda, ayarlar iletişim kutusunu açmadan bir zamanlayıcı veya kronometreden başlatmak, durdurmak, duraklatmak, devam ettirmek ve ilerleme göstergeleri almak mümkündür.

#### Nasıl çalışır?

* Zamanlayıcıyı veya kronometreyi başlatmak veya durdurmak için ctrl + shift + NVDA + s tuşlarına basın.
    * Çalışan bir zamanlayıcı veya kronometre yoksa, mevcut ayar moduna göre bunlardan biri başlayacaktır.
    * Bunlardan biri çalışıyorsa duracaktır. Bir zamanlayıcı durdurulmuşsa, geçen süre bildirilecektir.
    *     Bir zamanlayıcı başlamaya çalışırsa ve yapılandırılmış bir başlangıç ​​zaman değeri yoksa, bir uyarı verilir.
* Bir zamanlayıcıyı veya kronometreyi duraklatmak veya devam ettirmek için ctrl + shift + NVDA + p tuşlarına basın.
* Zamanlayıcının veya kronometrenin ilerlemesini kontrol etmek için ctrl + shift + NVDA + r tuşlarına basın. Bu, özellikle tüm ilerleme göstergeleri kapalıysa ve talep üzerine ilerlemeyi sorgulamanız gerekiyorsa kullanışlıdır.

### Süre yazımı:

Yapılandırma iletişim kutusunda, zamanlayıcının başlangıç ​​zamanı SS:DD:SS biçiminde girilir; burada HH saat, MM dakika ve SS saniye anlamına gelir.  

Tam formatı yazmak gerekli değildir, sistem bunu algılayacaktır:

* Basit bir sayı girilirse, yapılandırılan zaman birimi kullanılacaktır.
* Alt birimler belirtilmişse bunlar dikkate alınacaktır. Örneğin, seçilen zaman birimi "dakika" ise 01:05 bir dakika beş saniye olur.
Seçilen zaman birimi "saat" ise, 01:05 bir saat, beş dakika ve sıfır saniye olur.
* "Saniye" altındaki alt birimler geçerli değildir. Zaman birimi "dakika" ise 01:05:02 değeri kabul edilmeyecektir.

### Çalışan zamanlayıcılar ve kronometreler:

Bir seferde yalnızca bir zamanlayıcı veya kronometre başlatılabilir.  

İlerleme, hiçbiri, bir veya daha fazla istem etkinleştirilerek, yapılandırma iletişim kutusunun durum çubuğu okunarak veya ilerleme istemi için NVDA'nın komutuna, ctrl+shift+NVDA+r'ye basılarak izlenebilir.  

Bu nedenle, tüm uyarıları kapalı tutarak bir zamanlayıcıyı veya kronometreyi etkinleştirmek ve ayarlar diyaloğu açıkken durum çubuğunu okuyarak ilerlemeyi izlemek tamamen mümkündür.  

Başlatma, durdurma, duraklatma, devam ettirme ve talep üzerine ilerleme göstergesi alma komutları, yapılandırma diyaloğu etkinken bile kullanılabilir.  

Yalnızca bir yapılandırma iletişim kutusu açık olabilir. İletişim kutusu kapatıldığında bir zamanlayıcı veya kronometre çalışıyorsa, yürütme normal şekilde devam eder.  

Bir zamanlayıcı veya kronometre çalışırken yapılandırma iletişim kutusu açılırsa, güncellenen bilgiler buna göre görüntülenecektir.  

### zaman doğruluğu:

Bu eklenti, zamanı son derece doğru bir şekilde sayma yeteneğine sahip değildir.  

Bunun nedeni, NVDA'nın yazıldığı programlama dili olan Python'un, bilgisayarda birden fazla işlemci veya işlemci çekirdeği mevcut olsa bile, aynı anda birden fazla komut çalıştıramamasıdır.  

Bu nedenle, NVDA her konuştuğunda, hesapladığında veya işlediğinde, zaman sayımına küçük bir gecikme eklenir.  

Bununla birlikte, milisaniye düzeyinde doğruluğun gerekli olduğu veya bazı yanlışlıkların bazı süreçleri ciddi şekilde etkilediği durumlar dışında, doğruluk durumların büyük çoğunluğu için yeterince kabul edilebilir olmalıdır.  

En iyi sonuçlar için, ilerleme göstergeleri kapalı tutulmalı ve ilerleme göstergesi için NVDA komutu, ctrl+shift+NVDA+r veya yapılandırma iletişim kutusunun durum çubuğu okunarak talep üzerine ilerleme talep edilmelidir.  

### ilerleme göstergeleri:

#### ses göstergesi:

Etkin olduğunda, bu gösterge, yapılandırma iletişim kutusunda yapılandırılan zaman birimine göre zamanlayıcı veya kronometre zaman sayımı her yuvarlak bir değere ulaştığında bip sesi çıkarır.  

Örneğin, bir zamanlayıcıyı saat 02:30'da başlayacak şekilde ayarladıysanız, geri sayım 02:00 dakika olduğunda bir bip sesi ve geri sayım 01:00 dakika olduğunda diğeri çalar.  

NVDA'nın ilerleme göstergesi komutu olan ctrl+shift+NVDA+r'yi kullanarak yapılandırma iletişim kutusunun durum çubuğunu okuyarak tam süreyi istediğiniz zaman kontrol edebilirsiniz.  

#### ses komutu:

Etkin olduğunda, bu gösterge, yapılandırma iletişim kutusunda yapılandırılan zaman birimine göre, yuvarlak bir değere her ulaştığında geçerli zaman sayımını söyler.  

Örneğin, bir zamanlayıcıyı 02:30 dakikada başlayacak şekilde ayarladıysanız, sayım 02:00 dakika olduğunda 2" ve sayım 01:00 dakika olduğunda "1" söylenecektir.  

NVDA'nın ilerleme göstergesi komutu olan ctrl+shift+NVDA+r'yi kullanarak yapılandırma iletişim kutusunun durum çubuğunu okuyarak tam süreyi istediğiniz zaman kontrol edebilirsiniz.  

### Zamanlayıcı tamamlama göstergesi:

Bir zamanlayıcı için zaman sayımı 0'a ulaştığında, zamanlayıcı tamamlanır. Bu olay, etkin yapılandırma iletişim kutusundan bağımsız olarak, gizli bir çalar saat sesiyle bildirilir. Bu ses, aktif olan herhangi bir ilerleme göstergesine bağlı değildir.  

### Kronometre tamamlama göstergesi:

Kronometre durdurulduğunda, aktif yapılandırma iletişim kutusundan bağımsız olarak geçen süre duyurulur.  

Son kronometre çalışmasının geçen süresi, yapılandırma iletişim kutusunun durum çubuğu kontrol edilerek veya NVDA+ctrl+shift+r tuşlarına basılarak herhangi bir zamanda kontrol edilebilir. Bu bilgi, yeni bir zamanlayıcı veya kronometre başlatıldığında sıfırlanır.  

### Girdi hareketlerini değiştirme:

NVDA menüsü/Tercihler/Girdi hareketleri/NVDA için Zamanlayıcı'da bir girdi hareketini, yani varsayılan olarak atanan mevcut komut tuş kombinasyonlarını değiştirebiliriz.  

Tuş kombinasyonunun başka bir işleve atanmadığını veya kullandığımız uygulamaların hiçbiriyle örtüşmediğini unutmayın.  

# eklentiyi çevirmeye veya geliştirmeye yardımcı olmak:

Eklentiyi çevirmeye veya geliştirmeye yardımcı olmak istiyorsanız, lütfen [proje deposuna](${addon_url}) erişin ve dilinize eşdeğer belge dizininde Contribute.md dosyasını bulun.

## Katkıda Bulunanlar:

Özellikle ..... 'ya teşekkür

*  Marlon Brandão de Sousa - Brezilya'dan Portekizce çeviri
* Angelo Miguel Abrantes - Portekizce Çeviri
* Tarik Hadžirović - Hırvatça çeviri
* Rémy Ruiz - Fransızca Çeviri
* Remy Ruiz - İspanyolca Çeviri
* Umut KORKMAZ - Türkçe çeviri
* Danil Kostenkov - Rusça çeviri
* Heorhii - Ukraynaca çeviri
* Brian Missao da Vera - NVDA 2022.1 uyumluluğu
* Edilberto - NVDA 2024.1 uyumluluğu
