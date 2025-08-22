maior_altura = 0.0
menor_altura = 999.9
soma_altura_masculino = 0.0
soma_altura_feminino = 0.0
qtd_masculino = 0
qtd_feminino = 0

for i in range(1, 6):
    print(f"\nPessoa {i}:")
    altura = input("Digite a altura (em metros, ex: 1.75): ")
    altura1 = float(altura.replace(",", "."))
    genero = input("Digite o gênero (M para masculino e F para feminino): ").upper()

    if altura1 > maior_altura:
        maior_altura = altura1
    if altura1 < menor_altura:
        menor_altura = altura1

    if genero == "M":
        soma_altura_masculino += altura1
        qtd_masculino += 1
    elif genero == "F":
        soma_altura_feminino += altura1
        qtd_feminino += 1
    else:
        print("Gênero inválido, tente novamente.")

# calcular médias após o laço
media_altura_feminino = soma_altura_feminino / qtd_feminino if qtd_feminino > 0 else 0
media_altura_masculino = soma_altura_masculino / qtd_masculino if qtd_masculino > 0 else 0

# impressão final (fora do laço)
print("\n======== Resultados =========")
print(f"Maior altura: {maior_altura:.2f} m")
print(f"Menor altura: {menor_altura:.2f} m")
print(f"Média de altura das mulheres: {media_altura_feminino:.2f} m")
print(f"Média da altura dos homens: {media_altura_masculino:.2f} m")
print(f"Quantidade de mulheres: {qtd_feminino}")
print(f"Quantidade de homens: {qtd_masculino}")
