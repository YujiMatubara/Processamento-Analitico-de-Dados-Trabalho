import pandas as pd

def get_sintoma_columns():
    # using pandas, open saude_dataframe.csv, copy the following columns: "NOSOCOMIAL","FEBRE","TOSSE","GARGANTA","DISPNEIA","DESC_RESP","SATURACAO","DIARREIA","VOMITO","DOR_ABD","FADIGA","PERD_OLFT","PERD_PALA" and save to a new csv
    sintoma = pd.read_csv('saude_dataframe.csv', sep=',', on_bad_lines='skip', low_memory=False)
    sintoma_columns = sintoma[['NOSOCOMIAL', 'FEBRE', 'TOSSE', 'GARGANTA', 'DISPNEIA', 'DESC_RESP', 'SATURACAO', 'DIARREIA', 'VOMITO', 'DOR_ABD', 'FADIGA', 'PERD_OLFT', 'PERD_PALA']]
    sintoma_columns.to_csv('sintoma_columns.csv', sep=',', index=False)

    pass

def rename_columns():
    # using pandas, open sintoma_columns.csv, rename the columns to: 'Nosocomial', 'Febre', 'Tosse', 'Garganta', 'Dispneia', 'Desconforto_respiratorio', 'Saturacao', 'Diarreia', 'Vomito', 'Dor_abdominal', 'Fadiga', 'Perda_de_olfato', 'Perda_do_paladar' and save to a new csv
    sintoma_columns = pd.read_csv('sintoma_columns.csv', sep=',', on_bad_lines='skip', low_memory=False)
    sintoma_columns.rename(columns={'NOSOCOMIAL': 'Nosocomial', 'FEBRE': 'Febre', 'TOSSE': 'Tosse', 'GARGANTA': 'Garganta', 'DISPNEIA': 'Dispneia', 'DESC_RESP': 'Desconforto_respiratorio', 'SATURACAO': 'Saturacao', 'DIARREIA': 'Diarreia', 'VOMITO': 'Vomito', 'DOR_ABD': 'Dor_abdominal', 'FADIGA': 'Fadiga', 'PERD_OLFT': 'Perda_de_olfato', 'PERD_PALA': 'Perda_do_paladar'}, inplace=True)
    sintoma_columns.to_csv('sintoma_columns.csv', sep=',', index=False)

def format_sintoma_columns():
    # using pandas, open sintoma_columns.csv, change all values of 2.0 and 9.0 to 0.0, and change all void values to 0.0
    sintoma_columns = pd.read_csv('sintoma_columns.csv', sep=',', on_bad_lines='skip', low_memory=False)
    sintoma_columns.replace(2.0, 0.0, inplace=True)
    sintoma_columns.replace(9.0, 0.0, inplace=True)
    sintoma_columns.fillna(0.0, inplace=True)
    sintoma_columns.to_csv('sintoma_columns.csv', sep=',', index=False)


def main():
    # get_sintoma_columns()
    # rename_columns()
    format_sintoma_columns()
    pass

if __name__ == '__main__':
    main()