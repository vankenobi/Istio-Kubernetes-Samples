import requests
import time
import os
import logging

# Loglama yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Request sent successfully to: {url}")
        else:
            logging.error(f"Failed to send request to: {url}, Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"An error occurred while sending request to: {url}")
        logging.error(f"Error: {e}")

def main():
    url = os.getenv('TARGET_URL')  # İstek atılacak URL'i environment değişkeninden alır
    if not url:
        logging.error("TARGET_URL environment variable not set.")
        return

    while True:
        send_request(url)
        time.sleep(1)  # Her saniye bir istek göndermek için 1 saniye uyku

if __name__ == "__main__":
    main()
