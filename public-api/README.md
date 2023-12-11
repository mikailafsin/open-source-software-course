# Şifre Oluşturucu

Bu basit Python programı, belirli kriterlere göre özel şifreler oluşturmak için bir API kullanır. API, şifre oluşturma işlemlerini gerçekleştirir ve sonucu kullanıcıya döner.

## Kullanım

1. İlk olarak, projeyi klonlayın:

    ```bash
    git clone https://github.com/mikailafsin/open-source-software-course.git
    cd public-api
    ```

2. Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) Python'u indirip yükleyin. Veya,

	```bash
    apt install python3
    ```

3. Gerekli kütüphaneleri yükleyin:

    ```bash
    pip install requests
    ```

4. Şifre oluşturmak için programı çalıştırın:

    ```bash
    python app.py --num --char --caps --len 16
    ```

	Yardım için:

    ```bash
    python app.py -h
    ```

    Argümanlar:

    - `--num`: Rakam ekler.
    - `--char`: Özel karakter ekler.
    - `--caps`: Büyük harf ekler.
    - `--len`: Şifrenin uzunluğunu belirler (varsayılan: 12).

5. Programın çıktısını kontrol edin. Oluşturulan şifre görüntülenir.

## Örnek Kullanım

Rakam ve özel karakter içeren bir şifre oluşturmak için:

```bash
python app.py --num --char
```
