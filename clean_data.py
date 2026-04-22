import pandas as pd

def process_portal_data(input_file):
    # Cargamos los datos del portal de datos abiertos
    df = pd.read_csv(input_file)
    
    # Supongamos que extraemos una tabla de 'Datasets Actualizados'
    # Limpiamos nombres de columnas y quitamos nulos
    df.columns = [c.lower().replace(' ', '_') for c in df.columns]
    df = df.dropna(subset=['titulo', 'ultima_actualizacion'])
    
    # Convertimos la fecha a formato ISO
    df['fecha_limpia'] = pd.to_datetime(df['ultima_actualizacion']).dt.date
    
    # Generamos un archivo listo para Power BI
    df.to_csv('Datasets_Modernizados.csv', index=False)
    print("ETL completado: Datos listos para el dashboard.")

# Ejemplo de uso:
# process_portal_data('datos_extraidos.csv')
