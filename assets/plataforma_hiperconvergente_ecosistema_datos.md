# Plataforma hiperconvergente con gobernanza normativa de grandes volúmenes de datos digitales para procesos de analítica, ciencia e inteligencia artificial agéntica


# Glosario

| Término | Definición |
|---|---|
| API | Interfaz programática que permite la comunicación entre aplicaciones o servicios |
| CDC | Captura de cambios en una fuente de datos para replicar inserciones, modificaciones y eliminaciones |
| Data lake | Repositorio escalable para datos en múltiples formatos |
| Data lakehouse | Arquitectura que combina almacenamiento flexible con capacidades de gestión y consulta analítica |
| Data mesh | Enfoque de responsabilidad de datos distribuida por dominios con plataforma de autoservicio y gobierno federado |
| Data product | Conjunto de datos mantenible y documentado, con responsable, contrato y nivel de servicio |
| Data steward | Responsable operativo de definiciones, metadatos y calidad de un dominio |
| HCI | Infraestructura hiperconvergente que integra cómputo, almacenamiento y virtualización/gestión de red |
| IA agéntica | Sistemas de IA que planifican y realizan tareas mediante herramientas bajo límites establecidos |
| Linaje | Registro del origen y de las transformaciones que explican cómo se produjo un dato o resultado |
| MLOps | Prácticas para desarrollar, desplegar, operar y monitorear modelos de aprendizaje automático |
| RAG | Generación aumentada por recuperación de fuentes externas autorizadas |
| RPO | Objetivo de punto de recuperación: pérdida máxima de datos tolerable |
| RTO | Objetivo de tiempo de recuperación: tiempo máximo u objetivo para restablecer un servicio |

<br><br>

# 1. Fundamentos de Ecosistemas de Datos y Arquitecturas Hiperconvergentes

## 1.1. Descripción general

Un ecosistema de datos es el conjunto organizado de actores, fuentes, activos, plataformas, procesos, reglas y servicios que participan en la producción, intercambio, administración y aprovechamiento de datos. Su funcionamiento requiere acuerdos técnicos y organizativos: quién produce los datos, quién responde por ellos, quién puede utilizarlos, bajo qué condiciones, con qué calidad y para qué finalidades.

Una arquitectura hiperconvergente aporta una base de infraestructura integrada y escalable para ejecutar cargas de trabajo de datos. Sin embargo, por sí sola no resuelve problemas de semántica, calidad, privacidad, linaje, interoperabilidad o responsabilidad. Estos elementos deben diseñarse como servicios y controles de la plataforma de datos.

En el contexto de una plataforma institucional, el objetivo es establecer una base común que permita administrar datos estructurados, semiestructurados y no estructurados, y ofrecer capacidades reutilizables a las áreas de negocio, investigación, analítica e IA.

## 1.2. Objetivos

- Construir una visión integral de los datos como activo institucional y no como subproducto de los sistemas operativos.
- Integrar fuentes heterogéneas mediante patrones de interoperabilidad y contratos de datos.
- Proporcionar una arquitectura modular que crezca por capacidad y demanda, sin rediseños innecesarios.
- Separar las responsabilidades de infraestructura, operación de datos, gobierno y consumo analítico.
- Facilitar la reutilización segura de conjuntos de datos, productos de datos y servicios comunes.
- Reducir silos, duplicidad, inconsistencias y tiempos de acceso a información confiable.

## 1.3. Conceptos fundamentales

### Ecosistema, dominio y producto de datos

- **Dominio de datos:** ámbito de conocimiento o responsabilidad organizacional, por ejemplo, finanzas, operaciones, personas, investigación o atención ciudadana.
- **Propietario del dato (data owner):** responsable de las decisiones y reglas de negocio relativas a un conjunto de datos.
- **Custodio o administrador técnico (data steward/custodian):** mantiene definiciones, calidad, metadatos y controles operativos de acuerdo con las políticas aprobadas.
- **Producto de datos:** conjunto publicable y mantenible de datos, metadatos, reglas de calidad, interfaces, documentación, responsable, nivel de servicio y condiciones de uso.
- **Contrato de datos:** acuerdo explícito entre productor y consumidor sobre esquema, significado, periodicidad, calidad, disponibilidad, compatibilidad y tratamiento de cambios.

### Tipos de datos

- **Estructurados:** organizados en esquemas tabulares o relacionales.
- **Semiestructurados:** contienen etiquetas o estructuras flexibles, como JSON, XML y registros de eventos.
- **No estructurados:** documentos, imágenes, audio, video, texto libre, planos y otros objetos binarios.
- **Datos maestros y de referencia:** describen entidades centrales y catálogos compartidos, como personas, productos, ubicaciones, unidades de medida o clasificaciones.
- **Metadatos:** datos que describen otros datos: definición, estructura, origen, responsable, fecha, clasificación, calidad, retención y condiciones de uso.

### Arquitecturas de datos

- **Data warehouse:** almacén analítico con datos integrados y modelados para consulta y reporte.
- **Data lake:** repositorio escalable que conserva datos en diversos formatos, incluidos datos sin transformar o con transformación limitada.
- **Lakehouse:** patrón que combina almacenamiento flexible de lago con capacidades de gestión, transacciones, catálogo y consulta analítica propias de un almacén.
- **Data fabric:** enfoque de integración y gestión de datos que utiliza metadatos, automatización y servicios distribuidos para conectar fuentes y consumidores.
- **Data mesh:** enfoque organizativo y arquitectónico que distribuye la responsabilidad de los datos por dominios, con plataformas de autoservicio y gobierno federado.

Estos patrones no son excluyentes. Una organización puede utilizar un lakehouse como núcleo de almacenamiento analítico, prácticas de data mesh para asignar responsabilidad por dominio y servicios de data fabric para facilitar la integración y el descubrimiento.

## 1.4. Arquitectura de referencia

La solución puede organizarse en las siguientes capas lógicas:

| Capa | Función | Capacidades representativas |
|---|---|---|
| Fuentes y sistemas productores | Generar o proporcionar datos | Sistemas transaccionales, aplicaciones, sensores, dispositivos, archivos, APIs, repositorios científicos y fuentes externas autorizadas |
| Integración e ingesta | Incorporar datos de forma controlada | Conectores, APIs, transferencia de archivos, CDC, mensajería, streaming, validación de esquemas |
| Almacenamiento | Conservar datos según su uso y criticidad | Bases relacionales, NoSQL, almacenamiento de objetos, archivos distribuidos, lago/lakehouse, respaldo y archivo |
| Procesamiento | Transformar y preparar datos | ETL/ELT, procesamiento por lotes, motores distribuidos, procesamiento de eventos, limpieza y enriquecimiento |
| Metadatos y semántica | Describir, localizar e interpretar datos | Catálogo, glosario, modelos semánticos, linaje, clasificación y contratos de datos |
| Gobierno y protección | Establecer y verificar reglas | Identidad, autorización, políticas, calidad, privacidad, auditoría, retención, gestión de riesgos |
| Consumo y productos | Entregar datos y resultados | BI, APIs, notebooks, entornos de ciencia de datos, modelos ML, aplicaciones y agentes |
| Operación y observabilidad | Mantener el servicio | Monitoreo, telemetría, gestión de incidentes, capacidad, costos, SRE y continuidad |

La infraestructura hiperconvergente se ubica principalmente en la capa física y de virtualización que soporta almacenamiento, cómputo, redes y ejecución de servicios. No debe confundirse con las capas lógicas anteriores: estas pueden estar distribuidas entre diferentes plataformas y ubicaciones.

## 1.5. Componentes de una base hiperconvergente

1. **Nodos de cómputo:** CPU, memoria y aceleradores cuando las cargas de trabajo lo requieran.
2. **Almacenamiento integrado o definido por software:** discos locales, unidades de estado sólido, almacenamiento distribuido y políticas de resiliencia.
3. **Red de alto desempeño:** conectividad redundante, segmentación, balanceo, redes de almacenamiento y redes para tráfico de aplicaciones.
4. **Hipervisor o capa de virtualización/contenedores:** ejecución aislada y administración de máquinas virtuales, contenedores o ambos.
5. **Orquestación y administración centralizada:** aprovisionamiento, configuración, inventario, actualizaciones y automatización.
6. **Continuidad y protección:** replicación, respaldo, recuperación ante desastres, pruebas de restauración y capacidad de operación degradada.
7. **Aceleración especializada:** GPU u otros aceleradores para entrenamiento, inferencia o procesamiento paralelo, cuando exista un caso de uso que justifique la inversión.

## 1.6. Patrones de despliegue

- **Centro de datos local:** apropiado cuando existen requisitos de control físico, baja latencia local, integración con sistemas heredados o restricciones de ubicación.
- **Nube privada:** ofrece recursos compartidos y aprovisionamiento automatizado bajo control organizacional.
- **Nube pública:** permite elasticidad y acceso a servicios administrados, sujeto a evaluación de costos, residencia, privacidad, seguridad y dependencia del proveedor.
- **Arquitectura híbrida:** distribuye cargas entre entornos locales y nube; requiere identidad federada, conectividad segura, políticas consistentes, monitoreo común y control de movimiento de datos.
- **Arquitectura multicloud:** puede responder a resiliencia o necesidades especializadas, pero incrementa la complejidad de gobierno, operación, portabilidad y costos.

