
# ============================================================
# PEMROGRAMAN LINIER METODE GRAFIK
# Kasus: Optimasi Pendapatan Startup AI
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. MENDEFINISIKAN MODEL MATEMATIKA
# ------------------------------------------------------------

# Variabel keputusan:
# x = jumlah model Computer Vision
# y = jumlah model Natural Language Processing (NLP)

# Pendapatan setiap model
pendapatan_cv = 500_000
pendapatan_nlp = 400_000

# Kebutuhan sumber daya setiap model
gpu_cv = 3
gpu_nlp = 1
storage_cv = 1
storage_nlp = 2

# Kapasitas maksimum sumber daya per hari
kapasitas_gpu = 15
kapasitas_storage = 10


def hitung_pendapatan(x, y):
    """Menghitung total pendapatan dari kedua jenis model."""
    return pendapatan_cv * x + pendapatan_nlp * y


def memenuhi_kendala(x, y):
    """Memeriksa apakah kombinasi memenuhi semua kendala."""
    return (
        gpu_cv * x + gpu_nlp * y <= kapasitas_gpu
        and storage_cv * x + storage_nlp * y <= kapasitas_storage
        and x >= 0
        and y >= 0
    )


print("=" * 65)
print("OPTIMASI PENDAPATAN STARTUP AI - METODE GRAFIK")
print("=" * 65)

print("\nMODEL MATEMATIKA")
print("Maksimumkan Z = 500.000x + 400.000y")
print("Kendala GPU      : 3x + y <= 15")
print("Kendala Storage  : x + 2y <= 10")
print("Kendala non-negatif: x >= 0 dan y >= 0")


# ------------------------------------------------------------
# 2. MENGHITUNG TITIK POTONG GARIS KENDALA
# ------------------------------------------------------------

# Garis GPU: 3x + y = 15
titik_gpu_x = (kapasitas_gpu / gpu_cv, 0)
titik_gpu_y = (0, kapasitas_gpu / gpu_nlp)

# Garis Storage: x + 2y = 10
titik_storage_x = (kapasitas_storage / storage_cv, 0)
titik_storage_y = (0, kapasitas_storage / storage_nlp)

# Titik perpotongan kedua garis:
# 3x + y = 15
# x + 2y = 10

determinan = gpu_cv * storage_nlp - gpu_nlp * storage_cv

x_potong = (
    kapasitas_gpu * storage_nlp
    - gpu_nlp * kapasitas_storage
) / determinan

y_potong = (
    gpu_cv * kapasitas_storage
    - kapasitas_gpu * storage_cv
) / determinan

titik_perpotongan = (x_potong, y_potong)

print("\nTITIK POTONG GARIS KENDALA")
print(f"GPU - sumbu X     : {titik_gpu_x}")
print(f"GPU - sumbu Y     : {titik_gpu_y}")
print(f"Storage - sumbu X : {titik_storage_x}")
print(f"Storage - sumbu Y : {titik_storage_y}")
print(
    "Perpotongan kedua garis: "
    f"({x_potong:.2f}, {y_potong:.2f})"
)


# ------------------------------------------------------------
# 3. MENENTUKAN TITIK SUDUT DAERAH FEASIBLE
# ------------------------------------------------------------

# Kandidat titik sudut diperoleh dari titik potong garis
# kendala dengan sumbu dan titik perpotongan kedua garis.

kandidat_titik = [
    (0, 0),
    titik_gpu_x,
    titik_gpu_y,
    titik_storage_x,
    titik_storage_y,
    titik_perpotongan
]

# Hanya mempertahankan titik yang memenuhi semua kendala.
titik_feasible = []

for titik in kandidat_titik:
    x, y = titik

    if memenuhi_kendala(x, y):
        if not any(
            np.allclose(titik, titik_lama)
            for titik_lama in titik_feasible
        ):
            titik_feasible.append(titik)

# Urutkan titik untuk membentuk poligon daerah feasible
pusat_x = np.mean([p[0] for p in titik_feasible])
pusat_y = np.mean([p[1] for p in titik_feasible])

titik_feasible.sort(
    key=lambda p: np.arctan2(
        p[1] - pusat_y,
        p[0] - pusat_x
    )
)

print("\nTITIK SUDUT DAERAH FEASIBLE")
for i, (x, y) in enumerate(titik_feasible):
    print(f"{chr(65 + i)} = ({x:.2f}, {y:.2f})")


# ------------------------------------------------------------
# 4. MENGGAMBAR GRAFIK PEMROGRAMAN LINIER
# ------------------------------------------------------------

