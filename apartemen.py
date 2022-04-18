# Saya Silmi Aulia Rohmah mengerjakan Latihan 9 DPBO 2022 C1 dalam mata kuliah DPBO 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

# import
from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah, kapasitas_listrik, sumber_air, alamat):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, luas_tanah, kapasitas_listrik, sumber_air, alamat)
        self.nama_pemilik = nama_pemilik

    # metode getter
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik