"""""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até
 que um valor correto seja preenchido.
"""
def calcular_idade():
    while True:
        try:
          
            nome = input("Digite seu nome completo: ").strip()

           
            ano_nascimento = int(input("Digite o ano de nascimento: "))

          
            if 1922 <= ano_nascimento <= 2021:
               
                idade = 2022 - ano_nascimento
                print(f"\n{nome}, você completou ou completará {idade} anos em 2022.")
                break
            else:
                print("Erro: O ano de nascimento deve estar entre 1922 e 2021. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, digite um número válido para o ano de nascimento.")

# Executar o programa
calcular_idade()