La selección debe basarse en requisitos verificables, no en una preferencia tecnológica general. Deben evaluarse latencia, ancho de banda, costo total de propiedad, escalabilidad, disponibilidad, soberanía y residencia de datos, continuidad, habilidades disponibles y estrategia de salida.

## 1.7. Interoperabilidad y arquitectura empresarial

La interoperabilidad debe contemplarse en cuatro dimensiones:

- **Técnica:** conectividad, protocolos, APIs, formatos y mecanismos de intercambio.
- **Sintáctica:** compatibilidad de esquemas, codificaciones, estructuras y validaciones.
- **Semántica:** coincidencia en conceptos, unidades, definiciones, identificadores y reglas de negocio.
- **Organizativa:** acuerdos sobre responsables, finalidades, niveles de servicio, autorizaciones y resolución de controversias.

Es recomendable mantener un catálogo de APIs y eventos, un glosario institucional, modelos de datos compartidos y contratos versionados. La compatibilidad hacia atrás y las políticas de retiro de interfaces reducen el riesgo de romper consumidores existentes.

## 1.8. Proceso de implementación

1. **Descubrimiento:** inventariar fuentes, usuarios, procesos, volúmenes, velocidades, formatos, sensibilidad y restricciones.
2. **Definición de dominios:** asignar propietarios y responsables por conjuntos de datos y procesos.
3. **Arquitectura objetivo:** definir patrones de infraestructura, almacenamiento, integración, procesamiento, seguridad y consumo.
4. **Prueba de concepto:** validar cargas reales, rendimiento, interoperabilidad, recuperación, seguridad y costos.
5. **Construcción de una plataforma mínima viable:** desplegar servicios comunes y un primer conjunto de productos de datos.
6. **Escalamiento por dominios:** incorporar fuentes y consumidores mediante contratos y patrones reutilizables.
7. **Optimización continua:** revisar capacidad, costos, arquitectura, deuda técnica, calidad y niveles de servicio.

## 1.9. Entregables esperados

- Mapa del ecosistema y catálogo de fuentes.
- Arquitectura actual y arquitectura objetivo.
- Inventario de dominios, propietarios y custodios.
- Modelo de integración e interoperabilidad.
- Estándares de formatos, nomenclatura, APIs y contratos de datos.
- Diseño de infraestructura, capacidad, alta disponibilidad y recuperación.
- Matriz de decisiones tecnológicas y evaluación de proveedores.
- Hoja de ruta por fases y estimación de costo total de propiedad.

## 1.10. Indicadores de desempeño

- Porcentaje de fuentes prioritarias integradas.
- Porcentaje de productos de datos con propietario, contrato y documentación vigentes.
- Tiempo promedio para incorporar una nueva fuente.
- Disponibilidad de servicios de plataforma.
- Tiempo de aprovisionamiento de ambientes.
- Tasa de reutilización de productos de datos y APIs.
- Costo de almacenamiento y procesamiento por unidad de trabajo.
- Porcentaje de restauraciones y pruebas de continuidad exitosas.

## 1.11. Riesgos y medidas de mitigación

| Riesgo | Consecuencia | Medida de mitigación |
|---|---|---|
| Confundir HCI con una arquitectura completa de datos | Se adquiere infraestructura sin resolver integración, semántica ni gobierno | Diseñar por capas y definir responsables y servicios de datos antes de seleccionar productos |
| Dependencia excesiva de un proveedor | Costos de salida elevados y menor portabilidad | Usar estándares abiertos, interfaces documentadas, pruebas de exportación y estrategia de salida |
| Dimensionamiento incorrecto | Saturación o sobreinversión | Medir cargas, realizar pruebas representativas y planear capacidad con márgenes explícitos |
| Silos departamentales | Datos duplicados y definiciones contradictorias | Dominios responsables, catálogo común, contratos y gobierno federado |
| Falta de resiliencia | Pérdida o indisponibilidad de información | Redundancia, respaldos inmutables, replicación y simulacros de recuperación |

## 1.12. Resultado esperado

Un ecosistema de datos integrado y evolutivo, soportado por infraestructura escalable, en el que cada conjunto de datos tenga contexto, responsable, calidad conocida, reglas de acceso y mecanismos de uso reutilizables.

---

# 2. Gobernanza Normativa y Gestión Estratégica de Datos

## 2.1. Descripción general

La gobernanza de datos es el sistema de autoridad, responsabilidades, políticas, estándares y mecanismos de supervisión mediante el cual una organización dirige y controla el uso de sus datos. La gestión de datos ejecuta las actividades operativas necesarias para poner en práctica ese sistema. Ambas son complementarias: la gobernanza define quién decide y bajo qué reglas; la gestión implementa, opera y evidencia esas decisiones.

La gobernanza normativa añade la identificación y aplicación de leyes, reglamentos, normas técnicas, contratos, políticas institucionales y obligaciones sectoriales que condicionan la captura, almacenamiento, consulta, intercambio, conservación, eliminación y uso de datos, incluidos los datos usados para entrenar o ejecutar sistemas de IA.

La existencia de una plataforma tecnológica no garantiza por sí misma el cumplimiento normativo. El cumplimiento requiere identificar obligaciones aplicables, traducirlas a controles, asignar responsables, conservar evidencia y revisar su eficacia periódicamente.

## 2.2. Objetivos

- Reconocer los datos como activos institucionales con valor, riesgos y responsabilidades definidos.
- Establecer autoridad y rendición de cuentas a lo largo del ciclo de vida de los datos.
- Asegurar que el tratamiento de datos tenga finalidad, legitimidad y controles apropiados.
- Incorporar privacidad, seguridad, calidad, transparencia y ética en los procesos.
- Mantener evidencia verificable de decisiones, autorizaciones, transformaciones y accesos.
- Alinear las inversiones de datos con la estrategia institucional y sus objetivos de servicio, investigación o negocio.

## 2.3. Principios de gobernanza

1. **Responsabilidad identificable:** cada activo crítico cuenta con un propietario y responsables operativos.
2. **Finalidad explícita:** los datos se recolectan y usan para propósitos definidos y autorizados.
3. **Proporcionalidad y minimización:** se utiliza la cantidad y detalle de datos necesarios para la finalidad.
4. **Calidad y aptitud para el uso:** los datos se evalúan en función de su uso previsto.
5. **Trazabilidad:** se conservan registros de origen, transformaciones, accesos y decisiones relevantes.
6. **Seguridad y confidencialidad:** los controles protegen contra acceso, alteración, pérdida o divulgación no autorizados.
7. **Transparencia:** se documentan reglas, procesos y condiciones de uso de manera comprensible.
8. **Retención limitada:** se conservan los datos durante el tiempo justificado y se eliminan o anonimizan cuando corresponda.
9. **Interoperabilidad:** los datos se describen y comparten con formatos y definiciones consistentes.
10. **Uso responsable:** los usos secundarios, analíticos y algorítmicos se evalúan por su impacto y riesgo.

## 2.4. Modelo organizativo

Una estructura de gobierno puede incorporar los siguientes roles. En organizaciones pequeñas, una misma persona puede asumir más de un rol, siempre que se gestionen los conflictos de interés y se mantenga la segregación necesaria.

| Rol | Responsabilidad principal |
|---|---|
| Consejo o comité de gobierno de datos | Aprueba estrategia, políticas, prioridades, tolerancia al riesgo y resolución de asuntos transversales |
| Alta dirección o patrocinador ejecutivo | Asegura mandato, recursos y alineación institucional |
| Propietario del dato | Define uso legítimo, clasificación, reglas de negocio, acceso y criterios de calidad del dominio |
| Data steward | Mantiene definiciones, metadatos, reglas de calidad y coordinación del dominio |
| Custodio técnico | Opera almacenamiento, integridad, respaldos, controles y disponibilidad |
| Responsable de privacidad o función equivalente | Asesora sobre datos personales, derechos, evaluaciones de impacto y obligaciones aplicables |
| Seguridad de la información | Define y supervisa controles de ciberseguridad y gestión de riesgos |
| Arquitectura empresarial y de datos | Mantiene principios, modelos, estándares e interoperabilidad |
| Auditoría, cumplimiento y asesoría jurídica | Evalúan evidencia, obligaciones, independencia de controles y acciones correctivas |
| Usuarios y consumidores | Utilizan datos conforme a permisos, finalidad y condiciones documentadas |

## 2.5. Política, estándar, procedimiento y control

- **Política:** expresa principios y reglas obligatorias de alto nivel.
- **Estándar:** establece requisitos técnicos u operativos medibles.
- **Procedimiento:** describe los pasos para ejecutar una actividad.
- **Control:** previene, detecta o corrige un riesgo y produce evidencia de su operación.
- **Evidencia:** registro, aprobación, configuración, reporte o documento que permite demostrar que un control se ejecutó.

