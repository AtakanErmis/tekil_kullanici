# Tekil Kullanıcı

Ekşicode'a üye tekil kullanıcı sayısını ölçmek için yazılmış bir Python scripti.

# Kullanım

- `pip3 install virtualenv`
- `git clone https://github.com/AtakanErmis/tekil_kullanici`
- `cd tekil_kullanici`
- `virtualenv .`
- `source ./bin/activate`
- `pip3 install -r requirements.txt`
- `cp sample.env .env`
- .env dosyasına my.telegram.org'dan API token'ı alıp verilen ID ve Hash bilgilerini ekleyin.
- Tüm gruplardaki kullanıcı sayısını ölçmek için çalıştırmadan önce tüm ekşiCode gruplarına üye olmanız gerekmektedir.
- `python3 tekil.py`
