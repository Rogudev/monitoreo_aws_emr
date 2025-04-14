# Tarea evaluable 3ª evaluación, Monitoreo en AWS EMR


## Contenido

- pdf con la documentación
- **scripts/**: Scripts usados para la creación de los recursos de AWS
    - **NOTA**: Hay archivos _requirements.txt_ para la instalación de las librerías necesarias
- **config_files/**: Archivos de configuración

---

## Objetivo

- Crear un clúster AWS **EMR** con Hadoop usando un script de Python
- Descarga, configuración y uso de **JMX Exporter** para exponer las métricas del Namenode
- Creación de un clúster AWS **EC2** usando un script de python 
- Despliegue y configuración de **Prometheus** en el EC2 para la recolección de dichas métricas
- Instalación y uso de **Grafana** en el EC2 para la visualización de las métricas recogidas por **Prometheus**
- Construcción de dashboard en **Grafana** con las métricas:
    - Uso de CPU y memoria
    - Estado del Namenode
    - Espacio utilizado de HDFS