Ejemplo: una política puede exigir acceso basado en necesidad de conocer; un estándar puede requerir autenticación multifactor; un procedimiento describe el alta y baja de usuarios; el control valida periódicamente los permisos; la evidencia es el registro de revisión y remediación.

## 2.6. Gestión del ciclo de vida del dato

La política institucional debe cubrir, como mínimo, las siguientes etapas:

1. **Adquisición o generación:** identificar fuente, finalidad, autoridad, consentimiento o base jurídica cuando corresponda, y restricciones.
2. **Clasificación:** asignar categoría de sensibilidad, criticidad, titularidad y condiciones de uso.
3. **Ingesta:** validar origen, estructura, integridad, esquema, malware y autorización.
4. **Almacenamiento:** aplicar cifrado, ubicación, redundancia, retención, segregación y respaldo.
5. **Preparación y transformación:** conservar linaje, versiones, reglas de calidad y control de acceso.
6. **Uso y compartición:** verificar finalidad, permisos, acuerdos, minimización y restricciones de redistribución.
7. **Archivo:** asegurar autenticidad, legibilidad, integridad y recuperación durante el periodo de conservación.
8. **Eliminación o anonimización:** ejecutar procesos autorizados, verificables y coherentes con respaldos, réplicas y obligaciones de conservación.

## 2.7. Clasificación y controles

Una taxonomía ilustrativa —que debe adaptarse a las disposiciones aplicables— puede distinguir:

- **Pública:** información autorizada para difusión general.
- **Interna:** información de trabajo cuyo acceso se limita a la organización.
- **Confidencial:** información cuya divulgación puede causar perjuicio a personas u organización.
- **Restringida o altamente sensible:** información personal sensible, credenciales, secretos, información estratégica o datos cuya exposición podría generar impactos severos.

La clasificación debe conducir a controles concretos de acceso, cifrado, registro, compartición, retención, exportación, anonimización y respuesta a incidentes. No basta con agregar una etiqueta al catálogo.

## 2.8. Marco normativo y de referencia

El marco aplicable debe levantarse por jurisdicción, sector, tipo de dato, ubicación de los titulares, ubicación del tratamiento, relaciones contractuales y contexto de uso. Conviene mantener una **matriz de obligaciones** con: fuente normativa, artículo o requisito, proceso afectado, responsable, control, evidencia, frecuencia de revisión y estado de cumplimiento.

Como referencias de diseño —sin asumir que todas sean obligaciones legales en todos los países— pueden considerarse:

| Referencia | Enfoque | Uso dentro de la plataforma |
|---|---|---|
| ISO/IEC 38505-1:2026 | Aplicación de principios de gobierno de TI al gobierno de datos | Orientar la supervisión directiva y la toma de decisiones sobre datos |
| ISO/IEC 27001:2022 y su enmienda aplicable | Sistema de gestión de seguridad de la información | Gestionar riesgos, controles, auditoría y mejora de seguridad |
| ISO/IEC 27701 (edición vigente que corresponda) | Gestión de información de privacidad | Organizar controles y responsabilidades de privacidad |
| ISO/IEC 42001:2023 | Sistema de gestión de IA | Gestionar riesgos y responsabilidades de sistemas de IA durante su ciclo de vida |
| NIST AI RMF 1.0 y perfil de IA generativa NIST AI 600-1 | Gestión voluntaria de riesgos de IA | Estructurar actividades para gobernar, mapear, medir y gestionar riesgos de IA |
| DAMA-DMBOK | Cuerpo de conocimiento para gestión de datos | Referencia organizativa para calidad, metadatos, arquitectura, integración y gestión de datos |
| Legislación de privacidad y protección de datos aplicable | Derechos, bases de tratamiento, deberes y transferencias | Definir finalidades, derechos, avisos, retención, seguridad y gestión de incidentes |
| Legislación sectorial y contractual | Requisitos especiales por industria o servicio | Incorporar controles específicos para datos financieros, salud, educación, investigación u otros |

**Nota sobre obligatoriedad:** las normas ISO y los marcos NIST son referencias técnicas o de gestión; no se convierten automáticamente en leyes por el solo hecho de adoptarse. Pueden adquirir relevancia contractual, regulatoria o institucional según el contexto. Las leyes y reglamentos sí pueden imponer obligaciones vinculantes dentro de su ámbito de aplicación.

A la fecha de elaboración, el Reglamento de Inteligencia Artificial de la Unión Europea (Reglamento (UE) 2024/1689) tiene aplicación general desde el 2 de agosto de 2026, con disposiciones y obligaciones de alto riesgo sujetas a fechas escalonadas. Su aplicabilidad concreta depende del ámbito territorial y material del sistema y de las funciones de los participantes. Debe consultarse el texto consolidado y el análisis jurídico actualizado antes de tomar decisiones de cumplimiento.

Para una implementación en México, debe elaborarse un análisis jurídico específico de la legislación federal y local vigente en materia de protección de datos personales, transparencia, archivos, propiedad intelectual, firma y servicios digitales, así como de las disposiciones sectoriales y contractuales pertinentes. Este documento no sustituye ese dictamen ni presupone que un único marco normativo cubra todos los casos.

## 2.9. Gestión estratégica de datos

La estrategia de datos debe derivarse de los objetivos institucionales. Para cada objetivo se define qué decisiones o servicios se quieren mejorar, qué datos se necesitan, qué capacidades faltan, qué riesgos existen y cómo se medirá el valor.

Una estrategia práctica incluye:

- **Visión y objetivos:** resultados esperados a corto, mediano y largo plazo.
- **Portafolio de casos de uso:** priorizado por valor, viabilidad, riesgo, urgencia y reutilización.
- **Modelo operativo:** roles centrales, federados y responsabilidades por dominio.
- **Arquitectura objetivo:** capacidades comunes y principios de evolución.
- **Gestión de inversiones:** costos de plataforma, almacenamiento, cómputo, licencias, talento y operación.
- **Gestión del cambio:** comunicación, capacitación, adopción, soporte y comunidades de práctica.
- **Medición del valor:** ahorro, productividad, oportunidad, calidad, reducción de riesgo o mejora de resultados.

## 2.10. Controles mínimos recomendados

- Inventario y clasificación de activos de datos.
- Catálogo con propietario, finalidad, sensibilidad, retención y condiciones de uso.
- Acceso basado en roles y atributos, con privilegio mínimo y revisiones periódicas.
- Gestión de identidades privilegiadas y autenticación reforzada.
- Cifrado en tránsito y en reposo, con gestión separada de llaves.
- Registro de consultas, exportaciones, cambios administrativos y acciones sensibles.
- Reglas de calidad y monitoreo de incumplimientos.
- Linaje y versionado de datos y transformaciones.
- Evaluaciones de impacto de privacidad y de riesgo algorítmico cuando corresponda.
- Gestión de incidentes, brechas, solicitudes de titulares y ejercicio de derechos.
- Retención, archivo y eliminación segura.
- Evaluación de proveedores, subencargados, transferencias y dependencias tecnológicas.

## 2.11. Proceso de implantación

1. Realizar un diagnóstico de madurez y un inventario de obligaciones.
2. Establecer un comité y nombrar propietarios y responsables por dominio.
3. Aprobar políticas, taxonomía de clasificación y modelo de control.
4. Construir la matriz de obligaciones y controles con asesoría jurídica y de cumplimiento.
5. Incorporar metadatos, permisos y reglas de calidad en el catálogo y los flujos de datos.
6. Automatizar controles técnicamente verificables y establecer evidencias.
7. Ejecutar revisiones internas, pruebas de acceso, simulacros e inspecciones.
8. Medir resultados, corregir brechas y actualizar el marco ante cambios regulatorios o tecnológicos.

## 2.12. Entregables esperados

- Estrategia institucional de datos.
- Política general y estándares de gestión de datos.
- Modelo de gobierno, matriz RACI y designación de responsables.
- Inventario de activos, clasificación y catálogo de datos.
- Matriz de obligaciones normativas y contractuales.
- Matriz de riesgos, controles y evidencias.
- Procedimientos de acceso, compartición, retención, eliminación e incidentes.
- Evaluaciones de impacto de privacidad y riesgos de IA cuando sean necesarias.
- Programa de capacitación, auditoría y mejora continua.

## 2.13. Indicadores

- Porcentaje de activos críticos con propietario y clasificación asignados.
- Porcentaje de productos de datos con finalidad, base de uso y retención documentadas.
- Porcentaje de accesos revisados dentro del periodo definido.
- Número y severidad de hallazgos de auditoría abiertos y vencidos.
- Tiempo medio de atención de solicitudes de derechos o incidentes.
- Porcentaje de controles con evidencia vigente y automatizada.
- Porcentaje de conjuntos de datos que cumplen umbrales de calidad.
- Porcentaje de modelos y agentes registrados y evaluados antes de su puesta en producción.

## 2.14. Riesgos frecuentes

