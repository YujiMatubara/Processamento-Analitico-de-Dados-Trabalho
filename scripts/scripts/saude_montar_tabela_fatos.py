import pandas as pd

def concat_csv():
    # open dataFK.csv, localFK.csv, pacienteFK.csv, sintomasFK.csv, doencasFK.csv, situacaoFK.csv, gestanteFATO.csv and concatenate them in saude_estrela.csv
    dataFK = pd.read_csv('dataFK.csv', sep=',', on_bad_lines='skip', low_memory=False)
    localFK = pd.read_csv('localFK.csv', sep=',', on_bad_lines='skip', low_memory=False)
    pacienteFK = pd.read_csv('pacienteFK.csv', sep=',', on_bad_lines='skip', low_memory=False)
    sintomasFK = pd.read_csv('sintomasFK.csv', sep=',', on_bad_lines='skip', low_memory=False)
    doencasFK = pd.read_csv('doencasFK.csv', sep=',', on_bad_lines='skip', low_memory=False)
    situacaoFK = pd.read_csv('situacaoFK.csv', sep=',', on_bad_lines='skip', low_memory=False)
    gestanteFATO = pd.read_csv('gestanteFATO.csv', sep=',', on_bad_lines='skip', low_memory=False)
    
    saude_estrela = pd.concat([dataFK, localFK, pacienteFK, sintomasFK, doencasFK, situacaoFK, gestanteFATO], axis=1, sort=False)
    
    #Add a column 'Registro_ocorrencia' that is always 1 for every row
    saude_estrela['Registro_ocorrencia'] = 1

    saude_estrela.to_csv('saude_estrela.csv', index=False)

def main():

    concat_csv()

    pass

if __name__ == '__main__':
    main()