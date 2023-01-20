import pandas as pd

def merge_csv():
    # open saude_local_columns.csv and merge it with saude_local_locais.csv on the columns 'Estado', 'Regiao', 'Regiao_numero', 'Municipio', 'Municipio_numero', 'Unidade', 'Unidade_numero' and save it in localFK.csv
    saude_local_columns = pd.read_csv('saude_local_columns.csv', sep=',', on_bad_lines='skip', low_memory=False)
    saude_local_locais = pd.read_csv('saude_local_locais.csv', sep=',', on_bad_lines='skip', low_memory=False)
    localFK = saude_local_columns.merge(saude_local_locais, on=['Estado', 'Regiao', 'Regiao_numero', 'Municipio', 'Municipio_numero', 'Unidade', 'Unidade_numero'], how='left', sort=False)

    localFK.to_csv('localFK.csv', index=False)

    pass

def drop_all_saude_local_columns():
    # open localFK.csv and drop the columns 'Estado', 'Regiao', 'Regiao_numero', 'Municipio', 'Municipio_numero', 'Unidade', 'Unidade_numero' and save it in localFK.csv
    localFK = pd.read_csv('localFK.csv', sep=',', on_bad_lines='skip', low_memory=False)
    localFK.drop(columns=['Estado', 'Regiao', 'Regiao_numero', 'Municipio', 'Municipio_numero', 'Unidade', 'Unidade_numero'], inplace=True)
    localFK.to_csv('localFK.csv', index=False)
    pass

def main():
    # merge_csv()
    drop_all_saude_local_columns()
    pass

if __name__ == '__main__':
    main()