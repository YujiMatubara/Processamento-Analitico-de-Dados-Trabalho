import pandas as pd

def get_date_column():
    # Using pandas, open saude_dataframe.csv and copy only column DT_NOTIFIC and save to a new csv file named dataEntrada.csv
	
	# Open csv
	data = pd.read_csv('saude_dataframe.csv', low_memory=False, on_bad_lines='skip', sep=',')
	# Copy only column DT_NOTIFIC
	data = data[['DT_NOTIFIC']]
	# Save to csv
	data.to_csv('saudeColunaData.csv', index=False)

def format_date_column():

    # using pandas, change the date format from dd/mm/yyyy to yyyy-mm-dd, using saudeColunaData.csv
    df = pd.read_csv('saudeColunaData.csv')
    df['DT_NOTIFIC'] = pd.to_datetime(df['DT_NOTIFIC'], format='%d/%m/%Y')

    # Rename the column DT_NOTIFIC to DataCompleta
    df = df.rename(columns={'DT_NOTIFIC': 'DataCompleta'})

    # Save the dataframe to a csv file
    df.to_csv('saudeColunaDataFormatada.csv', index=False)


def merge_dataFrames_dates():

    #using pandas, open saudeColunaDataFormatada.csv and date_Table.csv and merge them into dataFK.csv, saving to a new csv file
    # Open csv
    dataEntradaFormatada = pd.read_csv('saudeColunaDataFormatada.csv')
    dataTable = pd.read_csv('date_Table.csv')

    # Merge dataEntradaFormatada and dataTable
    dataFK = pd.merge(dataEntradaFormatada, dataTable, on='DataCompleta', how='left', sort=False)

    # Drop the following columns: DataCompleta,Dia,Semana,Mes,MesNome,Ano,Mes-Ano,Trimestre,Trimestre-Ano,Semestre,Semestre-Ano
    dataFK = dataFK.drop(['DataCompleta', 'Dia', 'Semana', 'Mes', 'MesNome', 'Ano', 'Mes-Ano', 'Trimestre', 'Trimestre-Ano', 'Semestre', 'Semestre-Ano'], axis=1)

    # Rename the column Index to DataFK
    dataFK = dataFK.rename(columns={'Index': 'pkData'})

    # Save the result in dataFK.csv
    dataFK.to_csv('dataFK.csv', index=False)



def main():
	# get_date_column()
    # format_date_column()
    merge_dataFrames_dates()
    
    pass




if __name__ == '__main__':
	main()