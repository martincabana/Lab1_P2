import csv #importamos archivo csv
import os # importamos archivo os

class Tarea: # creamos una clase llamada Tarea
    def __init__(self, id, descripcion, prioridad, categoria="General"): # creamos un contructor y le damos parametros llamados (id, descripicion, prioridad y categoria)
        self.id = id # Asigna el valor del parámetro id al atributo id del objeto
        self.descripcion = descripcion # Asigna el valor del parámetro descripcion al atributo descripcion del objeto
        self.prioridad = prioridad  # Asigna el valor del parámetro prioridad al atributo prioridad del objeto
        self.completada = False  # Inicializa el atributo completada como false 
        self.categoria = categoria # Asigna el valor del parámetro categoria al atributo categoria del objeto

class Nodo: #creamos una clase llamada nodo
    def __init__(self, tarea): # creamos un contructor y le damos parametros llamada tarea
        self.tarea = tarea # Asigna el valor del parámetro tarea al atributo tarea del objeto
        self.siguiente = None # Inicializa el atributo siguiente como None

class ListaEnlazada: # creamos la clase listaEnlazada
    def __init__(self): # # creamos un contructor
        self.cabeza = None # Inicializa el atributo cabeza como None.
        self.id_actual = 1 # Inicializa el atributo id_actual como 1

    def esta_vacia(self): # definimos la funcion esta vacia
        return self.cabeza is None # nos devuelve la cabeza del la lista si es que no esta vacia
    
    def existe_tarea(self, descripcion): #definimos la funcion existe_tarea
        actual = self.cabeza # definimos una funcion llamada actual y le asignaremos el valor de cabeza
        while actual is not None: # mientras que actual sea diferente a none se ejecutara el while
            if actual.tarea.descripcion == descripcion: # si actual.Tarea.descripcion sean igual a descripicion
                return True # nos devolvera verdadero
            actual = actual.siguiente # la variable actual tomara el valor de actual.siguiente
        return False # nos devolvera false

    def agregar_tarea(self, descripcion, prioridad, categoria): # definimos una funcion llamada agregar_tarea y le pasamos los parametros (descripcion, prioridad, categoria)
        if self.existe_tarea(descripcion):# Si la tarea con la descripción dada ya existe en la lista (existe_tarea retorna True)
            print("La tarea ya existe") # nos devuelve el mensaje La tarea ya existe
            return # sale de la funcion si agregar la tarea
        
        tarea = Tarea(self.id_actual, descripcion, prioridad, categoria) # creamos la variable tarea y le asignaremos el valor de tarea con sus parametros
        nuevo_nodo = Nodo(tarea) #creamos la variable nuevo_nodo y le asignaremos el valor de Nodo(tarea)
        self.id_actual += 1 # se le sumara uno a id_actual

        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: # si self.esta_vacia o tarea.prioridad > self.cabeza.tarea.prioridad ingresara
            nuevo_nodo.siguiente = self.cabeza # nuevo_nodo.siguiente tomara el valor de self.cabeza
            self.cabeza = nuevo_nodo # self.cabeza tomara le asignaremos el valor de nuevo_nodo
        else: # si no cumple las condiciones ingresara
            actual = self.cabeza # la variable actual tomara el valor de self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: #mientras que se cumpla la condicion
                actual = actual.siguiente # actual tomara el valor de actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente # nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo # actual.siguiente tomara el valor de nuevo_nodo

        print("Tarea agregada con éxito.") # imprime el mensaje de tarea agregada con exito

    def buscar_tarea_descripcion(self, texto): # definimos la variable buscar_tarea_descripcion
        pass

    def completar_tarea(self, id): # defimos la funcion completar_tarea con sus parametros
        actual = self.cabeza # creamos la variable actual y tomara el valor de self.cabeza
        while actual is not None: # mientras que se cumpla la condicion ingresara
            if actual.tarea.id == id: # si actual.tarea.id es ingual a id
                actual.tarea.completada = True # actual.tarea.completada tomara el valor true
                print(f"Tarea con ID {id} completada.") # imprime el mensaje de tarea con id completada
                return # sale de la funcion
            actual = actual.siguiente # la variable actual tomara el valor de actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")  # imprime el mensaje de tarea con id no encontrada

    def eliminar_tarea(self, id):
        actual = self.cabeza
        previo = None
        while actual is not None:
            if actual.tarea.id == id:
                if previo is None:
                    self.cabeza = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
                print(f"Tarea eliminada: {actual.tarea.descripcion}")
                return
            previo = actual
            actual = actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")  

    def mostrar_tareas(self):
        actual = self.cabeza
        while actual is not None:
            estado = "Completada" if actual.tarea.completada else "Pendiente"
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}")
            actual = actual.siguiente

    def mostrar_tareas_pendientes(self):
        pass
        
    def mostrar_tareas_descripcion(self, texto):
        pass

    # Funciones estadísticas:
    def contar_tareas_pendientes(self):
        pass

    def mostrar_estadisticas(self):
        pass
        
    # Carga y guardado de archivos
    def guardar_en_csv(self, archivo):
        with open(archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            actual = self.cabeza
            while actual is not None:
                writer.writerow([actual.tarea.id, actual.tarea.descripcion, actual.tarea.prioridad, actual.tarea.categoria, actual.tarea.completada])
                actual = actual.siguiente
        print(f"Tareas guardadas en {archivo} con éxito.")

    def cargar_desde_csv(self, archivo):
        if not os.path.exists(archivo):
            print(f"Archivo {archivo} no encontrado.")
            return
        with open(archivo, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                id, descripcion, prioridad, categoria, completada = int(row[0]), row[1], int(row[2]), row[3], row[4] == 'True'
                tarea = Tarea(id, descripcion, prioridad, categoria)
                tarea.completada = completada
                self.agregar_tarea_existente(tarea)
            print(f"Tareas cargadas desde {archivo} con éxito.")

    def agregar_tarea_existente(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

        if tarea.id >= self.id_actual:
            self.id_actual = tarea.id + 1

def menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Eliminar tarea")
    print("4. Mostrar todas las tareas")
    print("5. Mostrar tareas pendientes")
    print("6. Guardar tareas en archivo CSV")
    print("7. Cargar tareas desde archivo CSV")
    print("8. Salir")

def main():
    lista_tareas = ListaEnlazada()
    archivo_csv = 'tareas.csv'

    # Cargar tareas desde CSV si el archivo existe
    lista_tareas.cargar_desde_csv(archivo_csv)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            if lista_tareas.existe_tarea(descripcion):
                print("La tarea ya existe")
                continue
            
            prioridad = int(input("Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta): "))
            categoria = input("Ingrese la categoría de la tarea: ")
            lista_tareas.agregar_tarea(descripcion, prioridad, categoria)
        elif opcion == "2":
            id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
            lista_tareas.completar_tarea(id_tarea)
        elif opcion == "3":
            id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
            lista_tareas.eliminar_tarea(id_tarea)
        elif opcion == "4":
            lista_tareas.mostrar_tareas()
        elif opcion == "5":
            lista_tareas.mostrar_tareas_pendientes()
        elif opcion == "6":
            lista_tareas.guardar_en_csv(archivo_csv)
        elif opcion == "7":
            lista_tareas.cargar_desde_csv(archivo_csv)
        elif opcion == "8":
            print("Saliendo del sistema de gestión de tareas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
