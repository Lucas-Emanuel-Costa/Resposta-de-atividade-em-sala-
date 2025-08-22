pessoas = []

for i in range(15):
    print(f"\nPessoa {i + 1}")

    while True:
        try:
            altura = float(input("Informe sua altura (em metros): "))
            if altura <= 0:
                print("Altura deve ser um número positivo. Tente novamente.")
                continue
            if altura > 3:
                print("Altura inválida! 3 metros é a altura máxima do ser humano. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número válido para a altura.")
    
    while True:
        sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().upper()
        if sexo in ['M', 'F']:
            break
        else:
            print("Entrada inválida. Por favor, digite apenas M ou F.")

    pessoa = {
        'altura': altura,
        'sexo': sexo
    }
    pessoas.append(pessoa)


print("\n=== DADOS COLETADOS ===")
for i, pessoa in enumerate(pessoas, start=1):
    sexo_extenso = 'Masculino' if pessoa['sexo'] == 'M' else 'Feminino'
    print(f"{i}. Altura: {pessoa['altura']:.2f} m | Sexo: {sexo_extenso}")


menor_altura = min(pessoas, key=lambda x: x['altura'])['altura']
maior_altura = max(pessoas, key=lambda x: x['altura'])['altura']


homens = [p for p in pessoas if p['sexo'] == 'M']
if homens:
    soma_alturas = sum(p['altura'] for p in homens)
    media_masculina = soma_alturas / len(homens)
else:
    media_masculina = None

quantidade_feminino = sum(1 for p in pessoas if p['sexo'] == 'F')


print("\n=== RESUMO FINAL ===")
print(f"Total de pessoas: {len(pessoas)}")
print(f"Número de homens: {len(homens)}")
print(f"Número de mulheres: {quantidade_feminino}")
print(f"Menor altura: {menor_altura:.2f} m")
print(f"Maior altura: {maior_altura:.2f} m")
if media_masculina is not None:
    print(f"Média de altura dos homens: {media_masculina:.2f} m")
else:
    print("Nenhum homem registrado para calcular a média de altura.")