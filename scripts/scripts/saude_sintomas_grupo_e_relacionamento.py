import pandas as pd

def criar_grupo_sintomas():
    # using pandas, open sintomas_columns.csv, drop all duplicate rows and save to a new file

    df = pd.read_csv('sintomas_columns.csv')
    df.drop_duplicates(inplace=True)
    df.to_csv('sintomas_columns_drop_duplicates.csv', index=False)

    pass

def add_index_column():
    # open sintomas_columns_drop_duplicates.csv and add an index column to it at the start of the header
    df = pd.read_csv('sintomas_columns_drop_duplicates.csv')
    df.index.name = 'pkGrupoSintoma'
    df.to_csv('sintoma_grupo.csv', index=True)
    pass

def match_sintoma():
    # open sintoma_grupo.csv
    df = pd.read_csv('sintoma_grupo.csv')

    # create a new csv with the columns: pkGrupo, pkSintoma
    df_new = pd.DataFrame(columns=['pkGrupo', 'pkSintoma'])

    # for each column in the sintoma_grupo.csv, if the value is 1.0, add a new row in df_new containing the row index as pkGrupo and the column index as pkSintoma
    for i in range(len(df)):
        for j in range(len(df.columns)):
            if df.iloc[i, j] == 1.0:
                df_new.loc[len(df_new)] = [i, j]

    # save df_new to a new file ponteSintoma.csv
    df_new.to_csv('sintoma_ponte.csv', index=False)

    ### Aqui nós adicionamos manualmente mais uma entrada para o arquivo ponteSIntoma.csv que é referente ao grupo 12 que não tem sintomas

    '''Ao usar o arquivo saude_sintomas_grupo_e_relacionamento.py para criar o arquivo sintoma_ponte.csv, devemos remover a tupla (1,0) do arquivo sintoma_ponte.csv'''

    pass

def main():
    # criar_grupo_sintomas()
    # add_index_column()
    match_sintoma()
    pass

if __name__ == '__main__':
    main()