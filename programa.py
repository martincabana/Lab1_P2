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
        actual = self.cabeza  # iniciamos desde la cabeza de la lista
        while actual is not None:  # mientras que actual sea diferente a None
            if texto in actual.tarea.descripcion:  # si el texto se encuentra en la descripción de la tarea actual
                return actual.tarea  # devolvemos la tarea encontrada
            actual = actual.siguiente  # pasamos al siguiente nodo
        return None  # si no se encuentra la tarea, devolvemos None

    def completar_tarea(self, id): # defimos la funcion completar_tarea con sus parametros
        actual = self.cabeza # creamos la variable actual y tomara el valor de self.cabeza
        while actual is not None: # mientras que se cumpla la condicion ingresara
            if actual.tarea.id == id: # si actual.tarea.id es ingual a id
                actual.tarea.completada = True # actual.tarea.completada tomara el valor true
                print(f"Tarea con ID {id} completada.") # imprime el mensaje de tarea con id completada
                return # sale de la funcion
            actual = actual.siguiente # la variable actual tomara el valor de actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")  # imprime el mensaje de tarea con id no encontrada

    def eliminar_tarea(self, id): # definimos una funcion de eliminar_tarea con su parametro
        actual = self.cabeza # la variable actual tomara el valor de self.cabeza
        previo = None # creamos una variable llamada previo y le sagnamos el valor de none
        while actual is not None: # mientras que actual es diferente a none ingresara
            if actual.tarea.id == id: # si actual.tarea.id es igual a id
                if previo is None: # si previo es none
                    self.cabeza = actual.siguiente # self.cabeza tomara el valor de actual.siguiente
                else: # si no
                    previo.siguiente = actual.siguiente # previo.siguiente tomara el valor de actual.siguiente
                print(f"Tarea eliminada: {actual.tarea.descripcion}") # imprime tarea eliminada y el valor que tenga actal.tarea.descripcion
                return # vuelve a la funcion
            previo = actual # previo tomara el valor de actual
            actual = actual.siguiente # actual tomara el valor de actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")   # imprime el mensaje tarea con id no encontrada

    def mostrar_tareas(self): # definimos la funcion mostrar_tarea 
        actual = self.cabeza # la variable actal tomara el valor de self.cabeza
        while actual is not None: # mientras que actual sea diferente a none
            estado = "Completada" if actual.tarea.completada else "Pendiente" # estado tomara el valor Completado si actual.tarea.completada si no estado tomara el valor de pendiente
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}") # imprime el mesaje con el id, la descripcion, la prioridad y la categorial de la tarea
            actual = actual.siguiente # actual tomara el valor de actual.siguiente

    def mostrar_tareas_pendientes(self): # definimos la funcion mostrar_tarea_pendiente
        pass
        
    def mostrar_tareas_descripcion(self, texto): # definimos la funcion  mostrar_tareas_descripcion
        pass

    # Funciones estadísticas:
    def contar_tareas_pendientes(self):  # definimos la funcion contar_tareas_pendientes
        pass

    def mostrar_estadisticas(self):  # definimos la funcion mostrar_estadisticas
        pass
        
    # Carga y guardado de archivos
    def guardar_en_csv(self, archivo):  # definimos la funcion
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

    def agregar_tarea_existente(self, tarea): # definimos la funcion agregar_tarea_existente
        nuevo_nodo = Nodo(tarea)  # Creamos un nuevo nodo que contiene la tarea
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: # Si la lista está vacía o la prioridad de la nueva tarea es mayor que la prioridad de la tarea en la cabeza de la lista
            nuevo_nodo.siguiente = self.cabeza  # El siguiente nodo del nuevo nodo será la cabeza actual de la lista
            self.cabeza = nuevo_nodo  # La cabeza de la lista ahora es el nuevo nodo
        else: 
            actual = self.cabeza # actual tomara el valor de cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: #mientras que actual.siguiente is diferente a none y actual.siguiente.tarea.prioridad >= tarea.prioridad ingresara al bucle
                actual = actual.siguiente # actual tomara el valor de actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente #  nuevo_nodo.siguiente tomara el valor de actual.siguiente
            actual.siguiente = nuevo_nodo # actual.siguiente tomara el valor de nuevo_nodo

        if tarea.id >= self.id_actual: # si tarea.id es mayor o igual a id_actual
            self.id_actual = tarea.id + 1 # id_actual tomara el valor de tarea.id + 1

def menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Eliminar tarea")
    print("4. Buscar tarea por descripcion")
    print("5. Mostrar todas las tareas")
    print("6. Mostrar tareas pendientes")
    print("7. Guardar tareas en archivo CSV")
    print("8. Cargar tareas desde archivo CSV")
    print("9. Salir")

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
             texto = input("Ingrese la descripción de la tarea: ")
             tarea = lista_tareas.buscar_tarea_descripcion(texto)  # Actualiza esta línea
             if tarea:
                 print(f"Tarea encontrada: ID: {tarea.id}, Descripción: {tarea.descripcion}, Prioridad: {tarea.prioridad}, Categoría: {tarea.categoria}, Estado: {'Completada' if tarea.completada else 'Pendiente'}")
                 
             else:
                 print("No se encontró ninguna tarea con esa descripción.")

            
        elif opcion == "5":
            lista_tareas.mostrar_tareas()
        elif opcion == "6":
            lista_tareas.mostrar_tareas_pendientes()
        elif opcion == "7":
            lista_tareas.guardar_en_csv(archivo_csv)
        elif opcion == "8":
            lista_tareas.cargar_desde_csv(archivo_csv)
        elif opcion == "9":
            print("Saliendo del sistema de gestión de tareas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
