import pandas as pd
import datetime

def clean_public_data(file_path):
    # Cargamos el reporte generado por el bot
    df = pd.read_excel(file_path)

    # Limpieza de montos: de "$ 1.200.500,00" a 1200500.00
    if 'Monto' in df.columns:
        df['Monto'] = df['Monto'].replace({'\$': '', '\.': '', ',': '.'}, regex=True).astype(float)

    # Estandarización de fechas
    df['Fecha'] = pd.to_datetime(df['Fecha']).dt.strftime('%Y-%m-%d')

    # Guardar versión limpia para el Dashboard
    output_name = f"Clean_Expedientes_{datetime.date.today()}.csv"
    df.to_csv(output_name, index=False)
    print(f"Archivo procesado: {output_name}")

# Ejemplo de ejecución
# clean_public_data('Reporte_Expedientes.xlsx')
