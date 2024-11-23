import requests
import json
import time

# URL untuk mendapatkan token dan untuk PUT request
get_token_url = "https://clicker-api.crashgame247.io/user/wallet/proof"
put_url = "https://clicker-api.crashgame247.io/meta/clicks"

# Fungsi untuk mendapatkan token baru dari API
def get_new_token():
    # Payload yang berisi token lama yang sudah dienkripsi
    payload = {
        "payload": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjoiMjhjOGE4NDQ2NDNhOWQ2MTI3MmE2ZGFhODk4NDlhNmE3ZDk4OGE1OWUxZGYzY2NlZmJlNWNiZjgzMDliZWU5NiIsImlhdCI6MTczMjM4OTE2NiwiZXhwIjoxNzMyMzkwMDY2fQ.ob9Pjkiy95RbsKEBWQ0Gf80ry_dk4UdgIY5sm81nFZ4"
    }

    # Mengirimkan permintaan POST untuk mendapatkan token baru
    headers = {
        "Content-Type": "application/json"
    }
    
    # Mengirimkan POST untuk mendapatkan token baru
    response = requests.post(get_token_url, json=payload, headers=headers)

    # Memeriksa apakah request berhasil
    if response.status_code == 200:
        data = response.json()
        new_token = data.get('token', '')  # Ambil token baru dari respons
        return new_token
    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        return None

# Fungsi untuk mengirimkan PUT request menggunakan token baru
def send_put_request(new_token):
    # Payload untuk PUT request
    payload = {
        "clicks": 10000
    }

    # Headers untuk PUT request
    headers = {
        "Authorization": f"Bearer {new_token}",
        "Content-Type": "application/json",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "origin": "https://clicker.crashgame247.io",
        "referer": "https://clicker.crashgame247.io/",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
    }

    # Mengirimkan PUT request ke API
    response = requests.put(put_url, json=payload, headers=headers)

    # Memeriksa apakah request berhasil
    if response.status_code == 200:
        print("Request berhasil:", response.json())
    else:
        print(f"Request gagal. Status code: {response.status_code}, Response: {response.text}")

# Fungsi utama untuk mendapatkan token baru dan mengirim PUT request
def main():
    while True:  # Looping terus-menerus
        # Mendapatkan token baru
        new_token = get_new_token()

        if new_token:
            print("Token baru berhasil didapat:", new_token)
            # Mengirimkan PUT request menggunakan token baru
            send_put_request(new_token)
        else:
            print("Gagal mendapatkan token baru.")
        
        # Menunggu 2 detik sebelum mengulang lagi
        time.sleep(2)

# Menjalankan program
if __name__ == "__main__":
    main()