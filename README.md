# Surat Maaf (Streamlit)

Halaman minta maaf interaktif. Klik **iya** untuk lanjut ke pesan berikutnya. Tombol **nggak** akan kabur ke posisi acak setiap kali didekati/disentuh, jadi tidak bisa diklik.

## Cara menjalankan

### Opsi 1 — pakai script setup (bikin virtualenv otomatis)

Linux/macOS:

```bash
chmod +x setup.sh   # cukup sekali
./setup.sh
source venv/bin/activate
streamlit run app.py
```

Windows (cmd):

```bat
setup.bat
venv\Scripts\activate
streamlit run app.py
```

Windows (PowerShell):

```powershell
.\setup.ps1
.\.venv\Scripts\Activate.ps1
streamlit run app.py
```

Kalau menjalankan `.ps1` diblokir ("running scripts is disabled"), jalankan sekali:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

### Opsi 2 — manual

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Browser akan terbuka otomatis ke `http://localhost:8501`.

## Cara mengedit isi pesan

Semua teks ada di bagian atas `app.py`:

- `GIRLFRIEND_NAME` — ganti `"Sayang"` dengan nama panggilan aslinya.
- `PAGES` — daftar pesan per halaman (`eyebrow`, `heading`, `body`, label tombol `yes`/`no`). Tambah, kurangi, atau ubah urutan sesuai kebutuhan.
- `FINAL` — halaman penutup (tanpa tombol, ada efek confetti hati).

Tidak perlu menyentuh bagian HTML/CSS/JS di bawahnya kecuali ingin mengubah tampilan atau perilaku tombol "nggak".

## Cara membagikan ke orang lain

Jalankan secara lokal dan bagikan lewat tunnel (mis. `ngrok`), atau deploy gratis ke [Streamlit Community Cloud](https://streamlit.io/cloud): push folder ini ke repo GitHub, lalu hubungkan repo tersebut di Streamlit Cloud dan set `app.py` sebagai entry point.