- **Gobernanza documental sin aplicación:** políticas que no se traducen en permisos, validaciones ni evidencia. Mitigación: convertir reglas en controles operativos y medirlos.
- **Responsabilidades ambiguas:** nadie decide sobre calidad, acceso o retención. Mitigación: propietarios y RACI por dominio.
- **Sobrerregulación:** controles uniformes que impiden usos legítimos. Mitigación: proporcionalidad basada en sensibilidad y riesgo.
- **Cumplimiento asumido:** interpretar una certificación como garantía universal. Mitigación: matriz de aplicabilidad y evaluación jurídica.
- **Datos sin contexto:** datasets usados fuera de su finalidad o condiciones originales. Mitigación: catálogo, contratos, etiquetas y controles de uso.

## 2.15. Resultado esperado

Un sistema sostenible de autoridad, políticas y controles que convierte las obligaciones normativas y los objetivos estratégicos en decisiones y operaciones verificables, y que permite demostrar quién usa qué datos, para qué, con qué autorización y bajo qué salvaguardas.

---

# 3. Infraestructura para Grandes Volúmenes de Datos

## 3.1. Descripción general

La infraestructura para grandes volúmenes de datos debe soportar la ingestión, almacenamiento, procesamiento, consulta y transferencia de cantidades elevadas de información, con diversidad de formatos y ritmos de generación. El reto no se limita al volumen: también comprende velocidad, variedad, variabilidad, calidad, distribución geográfica, concurrencia, seguridad y costo.

La arquitectura debe responder tanto a procesamiento por lotes como a flujos de eventos, consultas interactivas, entrenamiento de modelos, inferencia y acceso a datos no estructurados. Una plataforma hiperconvergente puede proporcionar recursos integrados de cómputo y almacenamiento, pero el diseño debe contemplar almacenamiento de objetos, redes, aceleradores y servicios distribuidos cuando el patrón de carga lo requiera.

## 3.2. Objetivos

- Proveer capacidad de almacenamiento y cómputo escalable, resiliente y administrable.
- Soportar datos estructurados, semiestructurados y no estructurados.
- Separar, cuando sea conveniente, el escalamiento de cómputo del escalamiento de almacenamiento.
- Mantener niveles definidos de disponibilidad, latencia, rendimiento y recuperación.
- Automatizar aprovisionamiento, configuración, despliegue, monitoreo y protección.
- Optimizar el costo total por volumen almacenado y por unidad de procesamiento.

## 3.3. Características de las cargas de trabajo

Antes de elegir infraestructura se deben caracterizar las cargas en términos de:

- Volumen inicial y crecimiento esperado de datos.
- Tasa de llegada de eventos y picos de ingesta.
- Tamaño medio y distribución de objetos o archivos.
- Concurrencia de usuarios, consultas y trabajos.
- Patrones de lectura y escritura, secuenciales o aleatorios.
- Latencia máxima tolerable y ventanas de procesamiento.
- Retención, archivado, replicación y eliminación.
- Sensibilidad y criticidad de la información.
- Necesidad de aceleradores, memoria elevada o cómputo intensivo.
- Ubicación de datos y consumidores, conectividad y transferencia.

Se recomienda documentar perfiles de carga representativos y probarlos con datos de tamaño, distribución y concurrencia similares a producción.

## 3.4. Componentes de infraestructura

### Cómputo

- CPU para procesamiento general, orquestación, bases de datos y servicios.
- Memoria para caché, motores en memoria, procesamiento distribuido y consultas.
- GPU u otros aceleradores para entrenamiento, inferencia y cargas paralelas específicas.
- Nodos especializados según perfil: almacenamiento, cómputo intensivo, memoria elevada o aceleración.

### Almacenamiento

| Tipo | Uso habitual | Consideraciones |
|---|---|---|
| Bloque | Bases de datos, máquinas virtuales y aplicaciones con requisitos de IOPS | Latencia, redundancia, snapshots, consistencia y rendimiento sostenido |
| Archivo | Sistemas compartidos, herramientas científicas y aplicaciones con semántica de archivos | Metadatos, concurrencia, permisos, bloqueo y número de archivos |
| Objetos | Lago de datos, documentos, imágenes, respaldos y repositorios masivos | Durabilidad, costo, ciclo de vida, versionado y compatibilidad de APIs |
| Relacional | Datos transaccionales y analíticos estructurados | Modelo, transacciones, índices, replicación y concurrencia |
| NoSQL | Datos de alta escala o esquemas flexibles | Modelo de consistencia, particionamiento, consulta y operación |
| Vectorial | Embeddings para búsqueda semántica y recuperación aumentada | Índices, filtrado, actualización, calidad de embeddings y costo de memoria |

### Redes

La red debe diseñarse como parte integral de la arquitectura. Es necesario evaluar ancho de banda, latencia, redundancia, segmentación, congestión y rutas de datos entre almacenamiento, cómputo, usuarios y servicios externos. El tráfico de gestión, almacenamiento, aplicaciones y administración privilegiada debe separarse lógicamente y, cuando el riesgo lo requiera, físicamente.

### Virtualización y orquestación

Se pueden combinar máquinas virtuales, contenedores y servicios administrados. La selección debe tomar en cuenta aislamiento, densidad, portabilidad, requisitos de hardware, compatibilidad de controladores, gestión de secretos y operación. La infraestructura como código y la configuración declarativa reducen desviaciones entre ambientes.

## 3.5. Patrones de almacenamiento y procesamiento

- **Data lake en almacenamiento de objetos:** conserva datos originales y derivados en formatos abiertos, con catálogo y políticas de ciclo de vida.
- **Lakehouse:** añade tablas administradas, transacciones, control de esquema y optimización para consulta analítica.
- **Warehouse analítico:** sirve consultas gobernadas, modelos dimensionales, indicadores y reportes de negocio.
- **Streaming:** procesa eventos conforme llegan, con particionamiento, retención, control de duplicados y tolerancia a fallas.
- **Batch distribuido:** ejecuta transformaciones periódicas sobre grandes conjuntos de datos.
- **Procesamiento en memoria:** acelera operaciones que requieren baja latencia, con análisis de costo y recuperación.
- **HPC y cómputo acelerado:** atiende simulación, entrenamiento, procesamiento científico y otras cargas intensivas.

La arquitectura puede utilizar varios patrones. La decisión debe responder a las características de cada caso de uso y evitar duplicar copias sin justificación, linaje ni control de retención.

## 3.6. Formatos y organización de datos

Se deben preferir formatos interoperables y adecuados al patrón de acceso. Por ejemplo, formatos columnares para analítica, formatos de texto estructurado para intercambio y formatos especializados para imágenes, audio, video o datos científicos. Los criterios de selección incluyen compresión, evolución del esquema, lectura parcial, compatibilidad entre motores y preservación a largo plazo.

La organización física y lógica debe definir zonas o estados de datos, por ejemplo:

- **Recepción o landing:** conserva la entrada original, con controles de integridad y procedencia.
- **Bronze/raw:** almacena datos originales o con intervención mínima.
- **Silver/curated:** aplica validación, normalización, limpieza y enriquecimiento.
- **Gold/serving:** ofrece conjuntos optimizados y orientados a productos, indicadores o modelos.
- **Archivo:** conserva información por requisitos de negocio, investigación, auditoría o regulación.

Estas denominaciones son un patrón operativo, no una norma obligatoria. Cada zona debe tener reglas de acceso, calidad, retención y promoción bien definidas.

## 3.7. Ingesta de datos

La ingesta debe soportar:

- Conectores a bases de datos y aplicaciones.
- APIs REST, eventos y mecanismos de transferencia segura.
- Captura de cambios (CDC) para replicar modificaciones incrementales.
- Mensajería y streaming para eventos continuos.
- Procesamiento de archivos en lotes.
- Ingesta de datos científicos y de dispositivos, con metadatos de origen y contexto.

Cada flujo debe implementar validación de esquema, control de duplicados, idempotencia cuando sea posible, manejo de errores, cuarentena de registros inválidos y reintentos controlados. Las cargas deben registrar marca temporal, origen, versión de esquema, identificador de lote o evento y resultado de validación.

## 3.8. Procesamiento distribuido

El procesamiento distribuido permite dividir una carga entre varios nodos. Su diseño debe considerar particionamiento, localidad de datos, paralelismo, tolerancia a fallas, skew, shuffle, caché y costo de transferencia. La escalabilidad no es automáticamente lineal: puede verse limitada por la red, el almacenamiento, la coordinación, los bloqueos o tareas que no pueden paralelizarse.

Se recomienda separar:

- Recursos de ingesta y mensajería.
- Recursos de almacenamiento persistente.
- Recursos de transformación batch.
- Recursos de consulta interactiva.
- Recursos de entrenamiento e inferencia.
- Recursos de administración y observabilidad.

La separación lógica o física dependerá de la concurrencia, aislamiento, niveles de servicio y criticidad de cada carga.

## 3.9. Disponibilidad, resiliencia y recuperación

La continuidad debe definirse mediante objetivos de negocio:

- **RPO (Recovery Point Objective):** pérdida máxima de datos tolerable, expresada como tiempo.
- **RTO (Recovery Time Objective):** tiempo objetivo para restablecer un servicio.
- **Disponibilidad objetivo:** proporción de tiempo en que el servicio debe operar.
- **Durabilidad:** probabilidad de conservar correctamente los datos durante el periodo previsto.

