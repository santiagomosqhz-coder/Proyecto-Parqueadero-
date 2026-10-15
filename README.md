### Sistema de Generación y Visualización de Placas de Parqueadero

## Contenido
- [Descripción del proyecto](#descripción del proyecto)
- [Componentes principales](#componentes principales)
- [Reglas de funcionamiento](#reglas de funcionamiento)
- [Tecnologías requeridas](tecnologías requeridas)

## Descripción del proyecto
El proyecto consiste en desarrollar un sistema que genere placas de vehículos y transmita la información mediante sockets en C++, para visualizar y controlar la ocupación de las celdas de un parqueadero.

## Componentes principales

1. **Generador de placas (C++):** Genera y envía placas de vehículos cada 2 o 5 segundos, incluyendo la hora y la celda de parqueadero asignada.

2. **Comunicación cliente-servidor (C++):** Utiliza sockets para transmitir y recibir la información entre dos procesos independientes: un cliente y un servidor.

3. **Visualizador (Python o Java):** Muestra la información recibida e incorpora una librería dinámica que permita acceder a los datos del generador de placas.

## Reglas de funcionamiento
- Cada registro debe incluir la placa, la hora y la celda de parqueadero.
- La información se transmite desde el generador hasta el visualizador.
- Cuando una placa aparece por primera vez, se registra la ocupación de una celda.
- Cuando una placa se recibe nuevamente, se interpreta como la salida del vehículo y la liberación de su celda.

## Tecnologías requeridas
- **C++:** Generación de placas y comunicación mediante sockets.
- **Python:** Desarrollo del visualizador.
- **Librería dinámica:** Integración entre el generador y el visualizador.
- **Sockets:** Comunicación entre los procesos cliente y servidor.
