# Flask ve Docker ile Örnek Uygulama

Bu proje, Flask web uygulamasını Docker container'ında çalıştırmak için basit bir şablondur.

## Gereksinimler

- Docker

## Nasıl Kullanılır

1. Bu depoyu bilgisayarınıza klonlayın:

    ```bash
    git clone https://github.com/mikailafsin/open-source-software-course.git
    cd open-source-software-course/flask-on-docker
    ```

2. Docker container'ını oluşturun ve çalıştırın:

    ```bash
    docker compose build
    docker compose up -d
    ```

3. Tarayıcınızda `http://localhost:8000` adresine giderek uygulamayı görüntüleyin.

## Proje Yapısı

- `docker-compose.yml`: Docker container'ını başlatmak için kullanılır.
- `README.md`: Bu dosya.
- `main.py`: Flask uygulamasının kodlarını içerir.
- `Dockerfile`: Docker container'ınızın nasıl oluşturulacağını tanımlar.
- `requirements.txt`: Gerekli Python kütüphanelerini içerir.
- `users.csv`: Kullanıcı bilgilerini depolar.
