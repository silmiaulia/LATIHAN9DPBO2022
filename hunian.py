# Saya Silmi Aulia Rohmah mengerjakan Latihan 9 DPBO 2022 C1 dalam mata kuliah DPBO 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, luas_tanah = 0, kapasitas_listrik = 0, sumber_air="", alamat=""):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luas_tanah = luas_tanah
        self.kapasitas_listrik = kapasitas_listrik
        self.sumber_air = sumber_air
        self.alamat = alamat

    # metode getter
    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_luas_tanah(self):
        return str(self.luas_tanah) + " m2"

    def get_kapasitas_listrik(self):
        return str(self.kapasitas_listrik) + " VA"

    def get_sumber_air(self):
        return self.sumber_air
    
    def get_alamat(self):
        return self.alamat

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."