Los controles pueden incluir redundancia de nodos, replicación, snapshots, respaldos separados, copias inmutables, recuperación geográfica y procedimientos manuales alternos. La replicación no sustituye al respaldo: replica también borrados, corrupción o cifrado malicioso si no existen mecanismos de protección adecuados.

Los planes deben probarse mediante restauraciones, failover, simulación de pérdida de zona y ejercicios de continuidad. Se debe registrar el resultado y corregir las diferencias respecto de los RPO y RTO aprobados.

## 3.10. Seguridad de la infraestructura

- Segmentación de redes y aislamiento de cargas.
- Gestión centralizada de identidades y acceso privilegiado.
- Autenticación multifactor para accesos administrativos y sensibles.
- Cifrado en tránsito y en reposo.
- Gestión de llaves, certificados y secretos.
- Endurecimiento y configuración segura de nodos, hipervisores, contenedores y sistemas operativos.
- Gestión de vulnerabilidades, parches y cadena de suministro de software.
- Registro centralizado y protección de logs.
- Escaneo de imágenes, artefactos y archivos entrantes cuando proceda.
- Respaldos aislados o inmutables y pruebas de restauración.

## 3.11. Observabilidad y FinOps

La observabilidad debe vincular métricas técnicas con servicios y productos de datos. Como mínimo, debe medir:

- CPU, memoria, GPU, almacenamiento, IOPS y latencia.
- Ancho de banda, errores y saturación de red.
- Duración, retraso y tasa de error de flujos y procesos.
- Disponibilidad y latencia de APIs y consultas.
- Consumo por equipo, dominio, proyecto o producto.
- Costos por almacenamiento, transferencia, cómputo, licencias y soporte.

La disciplina FinOps o de gestión económica de nube puede extenderse a entornos locales: asignar costos, etiquetar recursos, establecer presupuestos, identificar capacidad ociosa y comparar costo por unidad de trabajo. Toda optimización debe respetar requisitos de resiliencia, seguridad y retención.

## 3.12. Dimensionamiento y selección tecnológica

El dimensionamiento debe partir de pruebas de concepto y curvas de crecimiento. Se recomienda comparar alternativas con una matriz que incluya rendimiento real, escalabilidad, resiliencia, interoperabilidad, facilidad operativa, seguridad, costos, soporte, habilidades requeridas y estrategia de salida.

No debe elegirse una arquitectura únicamente por capacidad nominal de almacenamiento o número de núcleos. Las métricas determinantes pueden ser throughput sostenido, latencia en percentiles, IOPS, tiempo de reconstrucción, rendimiento bajo fallas, costos de red y comportamiento con consultas concurrentes.

## 3.13. Entregables esperados

- Catálogo de cargas de trabajo y perfiles de rendimiento.
- Diseño de cómputo, almacenamiento, red y virtualización.
- Modelo de zonas de datos y ciclo de vida de almacenamiento.
- Arquitectura de ingesta batch y streaming.
- Plan de capacidad y crecimiento.
- Diseño de alta disponibilidad, respaldo y recuperación ante desastres.
- Baseline de seguridad y hardening.
- Tableros de observabilidad, alertamiento y costos.
- Pruebas de carga, resiliencia, recuperación y aceptación técnica.

## 3.14. Indicadores

- Capacidad utilizada frente a capacidad instalada y reservada.
- Rendimiento y latencia por tipo de carga.
- Disponibilidad de servicios y cumplimiento de RPO/RTO.
- Tiempo de ingesta y retraso de procesamiento.
- Porcentaje de trabajos completados sin reintento o intervención.
- Costo por terabyte-mes, por consulta o por trabajo procesado.
- Tasa de éxito de respaldos y restauraciones.
- Tiempo de aprovisionamiento y recuperación de nodos.
- Consumo energético por unidad de procesamiento, cuando pueda medirse.

## 3.15. Resultado esperado

Una infraestructura escalable, segura y resiliente que absorba el crecimiento de los datos y entregue capacidad de procesamiento predecible, con costos y niveles de servicio medibles y con mecanismos demostrables de continuidad.

---

# 4. Analítica Avanzada, Ciencia de Datos e Inteligencia Artificial

## 4.1. Descripción general

La analítica avanzada y la ciencia de datos convierten datos preparados y contextualizados en explicaciones, predicciones, recomendaciones y decisiones. La inteligencia artificial amplía estas capacidades mediante técnicas de aprendizaje automático, aprendizaje profundo, procesamiento del lenguaje natural, visión computacional, sistemas de recomendación, modelos generativos y otros enfoques.

En una plataforma institucional, estas capacidades deben operar sobre datos gobernados, con entornos reproducibles, trazabilidad de experimentos, controles de acceso y mecanismos de validación antes de su uso operativo. El éxito no debe medirse solo por la precisión de un modelo: también importa su utilidad, robustez, explicabilidad, costo, equidad, seguridad, mantenibilidad y adecuación al contexto.

## 4.2. Objetivos

- Transformar preguntas institucionales en problemas analíticos bien definidos.
- Desarrollar análisis descriptivos, diagnósticos, predictivos y prescriptivos.
- Habilitar experimentación científica reproducible y colaboración interdisciplinaria.
- Construir, evaluar, desplegar y monitorear modelos de aprendizaje automático.
- Integrar resultados analíticos en procesos de decisión y productos digitales.
- Mantener control sobre datos, código, modelos, experimentos y versiones.

## 4.3. Tipos de analítica

1. **Descriptiva:** responde qué ocurrió mediante indicadores, reportes y agregaciones.
2. **Diagnóstica:** investiga por qué ocurrió, mediante segmentación, correlaciones, análisis de causas y exploración.
3. **Predictiva:** estima resultados o eventos futuros, por ejemplo, demanda, riesgo, fallas o abandono.
4. **Prescriptiva:** propone acciones considerando objetivos, restricciones y escenarios.
5. **Causal:** estima efectos de intervenciones mediante diseños experimentales o cuasiexperimentales, con supuestos explícitos.
6. **Exploratoria y científica:** busca patrones, genera hipótesis y valida conocimiento mediante métodos reproducibles.

La elección debe partir de la pregunta y del tipo de decisión. Un modelo predictivo no demuestra causalidad; una correlación no basta para justificar una intervención.

## 4.4. Ciclo de vida de un proyecto de ciencia de datos

1. **Planteamiento del problema:** definir la decisión, población, unidad de análisis, horizonte y criterio de éxito.
2. **Adquisición de datos:** identificar fuentes autorizadas y evaluar su cobertura, calidad, representatividad y sesgos.
3. **Exploración y comprensión:** analizar distribuciones, valores faltantes, anomalías, relaciones y limitaciones.
4. **Preparación:** limpiar, integrar, transformar, etiquetar y documentar los datos.
5. **Diseño metodológico:** establecer línea base, particiones de entrenamiento/validación/prueba y protocolo de evaluación.
6. **Experimentación:** comparar modelos, hiperparámetros, variables y métodos con control de versiones.
7. **Evaluación:** medir desempeño técnico, utilidad, robustez, explicabilidad, equidad y riesgo.
8. **Aprobación y despliegue:** revisar criterios, controles y autorizaciones para llevar el modelo a producción.
9. **Monitoreo:** vigilar desempeño, deriva, cambios de datos, fallos, costos y efectos no deseados.
10. **Retiro o actualización:** versionar cambios, reentrenar cuando proceda y retirar modelos que ya no sean adecuados.

## 4.5. Arquitectura para ciencia de datos y ML

La plataforma debe ofrecer servicios coordinados para:

- **Ambientes de trabajo:** notebooks, IDE, terminales y contenedores reproducibles.
- **Acceso a datos:** consultas gobernadas, conjuntos de entrenamiento y vistas controladas.
- **Preparación y cómputo:** motores distribuidos, procesamiento en memoria y aceleradores.
- **Experimentación:** seguimiento de parámetros, métricas, código, datos y artefactos.
- **Gestión de características (feature store):** definición, cálculo, versionado y reutilización de variables cuando la complejidad lo amerite.
- **Registro de modelos:** versiones, metadatos, responsables, evaluaciones, aprobaciones y restricciones.
- **Pipelines:** automatización de preparación, entrenamiento, validación, despliegue y pruebas.
- **Serving:** APIs, procesamiento batch, inferencia en tiempo real o ejecución local.
- **Monitoreo:** calidad de entrada, deriva, rendimiento, latencia, consumo y comportamiento.

Una arquitectura MLOps integra prácticas de ingeniería de software, datos y aprendizaje automático para operar modelos de forma repetible y controlada.

## 4.6. Gestión del ciclo de vida de modelos

Cada modelo productivo debe contar, como mínimo, con:

