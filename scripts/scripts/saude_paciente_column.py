import pandas as pd

def get_paciente_columns():
    # using pandas, open saude_dataframe.csv, copy the following columns: 'CS_SEXO','DT_NASC','VACINA_COV', 'DOSE_1_COV', 'DOSE_2_COV', 'DOSE_REF', 'FAB_COV_1', 'FAB_COV_2', 'FAB_COVREF' and save the result in a new csv file called saude_paciente_columns.csv
    saude_dataframe = pd.read_csv('saude_dataframe.csv', sep=',', on_bad_lines='skip', low_memory=False)
    saude_paciente_columns = saude_dataframe[['CS_SEXO','DT_NASC','VACINA_COV', 'DOSE_1_COV', 'DOSE_2_COV', 'DOSE_REF', 'FAB_COV_1', 'FAB_COV_2', 'FAB_COVREF']]
    
    
    # Rename the columns as follows: 'CS_SEXO' -> 'sexo' 'DT_NASC' -> 'data_nascimento' 'VACINA_COV' -> 'recebeu_vacina' 'DOSE_1_COV' -> 'data_dose_1' 'DOSE_2_COV' -> 'data_dose_2' 'DOSE_REF' -> 'data_dose_ref' 'FAB_COV_1' -> 'fab_1' 'FAB_COV_2' -> 'fab_2' 'FAB_COVREF' -> 'fab_ref'
    saude_paciente_columns.rename(columns={'CS_SEXO': 'sexo', 'DT_NASC': 'data_nascimento', 'VACINA_COV': 'recebeu_vacina', 'DOSE_1_COV': 'data_dose_1', 'DOSE_2_COV': 'data_dose_2', 'DOSE_REF': 'data_dose_ref', 'FAB_COV_1': 'fab_1', 'FAB_COV_2': 'fab_2', 'FAB_COVREF': 'fab_ref'}, inplace=True)

    saude_paciente_columns.index.name = 'pkPaciente'

    saude_paciente_columns.to_csv('saude_paciente_columns.csv', sep=',', index=True)

    pass

def formatar_paciente_columns():
    # using pandas, open saude_paciente_columns.csv
    # 1. at the following column: 'recebeu_vacina' replace the value 2 to 0
    # 2. save the result in a new csv file called saude_paciente_columns.csv

    saude_paciente_columns = pd.read_csv('saude_paciente_columns.csv', sep=',', on_bad_lines='skip', low_memory=False)
    saude_paciente_columns.replace(2, 0, inplace=True)
    
    saude_paciente_columns.to_csv('saude_paciente_columns.csv', sep=',', index=False)

def main():

    get_paciente_columns()
    formatar_paciente_columns()

    pass

if __name__ == '__main__':
    main()