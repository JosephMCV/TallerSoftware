class Ciudad:
    def __init__(self, nombre, departamento, pais, poblacion, clima):
        self.nombre = nombre
        self.departamento = departamento
        self.pais = pais
        self.poblacion = poblacion
        self.clima = clima

    def __repr__(self):
        return (f"Ciudad(nombre={self.nombre}, departamento={self.departamento}, pais={self.pais}, "
                f"poblacion={self.poblacion}, clima={self.clima})")