- Identificador y versión inequívoca.
- Propósito, alcance y usos no permitidos.
- Propietario de negocio y responsable técnico.
- Fuentes, versiones y condiciones de los datos de entrenamiento.
- Variables, transformaciones y características relevantes.
- Método, parámetros y entorno de ejecución.
- Métricas y resultados de evaluación, con umbrales aprobados.
- Limitaciones conocidas, supuestos y riesgos.
- Evaluación de sesgos y desempeño por grupos cuando sea pertinente y lícito.
- Evidencia de revisión, aprobación y pruebas de seguridad.
- Procedimiento de monitoreo, actualización, reversión y retiro.

La documentación puede apoyarse en fichas de modelo y fichas de datos, sin convertirlas en sustitutos de controles técnicos.

## 4.7. Evaluación de modelos

La métrica debe corresponder al problema. Algunos ejemplos:

| Tipo de problema | Métricas posibles | Precaución |
|---|---|---|
| Clasificación | Precision, recall, F1, ROC-AUC, PR-AUC, calibración | Revisar desbalance de clases y costos de falsos positivos/negativos |
| Regresión | MAE, RMSE, MAPE cuando sea apropiado, R² | Revisar valores extremos y escala de la variable |
| Ranking y recomendación | NDCG, MAP, hit rate, cobertura, diversidad | Evaluar exposición, retroalimentación y sesgo de popularidad |
| Pronóstico temporal | MAE, RMSE, error por horizonte, cobertura de intervalos | Evitar fuga temporal y validar cambios de régimen |
| Clustering | Silhouette y métricas de estabilidad, además de validación de dominio | La calidad no se reduce a una única métrica matemática |
| Modelos generativos | Exactitud factual, relevancia, robustez, seguridad, tasa de alucinación estimada | Usar evaluaciones humanas y conjuntos de prueba representativos |

La evaluación debe incluir línea base, particiones apropiadas, validación externa cuando proceda y pruebas de sensibilidad. En decisiones de alto impacto se requieren pruebas adicionales y supervisión acorde con el riesgo.

## 4.8. Reproducibilidad y ciencia abierta responsable

La reproducibilidad exige registrar datos o identificadores de versiones, código, dependencias, parámetros, semillas cuando sean relevantes, hardware, resultados y limitaciones. En entornos con datos sensibles, la apertura debe equilibrarse con controles de privacidad, seguridad, propiedad intelectual y acuerdos de acceso.

Se recomienda separar los datos originales de los derivados, automatizar entornos, usar repositorios de código, registrar experimentos y documentar procedimientos para volver a ejecutar los análisis. Los resultados científicos deben incluir métodos, incertidumbre, limitaciones y condiciones que permitan su evaluación independiente cuando sea posible.

## 4.9. Analítica confiable y uso responsable de IA

Los controles deben cubrir:

- Calidad, representatividad y procedencia de datos.
- Sesgo de selección, medición, etiquetado y cobertura.
- Explicabilidad adecuada al usuario y al impacto de la decisión.
- Robustez frente a cambios, datos atípicos y perturbaciones.
- Protección de información confidencial y datos personales.
- Seguridad frente a manipulación de entradas y ataques al modelo.
- Supervisión humana, escalamiento y mecanismos de corrección.
- Transparencia sobre limitaciones y uso de modelos automatizados.
- Evaluación continua de efectos previstos y no previstos.

En sistemas generativos, deben analizarse además la exposición de datos, la generación de contenido falso, las citas o fuentes no verificables, la inyección de instrucciones, la fuga de contexto y la dependencia de proveedores externos.

## 4.10. Integración con procesos institucionales

Un resultado analítico solo genera valor cuando se integra en una decisión, servicio o proceso. Para ello, se deben definir:

- Quién recibe el resultado y qué decisión puede tomar.
- Qué nivel de confianza o incertidumbre es aceptable.
- Qué acción requiere aprobación humana.
- Cómo se presenta el resultado y sus limitaciones.
- Cómo se registra el uso y se mide su efecto.
- Qué ocurre cuando el modelo falla, se degrada o no puede emitir una respuesta.

La automatización de una predicción no debe confundirse con la autorización de una decisión. Las decisiones sensibles deben conservar revisión y vías de escalamiento apropiadas.

## 4.11. Entregables esperados

- Portafolio priorizado de casos de uso analíticos y de IA.
- Fichas de problema, criterios de éxito y evaluación de viabilidad.
- Conjuntos de datos versionados y documentados.
- Notebooks, pipelines y código reproducible.
- Registro de experimentos y modelos.
- Fichas de datos y modelos.
- Informes de evaluación técnica, funcional y de riesgos.
- APIs o servicios de inferencia.
- Tableros de monitoreo, alertas y procedimientos de retiro.
- Evidencias de revisión y autorización antes de producción.

## 4.12. Indicadores

- Tiempo desde definición del problema hasta prototipo validado.
- Porcentaje de proyectos con datos documentados y reproducibilidad comprobada.
- Porcentaje de modelos productivos con ficha, responsable y evaluación vigente.
- Desempeño del modelo frente a línea base y umbrales aprobados.
- Tasa de deriva y tiempo de detección/remediación.
- Disponibilidad, latencia y costo por inferencia.
- Porcentaje de casos de uso que generan una mejora operacional medida.
- Número de incidentes por uso indebido, exposición o degradación de modelos.

## 4.13. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Fuga de datos entre entrenamiento y prueba | Particiones apropiadas al tiempo, entidad y proceso; revisión del pipeline |
| Sesgos o falta de representatividad | Auditoría de datos, métricas por grupos y revisión de contexto |
| Sobreajuste y baja generalización | Validación rigurosa, línea base y pruebas fuera de muestra |
| Deriva de datos o concepto | Monitoreo, umbrales, reevaluación y reentrenamiento controlado |
| Resultados sin utilidad operativa | Alinear métricas con decisiones y medir impacto real |
| Modelos no reproducibles | Versionado de datos, código, ambiente, parámetros y artefactos |
| Uso de información sensible en servicios externos | Clasificación, minimización, contratos, controles técnicos y aprobación previa |

## 4.14. Resultado esperado

Una capacidad institucional de analítica, ciencia de datos y aprendizaje automático que transforma datos gobernados en conocimiento reproducible y servicios medibles, con modelos evaluados, controlados y sujetos a mejora continua.

---

# 5. Inteligencia Artificial Agéntica y Ecosistemas Inteligentes de Datos

## 5.1. Descripción general

La inteligencia artificial agéntica comprende sistemas que utilizan modelos de IA para interpretar objetivos, planificar pasos, consultar información, invocar herramientas y ejecutar acciones dentro de límites definidos. A diferencia de un asistente que solo genera una respuesta, un agente puede coordinar tareas y servicios; un sistema multiagente puede distribuir funciones entre varios agentes especializados.

En un ecosistema de datos, los agentes pueden ayudar a descubrir conjuntos de datos, explicar metadatos, generar consultas, validar calidad, documentar transformaciones, preparar análisis, monitorear flujos y asistir en la operación. Su utilidad depende de datos confiables, herramientas seguras, permisos verificables, trazabilidad y supervisión proporcional al impacto de sus acciones.

Un agente no debe recibir acceso irrestricto a todos los datos o sistemas. Debe operar bajo identidad propia, permisos mínimos, contexto acotado, herramientas autorizadas y políticas de ejecución explícitas.

## 5.2. Objetivos

- Automatizar tareas complejas de exploración, preparación y operación de datos.
- Facilitar interfaces en lenguaje natural para consultar capacidades de la plataforma.
- Coordinar herramientas analíticas, servicios de datos y flujos de trabajo.
- Aumentar la productividad sin eliminar la responsabilidad de los equipos humanos.
- Incorporar controles de seguridad, privacidad, calidad y riesgo en cada acción del agente.
- Mantener evidencia verificable de instrucciones, contexto, decisiones, herramientas y resultados.

## 5.3. Conceptos básicos

- **Agente:** sistema que recibe un objetivo, mantiene estado o contexto, razona sobre pasos y utiliza herramientas para alcanzar una meta dentro de restricciones.
- **Herramienta (tool):** API, consulta, función o servicio que el agente puede invocar para realizar una tarea concreta.
- **Orquestador:** componente que coordina agentes, herramientas, estados, políticas, reintentos y aprobaciones.
- **Memoria:** información contextual que el sistema conserva entre pasos o sesiones, sujeta a reglas de minimización, retención y acceso.
- **RAG (Retrieval-Augmented Generation):** patrón que recupera información de fuentes autorizadas y la incorpora al contexto del modelo para fundamentar respuestas.
- **Agente supervisor:** agente o componente encargado de distribuir tareas, revisar resultados o decidir cuándo solicitar intervención humana.
- **Sistema multiagente:** conjunto coordinado de agentes con funciones, herramientas y permisos diferenciados.
- **Guardrail o salvaguarda:** regla, filtro o control que limita entradas, salidas, herramientas, datos o acciones.

## 5.4. Casos de uso en un ecosistema de datos

