📑 Informe Técnico: Proyecto QA Integral
Autor: Alejandro Franco Acosta
Rol: QA Tester / Analista Programador
Periodo: Sprint 1 – Sprint 2

1. Introducción
   Este informe documenta el aseguramiento de calidad aplicado sobre distintas capas de un sistema, combinando pruebas manuales y automatizadas. El objetivo principal es demostrar la competencia técnica en validaciones de API, Base de Datos y UI, manteniendo una trazabilidad absoluta mediante Jira/Xray como eje de gestión.

2. Alcance del Proyecto
   Las pruebas cubrieron las siguientes áreas críticas:
   • API: Validación de servicios SOAP mediante contrato WSDL.
   • Base de Datos: Integridad y consistencia en MongoDB (Dockerizado).
   • UI: Automatización de flujos funcionales con Selenium.
   • Gestión QA: Ciclo de vida completo en Jira/Xray.

---

3. Pruebas de API (SOAP)
   Se utilizó SoapUI para validar un servicio público de calculadora, generando Test Suites y Test Cases a partir del WSDL.
   Evidencias de API

   - Validación de estructura de mensajes SOAP y códigos de respuesta HTTP.

     ![evidencia_request_response_soap](/evidencias/screenshots/evidencia_api_soap.png)

   * Implementación de assertions funcionales (Contains y XPath Match).

     ![evidencia_test_suite_soapui](/evidencias/screenshots/evidencia_test_Suite.png)

   * Registro de Test en Jira

     ![evidencia_test_jira](/evidencias/screenshots/evidencia_test_jira.png)

---

4. Pruebas de Base de Datos (MongoDB)
   Para garantizar la portabilidad, se utilizó Docker para levantar la instancia de MongoDB. Las validaciones incluyeron la existencia de registros, usuarios activos y formato de correos.

   - Evidencias de Base de Datos con modelado flexible
     Validación manual de colecciones y documentos en MongoDB Compass.

     ![evidencia_ddbb_NoSQL](/evidencias/screenshots/evidencia_mongo_ddbb.png)

   - Resultado del script de validación automatizada usando PyMongo.

     ![evidencia_script_validar_usuarios](/evidencias/screenshots/evidencia_script_confirmacion_usuarios.png)

---

5. Pruebas UI Automatizadas (Selenium + Pytest)
   Se automatizó el flujo de login de SauceDemo para validar el acceso exitoso y la redirección al inventario de productos.
   Evidencias de UI

   - Implementación de selectores DOM y aserciones con Pytest.

     ![evidencia_script_automatizacion](/evidencias/screenshots/evidencia_automatizacion_selenium.png)

   - Ejecución exitosa del test y generación de reporte JUnit XML.

     - UI despues de ejecutar script

       ![evidencia_ejecution_script](/evidencias/screenshots/evidencia_ejecucion_automatizacion.png)

     - Resultado de ejecución Pytest

       ![evidencia_reporte_JUnit](/evidencias/screenshots/evidencia_ejecucion_pytest.png)

     - Reporte JUnit XML

       ![evidencia_reporte_JUnit](/evidencias/screenshots/evidencia_reporte_junit.png)

---

6. Gestión de Pruebas y Trazabilidad (Jira + Xray)
   Toda la ejecución técnica se reflejó en Jira/Xray para asegurar la trazabilidad entre los requerimientos y los resultados.
   Evidencias de Gestión

   - Diseño de pasos detallados con datos y resultados esperados.

     - Creación de Test con imagen de referencia
       ![evidencia_crear_test](/evidencias/screenshots/evidencia_test_jira_xray.png)

     - Diseñar Test con pasos detallados
       ![evidencia_pasos_test](/evidencias/screenshots/evidencia_pasos_test_xray.png)

     - Crear Test Execution y agregar test para su ejecución y registro
       ![evidencia_test_execution](/evidencias/screenshots/evidencia_test_execution.png)

     - Registro de evidencias al ejecutar test
       ![evidencia_pasos_test](/evidencias/screenshots/evidencia_registro_evidencia_testExec.png)

   - Estado final de la ejecución (PASSED) tras importar el reporte XML.

     ![evidencia_XML_importado](/evidencias/screenshots/evidencia_import_junit_passed.png)

---

7. Conclusiones y Recomendaciones
   El proyecto permitió aplicar un enfoque de calidad multicapa exitoso. Como recomendaciones para futuras fases se sugiere:
1. Implementar Page Object Model (POM) en la automatización UI para mejorar la mantenibilidad.
1. Externalizar credenciales y datos sensibles de los scripts.
1. Integrar los reportes XML en pipelines de CI/CD para una ejecución continua.

---

Nota: "El código no es evidencia. La evidencia es el resultado observable: screenshots, logs y reportes. El script vive en Git, pero la evidencia vive en Jira/Xray".
