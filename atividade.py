import math

def verificar_triangulo():
    a = int(input("Lado A: "))
    b = int(input("Lado B: "))
    c = int(input("Lado C: "))
    if (abs(b-c) < a < b+c) and (abs(a-c) < b < a+c) and (abs(a-b) < c < a+b):
        if a == b == c:
            print("Triângulo equilátero")
        elif a == b or a == c or b == c:
            print("Triângulo isósceles")
        else:
            print("Triângulo escaleno")
    else:
        print("Não é um triângulo")

def calcular_equacao_segundo_grau():
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))
    if a == 0:
        print("Não é equação do segundo grau.")
        return
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não possui raízes reais.")
    elif delta == 0:
        print("Uma raiz:", -b/(2*a))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Raízes:", x1, "e", x2)

def conferir_data():
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    if mes not in range(1, 13):
        print("Data incorreta")
        return
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print("Data correta" if 1 <= dia <= dias[mes-1] else "Data incorreta")

def verificar_tamanho_texto():
    texto = input("Digite um texto: ")
    tamanho = len(texto)
    if tamanho < 5:
        print("Texto muito pequeno")
    elif tamanho < 15:
        print("Texto de tamanho médio")
    elif tamanho <= 20:
        print("Texto é grande")
    else:
        print("Texto inválido")

def analisar_cpf():
    cpf = input("CPF (somente números): ")
    print("CPF válido" if cpf.isdigit() and len(cpf) == 11 else "CPF inválido")

def contar_caracteres():
    texto = input("Digite um texto: ")
    vogais = sum(1 for c in texto if c.lower() in "aeiou")
    espacos = texto.count(" ")
    outros = len(texto) - vogais - espacos
    print("Vogais:", vogais, "\nEspaços:", espacos, "\nOutros:", outros)

def main():
    menu = (
        "Olá, Eduardo!\n"
        "Digite a opção desejada:\n"
        "1) Verificar triângulo\n"
        "2) Calcular equação do segundo grau\n"
        "3) Conferir data\n"
        "4) Verificar tamanho do texto\n"
        "5) Analisar CPF\n"
        "6) Contar caracteres\n"
        "7) Sair\n"
    )
    opcao = input(menu + "Opção: ")
    opcoes = {
        "1": verificar_triangulo,
        "2": calcular_equacao_segundo_grau,
        "3": conferir_data,
        "4": verificar_tamanho_texto,
        "5": analisar_cpf,
        "6": contar_caracteres,
        "7": lambda: print("Obrigado por utilizar nosso sistema.")
    }
    if opcao in opcoes:
        opcoes[opcao]()
    else:
        print("Opção inválida. Programa finalizado.")

if __name__ == "__main__":
    main()
