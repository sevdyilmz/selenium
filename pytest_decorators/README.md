Pytest_Decorators
Decorator'ler, testlerin davranışını ve işleyişini özelleştirmek için kullanılır. İşte pytest'te sıkça kullanılan decorator'lerin bir listesi ve her birinin kısa açıklaması:

@pytest.fixture: Testlerin başında veya sonunda belirli bir durum sağlamak için kullanılır. Bu durum, veritabanı bağlantısı, test verisi oluşturma veya dış kaynaklarla etkileşim gibi işlemleri içerebilir. Fixture'lar, test fonksiyonları içinde parametre olarak kullanılabilir.

@pytest.mark.parametrize: Bir test fonksiyonunu birden çok kez belirli parametrelerle çalıştırmak için kullanılır. Her bir parametre seti, test fonksiyonuna ayrı bir çağrı olarak aktarılır ve test sonuçları ayrı ayrı raporlanır.

@pytest.mark.skip: Bir test fonksiyonunun geçici olarak atlanmasını sağlar. Testin henüz uygulanmamış veya geçici olarak devre dışı bırakılmış olduğu durumlarda kullanılabilir.

@pytest.mark.xfail: Bir testin bilerek başarısız olabileceğini belirtir. Yani, testin hata üretmesi beklenir ve bu hata testin başarısız olmasını önlemez. Genellikle hata düzeltme sürecinde kullanılır.

@pytest.mark.skipif: Belirli bir koşulun doğru olması durumunda bir testin atlanmasını sağlar. Örneğin, belirli bir Python sürümünde veya işletim sisteminde bir testin çalışmaması gerekiyorsa bu decorator kullanılabilir.

@pytest.mark.usefixtures: Belirli bir fixture'ın bir test fonksiyonunda otomatik olarak kullanılmasını sağlar. Bu, test fonksiyonu içinde belirtilen fixture'ın çağrılmasını sağlar.

@pytest.mark.timeout: Bir testin maksimum süresini belirler. Eğer test belirtilen süre içinde tamamlanmazsa, timeout hatası alınır.

@pytest.mark.parametrize ile @pytest.mark.skipif birleşimi: Belirli koşullar altında bir testin atlanmasını sağlar. Parametrize decorator'üyle birleştirilerek, belirli parametrelerle ilgili koşullar altında bir testin atlanması sağlanabilir.

Bu decorator'ler, pytest'in esnekliğini artırır ve testlerinizi daha modüler ve okunabilir hale getirir. Özellikle büyük ve karmaşık test suitleri için çok faydalıdırlar.decorator'ler, testlerin davranışını ve işleyişini özelleştirmek için kullanılır.