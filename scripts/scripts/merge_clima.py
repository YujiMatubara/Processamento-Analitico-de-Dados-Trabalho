import pandas as pd

def merge_datasets():
    # Using pandas, concatenate below the datasets of norte.csv, sul.csv, sudeste.csv, nordeste.csv and centroeste.csv and merge estacoes.csv based on the region, station and state columns and save to a new csv
    norte = pd.read_csv('norte.csv')
    sul = pd.read_csv('sul.csv')
    sudeste = pd.read_csv('sudeste.csv')
    nordeste = pd.read_csv('nordeste.csv')
    centroeste = pd.read_csv('centroeste.csv')

    estacoes = pd.read_csv('estacoes.csv')
    
    norte = norte.merge(estacoes, on=['region', 'station', 'state'])
    sul = sul.merge(estacoes, on=['region', 'station', 'state'])
    sudeste = sudeste.merge(estacoes, on=['region', 'station', 'state'])
    nordeste = nordeste.merge(estacoes, on=['region', 'station', 'state'])
    centroeste = centroeste.merge(estacoes, on=['region', 'station', 'state'])

    # Concatenate the 5 datasets
    todas_estacoes = pd.concat([norte, sul, sudeste, nordeste, centroeste])
    todas_estacoes.to_csv('todas_estacoes.csv', index=False)


    
    
def drop_columns():
    # Using pandas, drop the following columns: station_code, Pais, state, region, station
    todas_estacoes = pd.read_csv('todas_estacoes.csv')
    todas_estacoes.drop(['station_code', 'Pais', 'state', 'region', 'station'], axis=1, inplace=True)
    todas_estacoes.to_csv('todas_estacoes.csv', index=False)


def main():
    merge_datasets()
    drop_columns()

    pass


if __name__ == '__main__':
    main()