import pandas as pd
import numpy as np

def get_doente_column():
    # using pandas, open doencasFK.csv and replace all non-zero values with 1 and save it as a new csv file called 'saude_situacao_doente_column.csv'
    # open doencasFK.csv
    df = pd.read_csv('doencasFK.csv', sep=',', on_bad_lines='skip', low_memory=False)
    
    # replace all non-zero values with 1 and save it as a new csv file called 'saude_situacao_doente_column.csv'
    lst_values: list = np.arange(1,300) 
    '''Pegamos um valor de 300 (maior que o numero de grupos de doenças)'''
    
    df.replace(lst_values, 1, inplace=True)
    
    # rename the column pkGrupoDoenca to situacao_doente
    df.rename(columns={'pkGrupoDoenca': 'situacao_doente'}, inplace=True)
    
    df.to_csv('saude_situacao_doente_column.csv', index=False)

    pass

def main():
    get_doente_column()
    pass

if __name__ == '__main__':
    main()