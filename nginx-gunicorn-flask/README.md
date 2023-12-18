Bu depoda, Python sanal ortamında basit bir Flask uygulaması oluşturuldu. WSGI özellikli herhangi bir uygulama sunucusunun arayüz oluşturabilmesi için
bir WSGI giriş noktası oluşturuldu ve ardından Gunicorn uygulama sunucusu bu işlevi sağlayacak şekilde yapılandırıldı. Daha sonra, önyükleme sırasında
uygulama sunucusunu otomatik olarak başlatmak için bir systemd hizmet dosyası oluşturuldu. Ayrıca web istemci trafiğini uygulama sunucusuna aktaran
bir Nginx sunucu bloğu oluşturuldu. 

Depo içerisinde bulunan "etc" klasörünün altındaki klasörleri kendi sisteminizin altındaki "etc" klasörünün altına taşımayı unutmayınız.

Herhangi bir sorunla karşılaşmanız durumunda benimle iletişime geçiniz.
