import pandas as pd

def filter_by_date():
    # Using pandas, open a northeast.csv file and remove indexes from before 2021-01-01
    northeast = pd.read_csv('northeast.csv')
    northeast = northeast[northeast["Data"] >= '2021-01-01']
    northeast.to_csv('northeast_filtered.csv', index=False)

def drop_columns():

    # Using pandas, save to a new csv file the data from northeast_filtered.csv without the columns "PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)","PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)","PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)","RADIACAO GLOBAL (Kj/m²)","TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)","TEMPERATURA DO PONTO DE ORVALHO (°C)","TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)","TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)","UMIDADE RELATIVA DO AR, HORARIA (%)","VENTO, DIREÇÃO HORARIA (gr) (° (gr))","VENTO, RAJADA MAXIMA (m/s)","station_code","latitude","longitude","height"
    northeast = pd.read_csv('northeast_filtered.csv')
    northeast = northeast.drop(columns=['PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)','PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)','PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)','RADIACAO GLOBAL (Kj/m²)','TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)','TEMPERATURA DO PONTO DE ORVALHO (°C)','TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)','TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)','UMIDADE RELATIVA DO AR, HORARIA (%)','VENTO, DIREÇÃO HORARIA (gr) (° (gr))','VENTO, RAJADA MAXIMA (m/s)','station_code','latitude','longitude','height'])
    northeast.to_csv('northeast_filtered_drop_columns.csv', index=False)

def change_chuva_value():
    # Using pandas, change "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)" values of -9999.0 to 0.0
    northeast = pd.read_csv('northeast_filtered_drop_columns.csv')
    northeast['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'] = northeast['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'].replace(-9999.0, 0.0)
    northeast.to_csv('northeast_filtered_drop_columns_chuva.csv', index=False)


def change_min_values():
    # Using pandas, change values -9999.0 to 9999.0 from columns TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C),UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)
    northeast = pd.read_csv('northeast_filtered_drop_columns_chuva.csv')
    northeast['TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)'] = northeast['TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)'].replace(-9999.0, 9999.0)
    northeast['UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)'] = northeast['UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)'].replace(-9999.0, 9999.0)
    northeast.to_csv('northeast_filtered_drop_columns_chuva_min.csv', index=False)

def calc_max_chuva():
    # Using pandas, replace "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)" with the sum of "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)" by date, state, region and station and save to a new csv
    northeast = pd.read_csv('northeast_filtered_drop_columns_chuva_min.csv')
    northeast['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'] = northeast.groupby(['Data', 'state', 'region', 'station'])['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'].transform('sum')
    northeast.to_csv('northeast_filtered_drop_columns_chuva_min_max.csv', index=False)


def change_min_temp_values():
    # Using pandas, replace TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C) with the minimum of TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C) by date, state, region and station and save to a new csv
    northeast = pd.read_csv('northeast_filtered_drop_columns_chuva_min_max.csv')
    northeast['TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)'] = northeast.groupby(['Data', 'state', 'region', 'station'])['TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)'].transform('min')
    northeast.to_csv('northeast_filtered_drop_columns_chuva_min_max_min.csv', index=False)

def change_min_umidity_values():
    # Using pandas, replace UMIDADE REL. MIN. NA HORA ANT. (AUT) (%) with the minimum of UMIDADE REL. MIN. NA HORA ANT. (AUT) (%) by date, state, region and station and save to a new csv
    northeast = pd.read_csv('northeast_filtered_drop_columns_chuva_min_max_min.csv')
    northeast['UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)'] = northeast.groupby(['Data', 'state', 'region', 'station'])['UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)'].transform('min')
    northeast.to_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity.csv', index=False)

def change_max_temp_values():
    # Using pandas, replace TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C) with the maximum of TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C) by date, state, region and station and save to a new csv
    northeast = pd.read_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity.csv')
    northeast['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'] = northeast.groupby(['Data', 'state', 'region', 'station'])['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'].transform('max')
    northeast.to_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity_max.csv', index=False)

def change_max_umidity_values():
    # Using pandas, replace UMIDADE REL. MAX. NA HORA ANT. (AUT) (%) with the maximum of UMIDADE REL. MAX. NA HORA ANT. (AUT) (%) by date, state, region and station and save to a new csv
    northeast = pd.read_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity_max.csv')
    northeast['UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)'] = northeast.groupby(['Data', 'state', 'region', 'station'])['UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)'].transform('max')
    northeast.to_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity_max_max.csv', index=False)

def change_max_vento_values():
    # Using pandas, replace "VENTO, VELOCIDADE HORARIA (m/s)" with the maximum of "VENTO, VELOCIDADE HORARIA (m/s)" by date, state, region and station and save to a new csv
    northeast = pd.read_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity_max_max.csv')
    northeast['VENTO, VELOCIDADE HORARIA (m/s)'] = northeast.groupby(['Data', 'state', 'region', 'station'])['VENTO, VELOCIDADE HORARIA (m/s)'].transform('max')
    northeast.to_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity_max_max_vento.csv', index=False)


def remove_hora_and_index_column():
    # Using pandas, remove the columns "Hora" and "index" and save to a new csv
    northeast = pd.read_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity_max_max_vento.csv')
    northeast.drop(['Hora', 'index'], axis=1, inplace=True)
    northeast.to_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity_max_max_vento_remove_hora_and_index.csv', index=False)

def remove_duplicate_rows():
    # Using pandas, remove the duplicate rows and save to a new csv
    northeast = pd.read_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity_max_max_vento_remove_hora_and_index.csv')
    northeast.drop_duplicates(inplace=True)
    northeast.to_csv('northeast_filtered_drop_columns_chuva_min_max_min_umidity_max_max_vento_remove_hora_and_index_remove_duplicate_rows.csv', index=False)

    
def main():
    
    filter_by_date()
    drop_columns()
    change_chuva_value()
    change_min_values()
    calc_max_chuva()
    change_min_temp_values()
    change_min_umidity_values()
    change_max_temp_values()
    change_max_umidity_values()
    change_max_vento_values()
    remove_hora_and_index_column()
    remove_duplicate_rows()

    


# If name main program
if __name__ == '__main__':
    main()