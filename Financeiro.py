# Login e Cadastro de Usuário

TemCadastro = input("Você já possui cadastro? (sim/não): ").strip().lower()
if TemCadastro == 'sim':
    usuario_cpf = input("Digite o cpf para login: ")
    senha = input("Digite sua senha: ")
    # Aqui você pode adicionar a lógica para verificar o usuário e senha no banco de dados
    print(f"Bem-vindo de volta, {usuario_cpf}!")
else:
    cpf = input("Digite seu CPF para cadastro: ")
    usuario = input("Digite um nome de usuário para cadastro: ")
    senha = input("Digite uma senha para cadastro: ")
    # Aqui você pode adicionar a lógica para salvar o novo usuário e senha no banco de dados
    print(f"Cadastro realizado com sucesso! Bem-vindo, {usuario}!")

# Quantidade de moradores
# Para cadastro de moradores, devemos solicitar a quantidade de moradores na residencia. onde solicitaremos nome, cpf, idade, salario e gastos, serão sempre as mesma perguntas para cada morador, e no final do cadastro de moradores, devemos calcular a soma dos salários e gastos de todos os moradores, e exibir o resultado na tela.

Quantidade_moradores = int(
    input("Digite a quantidade de moradores na residência: "))
if Quantidade_moradores > 0:
    soma_salarios = 0
    soma_gastos = 0
    for i in range(Quantidade_moradores):
        print(f"\nCadastro do morador {i + 1}:")
        parentesco = input(
            "Digite o parentesco do morador (ex: pai, mãe, filho, etc.): ")
        nome = input(f"Digite o nome do {parentesco}: ")
        cpf = input(f"Digite o CPF do {nome}: ")
        idade = int(input(f"Digite a idade do {nome}: "))
        salario = float(input(f"Digite o salário do {nome}: "))
        gastos = float(input(f"Digite os gastos do {nome}: "))

        soma_salarios += salario
        soma_gastos += gastos

    saldo_final = soma_salarios - soma_gastos

    print("\nResumo Financeiro da Residência:")
    print(
        f"\nA soma dos salários de todos os moradores é: R$ {soma_salarios:.2f}")
    print(f"A soma dos gastos de todos os moradores é: R$ {soma_gastos:.2f}")
    print(f"\nO saldo final dos moradores é: R$ {saldo_final:.2f}")

    if saldo_final > 0:
        print(f"O saldo final da residência é positivo: R$ {saldo_final:.2f}")
    elif saldo_final == 0:
        print(f"O saldo final da residência é neutro: R$ {saldo_final:.2f}")
    else:
        print(f"O saldo final da residência é negativo: R$ {saldo_final:.2f}")

# Definição de ganhos
Trabalho = input("Trabalha registrado? (CLT) (sim/não): ").strip().lower()
if Trabalho == 'sim':
    salario_mensal = float(input("Digite o valor do seu salário mensal: "))
elif Trabalho == 'não':
    autônomo = input("Trabalha como autônomo? (sim/não): ").strip().lower()
    if autônomo == 'sim':
        salario_mensal = float(input("Digite o valor do seu salário mensal: "))
    else:
        salario_mensal = 0
else:
    salario_mensal = 0

Renda_Extra = input(
    'Realiza alguma trabalho  como renda extra como freelancers, venda de produtos, serviço de entregas e entre outros? (sim/não): ').strip().lower()
if Renda_Extra == 'sim':
    renda_extra_mensal = float(
        input("Digite o valor da sua renda extra mensal: "))
else:
    renda_extra_mensal = 0

Renda_Passiva = input(
    'Possui alguma renda passiva como investimentos, alugueis, royalties e entre outros? (sim/não): ').strip().lower()
if Renda_Passiva == 'sim':
    renda_passiva_mensal = float(
        input("Digite o valor da sua renda passiva mensal: "))
else:
    renda_passiva_mensal = 0

ganhos_totais = salario_mensal + renda_extra_mensal + renda_passiva_mensal
print(f"\nO total de ganhos mensais é: R$ {ganhos_totais:.2f}")

# Definição de gastos
# Para definir os gastos, podemos criar uma função que solicita ao usuário os tipos de gastos que ele deseja registrar, como alimentação, transporte, lazer, entre outros. Em seguida, podemos calcular o total de gastos e exibir o resultado na tela.

# Gastos de alimentação
Possui_Beneficio = input(
    "Você possui benefício de alimentação? (sim/não): ").strip().lower()
if Possui_Beneficio == 'sim':
    Beneficio_alimentacao = float(
        input("Digite o valor do benefício de alimentação: "))
else:
    Beneficio_alimentacao = 0

saldo_alimentacao = Beneficio_alimentacao
print(f"\nO saldo disponível para alimentação é: R$ {saldo_alimentacao:.2f}")
# Alimentação Essencial (Consumo em casa)
Gastos_Mercado = input(
    'Realiza compras no mercados? (sim/não): ').strip().lower()
