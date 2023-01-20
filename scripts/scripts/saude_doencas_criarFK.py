import pandas as pd

def merge_csv():
    # using pandas, merge doencas_columns.csv and doencas_grupo.csv on the following columns: "influenza_A","influenza_B","VSR","SarsCov2","Parainfluenza_1","Parainfluenza_2","Parainfluenza_3","Parainfluenza_4","Adenovirus","Metapneumovirus","Bocavirus","Rinovirus","Outro_virus" and save the result to a new csv file called doencasFK.csv
    df = pd.read_csv('doencas_columns.csv')
    df2 = pd.read_csv('doencas_grupo.csv')
    df3 = df.merge(df2, on=["influenza_A","influenza_B","VSR","SarsCov2","Parainfluenza_1","Parainfluenza_2","Parainfluenza_3","Parainfluenza_4","Adenovirus","Metapneumovirus","Bocavirus","Rinovirus","Outro_virus"], how='left', sort=False)
    df3.to_csv('doencasFK.csv', index=False)

def drop_all_doencas_columns():
    #using pandas, open doencasFK.csv, drop the following columns: "influenza_A","influenza_B","VSR","SarsCov2","Parainfluenza_1","Parainfluenza_2","Parainfluenza_3","Parainfluenza_4","Adenovirus","Metapneumovirus","Bocavirus","Rinovirus","Outro_virus" and save the result to a new csv file called doencasFK.csv
    df = pd.read_csv('doencasFK.csv')
    df.drop(columns=["influenza_A","influenza_B","VSR","SarsCov2","Parainfluenza_1","Parainfluenza_2","Parainfluenza_3","Parainfluenza_4","Adenovirus","Metapneumovirus","Bocavirus","Rinovirus","Outro_virus"], inplace=True)
    df.to_csv('doencasFK.csv', index=False)
    pass


def main():

    # merge_csv()
    drop_all_doencas_columns()
    pass

if __name__ == '__main__':
    main()