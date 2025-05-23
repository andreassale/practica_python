import csv
"""## **Etapa 2.**
**Carga de la Información de los Consumidores**

Consigna 7

Definir una clase **Consumidor** que tenga los siguientes

  - Atributos:

    `submission_id`: Identificador único del consumidor.

    `age`: Rango de edad (str).

    `gender`: Género (str).

    `cups`: Número de tazas que consume por día (str).

    `where_drink`: Lugares donde consume café (list[str]).

    `favorite`: Café preferido (str).

    `roast_level`: Nivel de tueste (str).

    `caffeine`: Tipo de cafeína (str).

    `education_level`: Nivel de educación (str).

    `employment_status`: Estado o situación laboral (str).

  - Métodos:

    `__init__`: Para inicializar los atributos.

    `__str__`: Para representar al consumidor de manera legible.

  Complete el siguiente código. Agregue todos los argumentos que necesite a los métodos.
"""

class Consumidor:

  def __init__(self, submission_id, age, gender, cups, where_drink, favorite, roast_level, caffeine, education_level, employment_status):

    self.submission_id = submission_id #Identificador único del consumidor.
    self.age = age #Rango de edad (str).
    self.gender = gender  #Género (str).
    self.cups = cups #Número de tazas que consume por día (str).
    self.where_drink = where_drink #Lugares donde consume café (list[str]).
    self.favorite = favorite #Café preferido (str).
    self.roast_level = roast_level #Nivel de tueste (str).
    self.caffeine = caffeine #Tipo de cafeína (str).
    self.education_level=  education_level #Nivel de educación (str).
    self.employment_status = employment_status #Estado o situación laboral (str).
    

  def __str__(self):
    return f"ID: {self.submission_id}: \
      \nAños: {self.age} \
      \nGénero: {self.gender}\
      \nN°de tazas que consume por día: {self.cups}\
      \nLugares donde consume café: {self.where_drink}\
      \nCafé preferido: {self.favorite}\
      \nNivel de tueste: {self.roast_level}\
      \nTipo de cafeína: {self.caffeine}\
      \nNivel de educación: {self.education_level}\
      \nEstado o situación laboral: {self.employment_status}"
  
  def __repr__(self):
    return self.__str__() 

#Esto es para probar la función _str_
#persona = Consumidor(1, 25, "Fem", "dos", "casa", "negro", "medio", "alto", "Uni", "empleado")
#print(persona)
  
  
'''
Consigna 8:

Implemente una función llamada **cargar_consumidores** que reciba como argumento el nombre del archivo de la encuesta 
y devuelva un diccionario donde la clave sea el `submission_id` (ID del consumidor) y el valor sea una instancia de la clase `Consumidor`."""

'''
  
def cargar_consumidores(archivo:str) -> dict[str,'Consumidor']:
  consumidores_dic = {}
  id, age, gender, cups, where_drink, favorite, roast_level, caffeine, education_level, employment_status = '', '', '', '', '', '', '', '', '', ''

  with open(archivo, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)        
    for row in reader:
      for clave, valor in row.items():
        if clave == "submission_id":
          id = valor
        if clave == "age": 
          age = valor
        if clave == "gender":
          gender = valor
        if clave == "cups":
          cups = valor
        if clave == "where_drink":
          where_drink = valor
        if clave == "favorite":
          favorite = valor
        if clave == "roast_level":
          roast_level = valor
        if clave == "caffeine":
          caffeine = valor
        if clave == "education_level":
          education_level = valor
        if clave == "employment_status":
          employment_status = valor
      persona = Consumidor(id, age, gender, cups, where_drink, favorite, roast_level, caffeine, education_level, employment_status)
      consumidores_dic[id] = persona
  return consumidores_dic

#Esto es para llamar y probar la función
consumidores = cargar_consumidores("coffee_survey.csv")
#print(consumidores)

'''
Consigna 9:

Implemente una función llamada **filtrar_por_atributo_valor** que reciba un diccionario de consumidores 
como el creado en el punto anterior, un nombre de atributo (cualquiera de los atributos presentes en la clase Consumidor) 
y un valor de dicho atributo como argumentos. La función debe recorrer el diccionario y filtrar los consumidores, 
devolviendo otro diccionario cuyos consumidores hayan pasado el filtro aplicado."""
'''

def filtrar_por_atributo_valor(cons:dict[str,'Consumidor'], atributo:str, valor:str) -> dict[str,'Consumidor']:
  filtrar_atributo_dic = {}

  for clave, dato in cons.items():
    if getattr(dato, atributo) == valor:
      filtrar_atributo_dic[clave] = dato
  return filtrar_atributo_dic 

#filtrar_atributo = filtrar_por_atributo_valor(consumidores, "where_drink", "At the office")
#print(filtrar_atributo)
  
"""
Consigna 10: 

Invocando a las funciones anteriores, ¿podría crear un diccionario que corresponda a los consumidores de género femenino (*Female*) 
cuya edad supere los 44 años?
"""
fem_45 = {}

filtrar_atributo = filtrar_por_atributo_valor(consumidores, "gender", "Female")

for clave, valor in filtrar_atributo.items():
  if valor.age == "45-54 years old" or valor.age == "55-64 years old" or valor.age == ">65 years old":
    fem_45[clave] = valor

print(fem_45)
