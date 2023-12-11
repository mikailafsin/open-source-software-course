import requests
import argparse

def generate_password(api_url, options):
    response = requests.get(api_url, params=options)
    
    if response.status_code == 200:
        password = response.json().get('data')
        print(f"Oluşturulan şifre: {password}")
    else:
        print(f"Hata oluştu. HTTP Hata Kodu: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="API üzerinden özel şifre oluşturan Python programı.")
    
    parser.add_argument("--num", action="store_const", const="True", default=None, help="Rakam ekler.")
    parser.add_argument("--char", action="store_const", const="True", default=None, help="Özel karakter ekler.")
    parser.add_argument("--caps", action="store_const", const="True", default=None, help="Büyük harf ekler.")
    parser.add_argument("--len", type=int, default=12, help="Şifrenin uzunluğunu belirler. Varsayılan: 12")
    
    args = parser.parse_args()
    
    api_url = "https://passwordinator.onrender.com"
    options = {
        "num": args.num,
        "char": args.char,
        "caps": args.caps,
        "len": args.len
    }
	
    if not any(options.values()):
        options = {}
    
    generate_password(api_url, options)
