# Actividad integradora 1 - Sistemas multiagentes con GC

[![Simulation](https://drive.google.com/uc?export=view&id=1rkH55rg_BLRk9X0niicMeJpPiFH06AcR)](https://www.youtube.com/watch?v=1aoD5HiduaQ)

Jorge Loredo Meléndez             A01284185


## Recursos

Youtube video Simulation: [Simulation](https://youtu.be/OlZmQauGZtE)

Unity Complete Project: [Unity Zip File](https://drive.google.com/file/d/1COnZUTlj568mGyonaclWxen3A8b20cBS/view?usp=sharing)

Simulation in Unity: [Robots.exe](https://github.com/JorgeLoredo-1852/Agentes/blob/main/Robots.exe)

Mesa Agents and Simulation: [Mesa Agents](https://github.com/JorgeLoredo-1852/Agentes/blob/main/mesaAgents.py)

Api Script: [api_https.py](https://github.com/JorgeLoredo-1852/Agentes/blob/main/api_https.py)

## Reporte

### Introducción

El equipo es propietario de un 5 robots que deben de ser programados para recolectar cajas dentro de un Almacén. Los robots se pueden mover en las 4 direcciones adyacentes y cada pila de cajas debe de tener máximo 5 cajas apiladas. El propósito final es que todas las cajas estén ordenadas en estas pilas y el piso limpio.

### Solución

Se modelaron 3 agentes con las siguientes funciones:

![image](https://drive.google.com/uc?export=view&id=1kABjmaow2pnT7cuu5dOc_gyzfk5Aid4C)

Con cada invocación de la funcion step(), cada agente realizaba sus funciones. Así mismo se agregaba una línea a los archivos [movimientos.txt](https://github.com/JorgeLoredo-1852/Agentes/blob/main/movement.txt) (Movimiento de los robots) y [boxes.txt ps://github.com/JorgeLoredo-1852/Agentes/blob/main/boxes.txt) (Movimiento de las cajas) con las coordenadas de cada agente y su estado actual.



## Instalación
