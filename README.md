# SOAR Log Analyzer

## Descripción General

SOAR Log Analyzer es un proyecto de automatización en ciberseguridad diseñado para detectar ataques de fuerza bruta a partir de registros de autenticación.

El proyecto simula parte del flujo de trabajo de un Centro de Operaciones de Seguridad (SOC) mediante la automatización de las siguientes tareas:

* Análisis de registros de autenticación
* Detección de actividades sospechosas
* Mapeo de detecciones con MITRE ATT&CK
* Clasificación de niveles de severidad
* Generación de evidencias en formato JSON
* Creación de reportes de incidentes en HTML
* Envío de notificaciones a través de Telegram y Discord

## Características

* Detección de ataques de fuerza bruta
* Mapeo con MITRE ATT&CK (T1110)
* Clasificación de severidad
* Generación de alertas en formato JSON
* Recolección de evidencias de incidentes
* Generación de reportes HTML
* Notificaciones mediante Telegram
* Notificaciones mediante Discord

## Tecnologías Utilizadas

* Python
* Docker
* Dev Containers
* Git
* GitHub
* MITRE ATT&CK
* API de Telegram
* Webhooks de Discord

## Estructura del Proyecto

src/
logs/
alerts/
reports/
evidence/

## Hoja de Ruta

* Panel de control con FastAPI
* Integración con TheHive
* Integración con Wazuh
* Gestión de IOC (Indicadores de Compromiso)
* Integración de fuentes de Inteligencia de Amenazas
* Acciones automatizadas de respuesta ante incidentes

## Autor

Ezequiel Perez
Ciberseguridad | Blue Team | SOC | DFIR
