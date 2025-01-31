import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split



def input_subSpecie(model):
    sub_specie_translation = {
    'Pygmy three-toed sloth': "Preguiça-anã",
    'Maned three-toed sloth': "Preguiça-de-coleira",
    'Pale-throated sloth': "Preguiça-de-bentinho",
    'Brown-throated sloth': "Preguiça-comum",
    'Linnaeus’s two-toed sloth': "Preguiça-real",
    'Hoffman’s two-toed sloth': "Preguiça-de-Hoffmann"
}

    claw_length_cm = float(input("Largura da garra (cm): "))#[1.75 - 12.2 cm]
    size_cm = float(input("Tamanho (cm): "))#[46.9 - 68.8 cm]
    while True:
            specie = int(input("Espécie \n[1]- Três Dedos \n[2]- Dois dedos\n"))
            if specie == 1 or specie == 2:
                break
            else:
                print("Opção inválida. Por favor, escolha 1 ou 2.")
    tail_length_cm = float(input("Tamanho da cauda (cm): ")) #[-2.94 - 8.54 cm]
    weight_kg = float(input("Peso (kg): "))#[0.95 - 10kg]

    df_usuario = pd.DataFrame({
        'claw_length_cm': [claw_length_cm],
        'size_cm': [size_cm],
        'specie': [specie],
        'tail_length_cm': [tail_length_cm],
        'weight_kg': [weight_kg]
    })

    sub_specie_prediction = model.predict(df_usuario)
    sub_specie_name = sub_specie_prediction[0]

      # Traduzir o nome da subespécie
    sub_specie_name_translated = sub_specie_translation.get(sub_specie_name, sub_specie_name)

    print("\nSua Subespécie foi:", sub_specie_name_translated)


def sub_species_distribution(df):
    sub_specie_translation = {
    'Pygmy three-toed sloth': "Preguiça-anã",
    'Maned three-toed sloth': "Preguiça-de-coleira",
    'Pale-throated sloth': "Preguiça-de-bentinho",
    'Brown-throated sloth': "Preguiça-comum",
    'Linnaeus’s two-toed sloth': "Preguiça-real",
    'Hoffman’s two-toed sloth': "Preguiça-de-Hoffmann"
}
    df['sub_specie'] = df['sub_specie'].map(sub_specie_translation)

    # Contagem de subespécies para preguiças de dois e três dedos
    dois_dedos = df[df['specie'] == 2]['sub_specie'].value_counts().sort_index()
    tres_dedos = df[df['specie'] == 1]['sub_specie'].value_counts().sort_index()

    # Combinar as contagens em um único DataFrame // reordenar as colunas para que 'Dois Dedos' venha primeiro
    counts = pd.DataFrame({'Dois Dedos': dois_dedos, 'Três Dedos': tres_dedos})[['Dois Dedos', 'Três Dedos']]

    ordered_index = [
        "Preguiça-de-Hoffmann", "Preguiça-real",  # Dois Dedos
        "Preguiça-de-bentinho", "Preguiça-comum", "Preguiça-de-coleira", "Preguiça-anã"  # Três Dedos
    ]
    counts = counts.reindex(ordered_index)

    # Plotar o gráfico de barras lado a lado
    counts.plot(kind='bar', figsize=(8, 5), color = ['#672aff','#ff3535'])

    plt.title('Distribuição das Subespécies nas Preguiças de Dois e Três Dedos')
    plt.xlabel('Subespécie')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Tipo de Preguiça')

    plt.tight_layout()
    plt.show()

def dispersion_species(df):
    species_names = {1: 'Três dedos', 2: 'Dois dedos'}
    df['specie'] = df['specie'].map(species_names)

    sns.set_palette("deep")

    sns.scatterplot(x='size_cm', y='weight_kg', hue='specie',palette = ['#ebd1cc','#6e6177'], data=df)
    plt.title('Relação entre Tamanho e Peso por Espécie')
    plt.xlabel('Tamanho (cm)')
    plt.ylabel('Peso (kg)')

    plt.legend(title='Espécies')

    plt.show()

