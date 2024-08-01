import csv  # Importa el módulo csv de la biblioteca estándar de Python
import os  # Importa el módulo os de la biblioteca estándar de Python

# Define la clase Tarea
class Tarea:
    def __init__(self, id, descripcion, prioridad, categoria="General"):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
        self.categoria = categoria

# Define la clase Nodo para la lista enlazada
class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

# Define la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.id_actual = 1
        self.total_pendientes = 0  # Cuenta las tareas pendientes

    def esta_vacia(self):
        return self.cabeza is None

    # Esta función permite agregar una tarea nueva a la lista enlazada
    def agregar_tarea(self, descripcion, prioridad, categoria):
        if self.buscar_tarea_descripcion(descripcion):  # Verifica si la tarea ya existe
            print("La tarea ya existe.")
            return
        
        tarea = Tarea(self.id_actual, descripcion, prioridad, categoria)
        nuevo_nodo = Nodo(tarea)
        self.id_actual += 1

        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

        self.total_pendientes += 1
        print("Tarea agregada con éxito.")

    # Esta función busca una tarea por su descripción
    def buscar_tarea_descripcion(self, texto):
        actual = self.cabeza
        while actual is not None:
            if texto in actual.tarea.descripcion:
                return True
            actual = actual.siguiente
        return False

    # Esta función completa la tarea por su ID
    def completar_tarea(self, id):
        actual = self.cabeza
        while actual is not None:
            if actual.tarea.id == id:
                if actual.tarea.completada:
                    print("La tarea ya está completada.")
                else:
                    actual.tarea.completada = True
                    self.total_pendientes -= 1
                    print(f"Tarea completada: {actual.tarea.descripcion}")
                return
            actual = actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")

    # Esta función permite eliminar una tarea por su ID
    def eliminar_tarea(self, id):
        actual = self.cabeza
        previo = None
        while actual is not None:
            if actual.tarea.id == id:
                if previo is None:
                    self.cabeza = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
                if not actual.tarea.completada:
                    self.total_pendientes -= 1
                print(f"Tarea eliminada: {actual.tarea.descripcion}")
                return
            previo = actual
            actual = actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")

    # Esta función muestra todas las tareas
    def mostrar_tareas(self):
        actual = self.cabeza
        while actual is not None:
            estado = "Completada" if actual.tarea.completada else "Pendiente"
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}")
            actual = actual.siguiente

    # Esta función muestra las tareas pendientes
    def mostrar_tareas_pendientes(self):
        actual = self.cabeza
        while actual is not None:
            if not actual.tarea.completada:
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: Pendiente")
            actual = actual.siguiente

    # Esta función muestra las tareas por descripción
    def mostrar_tareas_descripcion(self, text):
        actual = self.cabeza
        while actual is not None:
            if text in actual.tarea.descripcion:
                estado = "Completada" if actual.tarea.completada else "Pendiente"
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}")
            actual = actual.siguiente

    # Esta función se usa para contar las tareas pendientes
    def contar_tareas_pendientes(self):
        return self.total_pendientes

    # Esta función permite mostrar estadísticas
    def mostrar_estadisticas(self):
        total_tareas = 0
        total_completadas = 0
        actual = self.cabeza
        while actual is not None:
            total_tareas += 1
            if actual.tarea.completada:
                total_completadas += 1
            actual = actual.siguiente
        print(f"Total de tareas: {total_tareas}")
        print(f"Tareas completadas: {total_completadas}")
        print(f"Tareas pendientes: {self.total_pendientes}")

    # Con esta función se puede guardar las tareas en un archivo CSV
    def guardar_en_csv(self, archivo):
        with open(archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            actual = self.cabeza
            while actual is not None:
                writer.writerow([actual.tarea.id, actual.tarea.descripcion, actual.tarea.prioridad, actual.tarea.categoria, actual.tarea.completada])
                actual = actual.siguiente
        print(f"Tareas guardadas en {archivo} con éxito.")

    # Con esta función se cargan las tareas desde un archivo CSV
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

    # Con esta función se agrega una tarea existente (se usa al cargar desde CSV)
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

# Implementando esta función sirve para mostrar el menú de opciones
def menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Eliminar tarea")
    print("4. Mostrar todas las tareas")
    print("5. Mostrar tareas pendientes")
    print("6. Mostrar tareas por descripción")
    print("7. Cargar tareas desde archivo CSV")
    print("8. Guardar tareas en archivo CSV")
    print("9. Mostrar estadísticas")
    print("10. Salir")

# Función principal
def main():
    lista_tareas = ListaEnlazada()
    archivo_csv = 'tareas.csv'

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
            lista_tareas.mostrar_tareas()  # Llama al método mostrar_tarea() para imprimir las tareas de la lista.

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

