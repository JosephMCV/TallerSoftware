import csv
from faker import Faker
import random


fake = Faker()

num_personas = 100000
num_ciudades = 1000


ciudades = []
with open('database/ciudad.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['nombre', 'departamento', 'pais', 'poblacion', 'clima']) 
    
    for _ in range(num_ciudades):
        nombre = fake.city()
        departamento = fake.state()
        pais = fake.country()
        poblacion = fake.random_int(min=50000, max=1000000)
        clima = random.choice(['Tropical', 'Seco', 'Templado', 'Frío'])
        
        writer.writerow([nombre, departamento, pais, poblacion, clima])
        ciudades.append(nombre)  


with open('database/persona.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'nombre', 'genero', 'cedula', 'edad', 'telefono', 'ciudad']) 
    
    for i in range(1, num_personas + 1):
        nombre = fake.name()
        genero = random.choice(['M', 'F'])
        cedula = fake.unique.random_int(min=1000000, max=9999999)
        edad = fake.random_int(min=18, max=90)
        telefono = fake.phone_number()
        ciudad = random.choice(ciudades)  

        writer.writerow([i, nombre, genero, cedula, edad, telefono, ciudad])