1. **Descubrimiento de datos:** localizar activos por significado, propietario, calidad, sensibilidad y condiciones de acceso.
2. **Asistente de metadatos:** proponer descripciones, clasificaciones o términos de glosario para revisión humana.
3. **Asistencia de calidad:** detectar anomalías, explicar reglas incumplidas y sugerir correcciones sin modificar datos productivos sin autorización.
4. **Generación de consultas:** traducir preguntas a SQL u otros lenguajes, validar permisos y explicar los resultados.
5. **Orquestación analítica:** coordinar tareas de extracción, transformación, análisis y generación de reportes.
6. **Asistencia científica:** apoyar búsqueda bibliográfica, preparación de datos, ejecución de análisis y documentación de experimentos, respetando licencias y confidencialidad.
7. **Operación de plataforma:** interpretar alertas, recopilar evidencias y proponer acciones correctivas.
8. **Gobernanza asistida:** identificar activos sin propietario, accesos inusuales, datos sin clasificación o controles vencidos.
9. **Interacción con productos de datos:** explicar métricas, definiciones y restricciones a usuarios autorizados.

Los agentes pueden recomendar acciones; la ejecución automática debe limitarse a operaciones de bajo riesgo aprobadas previamente. Acciones que afecten derechos, dinero, sistemas críticos, datos sensibles o servicios externos requieren controles más estrictos y, en muchos casos, aprobación humana.

## 5.5. Arquitectura de referencia de un sistema agéntico

| Componente | Función | Controles necesarios |
|---|---|---|
| Interfaz de usuario o API | Recibe la solicitud y presenta resultados | Autenticación, autorización, avisos de uso y gestión de sesión |
| Modelo de lenguaje o modelo especializado | Interpreta instrucciones y propone pasos | Selección de modelo, evaluación, límites de contexto y protección de datos |
| Orquestador | Administra tareas, estados, pasos y coordinación | Máquina de estados, límites de iteración, timeouts y trazabilidad |
| Catálogo y capa semántica | Proporciona contexto de activos, conceptos y definiciones | Filtrado por permisos, calidad de metadatos y versión |
| Recuperación/RAG | Recupera documentos o datos autorizados | Control de acceso en recuperación, procedencia, frescura y defensa contra inyección |
| Herramientas y conectores | Ejecutan consultas y operaciones | Lista permitida, identidad de servicio, validación de parámetros y permisos mínimos |
| Memoria y estado | Conserva contexto pertinente | Minimización, clasificación, cifrado, retención y borrado verificable |
| Motor de políticas | Autoriza o bloquea acciones | Políticas externas al modelo, separación de funciones y evaluación de riesgo |
| Registro y observabilidad | Conserva eventos y permite investigar | Logs protegidos, correlación, auditoría y monitoreo de anomalías |
| Supervisión humana | Revisa o autoriza pasos sensibles | Aprobaciones explícitas, contexto suficiente y registro de decisión |

El modelo no debe ser el único mecanismo que decide si una acción está permitida. Las autorizaciones deben aplicarse mediante controles externos al modelo y verificarse en el servicio que ejecuta la acción.

## 5.6. Ciclo de ejecución controlado

Un flujo de trabajo agéntico seguro puede seguir esta secuencia:

1. **Autenticación:** identificar al usuario y el contexto de la solicitud.
2. **Interpretación:** convertir la solicitud en una tarea estructurada y detectar ambigüedades o riesgos.
3. **Planificación:** proponer pasos, datos y herramientas requeridos.
4. **Autorización:** verificar permisos, finalidad, clasificación y políticas antes de acceder a recursos.
5. **Ejecución:** invocar herramientas con parámetros validados y límites de alcance.
6. **Verificación:** comprobar resultados, consistencia, procedencia y efectos secundarios.
7. **Aprobación humana:** detener el flujo cuando la acción supere el umbral de riesgo o requiera autorización.
8. **Registro:** conservar el rastro de la solicitud, plan, contexto, herramientas, decisiones, resultados y responsable.
9. **Respuesta:** presentar resultados, fuentes, incertidumbre, acciones realizadas y pendientes.
10. **Cierre:** expirar credenciales temporales, liberar recursos y aplicar políticas de retención de memoria y registros.

## 5.7. Seguridad específica de agentes

Los sistemas agénticos introducen riesgos adicionales porque el modelo puede interpretar contenido externo, consultar múltiples fuentes y ejecutar herramientas. Entre los controles necesarios se encuentran:

- **Identidad por agente:** credenciales y permisos diferenciados para cada agente o función.
- **Privilegio mínimo:** acceso exclusivamente a recursos necesarios para una tarea.
- **Allowlist de herramientas:** invocación únicamente de herramientas autorizadas y registradas.
- **Validación de parámetros:** tipado, límites, sanitización y rechazo de valores inesperados.
- **Separación de instrucciones y datos:** tratar documentos, resultados web y contenido recuperado como datos no confiables, no como instrucciones de política.
- **Defensa contra prompt injection:** filtrar y marcar contenido externo, limitar herramientas y verificar todas las acciones fuera del modelo.
- **Límites de ejecución:** topes de tiempo, costo, iteraciones, tamaño de contexto, consultas y operaciones.
- **Protección frente a exfiltración:** controles de salida, detección de secretos y restricciones de transferencia.
- **Aprobación humana:** autorización explícita para operaciones irreversibles, privilegiadas o de impacto elevado.
- **Entorno aislado:** sandbox para código, scripts, archivos y herramientas con acceso a sistemas.
- **Trazabilidad:** registro de herramientas, argumentos, resultado, identidad y correlación de pasos.
- **Pruebas adversariales:** evaluar intentos de abuso, manipulación, fuga de datos, escalamiento de privilegios y acciones fuera de alcance.

## 5.8. Gobernanza de datos para agentes

Los agentes deben consumir productos de datos gobernados. Esto requiere que el catálogo exponga metadatos útiles para la automatización, como propietario, clasificación, finalidad, sensibilidad, permisos, retención, calidad, frescura, linaje y condiciones de uso.

La política de autorización debe aplicarse tanto al usuario como al agente. No debe suponerse que el agente puede utilizar todos los datos a los que tiene acceso el usuario ni que una respuesta en lenguaje natural equivale a una autorización. Las consultas deben filtrarse en origen o en una capa de políticas confiable, no únicamente en el prompt.

Cuando un agente genera o modifica datos, debe registrar su intervención, versión del modelo, herramientas utilizadas, transformaciones realizadas y revisión humana cuando exista. Los datos sintéticos, anotaciones y salidas generadas deben etiquetarse como tales y no confundirse con observaciones originales.

## 5.9. Calidad y evaluación de agentes

La evaluación debe combinar pruebas técnicas y de proceso:

- **Éxito de tarea:** porcentaje de objetivos completados correctamente bajo condiciones definidas.
- **Exactitud factual:** proporción de afirmaciones sustentadas por fuentes válidas.
- **Calidad de recuperación:** relevancia, cobertura y vigencia de documentos recuperados.
- **Uso correcto de herramientas:** elección de herramienta, argumentos y secuencia de invocación.
- **Cumplimiento de políticas:** tasa de acciones permitidas, bloqueadas o escaladas correctamente.
- **Robustez:** comportamiento frente a instrucciones ambiguas, errores de herramientas y contenido malicioso.
- **Seguridad:** tasa de intentos de exfiltración o ejecución no autorizada que fueron bloqueados.
- **Eficiencia:** latencia, tokens, costo, número de pasos y tasa de reintentos.
- **Supervisión:** proporción de tareas que requieren intervención humana y calidad de las aprobaciones.
- **Satisfacción y utilidad:** valoración del usuario y mejora observada en el proceso.

Las pruebas deben incluir casos normales, límites, errores, abuso y regresión después de cambios de modelo, prompt, herramienta o política. Las evaluaciones automatizadas deben complementarse con revisión humana en escenarios de mayor impacto.

## 5.10. Memoria, contexto y recuperación

La memoria agéntica debe diseñarse con reglas explícitas. No toda conversación o dato debe persistirse. Se debe definir qué información se conserva, con qué propósito, durante cuánto tiempo, quién puede consultarla y cómo se elimina. La memoria debe clasificarse y protegerse como cualquier otro activo de datos.

En sistemas RAG, la recuperación debe respetar permisos y filtros de seguridad del usuario. Se deben almacenar referencias a la fuente, fecha, versión y fragmentos utilizados; evitar que documentos obsoletos o de baja calidad dominen la respuesta; y proporcionar mecanismos de actualización, invalidación y eliminación.

Los embeddings también pueden revelar información sensible por asociación o recuperación. Deben gestionarse con controles de acceso, retención y borrado adecuados, sin asumir que la vectorización anonimiza los datos.

## 5.11. Interacción multiagente

La colaboración multiagente puede ser útil cuando se requieren especialización y división del trabajo. Un diseño posible contempla:

- **Agente de planificación:** descompone la solicitud en tareas.
- **Agente de descubrimiento:** consulta catálogo y metadatos autorizados.
- **Agente de análisis:** ejecuta consultas y procedimientos analíticos permitidos.
- **Agente de validación:** revisa consistencia, evidencia y criterios de aceptación.
- **Agente de gobernanza:** comprueba clasificación, finalidad y restricciones.
- **Agente de reporte:** presenta resultados con fuentes y limitaciones.

