import random
import sqlite3

def generar_censo(cantidad):
  censo = []
  alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZAEIOUAEOI"
  numero = 0

  print("Creando censo...")

  for i in range(500_000):
    aumento = random.randint(1,2)
    numero += aumento
    letras = random.sample(alfabeto, 5)
    nombre = "".join(letras)
    edad = random.randint(18,99)
    impuestos = random.choice((True, True, True, False))
    censo.append([numero, nombre, edad, impuestos])
  return censo

def main():
  cantidad_registros =  1050000
  censo = generar_censo(cantidad_registros)

#conecion a la base de datos