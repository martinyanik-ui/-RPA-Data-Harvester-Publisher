graph TD
    A[Inicio del Proceso] --> B[Acceso al Portal Público]
    B --> C{¿Carga Exitosa?}
    C -- No --> D[Reintento / Registro de Error]
    C -- Sí --> E[Extracción de Datos de la Tabla]
    E --> F[Transformación y Limpieza (Python/Pandas)]
    F --> G[Generación de Reporte Estructurado .csv/.xlsx]
    G --> H[Notificación de Finalización]
    H --> I[Fin del Proceso]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#dfd,stroke:#333,stroke-width:2px
    style I fill:#f9f,stroke:#333,stroke-width:2px
