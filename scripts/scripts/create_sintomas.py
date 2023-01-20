import pandas as pd

def create_sintomas():
    possible_sintomas: list = ["Nao_sintoma","Nosocomial","Febre","Tosse","Garganta","Dispneia","Desconforto_respiratorio","Saturacao","Diarreia","Vomito","Dor_abdominal","Fadiga","Perda_de_olfato","Perda_do_paladar"]

    # Using pandas and the given list, create a indexed csv file with the sintomas as a column
    df = pd.DataFrame(possible_sintomas, columns=['Sintomas'])
    
    df.index.name = 'pkSintoma'

    # Add index to the header
    df.to_csv('sintomas.csv', index=True, header=True)

    
    


def main():
    create_sintomas()


if __name__ == '__main__':
    main()