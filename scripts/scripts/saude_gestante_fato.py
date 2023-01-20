import pandas as pd

def get_gestante_column():
    # using pandas, open saude_dataframe.csv, copy the column 'CS_GESTANT' and save the result in a new csv file called gestanteFATO.csv
    saude_dataframe = pd.read_csv('saude_dataframe.csv', sep=',', on_bad_lines='skip', low_memory=False)
    gestanteFATO = saude_dataframe['CS_GESTANT']

    gestanteFATO.to_csv('gestanteFATO.csv', sep=',', index=False)

    pass

def formatar_gestante_column():
    # using pandas, open gestanteFATO.csv and replace [1,2,3,4] with 1 and [5,6,9] with 0 and save the result in a new csv file called gestanteFATO.csv
    gestanteFATO = pd.read_csv('gestanteFATO.csv', sep=',', on_bad_lines='skip', low_memory=False)
    
    gestanteFATO.replace([1,2,3,4], 1, inplace=True)
    gestanteFATO.replace([5,6,9], 0, inplace=True)
    
    #rename the column 'CS_GESTANT' to 'Gestante'
    gestanteFATO.rename(columns={'CS_GESTANT': 'Gestante'}, inplace=True)

    gestanteFATO.to_csv('gestanteFATO.csv', sep=',', index=False)

def main():

    get_gestante_column()
    formatar_gestante_column()

    pass

if __name__ == '__main__':
    main()