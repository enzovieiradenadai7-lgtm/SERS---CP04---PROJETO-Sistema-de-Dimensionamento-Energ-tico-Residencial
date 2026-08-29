nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")
area = input("Quantos m² tem sua casa? ")
moradores = int(input("Quantas pessoas moram na casa? "))
valor_kwh = float(input("Digite o valor do kWh: R$ "))

equipamentos = {
    1: ("Geladeira", "Cozinha", 150),
    2: ("Chuveiro Elétrico", "Banheiro", 5500),
    3: ("TV", "Sala", 100),
    4: ("Ar-condicionado", "Quarto", 900),
    5: ("Computador", "Escritório", 200),
    6: ("Lâmpada LED", "Iluminação", 9),
    7: ("Máquina de Lavar", "Lavanderia", 500),
    8: ("Micro-ondas", "Cozinha", 1200)
}

print("\nEquipamentos disponíveis:")

for codigo in equipamentos:
    print(codigo, equipamentos[codigo][0], equipamentos[codigo][2])

consumo_total = 0
continuar = "s"

while continuar == "s":

    codigo = int(input("\nDigite o código do equipamento: "))

    nome_equipamento = equipamentos[codigo][0]
    potencia = equipamentos[codigo][2]

    quantidade = int(input("Quantidade: "))
    horas = float(input("Horas de uso por dia: "))

    consumo = potencia * quantidade * horas * 30 / 1000

    consumo_total = consumo_total + consumo

    print("Consumo de", nome_equipamento, ":", round(consumo, 2), "kWh/mês")

    continuar = input("Adicionar outro equipamento? (s/n): ")

print("\nConsumo total:", round(consumo_total, 2), "kWh/mês")

custo = consumo_total * valor_kwh

print("Custo total: R$", round(custo, 2))