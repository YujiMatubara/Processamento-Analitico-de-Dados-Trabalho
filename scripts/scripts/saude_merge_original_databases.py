import pandas as pd

def concat_dataBases():

    # using pandas, open the following files: INFLUD21-11-07-2022.csv and INFLUD22-11-07-2022.csv and concatenate them and save to a new csv
    influd21 = pd.read_csv('INFLUD21-11-07-2022.csv', low_memory=False, on_bad_lines='skip', sep=';')
    influd22 = pd.read_csv('INFLUD22-11-07-2022.csv', low_memory=False, on_bad_lines='skip', sep=';')
    influd = pd.concat([influd21, influd22])
    influd.to_csv('influd.csv', index=False)

    pass

def main():

    concat_dataBases()

    pass

if __name__ == '__main__':
    main()