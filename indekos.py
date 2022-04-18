# Saya Silmi Aulia Rohmah mengerjakan Latihan 9 DPBO 2022 C1 dalam mata kuliah DPBO 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

# import
from hunian import Hunian 

class Indekos(Hunian): 

    def __init__(self, nama_pemilik, nama_penghuni, luas_tanah, kapasitas_listrik, sumber_air, alamat, harga_sewa):
        super().__init__("Indekos", 1, 1, luas_tanah, kapasitas_listrik, sumber_air, alamat)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.harga_sewa = harga_sewa

    # metode getter
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_harga_sewa(self):
        return self.harga_sewa + " per bulan"

    def get_summary(self):
        return "Hunian Indekos."