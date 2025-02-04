# import requests
# from pymongo import MongoClient
# from pymongo.errors import ConnectionFailure  # Perbaikan di sini

# # URL API
# api_url = 'https://equran.id/api/v2/surat'

# # Koneksi ke MongoDB
# mongo_client = MongoClient(
#     'mongodb://admin:admin123@localhost:27777/indo_quran?authSource=admin'
# )

# # Pilih database dan collection
# db = mongo_client['indo_quran']
# collection = db['daftar_surah']

# # Request data dari API
# response = requests.get(api_url)

# # Cek apakah request berhasil
# if response.status_code == 200:
#     data = response.json()['data']
#     # Masukkan data ke dalam MongoDB
#     try:
#         # Insert data ke collection "surat"
#         collection.insert_many(data)
#         print("Data berhasil disimpan ke MongoDB.")
#     except Exception as e:
#         print(f"Terjadi error saat memasukkan data ke MongoDB: {e}")
# else:
#     print(f"Request ke API gagal, status code: {response.status_code}")





# import requests
# from pymongo import MongoClient
# from tqdm import tqdm

# # URL API untuk mendapatkan hadis dengan nomor tertentu
# api_url_hadist = 'https://hadis-api-id.vercel.app/hadith/'

# # Koneksi ke MongoDB
# mongo_client = MongoClient(
#     'mongodb://admin:admin123@localhost:27777/indo_quran?authSource=admin'
# )

# # Pilih database dan koleksi
# db = mongo_client['indo_quran']
# collection_detail_hadist = db['detail_hadist']  # Koleksi untuk detail hadist

# # Fungsi untuk mengambil detail hadis dan menyimpannya ke MongoDB
# def save_detail_hadist():
#     # Daftar slug untuk berbagai kitab hadis
#     slugs = ['abu-dawud', 'ahmad', 'bukhari', 'darimi', 'ibnu-majah', 'malik', 'muslim', 'nasai', 'tirmidzi']
    
#     # Looping melalui setiap slug dan mengambil semua hadis yang ada
#     for slug in slugs:
#         print(f"Memulai pengambilan hadis untuk {slug}...")

#         # Ambil total hadis dari koleksi untuk kitab ini
#         response = requests.get(f'https://hadis-api-id.vercel.app/hadith/{slug}')
#         if response.status_code == 200:
#             total_hadith = response.json()['total']
#         else:
#             print(f"Gagal mendapatkan total hadis untuk {slug}.")
#             continue
        
#         # Ambil data hadis per nomor dan masukkan ke MongoDB
#         for i in tqdm(range(1, total_hadith + 1), desc=f"Proses Hadis {slug}", ncols=100):
#             # Ambil data hadis per nomor
#             response = requests.get(f'https://hadis-api-id.vercel.app/hadith/{slug}/{i}')
            
#             if response.status_code == 200:
#                 data = response.json()
#                 try:
#                     # Insert data ke dalam koleksi "detail_hadist"
#                     collection_detail_hadist.insert_one(data)
#                 except Exception as e:
#                     print(f"Terjadi error saat memasukkan hadis nomor {i} ke MongoDB: {e}")
#             else:
#                 print(f"Hadis nomor {i} gagal diambil.")
#         print(f"Proses pengambilan hadis untuk {slug} selesai.")

# # Panggil fungsi untuk menyimpan detail hadis
# save_detail_hadist()



import requests
from pymongo import MongoClient

# URL API untuk mengambil semua doa harian
api_url = "https://islamic-api-zhirrr.vercel.app/api/doaharian"

# Koneksi ke MongoDB
mongo_client = MongoClient(
    'mongodb://admin:admin123@localhost:27777/indo_quran?authSource=admin'
)

# Pilih database dan koleksi
db = mongo_client['indo_quran']
collection_doa_harian = db['doa_harian']  # Koleksi untuk doa harian

# Ambil data dari API
response = requests.get(api_url)

if response.status_code == 200:
    doa_data = response.json()

    if "data" in doa_data:
        # Masukkan data ke MongoDB
        collection_doa_harian.insert_many(doa_data["data"])
        print(f"Berhasil menyimpan {len(doa_data['data'])} doa harian ke MongoDB!")
    else:
        print("Data doa harian kosong atau tidak ditemukan.")
else:
    print(f"Gagal mengambil data doa harian! Status code: {response.status_code}")



