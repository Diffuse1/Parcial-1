import csv

class Tablaestudiantes():
    with open('Datos1.csv') as per:
        reader=csv.reader(per)
        for fila in reader:
            print(f'|{fila[0]}|{fila[1]}|{fila[2]}|{fila[3]}|{fila[4]}|{fila[5]}|{fila[6]}|{fila[7]}|{fila[8]}|{fila[9]}|{fila[10]}|{fila[11]}')

print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
class Informaciónestudiantes():
    print('                               \033[36mDatos estudiantes de actuaría UTECA\033[0m')
    with open('Datos.csv') as Lista:
        reader=csv.reader(Lista)
        for fila in reader:
            print(f'Matricula: {fila[0]} Nombre: {fila[1]} Edad: {fila[2]} Cal.1: {fila[3]} Cal.2: {fila[4]} Cal.3: {fila[5]} Cal.4: {fila[6]} Cal.5: {fila[7]} Promedio: {fila[8]} Graduado: {fila[9]} fecha Graduación: {fila[10]} Tesis: {fila[11]}')