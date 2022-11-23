# Actividad integradora 1 - Sistemas multiagentes con GC

[![Simulation](https://drive.google.com/uc?export=view&id=1rkH55rg_BLRk9X0niicMeJpPiFH06AcR)](https://www.youtube.com/watch?v=1aoD5HiduaQ)

<p align="center">
Jorge Loredo Meléndez                 A01284185
</p>
<p align="center">
José Carlos de la Torre Hernández     A01235953
</p>
<p align="center">
Rogelio Zaid Sariñana Hernández       A01620778
</p>
<p align="center">
Luis Fernando Delgado Martínez        A01235993
</p>
<p align="center">
Emilio Antonio Pérez Fematt           A01236167
</p>


## Recursos

**Youtube video Simulation:** [Simulation](https://youtu.be/OlZmQauGZtE)

**Unity Complete Project:** [Unity Zip File](https://drive.google.com/file/d/1COnZUTlj568mGyonaclWxen3A8b20cBS/view?usp=sharing)

**Simulation in Unity:** [Robots.exe](https://github.com/JorgeLoredo-1852/Agentes/blob/main/Robots.exe)

**Mesa Agents and Simulation:** [Mesa Agents](https://github.com/JorgeLoredo-1852/Agentes/blob/main/mesaAgents.py)

**Api Script:** [api_https.py](https://github.com/JorgeLoredo-1852/Agentes/blob/main/api_https.py)

## Reporte

### Introducción

El equipo es propietario de un 5 robots que deben de ser programados para recolectar cajas dentro de un Almacén. Los robots se pueden mover en las 4 direcciones adyacentes y cada pila de cajas debe de tener máximo 5 cajas apiladas. El propósito final es que todas las cajas estén ordenadas en estas pilas y el piso limpio.

### Solución

Se modelaron 3 agentes con las siguientes funciones:

![image](https://drive.google.com/uc?export=view&id=1kABjmaow2pnT7cuu5dOc_gyzfk5Aid4C)

Con cada invocación de la funcion **step()**, cada agente realizaba sus funciones. Así mismo se agregaba una línea a los archivos [movimientos.txt](https://github.com/JorgeLoredo-1852/Agentes/blob/main/movement.txt) (Movimiento de los robots) y [boxes.txt](https://github.com/JorgeLoredo-1852/Agentes/blob/main/boxes.txt) (Movimiento de las cajas) con las coordenadas de cada agente y su estado actual.

Finalmente, dentro del archivo de Mesa se definió una **MultiGrid** ("Almacen") que se encargó de crear y posicionar los Robots, Cajas y Pilas. Para comenzar el programa se ejecutaron las siguientes líneas de código:

![image](https://drive.google.com/uc?export=view&id=1XHmglqpiFi_ZrJLUyW5y5h0tDfbeR5kv)

Los parámetros de la clase Almacén son **(Número de Robots, Número de Cajas, width, height)**. La simulación se correrá hasta que no existan más cajas en el piso y se imprimirá el número de total de pasos hechos por cada robot.

### API

Utilizando python y Flask, se crearon dos rutas. La primera para recuperar información sobre los Robots y la segunda para información de las cajas.

![image](https://drive.google.com/uc?export=view&id=19S9Z__pBCZdB6hz-352kq4qr5sbZNwsA)

### Unity

Se crearon assets para el Almacén, las cajas y prefabs para los Robots. De igual manera, se creó un objeto **RobotManager** que se encarga de posicionar cada agente en la siguiente posición (step). 

![image](https://drive.google.com/uc?export=view&id=1z7fcIzHkP7qnkxBV5OFvASH_N1XZamPZ)

Esto se logró a partir de Peticiones a la API. El siguiente Snippet es la funcionalidad general de la Get Request y el posicionamiento con los datos recuperados.

![image](https://drive.google.com/uc?export=view&id=16woJ0JGza6S8xHERSSqUWBF2xJZ-m7oc)




## Instalación

1. Ejecutar mesaAgents.py en ambiente Jupyter o cualquiera que tenga instalado los paquetes mesa y numpy.
2. Se generarán los archivos "movement.txt" y "boxes.txt".
3. Ejecutar api_https.py en ambiente local (python api_https.py) y asegurarse que los archivos .txt estén en el mismo directorio.
4. Instalar el proyecto de Unity o descargar el archivo .exe y ejecutar la simulación.