def dispersion_subspecies(df):

    sub_specie_translation = {
    'Pygmy three-toed sloth': "Preguiça-anã",
    'Maned three-toed sloth': "Preguiça-de-coleira",
    'Pale-throated sloth': "Preguiça-de-bentinho",
    'Brown-throated sloth': "Preguiça-comum",
    'Linnaeus’s two-toed sloth': "Preguiça-real",
    'Hoffman’s two-toed sloth': "Preguiça-de-Hoffmann"
}

    df['sub_specie'] = df['sub_specie'].map(sub_specie_translation)
    sns.scatterplot(x='size_cm', y='weight_kg', hue='sub_specie', data=df)
    plt.title('Relação entre Tamanho e Peso por Subespécies')
    plt.xlabel('Tamanho (cm)')
    plt.ylabel('Peso (kg)')
    plt.legend(title='Subespécies')

    plt.show()

def claw_lenght(df):

    df['claw_length_cm'].hist(bins=30)
    plt.title('Distribuição do Comprimento da Garra')
    plt.xlabel('Comprimento da Garra (cm)')
    plt.ylabel('Frequência')
    plt.show()

df = pd.read_csv('sloth_data.csv')
specie_mapping = {name: i for i, name in enumerate(df['specie'].unique(), start=1)}

df['specie'] = df['specie'].map(specie_mapping)

df = df.drop(['index','endangered'], axis=1)
X = df.drop(['sub_specie'],axis=1)
y = df['sub_specie']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)

y_prediction = clf.predict(X_test)


# Interação do usuário
loop = True
while loop:
    print("\n╔════════════════════════════════════════════╗")
    print("║  Identificador de Subespécies de preguiça  ║")
    print("╚════════════════════════════════════════════╝")
    print("\n\n\033[1mDigite a escolha desejada\033[0m")
    user_choice = int(input("\n[1] Descubra o tipo da subespécie de preguiça\n[2] Mostrar Árvore\n[3] Mostrar Acurácia\n[4] Gráficos\n[5] Debugs\n[0] Finalizar consulta\n\n"))

    match user_choice:
        case 1:
            input_subSpecie(clf)
            loop = input("\n\nDeseja fazer outra consulta? (s/n): ").lower() == 's'

        case 2:
            plt.figure(figsize=(20, 16))
            tree.plot_tree(clf, feature_names=X.columns, class_names=y.unique(), filled=True)
            plt.show()

        case 3:
            print("\n\033[1mAcurácia:\033[0m", accuracy_score(y_test, y_prediction))

        case 4:
            while True:
                print("\n\n\033[1mQual gráfico deseja escolher?\033[0m")
                graph_choice = int(input("\n[1] Distribuição de Subespécie\n[2] Dispersão de espécies (tamanho e peso)\n[3] Frequência do comprimento das garras\n[4] Dispersão de Subespécies\n[0] Voltar ao menu principal\n\n"))
                
                match graph_choice:
                    case 1: sub_species_distribution(df)
                    case 2: dispersion_species(df)
                    case 3: claw_lenght(df)
                    case 4: dispersion_subspecies(df)
                    case 0: break
                    case _: print("Escolha inválida. Selecione uma opção válida.")
        
        case 5:
            login, password = input("\nDigite o login: "), input("Digite a senha: ")
            if login == "admin" and password == "admin":
                print("\n\033[1mLogin realizado com sucesso!\033[0m")
                while True:
                    print("\n\n\033[1mO que deseja escolher?\033[0m")
                    debug_choice = int(input("\n[1] Distribuição de treinamento\n[2] Predição da árvore de decisão\n[0] Voltar ao menu principal\n\n"))
                    
                    match debug_choice:
                        case 1:
                            print("\n\033[3mPorcentagem usada em cada coluna para a predição\033[0m")
                            for feature, importance in zip(X.columns, clf.feature_importances_):
                                print(f"{feature}: {importance}")
                        case 2:
                            print("\n\033[3mDados usados para a predição\033[0m")
                            print("\nPrediction for Decision Tree: ", y_prediction)
                        case 0: break
                        case _: print("Escolha inválida. Selecione uma opção válida.")
            else:
                print("\n\033[1mLogin ou senha incorretos, tente novamente...\033[0m")

        case 0:
            loop = False
        
        case _:
            print("Escolha inválida. Selecione uma opção válida.")
