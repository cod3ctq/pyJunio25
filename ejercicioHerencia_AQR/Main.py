from ejercicioHerencia_AQR.Celular import Celular
from ejercicioHerencia_AQR.Laptop import Laptop

class main():
    cel = Celular("Samsung", 666.99, 108)
    lap = Laptop("Lenovo", 1111.00, 16)

    print("Información inicial")
    print(cel)
    print(lap)

    # Actualizar atributos con setters
    cel.set_precio(999.99)
    cel.set_camara_mp(50)
    lap.set_precio(2222.00)
    lap.set_ram_gb(32)

    print("\nDespués de actualizar")
    print(f"Celular – Marca: {cel.get_marca()}, Precio: ${cel.get_precio()}, Cámara: {cel.get_camara_mp()} MP")
    print(f"Laptop  – Marca: {lap.get_marca()}, Precio: ${lap.get_precio()}, RAM: {lap.get_ram_gb()} GB")

