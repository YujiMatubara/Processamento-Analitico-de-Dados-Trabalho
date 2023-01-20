import pandas as pd

def passar_valores_float_para_int():
    # using pandas, read the csv file doencas_grupo.csv, and save the dataframe with the same name as the file
    doencas_grupo = pd.read_csv('doencas_grupo.csv')
    doencas_grupo.to_csv('doencas_grupo.csv', index=False, float_format='%.0f')

    #using pandas, read the csv file sintoma_grupo.csv, and save the dataframe with the same name as the file
    sintoma_grupo = pd.read_csv('sintoma_grupo.csv')
    sintoma_grupo.to_csv('sintoma_grupo.csv', index=False, float_format='%.0f')


def main():

    passar_valores_float_para_int()

    pass

if __name__ == '__main__':
    main()