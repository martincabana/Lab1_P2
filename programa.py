import csv  # Importa el módulo csv de la biblioteca estándar de Python
import os  # Importa el módulo os de la biblioteca estándar de Python

# Define la clase Tarea
class Tarea:
    def __init__(self, id, descripcion, prioridad, categoria="General"):
        self.id = id  # ID de la tarea
        self.descripcion = descripcion  # Descripción de la tarea
        self.prioridad = prioridad  # Prioridad de la tarea
        self.completada = False  # Estado de la tarea, por defecto es no completada
        self.categoria = categoria  # Categoría de la tarea

# Define la clase Nodo para la lista enlazada
class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea  # Tarea que guarda el nodo
        self.siguiente = None  # Apunta al siguiente nodo en la lista

# Define la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Cabeza de la lista, inicialmente vacía
        self.id_actual = 1  # ID actual para nuevas tareas
        self.total_pendientes = 0  # Cuenta las tareas pendientes
        
    def esta_vacia(self):
        return self.cabeza is None  # Retorna True si la lista está vacía

    # Agrega una nueva tarea a la lista enlazada
    def agregar_tarea(self, descripcion, prioridad, categoria):
        if self.buscar_tarea_descripcion(descripcion):  # Verifica si la tarea ya existe
            print("La tarea ya existe.")  # Imprime mensaje si la tarea ya está en la lista
            return  # Sale de la función si la tarea ya existe
        
        tarea = Tarea(self.id_actual, descripcion, prioridad, categoria)  # Crea una nueva tarea
        nuevo_nodo = Nodo(tarea)  # Crea un nuevo nodo para la tarea
        self.id_actual += 1  # Incrementa el ID actual

        # Inserta el nuevo nodo en la lista según la prioridad de la tarea
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:
            nuevo_nodo.siguiente = self.cabeza  # Apunta el siguiente nodo del nuevo nodo a la cabeza actual
            self.cabeza = nuevo_nodo  # Actualiza la cabeza de la lista al nuevo nodo
        else:
            actual = self.cabeza  # Comienza desde la cabeza de la lista
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente  # Recorre la lista hasta encontrar la posición adecuada
            nuevo_nodo.siguiente = actual.siguiente  # Apunta el siguiente nodo del nuevo nodo al siguiente nodo del nodo actual
            actual.siguiente = nuevo_nodo  # Actualiza el siguiente nodo del nodo actual al nuevo nodo

        self.total_pendientes += 1  # Incrementa el contador de tareas pendientes
        print("Tarea agregada con éxito.")  # Imprime un mensaje de éxito

    # Busca una tarea por su descripción
    def buscar_tarea_descripcion(self, texto):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual is not None:
            if texto in actual.tarea.descripcion:  # Verifica si el texto está en la descripción de la tarea
                return True  # Retorna True si la tarea se encuentra
            actual = actual.siguiente  # Avanza al siguiente nodo en la lista
        return False  # Retorna False si no se encuentra la tarea

    # Completa la tarea por su ID
    def completar_tarea(self, id):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual is not None:
            if actual.tarea.id == id:  # Verifica si el ID coincide
                if actual.tarea.completada:
                    print("La tarea ya está completada.")  # Imprime mensaje si la tarea ya está completada
                else:
                    actual.tarea.completada = True  # Marca la tarea como completada
                    self.total_pendientes -= 1  # Decrementa el contador de tareas pendientes
                    print(f"Tarea completada: {actual.tarea.descripcion}")  # Imprime mensaje de éxito
                return  # Sale de la función
            actual = actual.siguiente  # Avanza al siguiente nodo en la lista
        print(f"Tarea con ID {id} no encontrada.")  # Imprime mensaje si no se encuentra la tarea

    # Elimina una tarea por su ID
    def eliminar_tarea(self, id):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        previo = None  # Nodo previo, inicialmente None
        while actual is not None:
            if actual.tarea.id == id:  # Verifica si el ID coincide
                if previo is None:
                    self.cabeza = actual.siguiente  # Actualiza la cabeza de la lista si el nodo a eliminar es la cabeza
                else:
                    previo.siguiente = actual.siguiente  # Actualiza el siguiente nodo del nodo previo
                if not actual.tarea.completada:
                    self.total_pendientes -= 1  # Decrementa el contador de tareas pendientes si la tarea no está completada
                print(f"Tarea eliminada: {actual.tarea.descripcion}")  # Imprime mensaje de éxito
                return  # Sale de la función
            previo = actual  # Actualiza el nodo previo
            actual = actual.siguiente  # Avanza al siguiente nodo en la lista
        print(f"Tarea con ID {id} no encontrada.")  # Imprime mensaje si no se encuentra la tarea

    # Muestra todas las tareas
    def mostrar_tareas(self):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual is not None:
            estado = "Completada" if actual.tarea.completada else "Pendiente"  # Define el estado de la tarea
            # Imprime la información de la tarea
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}")
            actual = actual.siguiente  # Avanza al siguiente nodo en la lista

    # Muestra solo las tareas pendientes
    def mostrar_tareas_pendientes(self):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual is not None:
            if not actual.tarea.completada:  # Verifica si la tarea no está completada
                # Imprime la información de la tarea pendiente
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: Pendiente")
            actual = actual.siguiente  # Avanza al siguiente nodo en la lista

    # Muestra las tareas que contienen un texto específico en la descripción
    def mostrar_tareas_descripcion(self, text):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual is not None:
            if text in actual.tarea.descripcion:  # Verifica si el texto está en la descripción de la tarea
                estado = "Completada" if actual.tarea.completada else "Pendiente"  # Define el estado de la tarea
                # Imprime la información de la tarea que contiene el texto
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}")
            actual = actual.siguiente  # Avanza al siguiente nodo en la lista

    # Cuenta las tareas pendientes
    def contar_tareas_pendientes(self):
        return self.total_pendientes  # Retorna el número de tareas pendientes

    # Muestra estadísticas sobre las tareas
    def mostrar_estadisticas(self):
        total_tareas = 0  # Contador de tareas totales
        total_completadas = 0  # Contador de tareas completadas
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual is not None:
            total_tareas += 1  # Incrementa el contador de tareas totales
            if actual.tarea.completada:
                total_completadas += 1  # Incrementa el contador de tareas completadas
            actual = actual.siguiente  # Avanza al siguiente nodo en la lista
        # Imprime las estadísticas de las tareas
        print(f"Total de tareas: {total_tareas}")
        print(f"Tareas completadas: {total_completadas}")
        print(f"Tareas pendientes: {self.total_pendientes}")

    # Guarda las tareas en un archivo CSV
    def guardar_en_csv(self, archivo):
        with open(archivo, mode='w', newline='') as file:  # Abre el archivo en modo escritura
            writer = csv.writer(file)  # Crea un objeto writer para escribir en el archivo CSV
            actual = self.cabeza  # Comienza desde la cabeza de la lista
            while actual is not None:
                # Escribe la información de cada tarea en una fila del archivo CSV
                writer.writerow([actual.tarea.id, actual.tarea.descripcion, actual.tarea.prioridad, actual.tarea.categoria, actual.tarea.completada])
                actual = actual.siguiente  # Avanza al siguiente nodo en la lista
        print(f"Tareas guardadas en {archivo} con éxito.")  # Imprime mensaje de éxito

    # Carga las tareas desde un archivo CSV
    def cargar_desde_csv(self, archivo):
        if not os.path.exists(archivo):  # Verifica si el archivo no existe
            print(f"Archivo {archivo} no encontrado.")  # Imprime mensaje si el archivo no se encuentra
            return  # Sale de la función
        with open(archivo, mode='r') as file:  # Abre el archivo en modo lectura
            reader = csv.reader(file)  # Crea un objeto reader para leer el archivo CSV
            for row in reader:
                id, descripcion, prioridad, categoria, completada = int(row[0]), row[1], int(row[2]), row[3], row[4] == 'True'  # Lee los datos de cada fila
                tarea = Tarea(id, descripcion, prioridad, categoria)  # Crea una nueva tarea con los datos leídos
                tarea.completada = completada  # Establece el estado de completado de la tarea
                self.agregar_tarea_existente(tarea)  # Agrega la tarea existente a la lista
            print(f"Tareas cargadas desde {archivo} con éxito.")  # Imprime mensaje de éxito

    # Agrega una tarea existente (se usa al cargar desde CSV)
    def agregar_tarea_existente(self, tarea):
        nuevo_nodo = Nodo(tarea)  # Crea un nuevo nodo para la tarea existente
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:
            nuevo_nodo.siguiente = self.cabeza  # Apunta el siguiente nodo del nuevo nodo a la cabeza actual
            self.cabeza = nuevo_nodo  # Actualiza la cabeza de la lista al nuevo nodo
        else:
            actual = self.cabeza  # Comienza desde la cabeza de la lista
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente  # Recorre la lista hasta encontrar la posición adecuada
            nuevo_nodo.siguiente = actual.siguiente  # Apunta el siguiente nodo del nuevo nodo al siguiente nodo del nodo actual
            actual.siguiente = nuevo_nodo  # Actualiza el siguiente nodo del nodo actual al nuevo nodo

        if tarea.id >= self.id_actual:
            self.id_actual = tarea.id + 1  # Actualiza el ID actual si el ID de la tarea es mayor o igual

