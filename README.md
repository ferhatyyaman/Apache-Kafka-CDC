# Apache Kafka ile Basit CDC Uygulaması

Bu proje, MongoDB veritabanındaki belirli bir koleksiyondaki yeni dokümanları sorgulayarak Apache Kafka'ya bir JSON mesajı olarak üreten ve bu mesajları tüketen basit bir CDC (Değişiklik Verilerini Yakalama) uygulamasıdır.



## Proje Tanımı

Proje, seçtiğiniz bir programlama diliyle geliştirilmiş iki uygulamadan oluşmaktadır:

1. Mesaj Üreten Uygulama (A Uygulaması): Bu uygulama, 10 saniyede bir MongoDB veritabanındaki belirli bir koleksiyonu sorgular ve önceki çalışmasından sonra eklenen yeni dokümanları tespit eder. Ardından, yeni dokümanı JSON mesajı olarak Apache Kafka'ya gönderir.

2. Mesaj Tüketen Uygulama (B Uygulaması): Bu uygulama, Apache Kafka'dan aldığı mesajları konsola yazdırır. Bu uygulama, üç kopya olarak çalışır ve mesajları eş zamanlı olarak tüketir.

Proje ayrıca Docker kullanılarak iki uygulama ve Apache Kafka'yı içeren bir ortamın oluşturulmasını da içermektedir. Docker imajları, bir Dockerfile kullanılarak oluşturulacak ve Docker Compose ile çalıştırılacaktır.

## Proje Diagramı

Proje yapısını aşağıdaki şekilde gösteren bir diagram:



## Gereksinimler

Projenin çalıştırılması için aşağıdaki gereksinimlere ihtiyaç vardır:

- Programlama Dilinin ve Sürümünün belirtilmesi
- MongoDB veritabanı bağlantısı için gereken bilgiler
- Apache Kafka bağlantısı için gereken bilgiler

   ## Kurulum ve Çalıştırma

Uygulamaları oluşturmak ve çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

**1. Projeyi Kopyalayın:**

İlk olarak, projeyi GitHub'dan kopyalamanız gerekmektedir. Aşağıdaki komutu kullanarak projeyi yerel makinenize klonlayabilirsiniz:

```shell
   git clone https://github.com/ferhatyyaman/Apache-Kafka-CDC
```

**2. Proje Dizinine Girin:**

Klonlama işlemi tamamlandıktan sonra, projenin olduğu dizine gidin:

```
cd Apache-Kafka-CDC
```

**3. Docker İmajlarını Oluşturun ve Servisleri Çalıştırın:**

Docker Compose kullanarak Docker imajlarını oluşturabilir ve uygulama servislerini çalıştırabilirsiniz. Aşağıdaki komutu kullanarak Docker Compose'u çalıştırın:

```
docker-compose up --build
```

Bu komut, projede tanımlanan servisleri oluşturacak ve başlatacaktır. İmajların oluşturulması biraz zaman alabilir. İşlem tamamlandığında, uygulamalar çalışır durumda olacak ve veri akışı başlayacaktır.

**4. Veri Akışını Başlatın:**

Veri akışını sağlamak için bir terminal açın ve proje dizininde olduğunuzdan emin olun. Ardından, aşağıdaki komutu girerek veri üreticisini başlatabilirsiniz:

```
python kafka-producer.py
```

Bu komut, MongoDB veritabanındaki belirli bir koleksiyondan yeni dokümanları sorgulayacak ve bu dokümanları JSON mesajları olarak Apache Kafka'ya gönderecektir.

Bu adımları takip ettikten sonra, veri akışını hem terminalde gözlemleyebilir hem de Apache Kafka ve MongoDB üzerindeki değişiklikleri kontrol edebilirsiniz.

