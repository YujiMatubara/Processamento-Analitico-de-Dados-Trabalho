import pandas as pd

def get_local_columns():
    # using pandas, open saude_dataframe.csv, copy the following columns: 'SG_UF_NOT', 'ID_REGIONA', 'CO_REGIONA', 'ID_MUNICIP', 'CO_MUN_NOT', 'ID_UNIDADE', 'CO_UNI_NOT' and save it in saude_local_columns.csv
    saude_dataframe = pd.read_csv('saude_dataframe.csv', sep=',', on_bad_lines='skip', low_memory=False)
    saude_local_columns = saude_dataframe[['SG_UF_NOT', 'ID_REGIONA', 'CO_REGIONA', 'ID_MUNICIP', 'CO_MUN_NOT', 'ID_UNIDADE', 'CO_UNI_NOT']]

    # Rename the columns as Estado, Regiao, Regiao_numero, Municipio, Municipio_numero, Unidade, Unidade_numero
    saude_local_columns.rename(columns={'SG_UF_NOT': 'Estado', 'ID_REGIONA': 'Regiao', 'CO_REGIONA': 'Regiao_numero', 'ID_MUNICIP': 'Municipio', 'CO_MUN_NOT': 'Municipio_numero', 'ID_UNIDADE': 'Unidade', 'CO_UNI_NOT': 'Unidade_numero'}, inplace=True)

    saude_local_columns.to_csv('saude_local_columns.csv', index=False)

    pass

def drop_duplicates():
    # using pandas, open saude_local_columns.csv and drop the duplicates and save it in saude_local_locais.csv
    saude_local_columns = pd.read_csv('saude_local_columns.csv', sep=',', on_bad_lines='skip', low_memory=False)
    saude_local_locais = saude_local_columns.drop_duplicates()


    saude_local_locais.to_csv('saude_local_locais.csv', index=False)

    pass

def add_index():
    #using pandas, open saude_local_locais.csv and add an index column and save it in saude_local_locais.csv
    saude_local_locais = pd.read_csv('saude_local_locais.csv', sep=',', on_bad_lines='skip', low_memory=False)
    
    saude_local_locais.index.name = 'pkLocal'

    saude_local_locais.to_csv('saude_local_locais.csv', index=True)

    pass

def main():
    # get_local_columns()
    # drop_duplicates()
    add_index()
    pass

if __name__ == '__main__':
    main()