La separación debe aportar una ventaja verificable. Multiplicar agentes sin necesidad puede aumentar costos, latencia, superficie de ataque y dificultad de depuración. Las decisiones de autorización no deben delegarse entre agentes de forma que se pierda la responsabilidad o se evadan controles.

## 5.12. Protocolo de adopción

1. Seleccionar un caso de uso acotado, frecuente y con impacto medible.
2. Definir qué datos puede consultar el agente y qué acciones puede ejecutar.
3. Construir herramientas pequeñas, tipadas y con permisos mínimos.
4. Establecer criterios de aceptación, casos de prueba y umbrales de riesgo.
5. Desplegar en ambiente aislado y con datos no productivos o minimizados.
6. Realizar pruebas funcionales, de seguridad, privacidad y abuso.
7. Incorporar aprobación humana para acciones relevantes.
8. Ejecutar un piloto con usuarios controlados y monitoreo intensivo.
9. Evaluar resultados, incidentes, costos y calidad.
10. Ampliar gradualmente el alcance, manteniendo revisiones y posibilidad de reversión.

## 5.13. Entregables esperados

- Inventario y clasificación de agentes, modelos, herramientas y conectores.
- Registro de casos de uso, propietarios, finalidad y nivel de riesgo.
- Arquitectura de referencia de orquestación y ejecución.
- Catálogo de herramientas autorizadas y contratos de API.
- Matriz de permisos por agente, usuario, herramienta y recurso.
- Políticas de memoria, recuperación, retención y borrado.
- Evaluaciones de seguridad, privacidad y riesgos de IA.
- Banco de pruebas y resultados de evaluación continua.
- Procedimientos de supervisión, escalamiento, reversión y respuesta a incidentes.
- Paneles de observabilidad, costos y cumplimiento.

## 5.14. Indicadores

- Porcentaje de agentes registrados y aprobados antes de producción.
- Porcentaje de herramientas con contratos, propietario y permisos documentados.
- Tasa de éxito de tareas y tasa de respuestas sustentadas.
- Tasa de acciones bloqueadas correctamente por política.
- Número de acciones no autorizadas o incidentes de exposición.
- Porcentaje de operaciones sensibles sujetas a aprobación humana.
- Latencia, costo medio y consumo por tarea completada.
- Tasa de derivación a personal humano y tiempo de resolución.
- Deriva de desempeño y tiempo para detectar y corregir degradación.

## 5.15. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Prompt injection o instrucciones maliciosas en fuentes | Separar datos e instrucciones; limitar herramientas; verificar políticas fuera del modelo |
| Exceso de permisos | Identidades específicas, privilegio mínimo, credenciales temporales y revisión de permisos |
| Alucinaciones o información sin evidencia | RAG gobernado, citas verificables, evaluación y declaración de incertidumbre |
| Acciones irreversibles no autorizadas | Aprobación humana, límites de acción, simulación previa y mecanismo de reversión |
| Fuga de datos por memoria o salida | Minimización, clasificación, filtros de salida, cifrado y retención definida |
| Bucles de agentes y costos inesperados | Límites de pasos, presupuesto, timeout, circuit breaker y supervisión |
| Dificultad para atribuir responsabilidades | Registro de identidad, versión, plan, herramientas, aprobación y resultado |
| Dependencia del modelo o proveedor | Interfaces desacopladas, evaluación de alternativas y estrategia de sustitución |

## 5.16. Resultado esperado

Un ecosistema inteligente en el que los agentes amplían el acceso y la productividad sobre datos gobernados, coordinan servicios y automatizan tareas bajo controles verificables, sin sustituir la autoridad institucional ni eliminar la supervisión humana necesaria.

---

# Anexo A. Relación entre los cinco componentes

Los cinco componentes se complementan de la siguiente manera:

| Componente | Pregunta que responde | Capacidad principal | Dependencia crítica |
|---|---|---|---|
| 1. Ecosistemas de datos y arquitecturas hiperconvergentes | ¿Cómo se organiza e integra el entorno? | Arquitectura, interoperabilidad y modelo operativo | Roles, dominios y arquitectura objetivo |
| 2. Gobernanza normativa y gestión estratégica | ¿Quién puede hacer qué, con qué datos y bajo qué reglas? | Autoridad, políticas, controles y evidencia | Responsabilidad y marco normativo aplicable |
| 3. Infraestructura para grandes volúmenes | ¿Dónde y cómo se almacenan y procesan los datos? | Cómputo, almacenamiento, red, resiliencia y operación | Perfiles de carga y niveles de servicio |
| 4. Analítica, ciencia de datos e IA | ¿Cómo se convierten los datos en conocimiento y decisiones? | Modelos, experimentación, analítica y MLOps | Datos adecuados, reproducibilidad y evaluación |
| 5. IA agéntica y ecosistemas inteligentes | ¿Cómo se coordinan tareas y servicios de manera autónoma y controlada? | Agentes, herramientas, recuperación y orquestación | Identidad, permisos, políticas, trazabilidad y supervisión |

## Flujo lógico de extremo a extremo

1. Las fuentes generan o proporcionan datos.
2. Los mecanismos de integración los incorporan y validan.
3. La infraestructura los conserva y procesa.
4. El catálogo y las capas semánticas proporcionan contexto y descubrimiento.
5. La gobernanza controla clasificación, finalidad, calidad, permisos y retención.
6. La analítica y la ciencia de datos producen indicadores, hipótesis y modelos.
7. Los agentes pueden descubrir, coordinar y ejecutar tareas autorizadas sobre esos servicios.
8. La observabilidad registra desempeño, costos, riesgos y resultados.
9. La evaluación y la retroalimentación alimentan la mejora continua.

# Anexo B. Hoja de ruta sugerida de implementación

La secuencia es orientativa. Las etapas pueden solaparse cuando existan responsables, dependencias y controles claramente establecidos.

| Fase | Prioridad | Actividades principales | Criterio de salida |
|---|---|---|---|
| 0. Diagnóstico y alineación | Alcance y mandato | Inventario de fuentes, cargas, obligaciones, casos de uso, riesgos y capacidades | Alcance, patrocinador, objetivos y línea base aprobados |
| 1. Fundamentos de arquitectura | Base común | Arquitectura objetivo, dominios, estándares, red, identidad y diseño de infraestructura | Diseño validado y prueba de concepto representativa |
| 2. Plataforma de datos mínima | Integración y almacenamiento | Ingesta, almacenamiento, catálogo, metadatos, calidad y acceso | Primeros productos de datos con responsables y controles |
| 3. Gobierno operativo | Control y evidencia | Políticas, matriz normativa, clasificación, auditoría y retención | Controles implementados y evidencia revisable |
| 4. Analítica y MLOps | Valor analítico | Entornos, pipelines, registro de modelos, evaluación y monitoreo | Primeros casos de uso validados y operados |
| 5. Agentes controlados | Automatización | Herramientas, orquestación, RAG, permisos, evaluaciones y supervisión | Piloto acotado con pruebas de seguridad y criterios de salida |
| 6. Escalamiento | Industrialización | Nuevos dominios, optimización, automatización y mejora continua | Niveles de servicio, costos y resultados sostenibles |

## Condiciones para avanzar de fase

- Existe un responsable institucional y responsables operativos identificados.
- Los riesgos relevantes están documentados y tienen tratamiento aprobado.
- Los datos y servicios cuentan con requisitos de calidad, acceso y disponibilidad.
- Los mecanismos de recuperación y auditoría se han probado.
- Los usuarios reciben capacitación y conocen sus responsabilidades.
- Los resultados se miden con indicadores acordados.


# Referencias


1. **ISO/IEC 38505-1:2026 — Information technology — Governance of data — Part 1: Application of ISO/IEC 38500 to the governance of data.** Publicación de 2026. [Ficha oficial de ISO](https://www.iso.org/standard/87195.html).
2. **ISO/IEC 27001:2022 — Information security, cybersecurity and privacy protection — Information security management systems — Requirements.** Consultar también las enmiendas aplicables. [Ficha oficial de ISO](https://www.iso.org/standard/27001).
3. **ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system.** Requisitos para establecer y mejorar un sistema de gestión de IA. [Ficha oficial de ISO](https://www.iso.org/standard/42001).
4. **NIST AI Risk Management Framework (AI RMF 1.0).** Marco voluntario para gestionar riesgos de sistemas de IA. [Portal oficial de NIST](https://www.nist.gov/itl/ai-risk-management-framework).
5. **NIST AI 600-1 — Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (2024).** Perfil de riesgos para IA generativa. [Publicación oficial de NIST](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).
6. **Reglamento (UE) 2024/1689 — Reglamento de Inteligencia Artificial.** Consultar la versión consolidada, fechas de aplicación y ámbito material/territorial. [Texto en EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689).
7. **DAMA International — Data Management Body of Knowledge (DAMA-DMBOK).** Referencia de conocimiento profesional sobre gestión de datos. [Sitio de DAMA International](https://www.dama.org/).

______________________

> CISO | oswaldo.diaz@inegi.org.mx 

