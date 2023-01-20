import pandas as pd

def criar_grupo_doencas():
    # using pandas, open doencas_columns.csv, drop all duplicate rows and save to a new file
    df = pd.read_csv('doencas_columns.csv')
    df.drop_duplicates(inplace=True)
    df.to_csv('doencas_columns_drop_duplicates.csv', index=False)
    pass

def add_index_column():
    # open doencas_columns_drop_duplicates.csv and add an index column to it at the start of the header
    df = pd.read_csv('doencas_columns_drop_duplicates.csv')
    df.index.name = 'pkGrupoDoenca'
    df.to_csv('doencas_grupo.csv', index=True)
    pass

def match_doenca():
    # open doencas_grupo.csv
    df = pd.read_csv('doencas_grupo.csv')

    # create a new csv with the columns: pkGrupo, pkDoenca
    df_new = pd.DataFrame(columns=['pkGrupo', 'pkDoenca'])

    # adicionar a tupla 0,0 para o grupo 0 (sem doenca)
    df_new.loc[len(df_new)] = [0, 0]
    
    # for each column in the doencas_grupo.csv, if the value is 1.0, add a new row in df_new containing the row index as pkGrupo and the column index as pkDoenca
    for i in range(len(df)):
        for j in range(len(df.columns)):
            if df.iloc[i, j] == 1.0:
                df_new.loc[len(df_new)] = [i, j]

    # save df_new to a new file ponteDoenca.csv
    df_new.to_csv('doencas_ponte.csv', index=False)

    '''Ao usar o arquivo saude_doencas_grupo_e_relacionamento.py para criar o arquivo doencas_ponte.csv, devemos remover a tupla (1,0) do arquivo doencas_ponte.csv'''

    pass

def main():
    # criar_grupo_doencas()
    # add_index_column()
    match_doenca()
    pass

if __name__ == '__main__':
    main()