# Función para mostrar el menú de opciones
def menu():
    print("\nMenú:")
    print("1. Agregar tarea")  # Opción para agregar una nueva tarea
    print("2. Completar tarea")  # Opción para completar una tarea existente
    print("3. Eliminar tarea")  # Opción para eliminar una tarea existente
    print("4. Mostrar todas las tareas")  # Opción para mostrar todas las tareas
    print("5. Mostrar tareas pendientes")  # Opción para mostrar solo las tareas pendientes
    print("6. Guardar tareas en archivo CSV")  # Opción para guardar las tareas en un archivo CSV
    print("7. Cargar tareas desde archivo CSV")  # Opción para cargar tareas desde un archivo CSV
    print("8. Mostrar tareas por descripción")  # Opción para mostrar tareas que contienen un texto en la descripción
    print("9. Mostrar estadísticas")  # Opción para mostrar estadísticas de las tareas
    print("10. Salir")  # Opción para salir del programa

# Función principal
def main():
    lista_tareas = ListaEnlazada()  # Crea una instancia de ListaEnlazada
    archivo_csv = 'tareas.csv'  # Nombre del archivo CSV

    # Carga las tareas desde CSV si el archivo ya existe
    lista_tareas.cargar_desde_csv(archivo_csv)

    while True:
        menu()  # Llama a la función menu() que imprime el menú de opciones.
        opcion = input("Seleccione una opción: ")  # Espera que el usuario elija una opción del menú.

        # Agrega una nueva tarea.
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")  # Solicita la descripción de una tarea.
            prioridad = int(input("Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta): "))  # Solicita la prioridad de una tarea y la convierte en un entero.
            categoria = input("Ingrese la categoría de la tarea: ")  # Solicita la categoría de una tarea.
            lista_tareas.agregar_tarea(descripcion, prioridad, categoria)  # Llama al método agregar_tarea() para añadir la nueva tarea a la lista.

        # Completar una tarea existente.
        elif opcion == "2":
            id_tarea = int(input("Ingrese el ID de la tarea a completar: "))  # Solicita el ID de la tarea que hay que completar.
            lista_tareas.completar_tarea(id_tarea)  # Llama al método completar_tarea() para marcar la tarea como completada.

        # Elimina una tarea existente.
        elif opcion == "3":
            id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))  # Solicita el ID de la tarea que va a eliminar.
            lista_tareas.eliminar_tarea(id_tarea)  # Llama al método eliminar_tarea() para eliminar la tarea de la lista.

        # Mostrar todas las tareas.
        elif opcion == "4":
            lista_tareas.mostrar_tareas()  # Llama al método mostrar_tareas() para imprimir las tareas de la lista.

        # Mostrar tareas pendientes.
        elif opcion == "5":
            lista_tareas.mostrar_tareas_pendientes()  # Llama al método mostrar_tareas_pendientes() para imprimir las tareas que todavía no se completaron.
       
        # Guardar tareas en un archivo CSV.
        elif opcion == "6":
            lista_tareas.guardar_en_csv(archivo_csv)  # Llama al método guardar_en_csv() para guardar las tareas en un archivo CSV.
        
        # Cargar tareas desde un archivo CSV.
        elif opcion == "7":
            lista_tareas.cargar_desde_csv(archivo_csv)  # Llama al método cargar_desde_csv() para cargar las tareas desde un archivo CSV.

        # Buscar tareas por descripción.
        elif opcion == "8":
            texto = input("Ingrese el texto de la descripción a buscar: ")  # Solicita el texto que se va a buscar en la descripción de la tarea.
            lista_tareas.mostrar_tareas_descripcion(texto)  # Llama al método mostrar_tareas_descripcion() para buscar y mostrar tareas que contienen el texto especificado.

        # Mostrar estadísticas de las tareas.
        elif opcion == "9":
            lista_tareas.mostrar_estadisticas()  # Llama al método mostrar_estadisticas() para imprimir estadísticas sobre las tareas.

        # Salir del programa.
        elif opcion == "10":
            print("Saliendo del sistema de gestión de tareas.")  # Imprime un mensaje de salida.
            break  # Rompe el bucle while y sale del programa.

        # Opción no válida.
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")  # Imprime un mensaje de error si la opción no es válida.

if __name__ == "__main__":
    main()  # Llama a la función main() para iniciar el programa.
