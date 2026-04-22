graph TD
    A[Inicio del Bot] --> B[Acceso a Portal Público]
    B --> C{¿Carga Exitosa?}
    C -- No --> D[Reintento / Log Error]
    C -- Sí --> E[Extracción de Datos de Tabla]
    E --> F[Limpieza de Datos en Memoria]
    F --> G[Generación de Excel con Timestamp]
    G --> H[Fin del Proceso]
