from datetime import date

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    return ano_atual - ano_nascimento

def classificar_idade(idade):
    if idade < 10:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 65:
        return "Adulto"
    else:
        return "Sénior"

def pedir_ano_nascimento():
    while True:
        try:
            ano = int(input("Introduza o seu ano de nascimento: "))
            ano_atual = date.today().year

            if ano <= 0 or ano > ano_atual:
                print("Ano inválido. Tente novamente.")
            else:
                return ano

        except ValueError:
            print("Erro: deve inserir um número válido.")

def main():
    while True:
        ano_nasc = pedir_ano_nascimento()
        idade = calcular_idade(ano_nasc)
        categoria = classificar_idade(idade)

        print(f"\nTem {idade} anos.")
        print(f"Classificação: {categoria}\n")

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Programa terminado. Obrigado!")
            break

if __name__ == "__main__":
    main()
