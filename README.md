# Tarea evaluable 3ª evaluación, Monitoreo en AWS EMR


## Contenido

- **pdf con la documentación**
- **scripts/**: Scripts usados para la creación de los recursos de AWS
    - **NOTA**: Hay archivos _requirements.txt_ para la instalación de las librerías necesarias.
- **config_files/**: Archivos de configuración

---

## Requerimientos

- AWS instalado en el sistema
- Python instalado en el sistema
- Uso de entornos _venv_ de Python _(opcional)_

---

## Objetivo de la práctica

- Crear un clúster AWS **EMR** con Hadoop usando un script de Python
- Descarga, configuración y uso de **JMX Exporter** para exponer las métricas del Namenode
- Creación de un clúster AWS **EC2** usando un script de python 
- Despliegue y configuración de **Prometheus** en el EC2 para la recolección de dichas métricas
- Instalación y uso de **Grafana** en el EC2 para la visualización de las métricas recogidas por **Prometheus**
- Construcción de dashboard en **Grafana** con las métricas:
    - Uso de CPU y memoria
    - Estado del Namenode
    - Espacio utilizado de HDFS

---

## Anotaciones

- El archivo _labsuser.pem_ empleado es el otorgado por el laboratorio de AWS Academy.
- Es aconsejable el uso de los scripts en entornos (o uno solo) _env_.
- Los scripts no emplean claves de acceso al laboratorio AWS porque **están guardadas en el sistema**.
- Se pueden desplegar los clústeres EC2 y EMR desde la consola web de AWS, **el uso de los scripts es opcional**.
- Las IPs empleadas **deberán ser sustituidas** por el que pretenda replicar la práctica **con sus propias IPs**.
- En un entorno de producción **JAMÁS** se deberán usar permisos 777 como se muestra en la práctica; **la práctica fue desarrollada en un entorno de pruebas**.
- En un entorno de producción, es aconsejable que en las exposiciones de puertos se realicen con una, o varias, IPs.