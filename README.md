# 🛡️ Sistema de Control de Turnos y Seguridad Operativa (Flask)

Sistema web Full-Stack de grado corporativo desarrollado para optimizar la gestión operativa de protecciones de seguridad. Permite un control riguroso y en tiempo real de la asistencia, los tiempos de trabajo, las colisiones, las rondas de vigilancia y la bitácora de incidentes laborales.

---

## 🚀 Características Principales

* **Autenticación completa:** Módulo seguro de registro e inicio de sesión para el personal de seguridad[citar: 5].
* **Control Operativo de Jornada (Turnos):** 
  * Registro de fichaje de entrada al turno.
  * Monitoreo dinámico del tiempo efectivo de trabajo.
  * Gestión automatizada de sales y regresos de colación.
  * Cierre y finalización formal de la jornada laboral.
* **Rondas de Vigilancia:** Los operadores pueden iniciar, visualizar y registrar rondas de control cuyas rutas y marcas se almacenan de forma persistente[citar: 5].
* **Bitácora de Incidentes:** Módulo dedicado al informe y marco de anomalías o eventuales ocurridas durante el estado laboral[citar: 5].

---

## 🛠️ Tecnologías y Arquitectura

El proyecto implementa un stack tecnológico moderno combinando el desarrollo backend estructurado con arquitecturas de **API RESTful** y un frontend dinámico:

* **Backend y API:** Python 3.10+, Flask, Arquitectura de API RESTful[citar: 5]
* **Base de Datos:** MongoDB (NoSQL) con PyMongo para la persistencia optimizada de datos[citar: 5]
* **Frontend y vistas:** Manillar (Hbs), CSS3 para enfermedad responsivo y moderno[citar: 5]
* **Comunicación Asíncrona:** Obtener API para transacciones dinámicas sin recordar la página (turnos, rondas e incidentes)[citar: 5]
* **Control de versiones:** Git y GitHub

---

## 📁 Estructura del Proyecto

El código fuente se encuentra organizado bajo una estructura arquitectura modular para facilitar el mantenimiento y la escalabilidad:

* `config/` — Configuración general del servicio y parámetros de conexión.
* `controladores/` — Lógica de enrutamiento y manejo de peticiones HTTP de la API.
* `base de datos/` — Capa de conexión y gestión con el motor de base de datos.
* `modelos/` — Esquemas de datos para interactuar con la base de datos NoSQL.
* `servicios/` — Lógica de negocio y proceso interno de los fluidos operativos.
* `estético/` — Archivos de recursos visuales, estilos CSS y scripts del cliente.
* `plantillas/` — Interfaces de usuario dinámicas basadas en plantillas[citar: 5].
* `requisitos.txt` — Dependencias y libertades necesarias del ecosistema Python[citar: 5].
* `run.py` — Punto de entrada principal para organizar el servicio web[citar: 5].

---

## ⚙️ Guía de Configuración e Inicio

Sigue estos pasos para desplegar y poner en marcha el sistema en tu entorno local:

### 1. Clonar el repositorio
```bash
clon de git [https://github.com/Byron06010/sistema-seguridad-flask.git](https://github.com/Byron06010/sistema-seguridad-flask.git)
cd sistema-seguridad-flask
