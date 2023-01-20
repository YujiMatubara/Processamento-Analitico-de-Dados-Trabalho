import pandas as pd

def create_doenca():
    # Using pandas, create a csv with column index and column doenca using the given vector
    doenca = ["Nao_doente","influenza_A","influenza_B","VSR","SarsCov2","Parainfluenza_1","Parainfluenza_2","Parainfluenza_3","Parainfluenza_4","Adenovirus","Metapneumovirus","Bocavirus","Rinovirus","Outro_virus"]
    df = pd.DataFrame(data=doenca, columns=['doenca'])
    df.index.name = 'pkDoenca'
    df.to_csv('doencas.csv', index=True, header=True)

def main():
    create_doenca()


if __name__ == '__main__':
    main()
