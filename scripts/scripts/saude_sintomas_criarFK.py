import pandas as pd

def merge_csv():
    # using pandas, merge sintomas_columns.csv and sintoma_grupo.csv on the following columns: 'Nosocomial', 'Febre', 'Tosse', 'Garganta', 'Dispneia', 'Desconforto_respiratorio', 'Saturacao', 'Diarreia', 'Vomito', 'Dor_abdominal', 'Fadiga', 'Perda_de_olfato', 'Perda_do_paladar' and save the result to a new csv file called sintomasFK.csv
    df = pd.read_csv('sintomas_columns.csv')
    df2 = pd.read_csv('sintoma_grupo.csv')
    df3 = df.merge(df2, on=['Nosocomial', 'Febre', 'Tosse', 'Garganta', 'Dispneia', 'Desconforto_respiratorio', 'Saturacao', 'Diarreia', 'Vomito', 'Dor_abdominal', 'Fadiga', 'Perda_de_olfato', 'Perda_do_paladar'], how='left', sort=False)
    df3.to_csv('sintomasFK.csv', index=False)

def drop_all_sintomas_columns():
    #using pandas, open sintomasFK.csv, drop the following columns: 'Nosocomial', 'Febre', 'Tosse', 'Garganta', 'Dispneia', 'Desconforto_respiratorio', 'Saturacao', 'Diarreia', 'Vomito', 'Dor_abdominal', 'Fadiga', 'Perda_de_olfato', 'Perda_do_paladar' and save the result to a new csv file called sintomasFK.csv
    df = pd.read_csv('sintomasFK.csv')
    df.drop(columns=['Nosocomial', 'Febre', 'Tosse', 'Garganta', 'Dispneia', 'Desconforto_respiratorio', 'Saturacao', 'Diarreia', 'Vomito', 'Dor_abdominal', 'Fadiga', 'Perda_de_olfato', 'Perda_do_paladar'], inplace=True)
    df.to_csv('sintomasFK.csv', index=False)
    pass


def main():

    # merge_csv()
    drop_all_sintomas_columns()
    pass

if __name__ == '__main__':
    main()