# Garis GPU hanya digambar pada rentang yang relevan
x_gpu = np.linspace(0, kapasitas_gpu / gpu_cv, 200)
y_gpu = kapasitas_gpu - gpu_cv * x_gpu

# Garis Storage hanya digambar pada rentang yang relevan
x_storage = np.linspace(
    0, kapasitas_storage / storage_cv, 200
)
y_storage = (
    kapasitas_storage - storage_cv * x_storage
) / storage_nlp

plt.figure(figsize=(10, 7))

plt.plot(
    x_gpu,
    y_gpu,
    label="Kendala GPU: 3x + y = 15",
    linewidth=2
)

plt.plot(
    x_storage,
    y_storage,
    label="Kendala Storage: x + 2y = 10",
    linewidth=2
)

# Mengarsir daerah feasible
koordinat_x = [p[0] for p in titik_feasible]
koordinat_y = [p[1] for p in titik_feasible]

plt.fill(
    koordinat_x,
    koordinat_y,
    alpha=0.25,
    label="Daerah Feasible"
)

# Menampilkan label setiap titik sudut
for i, (x, y) in enumerate(titik_feasible):
    plt.scatter(x, y, s=55, zorder=3)

    plt.annotate(
        f"{chr(65 + i)} ({x:.0f}, {y:.0f})",
        (x, y),
        xytext=(7, 7),
        textcoords="offset points",
        fontsize=9
    )

# Menandai solusi optimal pada grafik
plt.scatter(
    x_potong,
    y_potong,
    marker="*",
    s=230,
    label="Solusi Optimal",
    zorder=5
)

plt.xlabel("Jumlah Model Computer Vision (x)")
plt.ylabel("Jumlah Model NLP (y)")
plt.title("Grafik Pemrograman Linier - Startup AI")

plt.xlim(0, 11)
plt.ylim(0, 16)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(0, 17, 1))

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

# Simpan grafik agar dapat digunakan dalam laporan
plt.savefig(
    "grafik_pemrograman_linier.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nGrafik disimpan sebagai:")
print("grafik_pemrograman_linier.png")

plt.show()


# ------------------------------------------------------------
# 5. EVALUASI FUNGSI TUJUAN
# ------------------------------------------------------------

print("\nEVALUASI FUNGSI TUJUAN")
print("-" * 65)
print(
    f"{'Titik':<10}"
    f"{'x':>6}"
    f"{'y':>8}"
    f"{'Pendapatan':>24}"
)
print("-" * 65)

hasil_evaluasi = []

for i, (x, y) in enumerate(titik_feasible):
    pendapatan = hitung_pendapatan(x, y)

    hasil_evaluasi.append((x, y, pendapatan))

    print(
        f"{chr(65 + i):<10}"
        f"{x:>6.0f}"
        f"{y:>8.0f}"
        f"Rp{pendapatan:>21,.0f}"
    )


# ------------------------------------------------------------
# 6. MENENTUKAN SOLUSI OPTIMAL
# ------------------------------------------------------------

solusi_optimal = max(
    hasil_evaluasi,
    key=lambda hasil: hasil[2]
)

x_optimal, y_optimal, pendapatan_maksimum = solusi_optimal

penggunaan_gpu = gpu_cv * x_optimal + gpu_nlp * y_optimal

penggunaan_storage = (
    storage_cv * x_optimal
    + storage_nlp * y_optimal
)

print("\n" + "=" * 65)
print("HASIL SOLUSI OPTIMAL")
print("=" * 65)

print(f"Jumlah model Computer Vision : {x_optimal:.0f} model")
print(f"Jumlah model NLP             : {y_optimal:.0f} model")
print(f"Pendapatan maksimum          : Rp{pendapatan_maksimum:,.0f}")
print(
    f"Penggunaan GPU               : "
    f"{penggunaan_gpu:.0f} dari {kapasitas_gpu} jam"
)
print(
    f"Penggunaan Storage           : "
    f"{penggunaan_storage:.0f} dari {kapasitas_storage} TB"
)

print("\nPEMERIKSAAN KENDALA")
print(
    "GPU memenuhi kendala     :",
    penggunaan_gpu <= kapasitas_gpu
)
print(
    "Storage memenuhi kendala :",
    penggunaan_storage <= kapasitas_storage
)
print(
    "Jumlah model bilangan bulat:",
    x_optimal.is_integer() and y_optimal.is_integer()
)

print("\nKESIMPULAN")
print(
    f"Startup AI sebaiknya melatih {x_optimal:.0f} model "
    f"Computer Vision dan {y_optimal:.0f} model NLP "
    f"per hari, dengan pendapatan maksimum "
    f"Rp{pendapatan_maksimum:,.0f}."
)
print("=" * 65)