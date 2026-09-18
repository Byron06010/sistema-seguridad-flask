# 🛡️ Sistema de Control de Turnos y Seguridad Operativa (Flask)

Sistema web Full-Stack de grado corporativo desarrollado para optimizar la gestión operativa de guardias de seguridad. Permite un control riguroso y en tiempo real de la asistencia, los tiempos de trabajo, las colaciones, las rondas de vigilancia y la bitácora de incidentes laborales.

---

## 🚀 Características Principales

* **Autenticación Completa:** Módulo seguro de registro e inicio de sesión para el personal de seguridad.
* **Control Operativo de Jornada (Turnos):** 
  * Registro de fichaje de entrada al turno.
  * Monitoreo dinámico del tiempo efectivo de trabajo.
  * Gestión automatizada de salidas y regresos de colación.
  * Cierre y finalización formal de la jornada laboral.
* **Rondas de Vigilancia:** Los operadores pueden iniciar, visualizar y registrar rondas de control cuyas rutas y marcas se almacenan de forma persistente.
* **Bitácora de Incidentes:** Módulo dedicado al reporte y marcaje de anomalías o eventualidades ocurridas durante el estado laboral.

---

## 🛠️ Tecnologías y Arquitectura

El proyecto implementa un stack tecnológico moderno combinando el desarrollo backend estructurado con arquitecturas de **API RESTful** y un frontend dinámico:

* **Backend & API:** Python 3.10+, Flask, Arquitectura de API RESTful
* **Base de Datos:** MongoDB (NoSQL) con PyMongo para la persistencia optimizada de datos
* **Frontend & Vistas:** Handlebars (Hbs), CSS3 para diseño responsivo y moderno
* **Comunicación Asíncrona:** Fetch API para transacciones dinámicas sin recargar la página (turnos, rondas e incidentes)
* **Control de Versiones:** Git y GitHub

---

## 📁 Estructura del Proyecto

El código fuente se encuentra organizado bajo una estricta arquitectura modular para facilitar el mantenimiento y la escalabilidad:

* `config/` — Configuración general del servidor y parámetros de conexión.
* `controladores/` — Lógica de enrutamiento y manejo de peticiones HTTP de la API.
* `base de datos/` — Capa de conexión y gestión con el motor de base de datos.
* `modelos/` — Esquemas de datos para interactuar con la base de datos NoSQL.
* `servicios/` — Lógica de negocio y procesamiento interno de los flujos operativos.
* `estático/` — Archivos de recursos visuales, estilos CSS y scripts del cliente.
* `plantillas/` — Interfaces de usuario dinámicas basadas en plantillas.
* `requisitos.txt` — Dependencias y librerías necesarias del ecosistema Python.
* `run.py` — Punto de entrada principal para arrancar el servidor web.

---

## ⚙️ Guía de Configuración e Inicio

Sigue estos pasos para desplegar y poner en marcha el sistema en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Byron06010/sistema-seguridad-flask.git](https://github.com/Byron06010/sistema-seguridad-flask.git)
cd sistema-seguridad-flask
