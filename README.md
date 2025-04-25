# Adivineta

Bienvenido a Adivineta!  
Un juego de lógica matemática y conversión binaria/decimal hecho con Python donde podrás poner a prueba tu conocimiento.  
Ejecuta el juego, selecciona la dificultad y a disfrutar!

## Requisitos

### 1. Instalar Python  
Antes de comenzar asegurate de tener instalado Python. Si no lo tenes podes descargarlo desde el siguiente [enlace](https://www.python.org/downloads/).  

### 2. Instalar la librería readchar
Con Python ya descargado e instalado, el próximo paso será ejecutar el siguiente comando para instalar la librería readchar, que usaremos para hacer del programa un juego interactivo:

```
pip install readchar
```

### 3. Ejecutar el juego
Una vez instalado python y readchar, podremos ejecutar el juego desde la terminal o desde nuestro IDE favorito(VSCode, PyCharm, etc), con el siguiente comando:
```
python index.py
```

## ¿Cómo jugar?

Podremos navegar entre las opciones **Jugar**, **Cambiar la dificultad** y **Salir** con las teclas ↑(UP) y ↓(DOWN).

- Jugar:  
Ejecutamos el juego según la dificultad seleccionada.

- Cambiar la dificultad:  
Podremos seleccionar la dificultad que va a definir el modo de juego
  - *Fácil: Convertí números binarios a decimales.*
  - *Medio: Resolvé sumas o restas simples y convertí el resultado a binario.*
  - *Difícil: Resolvé multiplicaciones o divisiones, y convertí el resultado a binario*
- Salir:  
Fin del juego.

Respondé correctamente para acumular puntos!
Una respuesta incorrecta termina el juego.  


## Estructura del proyecto

El programa está dividido en módulos funcionales para facilitar la lectura  y mantenimiento:

### 1 . Importaciones  

Vamos a hacer uso de las siguientes librerías;  
 - **os**:  
 para poder ejecutar comandos del sistema operativo en el que estemos.

 - **random**:  
 para generar números y operaciones aleatorias.

 - **readchar**:  
 para detectar las teclas de direcciones UP/DOWN y así navegar entre las opciones.

### 2 . Menús  

Vamos a definir funciones que tendrán la lógica de mostrar un menú con sus opciones a partir de los parámetros recibidos, lo que brinda flexibilidad ya que el menú podrá adaptarse a distintos contextos, como veremos más adelante en *menu_principal*.

 - *clearConsole()*:  
 Limpia la consola según el Sistema operativo.

 - *mostrar_menu(titulo, opciones, seleccionada, nombre_equipo)*:  
 Muestra un menú interactivo a partir de los parametros recibidos.

 - *navegar_menu(titulo, opciones, nombre_equipo)*:  
Hacemos uso de la función *mostrar_menu* y la librería *readchar* para permitir la navegación por el menú con las teclas UP/DOWN y ENTER.

### 3 . Juego  

Definimos las funciones encargadas de comenzar el juego.

 - *juego(dificultad)*:  
 Inicia el juego según la dificultad recibida, también se encarga de mostra preguntas con sus respectivas opciones y acumula puntos al responder bien.

 - *decimal_a_binario(numero)*:  
 Convierte un número decimal a binario.

 - *generar_pregunta(dificultad)*:  
 Encargada de generar preguntas aleatorias según la dificultad seleccionada:
   - *Fácil: Convertir binario a decimal.*

   - *Medio: Operaciones de suma/resta con resultado en binario.*

   - *Difícil: Operaciones de multiplicación/división con resultado en binario.*

 - *generar_opciones(correcta, base)*:  
 Esta función es lancargada de crear una lista de cuatro opciones, con la correcta y tres falsas, en binario o decimal.

 ### 4 . Flujo principal  

 - *menu_principal()*:  
 Mostramos el menú principal del juego con las opciones *Jugar*, *Cambiar dificultad* y *Salir*.
 
 ### 5 . Inicio  

Nos aseguramos de iniciar el juego llamando a la función *menu_principal()* solo al ejecutar este archivo.