# Saya Silmi Aulia Rohmah mengerjakan Latihan 9 DPBO 2022 C1 dalam mata kuliah DPBO 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

# Instansiasi 
hunians = []
hunians.append(Apartemen("Saul Goodman", 3, 3, 50, 900, "PAM", "Jalan K.H. Mas Mansyur No. 45, Bandung"))
hunians.append(Rumah("Gustavo Fring", 5, 2, 120, 1300, "Sumur", "Jalan Raya Danau Maninjau No. 15, Mojokerto"))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", 30, 900, "Sumur", "Jalan Krajan No. 25, Banjarnegara", "Rp.500.000"))
hunians.append(Rumah("Mike Ehrmantraut", 1, 4, 80, 900, "PAM", "Jalan Gatot Subroto No. 176, Denpasar"))
hunians.append(Indekos("Thomas Shelby", "Rick Grimes", 20, 900, "Sumur", "Jalan Kerinci No. 13, Jakarta", "Rp.750.000"))

root = Tk()
root.title("Praktikum DPBO Python")

# proses untuk menampilkan window detail
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # menampilkan seluruh data detail hunian 

    d_nama_pemilik = Label(d_frame, text="Nama Pemilik: " + hunians[index].get_nama_pemilik(), anchor="w").grid(row=0, column=0, sticky="w")

    if hunians[index].get_jenis() == "Indekos": 
        # jika hunian berjenis indekos
        d_nama_penghuni = Label(d_frame, text="Nama Penghuni: " + hunians[index].get_nama_penghuni(), anchor="w").grid(row=1, column=0, sticky="w")
        d_harga_sewa = Label(d_frame, text="Harga Sewa: " + hunians[index].get_harga_sewa(), anchor="w").grid(row=6, column=0, sticky="w")
    else:
        # jika hunian bukan indekos
        d_jumlah_kamar = Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()), anchor="w").grid(row=1, column=0, sticky="w")
    

    d_jumlah_penghuni = Label(d_frame, text="Jumlah Penghuni: " + str(hunians[index].get_jml_penghuni()), anchor="w").grid(row=2, column=0, sticky="w")
    d_luas_tanah = Label(d_frame, text="Luas Tanah: " + hunians[index].get_luas_tanah(), anchor="w").grid(row=3, column=0, sticky="w")
    d_kapasitas_listrik = Label(d_frame, text="Kapasitas Listrik: " + hunians[index].get_kapasitas_listrik(), anchor="w").grid(row=4, column=0, sticky="w")
    d_sumber_air = Label(d_frame, text="Jenis Sumber Air: " + hunians[index].get_sumber_air(), anchor="w").grid(row=5, column=0, sticky="w")
    d_alamat = Label(d_frame, text="Alamat: " + hunians[index].get_alamat(), anchor="w").grid(row=7, column=0, sticky="w")
    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=8, column=0, sticky="w")
    d_dokumen = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=9, column=0, sticky="w")

    # fungsi untuk exit dari detail
    def close(): 
        top.destroy()
        # top.quit()

    # buat frame button exit
    button = LabelFrame(top, padx=8, pady=8)
    button.pack(padx=8, pady=8)

    # membuat button exit
    b_exit = Button(button, text="Exit", command=close)
    b_exit.grid(row=0, column=0)

frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

# untuk button add data
b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

# untuk button exit dari window utama
b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

# looping tampilkan data seluruh residen
for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    # menampilkan jenis hunian residen
    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    # menampilkan data residen yang bukan jenis indekos
    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    # tampilkan data residen jenis indekos
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    # membuat button detail
    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
