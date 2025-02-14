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

        # Query untuk Tafsir dengan threshold < 0.5
        cursor.execute("""
            SELECT 
                nomor,
                nama,
                nama_latin,
                jumlah_ayat,
                tempat_turun,
                arti,
                ayat,
                teks,
                teks_arab,
                teks_latin,
                teks_indonesia,
                vector <=> %s::vector AS distance_score
            FROM detail_tafsir_embedding
            WHERE (vector <=> %s::vector) < 0.5       -- threshold
            ORDER BY distance_score
            LIMIT 10;
        """, (user_vector, user_vector))
        
        tafsir_results = [dict(row) for row in cursor.fetchall()]

        # Return hasil pencarian (hanya tafsir)
        return {
            "tafsir": tafsir_results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
