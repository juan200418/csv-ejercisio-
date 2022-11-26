import csv


def menu_principal():
    print("*" * 45)
    print("\t1. Crear csv")
    print("\t2. Lectura de archivo csv")
    print("\t3. Actualizar archivo csv")
    print("\t4. Buscar y eliminar un dato")
    print("\t5. Salir")
    print("*" * 45)


def llenar(vector, cnt_personas):
    for i in range(cnt_personas):
        vector.append([])
        for j in range(3):
            dato = str(input("Digite el " + vector[0][j] + " de la persona: "))
            vector[i + 1].append(dato)


def creando(ubicacion_csv, lista_datos):  #Función crear archivo csv
    with open(
            ubicacion_csv, 'w', newline=''
    ) as csvfile:  #with open permite abrir el archivo y crearlo con la sentencia 'w'
        lista_datos = [['Código', 'Nombre',
                        'Apellido'], ['1', 'juan', 'jaimes '],
                       ['2', 'Juan',
                        'García']]  #lista a guardar dentro del archivo plano
        writer = csv.writer(
            csvfile, delimiter=';'
        )  #el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        writer.writerows(
            lista_datos
        )  #el objeto writerows me permite escribir toda la lista en líneas separadas


def leyendo():  #Función leer archivo csv
    dire = 'D:\\Python\\original.csv'  #Directorio donde se encuentra el archivo csv
    with open(
            dire, 'r', newline=''
    ) as csvfile:  #with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
        reader = csv.reader(
            csvfile, delimiter=';'
        )  #el objeto csv.reader permite leer el archivo por medio de los parametro dados
        for row in reader:  #Me permite hacer el recorrido del archivo plano para imprimirlo en pantalla
            print(row)  #Imprime la lista línea por línea


def agregando():  #Función agregar al final del archivo csv
    dire = 'D:\\Python\\original.csv'  #Directorio donde se encuentra el archivo csv
    with open(
            dire, 'r', newline=''
    ) as csvfile:  #with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
        reader = csv.reader(
            csvfile, delimiter=';'
        )  #el objeto csv.reader permite leer el archivo por medio de los parametro dados
        data = [
            line for line in reader
        ]  #La variable data cumple la función de una lista, la cual recibe los datos del csv y los almacena
    with open(
            dire, 'w', newline=''
    ) as csvfile:  #with open permite abrir el archivo y crearlo con la sentencia 'w'
        lista = [['3', 'miguel', 'Moncada'],
                 ['4', 'carlos ',
                  'Manuel ']]  #Lista a agregar al final del archivo
        writer = csv.writer(
            csvfile, delimiter=';'
        )  #el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        writer.writerows(data)  #Escribo los datos que contenia el csv de nuevo
        writer.writerows(
            lista)  #Escribo en el archivo csv los datos de la lista a agregar


def eliminando(
    search
):  #Funcion eliminar, esta elimina la línea que se entrega por parámetro
    dire = 'D:\\Python\\original.csv'  #Dirección del documento
    with open(
            dire, 'r', newline=''
    ) as csvfile:  #with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
        reader = csv.reader(
            csvfile, delimiter=';'
        )  #el objeto csv.reader permite leer el archivo por medio de los parametro dados
        data = [
            line for line in reader
        ]  #La variable data cumple la función de una lista, la cual recibe los datos del csv y los almacena
    with open(
            dire, 'w', newline=''
    ) as csvfile:  #with open permite abrir el archivo y crearlo con la sentencia 'w'
        writer = csv.writer(
            csvfile, delimiter=';'
        )  #el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        data.pop(
            search
        )  #llamando a la lista data se elimina la linea dada utilizando la función pop
        writer.writerows(
            data)  #Escribo los datos que contiene la lista modificada.


#guardar la lista anterior para actualizar el documento, consultar ¿Cómo retornar una lista en python?

vector=[]
cnt_personas=[]

def main():
    continuar=True
    submenu=True
    
    while continuar:
        menu_principal()
        opt=int(input("Seleccione una opción: "))
        if opt==1:
            op=int(input("Presione 1 para llenar la lista, 2 para salir al menu principal\n"))
            val_op=2
            if op == 1:
                while val_op != op:
                    llenar(vector,cnt_personas)
                    op = int(
                        input("Presione 1 para registrar otro partido, 2 para salir al menú principal \n"))
            else:
                print("Opcion no encontrada")

if __name__ == "__main__":
    menu_principal()
    ubicacion_csv = ' '
    lista_datos = [['id', 'nombre', 'apellido']]
    print("Llenar la lista")
    tam = int(input("Ingrese el tamaño de la lista: "))
    llenar(lista_datos, tam)
    print("*" * 68)
    ubicacion_csv = str(input("Ingrese la ubicacion del archivo: "))
    creando(ubicacion_csv, lista_datos)
