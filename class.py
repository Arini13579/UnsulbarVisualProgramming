class transportasi():
    mobil = "BMW"

    def __init__(self, input_nama):
        self.nama = input_nama #public
kendaraan = transportasi("Mobil BMW")

print(transportasi.mobil)
print(kendaraan.mobil)