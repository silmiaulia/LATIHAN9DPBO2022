# Saya Silmi Aulia Rohmah mengerjakan Latihan 9 DPBO 2022 C1 dalam mata kuliah DPBO 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

# import
from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah, kapasitas_listrik, sumber_air, alamat):
        super().__init__("Rumah", jml_penghuni, jml_kamar, luas_tanah, kapasitas_listrik, sumber_air, alamat)
        self.nama_pemilik = nama_pemilik

    # metode getter
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
   