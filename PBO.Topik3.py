class Mahasiswa:
    def __init__(self, nama, nim, prodi, angkatan):
        self.__nama = nama   # Private attribute
        self.__nim = nim     # Private attribute
        self.prodi = prodi
        self.angkatan = angkatan

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    # Getter untuk NIM
    def get_nim(self):
        return self.__nim

    # Setter untuk NIM
    def set_nim(self, nim_baru):
        self.__nim = nim_baru

    def praktikum(self):
        return f"{self.__nama} sedang mengikuti praktikum."

    def berorganisasi(self):
        return f"{self.__nama} aktif dalam kegiatan organisasi."

    def mengerjakan_tugas(self):
        return f"{self.__nama} sedang mengerjakan tugas."


# Membuat objek baru
mahasiswa2 = Mahasiswa("Alvin", "A710240007", "Teknik Informatika", 2025)

# Mengakses private attribute menggunakan getter
print("Nama:", mahasiswa2.get_nama())
print("NIM:", mahasiswa2.get_nim())

# Mengubah private attribute menggunakan setter
mahasiswa2.set_nama("Radian")
mahasiswa2.set_nim("123456")

# Mengecek perubahan yang telah dilakukan
print("Nama setelah diubah:", mahasiswa2.get_nama())
print("NIM setelah diubah:", mahasiswa2.get_nim())

# Memanggil metode lain
print(mahasiswa2.praktikum())
print(mahasiswa2.berorganisasi())
print(mahasiswa2.mengerjakan_tugas())