if Gastos_Mercado == 'sim':
    valor_gasto_mercado = float(
        input("Digite o valor gasto em compras no mercado ou aplicativos: "))
else:
    valor_gasto_mercado = 0

# Gastos delivery (Fast-food)
gastos_delivery = input(
    'Realiza pedidos em delivery? (sim/não): ').strip().lower()
if gastos_delivery == 'sim':
    valor_gasto_delivery = float(
        input("Digite o valor gasto em pedidos de delivery: "))
else:
    valor_gasto_delivery = 0

Gastos_Alimentação = valor_gasto_mercado + \
    valor_gasto_delivery - saldo_alimentacao
print(f"\nO total de gastos com alimentação é: R$ {Gastos_Alimentação:.2f}")

# Gastos de transporte
Possui_Beneficio_Transporte = input(
    "Você possui benefício de transporte? (sim/não): ").strip().lower()
if Possui_Beneficio_Transporte == 'sim':
    Beneficio_transporte = float(
        input("Digite o valor do benefício de transporte: "))
else:
    Beneficio_transporte = 0

Possui_Veiculo = input(
    "Você possui veículo próprio? (sim/não): ").strip().lower()
if Possui_Veiculo == 'sim':
    valor_gasto_veiculo = float(input(
        "Digite o valor gasto com seu veiculo (gasolina, manutenção, seguro e entre outros): "))
else:
    valor_gasto_veiculo = 0

Possui_Transporta_Aplicativo = input(
    "Você utiliza transporte por aplicativo? (sim/não): ").strip().lower()
if Possui_Transporta_Aplicativo == 'sim':
    valor_gasto_transporte_aplicativo = float(
        input("Digite o valor gasto com transporte por aplicativo: "))
else:
    valor_gasto_transporte_aplicativo = 0

saldo_transposte_total = Beneficio_transporte - \
    (valor_gasto_veiculo + valor_gasto_transporte_aplicativo)
print(
    f"\nO saldo disponível para transporte é: R$ {saldo_transposte_total:.2f}")

# Gastos de residencial
Residencia = input(
    'Você possui residência própria ou alugada? (própria/alugada): ').strip().lower()
if Residencia == 'alugada':
    valor_gasto_aluguel = float(input("Digite o valor gasto com aluguel: "))
condominio_iptu = float(
    input('Qual é o valor gasto com condomínio e IPTU? (Digite 0 se não houver): '))

contas_residencial_luz = float(
    input('Qual é o valor gasto com conta de luz? (Digite 0 se não houver): '))
contas_residencia_agua = float(
    input('Qual é o valor gasto com conta de água? (Digite 0 se não houver): '))
contas_residencia_internet = float(
    input('Qual é o valor gasto com conta de internet? (Digite 0 se não houver): '))
contas_residencia_telefone = float(
    input('Qual é o valor gasto com conta de telefone? (Digite 0 se não houver): '))
contas_residencia_outros = float(input(
    'Qual é o valor gasto com outras contas residenciais? (Digite 0 se não houver): '))

gastos_residencial_total = valor_gasto_aluguel + condominio_iptu + contas_residencial_luz + \
    contas_residencia_agua + contas_residencia_internet + \
    contas_residencia_telefone + contas_residencia_outros
print(
    f"\nO total de gastos com residência é: R$ {gastos_residencial_total:.2f}")

# gastos de lazer e estilo de vida

servicos_de_streaming = input(
    'Você possui serviços de streaming (Netflix, Spotify, etc.)? (sim/não): ').strip().lower()
if servicos_de_streaming == 'sim':
    valor_gasto_streaming = float(
        input("Digite o valor gasto com serviços de streaming: "))
else:
    valor_gasto_streaming = 0

hobbies_e_esportes = input(
    'Você possui hobbies ou pratica esportes que geram gastos? (sim/não): ').strip().lower()
if hobbies_e_esportes == 'sim':
    valor_gasto_hobbies = float(
        input("Digite o valor gasto com hobbies e esportes: "))
else:
    valor_gasto_hobbies = 0

Cuidados_pessoais = input(
    'Você possui gastos com cuidados pessoais (cabeleireiro, estética, etc.)? (sim/não): ').strip().lower()
if Cuidados_pessoais == 'sim':
    valor_gasto_cuidados_pessoais = float(
        input("Digite o valor gasto com cuidados pessoais: "))
else:
    valor_gasto_cuidados_pessoais = 0

viagens_e_passeios = input(
    'Você possui gastos com viagens e passeios? (sim/não): ').strip().lower()
if viagens_e_passeios == 'sim':
    valor_gasto_viagens = float(
        input("Digite o valor gasto com viagens e passeios: "))
else:
    valor_gasto_viagens = 0

Gastos_Lazer_Estilo_Vida = valor_gasto_streaming + valor_gasto_hobbies + \
    valor_gasto_cuidados_pessoais + valor_gasto_viagens
print(
    f"\nO total de gastos com lazer e estilo de vida é: R$ {Gastos_Lazer_Estilo_Vida:.2f}")
