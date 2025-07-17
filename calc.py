# 1. Módulo de Lógica: Funções para cada operação
# Cada função tem uma única responsabilidade: calcular.
def somar(n1, n2):
    """Retorna a soma de dois números."""
    return n1 + n2

def subtrair(n1, n2):
    """Retorna a diferença entre dois números."""
    return n1 - n2

def multiplicar(n1, n2):
    """Retorna o produto de dois números."""
    return n1 * n2

def dividir(n1, n2):
    """Retorna a divisão de dois números. Retorna None se a divisão por zero ocorrer."""
    if n2 == 0:
        print("Erro: Divisão por zero não é permitida.")
        return None
    return n1 / n2

# 2. Módulo de Controle: Lógica principal e interação com o usuário
def calculadora():
    """Função principal que gerencia a calculadora."""
    
    # 3. Despacho de Operações via Dicionário
    # Mapeia o símbolo da operação para a função correspondente.
    # Elegante, legível e escalável.
    operacoes = {
        '+': somar,
        '-': subtrair,
        '*': multiplicar,
        '/': dividir
    }

    print("Calculadora Simples em Python")
    print("Operações disponíveis: " + " ".join(operacoes.keys()))
    
    # 4. Interação com o Usuário (Interface de Linha de Comando)
    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")
        return

    # Verifica se o operador é válido
    if operador not in operacoes:
        print("Erro: Operação inválida.")
        return

    # Busca a função no dicionário e a executa
    funcao_calculo = operacoes[operador]
    resultado = funcao_calculo(num1, num2)

    # Exibe o resultado apenas se o cálculo foi bem-sucedido
    if resultado is not None:
        print(f"O resultado de {num1} {operador} {num2} é: {resultado}")


# 5. Ponto de Entrada do Script
# Este código só roda quando o arquivo é executado diretamente.
if __name__ == "__main__":
    calculadora()