# Base image olarak resmi Python image'ını kullan
FROM python:3.8-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinim dosyasını çalışma dizinine kopyala
COPY requirements.txt requirements.txt

# Bağımlılıkları yükle
RUN pip install -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Uygulamanın çalıştırılabilir portunu belirt
EXPOSE 8000

# Uygulamayı başlat
CMD ["python", "./HelloWorldApi/main.py"]