# Sistema de Gestión de Tareas

<<<<<<< HEAD
Este es un sistema de gestión de tareas simple creado en Python utilizando una lista enlazada. Permite agregar, completar, eliminar y mostrar tareas, tambien  guardar y cargar las tareas desde un archivo CSV.
=======
Este es un sistema de gestión de tareas simple creado en Python utilizando una lista enlazada. Permite agregar, completar, eliminar y mostrar tareas, así como guardar y cargar las tareas desde un archivo CSV.
>>>>>>> e6093808ac9715f343eb40c16afb5176e362066f

## Funcionalidades

- **Agregar Tarea**: Permite agregar una nueva tarea con descripción, prioridad y categoría.
- **Completar Tarea**: Marca una tarea como completada utilizando su ID.
- **Eliminar Tarea**: Elimina una tarea de la lista utilizando su ID.
- **Mostrar Todas las Tareas**: Muestra todas las tareas presentes en la lista.
- **Mostrar Tareas Pendientes**: Muestra únicamente las tareas pendientes.
- **Buscar Tareas por Descripción**: Muestra las tareas que contienen un texto específico en su descripción.
- **Guardar en CSV**: Guarda todas las tareas en un archivo CSV.
- **Cargar desde CSV**: Carga tareas desde un archivo CSV.
- **Mostrar Estadísticas**: Muestra estadísticas sobre las tareas (total, completadas y pendientes).

## para su Uso

1. Agregar una Tarea:
   - Selecciona la opción 1 en el menú principal.
   - Ingresa la descripción, prioridad, y categoría de la tarea.

2. Completar una Tarea:
   - Selecciona la opción 2 en el menú.
   - Ingresa el ID de la tarea que deseas marcar como completada.

3. Eliminar una Tarea:
   - Selecciona la opción 3 en el menú.
   - Ingresa el ID de la tarea que deseas eliminar.

4. Mostrar Todas las Tareas:
   - Selecciona la opción 4 en el menú para ver todas las tareas, completadas y pendientes.

5. Mostrar Tareas Pendientes:
   - Selecciona la opción 5 en el menú para ver solo las tareas que aún no han sido completadas.

6. Guardar Tareas en CSV:
   - Selecciona la opción 6 en el menú para guardar todas las tareas en un archivo CSV.

7. Cargar Tareas desde CSV:
   - Selecciona la opción 7 en el menú para cargar tareas desde un archivo CSV existente.

8. Buscar Tareas por Descripción:
   - Selecciona la opción 8 en el menú y proporciona un texto para buscar en las descripciones de las tareas.

9. Mostrar Estadísticas:
   - Selecciona la opción 9 para ver un resumen de las tareas.

10. Mostrar Tareas Pendientes por Categoría:
    - Selecciona la opción 10 para ver cuántas tareas pendientes hay en cada categoría


## Estructura del Código

### Clase Tarea
- Representa una tarea con los atributos: id, descripción, prioridad, completada, y categoría.

### Clase Nodo
- Un nodo que encapsula una tarea y un puntero al siguiente nodo.

### Clase ListaEnlazada
- Implementa una lista enlazada que contiene tareas.
- Métodos principales incluyen: agregar_tarea, completar_tarea, eliminar_tarea, mostrar_tareas, guardar_en_csv, cargar_desde_csv, numero_tareas_pendientes_lineal, y contar_tareas_pendientes.

### Función menu
- Muestra el menú principal.

### Función main
- Punto de entrada del programa, gestiona la interacción del usuario con el sistema de tareas.
### Ejecución del Programa

<<<<<<< HEAD
Para iniciar el programa, corre el archivo `main.py`:
=======
Para iniciar el programa,  corre el archivo `main.py`:
>>>>>>> e6093808ac9715f343eb40c16afb5176e362066f

```bash
python main.py
