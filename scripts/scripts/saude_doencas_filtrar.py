import pandas as pd

def get_doencas_columns():
    # using pandas, open saude_dataframe.csv, copy the following columns: "PCR_FLUASU","PCR_FLUBLI","PCR_VSR","PCR_SARS2","PCR_PARA1","PCR_PARA2","PCR_PARA3","PCR_PARA4","PCR_ADENO","PCR_METAP","PCR_BOCA","PCR_RINO","PCR_OUTRO" and save to a new csv
    doenca = pd.read_csv('saude_dataframe.csv', sep=',', on_bad_lines='skip', low_memory=False)
    doenca_columns = doenca[['PCR_FLUASU', 'PCR_FLUBLI', 'PCR_VSR', 'PCR_SARS2', 'PCR_PARA1', 'PCR_PARA2', 'PCR_PARA3', 'PCR_PARA4', 'PCR_ADENO', 'PCR_METAP', 'PCR_BOCA', 'PCR_RINO', 'PCR_OUTRO']]

    # rename the columns to 'influenza_A','influenza_B','VSR','SarsCov2','Parainfluenza_1','Parainfluenza_2','Parainfluenza_3','Parainfluenza_4','Adenovirus','Metapneumovirus','Bocavirus','Rinovirus','Outro_virus'
    doenca_columns.rename(columns={'PCR_FLUASU': 'influenza_A', 'PCR_FLUBLI': 'influenza_B', 'PCR_VSR': 'VSR', 'PCR_SARS2': 'SarsCov2', 'PCR_PARA1': 'Parainfluenza_1', 'PCR_PARA2': 'Parainfluenza_2', 'PCR_PARA3': 'Parainfluenza_3', 'PCR_PARA4': 'Parainfluenza_4', 'PCR_ADENO': 'Adenovirus', 'PCR_METAP': 'Metapneumovirus', 'PCR_BOCA': 'Bocavirus', 'PCR_RINO': 'Rinovirus', 'PCR_OUTRO': 'Outro_virus'}, inplace=True)

    doenca_columns.to_csv('doencas_columns.csv', sep=',', index=False)

def formatar_colunas():
    # using pandas, change all void values to 0
    doenca_columns = pd.read_csv('doencas_columns.csv', sep=',', on_bad_lines='skip', low_memory=False)
    doenca_columns.fillna(0, inplace=True)
    
    # replace all values 2, 3, 4, 5, 6 to 1
    doenca_columns.replace(2, 1, inplace=True)
    doenca_columns.replace(3, 1, inplace=True)
    doenca_columns.replace(4, 1, inplace=True)
    doenca_columns.replace(5, 1, inplace=True)
    doenca_columns.replace(6, 1, inplace=True)
    
    doenca_columns.to_csv('doencas_columns.csv', sep=',', index=False)

def main():
    # get_doencas_columns()
    formatar_colunas()

    pass

if __name__ == '__main__':
    main()