# Book Scraper

Web scraper CLI berbasis Python yang mengambil data buku dari [books.toscrape.com](https://books.toscrape.com) (situs latihan resmi untuk scraping), membersihkannya, lalu menyimpannya ke CSV dan JSON.

> **Status: dalam pengerjaan.** README ini sementara dan akan dilengkapi di Phase 9.

## Fitur (target)

- Ambil data buku dari beberapa halaman listing, termasuk halaman detail tiap buku
- Pagination otomatis
- Jeda antar request, retry, dan cache HTML mentah di `data/raw/`
- Tahan error: satu halaman gagal tidak menghentikan program
- Data dibersihkan (harga jadi angka, rating jadi 1-5, stok jadi angka)
- Output ke `data/books.csv` dan `data/books.json`
- Tes dasar dengan pytest (tanpa internet)

## Kolom data

| Kolom | Isi |
|---|---|
| `title` | Judul buku |
| `price` | Harga (float) |
| `rating` | Rating 1-5 |
| `category` | Kategori buku |
| `in_stock` | Tersedia atau tidak (True/False) |
| `stock_count` | Jumlah stok |
| `url` | Alamat halaman detail |

## Cara install

1. Clone repo ini dan masuk ke foldernya.
2. Buat dan aktifkan virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```

3. Install library:

   ```
   pip install -r requirements.txt
   ```

## Cara pakai

```
python main.py --pages 3
```

Argumen:

| Argumen | Fungsi | Default |
|---|---|---|
| `--pages` | Jumlah halaman listing yang di-scrape | 3 |
| `--delay` | Jeda antar request (detik) | dari `config.py` |
| `--out` | Folder output | `data` |

Menjalankan tes:

```
pytest
```

## Contoh output

_Akan diisi setelah program selesai._

## Struktur folder

```
Book-scraper/
├── main.py          # titik masuk CLI
├── fetcher.py       # ambil HTML (request, retry, jeda, cache)
├── parser.py        # ubah HTML jadi data mentah
├── cleaner.py       # rapikan data mentah
├── storage.py       # tulis CSV dan JSON
├── config.py        # konstanta
├── data/
│   ├── raw/         # cache HTML (tidak di-commit)
│   ├── books.csv
│   └── books.json
├── tests/
│   ├── fixtures/    # contoh HTML untuk tes
│   ├── test_parser.py
│   └── test_cleaner.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Catatan

Project ini hanya untuk belajar dan memakai situs latihan.