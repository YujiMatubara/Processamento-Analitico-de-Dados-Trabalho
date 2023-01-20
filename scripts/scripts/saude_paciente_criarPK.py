import pandas as pd

def criar_pk():
    # using pandas, open saude_paciente_columns.csv and copy the column pkPaciente and save the result in a new csv file called pacienteFK.csv
    saude_paciente_columns = pd.read_csv('saude_paciente_columns.csv', sep=',', on_bad_lines='skip', low_memory=False)
    pacienteFK = saude_paciente_columns['pkPaciente']
    pacienteFK.to_csv('pacienteFK.csv', sep=',', index=False)

    pass

def main():

    criar_pk()
    pass

if __name__ == '__main__':
    main()