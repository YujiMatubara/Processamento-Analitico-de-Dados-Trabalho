import pandas as pd

def concat_columns():
    # using pandas, open saude_situacao_doente_column.csv and saude_situacao_obito_column.csv and concat them side by side
    # write the filtered data to a csv file called saude_situacao_column.csv

    # read in the data
    saude_situacao_doente_column = pd.read_csv('saude_situacao_doente_column.csv')
    saude_situacao_obito_column = pd.read_csv('saude_situacao_obito_column.csv')

    # concat the data
    saude_situacao_column = pd.concat([saude_situacao_doente_column, saude_situacao_obito_column], axis=1)

    # write the data to a csv file
    saude_situacao_column.to_csv('saude_situacao_column.csv', index=False)

    pass

def merge_columns():
    # using pandas, open saude_situacao_column.csv and situacao.csv and merge them on the following columns: situacao_obito, situacao_doente and save the result to a csv filve called situacaoFK.csv
    # write the filtered data to a csv file called situacaoFK.csv

    # read in the data
    saude_situacao_column = pd.read_csv('saude_situacao_column.csv')
    situacao = pd.read_csv('situacao.csv')

    # merge the data
    situacaoFK = pd.merge(saude_situacao_column, situacao, on=['situacao_obito', 'situacao_doente'], sort=False, how='left')

    # drop situacao_obito and situacao_doente
    situacaoFK.drop(['situacao_obito', 'situacao_doente'], axis=1, inplace=True)
    
    # change index column name to fkSituacao
    situacaoFK.rename(columns={'index': 'fkSituacao'}, inplace=True)

    # write the data to a csv file
    situacaoFK.to_csv('situacaoFK.csv', index=False)


def main():

    # concat_columns()
    merge_columns()
    pass

if __name__ == '__main__':
    main()