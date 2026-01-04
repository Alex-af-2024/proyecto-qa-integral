🧪 Proyecto QA Integral - Aseguramiento de Calidad Multicapa

Este repositorio contiene la implementación técnica de un Proyecto QA Integral, cuyo objetivo es demostrar el dominio en el aseguramiento de calidad sobre distintas capas de un sistema (API, Base de Datos y UI), integrando pruebas manuales y automatizadas con una trazabilidad completa mediante Jira + Xray.

---

🧠 Filosofía de Calidad

"El código no es evidencia. La evidencia es el resultado observable de la prueba: screenshots, logs y reportes. El script vive en Git, pero la evidencia de ejecución vive en Jira/Xray".

---

🛠️ Stack Tecnológico

• Lenguajes: Python (Pytest, PyMongo, Selenium WebDriver).
• API Testing: SoapUI (Servicios SOAP/WSDL).
• Base de Datos: MongoDB (Dockerizado) + MongoDB Compass.
• Gestión y Trazabilidad: Jira Cloud + Xray (Gestión de Epic, Stories, Test Sets y Test Plans).
• Infraestructura: Docker (Entornos portables).

---

📖Documentación Formal

Para una revisión detallada de la gestión de Sprints (1 y 2), planificación en Jira/Xray y el análisis de resultados, puedes acceder a:

![Descargar Informe Integral QA(PDF)](/docs/Informe_Integral_QA.pdf)

🏗️ Estructura del Proyecto y Capas Probadas

1. Capa de API (Servicios SOAP)
   • Servicio: Web Service público de Calculadora.
   • Alcance: Validación de contrato mediante WSDL, creación de Test Suites y Test Cases en SoapUI.
   • Validaciones: Implementación de assertions de código de estado HTTP 200, validación de contenido XML y reglas de negocio mediante XPath Match.
2. Capa de Datos (MongoDB + Docker)
   • Entorno: Contenedor de MongoDB desplegado en Docker para garantizar un ambiente de pruebas limpio y portable.
   • Validaciones: Scripts en Python (PyMongo) para verificar la integridad de los datos.
   ◦ Existencia de registros y usuarios activos.
   ◦ Consistencia de formato en emails y verificación de campos obligatorios.
3. Capa de Interfaz de Usuario (UI Automation)
   • Herramientas: Selenium WebDriver + Pytest.
   • Flujo: Automatización del login funcional en la plataforma SauceDemo.
   • Lógica: Localización de elementos vía DOM, manejo de aserciones de URL y captura automática de evidencias (screenshots) ante fallos.

---

📊 Gestión de Pruebas y Trazabilidad (Jira + Xray)

La gestión del ciclo de vida de las pruebas no ocurre de forma aislada. Se utiliza Xray como núcleo de trazabilidad:
• Jerarquía: Epic ➔ User Story ➔ Test ➔ Test Execution.
• Resultados: Los tests automatizados ejecutados localmente generan reportes en formato JUnit XML, los cuales se importan automáticamente a Jira/Xray para registrar el estado (PASS/FAIL) y adjuntar las evidencias recolectadas.

---

🚀 Instalación y Ejecución

1. Clonar el repositorio:
2. Configurar entorno virtual (Recomendado):
3. Instalar dependencias:
4. Ejecutar pruebas UI y generar reporte XML para Xray:

---

👤 Información del Autor
• Nombre: Alejandro Franco Acosta
• Rol: Analista Programador | QA Consultant
• Educación: 4to Semestre Analista Programador - IP Santo Tomás (Promedio Destacado)

---

💡 Nota técnica para reclutadores:
Este repositorio demuestra un flujo de trabajo profesional donde Jira/Xray actúa como el sistema de registro, mientras que las herramientas técnicas (Selenium, SoapUI, Python) actúan como los ejecutores. La trazabilidad entre el código y la gestión de calidad es el eje central de mi metodología de trabajo.
