import pandas as pd

def get_obito_column():
    # using pandas, open saude_dataframe.csv and copy the column 'EVOLUCAO' and save it as a new csv file called 'saude_situacao_obito_column.csv'
    
    # open saude_dataframe.csv
    df = pd.read_csv('saude_dataframe.csv', sep=',', on_bad_lines='skip', low_memory=False)
    # copy the column 'EVOLUCAO' and save it as a new csv file called 'saude_situacao_obito_column.csv'
    df['EVOLUCAO'].to_csv('saude_situacao_obito_column.csv', index=False)

def format_obito_column():
    # using pandas, open saude_situacao_obito_column.csv and replace values with the following: 1.0 to 1, 2.0 to 0, 3.0 to 0, 9.0 to 9

    # Read in the data
    obito = pd.read_csv('saude_situacao_obito_column.csv', sep=';', on_bad_lines='skip', low_memory=False)

    # Replace the values
    obito.replace(1.0, 1, inplace=True)
    obito.replace(2.0, 0, inplace=True)
    obito.replace(3.0, 0, inplace=True)
    obito.replace(9.0, 9, inplace=True)

    # Fill void values with 9
    obito.fillna(9, inplace=True)

    # Rename the column EVOLUCAO to situacao_obito
    obito.rename(columns={'EVOLUCAO': 'situacao_obito'}, inplace=True)

    # Write the data to a csv file
    obito.to_csv('saude_situacao_obito_column.csv', index=False, float_format='%.0f')

def main():
    # get_obito_column()
    format_obito_column()
    pass

if __name__ == '__main__':
    main()