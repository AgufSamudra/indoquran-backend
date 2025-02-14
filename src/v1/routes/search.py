from fastapi import APIRouter, HTTPException
from src.v1.schemas import SmartSearch
from sentence_transformers import SentenceTransformer
import psycopg2
import psycopg2.extras

# Inisialisasi FastAPI Router
router = APIRouter(
    prefix="/search",
    tags=["search"]
)

# Load model embedding
model = SentenceTransformer('firqaaa/indo-sentence-bert-base')

# Koneksi ke PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="indo_quran",
    user="postgres",
    password="postgres123",
    port=5555
)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

@router.post("/smart_search")
async def smart_search(input: SmartSearch):
    try:
        # Buat embedding dari input user
        user_vector = model.encode(input.user_input).tolist()

        cursor.execute("""
            SELECT number, name, slug, arab, teks
            FROM detail_hadist_embedding
            ORDER BY vector <=> %s::vector
            LIMIT 10;
        """, (user_vector,))
        hadist_results = [dict(row) for row in cursor.fetchall()]

        # Query untuk Tafsir
        cursor.execute("""
            SELECT nomor, nama, nama_latin, jumlah_ayat, tempat_turun, arti, ayat, teks
            FROM detail_tafsir_embedding
            ORDER BY vector <=> %s::vector
            LIMIT 10;
        """, (user_vector,))
        tafsir_results = [dict(row) for row in cursor.fetchall()]

        # Return hasil pencarian
        return {
            "hadist": hadist_results,
            "tafsir": tafsir_results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))