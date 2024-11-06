class Persona:
    def __init__(self, id, nombre, genero, cedula, edad, telefono):
        self.id = id
        self.nombre = nombre
        self.genero = genero
        self.cedula = cedula
        self.edad = edad
        self.telefono = telefono

    def __repr__(self):
        return (f"Persona(id={self.id}, nombre={self.nombre}, genero={self.genero}, "
                f"cedula={self.cedula}, edad={self.edad}, telefono={self.telefono})")
