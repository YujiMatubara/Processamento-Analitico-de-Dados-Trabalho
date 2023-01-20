import pandas as pd
import datetime
import numpy as np

'''
Dia
Semana
Quinzena
Mês
Trimestre
Semestre
Ano
'''

meses =['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def create_date_table():
    # Using pd.dataframe, create dates in range of '2021-01-01' to '2022-12-31', with a step of 1 day
    dates = pd.date_range('2021-01-01', '2022-12-31', freq='D')

    # Convert date_range to DataFrame
    df = pd.DataFrame({'DataCompleta': dates})

    df['DataCompleta'] = pd.to_datetime(df['DataCompleta'])

    df['DataCompleta'].dt.to_period('M')

    df['DataCompleta'].dt.strftime('%m/%Y')

    df['Dia'] = pd.to_datetime(df['DataCompleta']).dt.day

    df['Semana'] = pd.to_datetime(df['DataCompleta']).dt.isocalendar().week
    # Replace semana values of 53 to 0
    df['Semana'] = df['Semana'].replace(53, 0)

    df['Mes'] = pd.to_datetime(df['DataCompleta']).dt.month
    df['Ano'] = pd.to_datetime(df['DataCompleta']).dt.year
    df['Ano'].astype(str) + '-'+ df['Mes'].astype(str)
    # Create column Mes-Ano, following the format yyyy-mm
    df['Mes-Ano'] = df['Ano'].astype(str) + '-'+ df['Mes'].astype(str)
    # Create column Mes nome, using the month number as index in the meses list
    df['MesNome'] = df['Mes'].apply(lambda x: meses[x-1])

    df['Trimestre'] = pd.to_datetime(df['DataCompleta']).dt.quarter
    # Create column Trimestre-Ano, following the format yyyy-qq
    df['Trimestre-Ano'] = df['Ano'].astype(str) + '-'+ df['Trimestre'].astype(str)

    df['Semestre']= np.where(pd.to_datetime(df['DataCompleta']).dt.quarter.gt(2),2,1).astype(str)
    # Create column Semestre-ano, following the format yyyy-ss
    df['Semestre-Ano'] = df['Ano'].astype(str) + '-'+ df['Semestre'].astype(str)
    
    # Create index column, starting from 1
    df['Index'] = df.index + 1
    # Move index column as first column, and column Ano after MesNome
    df = df[['Index', 'DataCompleta', 'Dia', 'Semana', 'Mes', 'MesNome', 'Ano', 'Mes-Ano', 'Trimestre', 'Trimestre-Ano', 'Semestre', 'Semestre-Ano']]

    # Save to a csv
    df.to_csv('date_table.csv', index=False)




def main():

    create_date_table()
    pass


if __name__ == '__main__':
    main()