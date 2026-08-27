lagu = []

def tambah_lagu(judul, penyanyi):
    lagu.append({"judul": judul, "penyanyi": penyanyi})

def tampilkan_lagu():
    if not lagu:
        print("Tidak ada lagu yang tersimpan.")
    else:
        for i, item in enumerate(lagu, start=1):
            print(f"{i}. {item['judul']} - {item['penyanyi']}")
            
def cari_lagu(keyword):
    hasil = list(filter(
        lambda item: keyword.lower() in item['penyanyi'].lower(), 
        lagu
    ))
    return hasil

# Simulasi
tambah_lagu("Cicak Di dinding", "andre")
tambah_lagu("Balon ku ada 5", "Dimas")
tambah_lagu("halo halo bandung", "Justin")

print("\n Daftar Lagu:")
tampilkan_lagu()

print("\n Cari Lagu dengan nama 'Andre':")
for b in cari_lagu("Andre"):
    print(f"- {b['penyanyi']}")