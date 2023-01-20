import pandas as pd

def drop_columns():
    # Using pandas, open stations.csv and drop the columns "first date","height","longitude","latitude" save the result as stations_clean.csv
    stations = pd.read_csv('stations.csv')
    stations.drop(columns=['first date', 'height', 'longitude', 'latitude'], inplace=True)
    stations.to_csv('stations_clean.csv', index=False)

def add_index_column():
    # Using pandas, open stations_clean.csv and add an index column called "index" save the result as stations_clean_index.csv
    stations = pd.read_csv('stations_clean.csv')
    stations.index = stations.index + 1

    #add index tag to header
    stations.index.name = 'index'
    stations.to_csv('stations_clean_index.csv', index=True)

def add_pais_column():
    # Using pandas, add a new column Pais with the value "BRA" to stations_clean_index.csv save the result as stations_clean_index_pais.csv
    stations = pd.read_csv('stations_clean_index.csv')
    stations['Pais'] = 'BRA'
    stations.to_csv('stations_clean_index_pais.csv', index=False)




def main():
    # drop_columns()
    #add_index_column()
    add_pais_column()


if __name__ == '__main__':
    main()
    # print('This program is being run by itself')
else:
    pass
