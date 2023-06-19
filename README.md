# Apache Kafka ile Basit CDC Uygulaması

Bu proje, MongoDB veritabanındaki belirli bir koleksiyondaki yeni dokümanları sorgulayarak Apache Kafka'ya bir JSON mesajı olarak üreten ve bu mesajları tüketen basit bir CDC (Değişiklik Verilerini Yakalama) uygulamasıdır.



## Proje Tanımı

Proje, seçtiğiniz bir programlama diliyle geliştirilmiş iki uygulamadan oluşmaktadır:

1. Mesaj Üreten Uygulama (A Uygulaması): Bu uygulama, 10 saniyede bir MongoDB veritabanındaki belirli bir koleksiyonu sorgular ve önceki çalışmasından sonra eklenen yeni dokümanları tespit eder. Ardından, yeni dokümanı JSON mesajı olarak Apache Kafka'ya gönderir.

2. Mesaj Tüketen Uygulama (B Uygulaması): Bu uygulama, Apache Kafka'dan aldığı mesajları konsola yazdırır. Bu uygulama, üç kopya olarak çalışır ve mesajları eş zamanlı olarak tüketir.

Proje ayrıca Docker kullanılarak iki uygulama ve Apache Kafka'yı içeren bir ortamın oluşturulmasını da içermektedir. Docker imajları, bir Dockerfile kullanılarak oluşturulacak ve Docker Compose ile çalıştırılacaktır.

## Proje Diagramı

Proje yapısını aşağıdaki şekilde gösteren bir diagram:

![image](https://github.com/ferhatyyaman/Apache-Kafka-CDC/assets/66822481/99d4c753-1646-4943-9c62-9722ba577da6)

## Gereksinimler

Projenin çalıştırılması için aşağıdaki gereksinimlere ihtiyaç vardır:

- Programlama Dilinin ve Sürümünün belirtilmesi
- MongoDB veritabanı bağlantısı için gereken bilgiler
- Apache Kafka bağlantısı için gereken bilgiler

## Kurulum ve Çalıştırma

1. Repoyu yerel makinenize klonlayın:

   ```shell
   git clone https://github.com/ferhatyyaman/Apache-Kafka-CDC
