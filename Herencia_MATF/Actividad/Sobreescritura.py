from Actividad.Animal import Animal
from Actividad.Animal_Acuatico import Animal_Acuatico
from Actividad.Animal_Terrestre import Animal_Terrestre

animal = Animal("Reptilia", "Iguana Marina")

animal_tierra = Animal_Terrestre("Canino", "Perro", "varias regiones del mundo")

animal_acuatico = Animal_Acuatico("Chondrichthyes", "Tiburón martillo", "pacifico")

animal.andar()

animal_tierra.andar()

animal_acuatico.andar()