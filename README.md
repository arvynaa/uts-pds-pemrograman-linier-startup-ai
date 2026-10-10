# uts-pds-pemrograman-linier-startup-ai
# Pemrograman Linier – Optimasi Produksi Startup AI

## Deskripsi
Proyek ini dibuat untuk menyelesaikan permasalahan optimasi produksi startup AI menggunakan metode grafik pada pemrograman linier.

## Permasalahan
Startup AI memproduksi dua jenis model, yaitu Computer Vision (CV) dan Natural Language Processing (NLP), dengan keterbatasan sumber daya GPU dan penyimpanan.

## Model Matematika
Variabel keputusan:
- x = jumlah model Computer Vision (CV)
- y = jumlah model Natural Language Processing (NLP)

Fungsi tujuan:

Maksimalkan Z = 500.000x + 400.000y

Kendala:
- 3x + y ≤ 15 (GPU)
- x + 2y ≤ 10 (penyimpanan)
- x, y ≥ 0

## Hasil
Solusi optimal diperoleh dengan memproduksi 4 model CV dan 3 model NLP per hari, dengan pendapatan maksimum Rp3.200.000 per hari.

## File Proyek
- `uts.py`: kode Python untuk perhitungan dan visualisasi.
- `grafik_pemrograman_linier.png`: hasil grafik pemrograman linier.

## Tools
- Python
- NumPy
- Matplotlib
