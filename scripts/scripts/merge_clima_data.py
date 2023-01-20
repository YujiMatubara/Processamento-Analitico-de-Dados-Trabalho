import pandas as pd


def merge_clima_data():
    # From date_table.csv and todas_estacoes.csv, merge the data on columns DataCompleta from date_table and Data from todas_estacoes and save to a new csv file

	# Read data_table.csv
	date_table = pd.read_csv('date_table.csv')
	# Read todas_estacoes.csv
	todas_estacoes = pd.read_csv('todas_estacoes.csv')
	# Merge data_table and todas_estacoes on columns DataCompleta and Data
	merged_data = pd.merge(date_table, todas_estacoes, left_on='DataCompleta', right_on='Data')

	# Replace DataCompleta header tag name to fkData
	merged_data.rename(columns={'Index': 'fkData'}, inplace=True)

	# Replace index header tag name to fkEstacao
	merged_data.rename(columns={'index': 'fkEstacao'}, inplace=True)

	# Save to a new csv file
	merged_data.to_csv('merged_data.csv', index=False)
	

def drop_columns():
	# Using pandas, drop only the following columns: DataCompleta,Dia,Semana,Mes,MesNome,Ano,Mes-Ano,Trimestre,Trimestre-Ano,Semestre,Semestre-Ano,Data and save to a new csv file
	# Read merged_data.csv
	merged_data = pd.read_csv('merged_data.csv')
	# Drop columns DataCompleta,Dia,Semana,Mes,MesNome,Ano,Mes-Ano,Trimestre,Trimestre-Ano,Semestre,Semestre-Ano,Data
	merged_data.drop(['DataCompleta','Dia','Semana','Mes','MesNome','Ano','Mes-Ano','Trimestre','Trimestre-Ano','Semestre','Semestre-Ano','Data'], axis=1, inplace=True)
	# Save to a new csv file
	merged_data.to_csv('merged_data_drop_columns.csv', index=False)


def clean_csv():
	# Change "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C),TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C),UMIDADE REL. MAX. NA HORA ANT. (AUT) (%),UMIDADE REL. MIN. NA HORA ANT. (AUT) (%),"VENTO, VELOCIDADE HORARIA (m/s)" to PrecipitacaoTotal, TempMax, TempMin, UmidMax, UmidMin, Vento
	# Read merged_data_drop_columns.csv
	merged_data_drop_columns = pd.read_csv('merged_data_drop_columns.csv')
	# Change "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C),TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C),UMIDADE REL. MAX. NA HORA ANT. (AUT) (%),UMIDADE REL. MIN. NA HORA ANT. (AUT) (%),"VENTO, VELOCIDADE HORARIA (m/s)" to PrecipitacaoTotal, TempMax, TempMin, UmidMax, UmidMin, Vento
	merged_data_drop_columns.rename(columns={'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)': 'PrecipitacaoTotal', 'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)': 'TempMax', 'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)': 'TempMin', 'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)': 'UmidMax', 'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)': 'UmidMin', 'VENTO, VELOCIDADE HORARIA (m/s)': 'Vento'}, inplace=True)

	# Move fkEstacao to the second column
	merged_data_drop_columns = merged_data_drop_columns[['fkData','fkEstacao', 'PrecipitacaoTotal', 'TempMax', 'TempMin', 'UmidMax', 'UmidMin', 'Vento']]
	# Save to a new csv file
	merged_data_drop_columns.to_csv('merged_data_drop_columns_clean.csv', index=False)


def main():
#	merge_clima_data()
	# drop_columns()
	clean_csv()
	pass

if __name__ == '__main__':
	main()