import matplotlib.pyplot as plt

# Função para calcular as coordenadas dos pontos do quadrilátero


def calculate_coordinates(laterals):
    # Ponto A (0, 0) - ponto de referência
    A = (0, 0)

    # Ponto B é calculado a partir da distância da lateral A (horizontal)
    B = (laterals[0], 0)  # lateral A (superior)

    # Ponto C é calculado a partir da lateral C (inferior) e
    # lateral B (direita)

    # A lateral C vai mover o ponto C para baixo, enquanto a
    # coordenada X de C é igual a de B.
    C_x = laterals[2]
    # A lateral B move o ponto C para baixo (eixo y negativo)
    C_y = -laterals[1]

    # Ponto D é calculado a partir da lateral D (esquerda) e lateral A
    D_x = 0  # O ponto D está alinhado verticalmente com A
    # A lateral D move o ponto D para baixo (eixo y negativo)
    D_y = -laterals[3]

    # Retorna as coordenadas de todos os pontos (A, B, C, D)
    return A, B, (C_x, C_y), (D_x, D_y)

# Função para desenhar o quadrilátero no gráfico


def plot_quadrilateral(laterals, area):
    # Obtém as coordenadas dos pontos do quadrilátero
    points = calculate_coordinates(laterals)

    # Desenha o quadrilátero conectando os pontos e fechando o desenho
    # Fechar o quadrilátero ao adicionar o primeiro ponto novamente
    x, y = zip(*list(points) + [points[0]])
    # Desenha as linhas entre os pontos
    plt.plot(x, y, marker='o', linestyle='-', color="blue")

    # Adiciona rótulos nos pontos A, B, C, D para identificação
    labels = ['A', 'B', 'C', 'D']
    for i, (px, py) in enumerate(points):
        # Coordenadas dos pontos
        plt.text(px, py, f"{labels[i]} ({px:.1f}, {
                    py:.1f})", fontsize=9, color='red')

    # Adiciona as medidas das laterais no meio de cada lado do quadrilátero
    for i, (lateral, p1, p2) in enumerate(
            zip(laterals, points, list(points[1:]) + [points[0]])):
        # Calcula o ponto médio entre os dois pontos
        mid_x = (p1[0] + p2[0]) / 2
        mid_y = (p1[1] + p2[1]) / 2
        # Exibe o valor da lateral no meio do segmento
        plt.text(mid_x, mid_y, f"{lateral:.2f}", fontsize=9, color='green')

    # Exibe a área calculada no título do gráfico
    plt.title(f"Quadrilátero\nÁrea: {area:.2f}")
    plt.grid()  # Adiciona a grade no gráfico
    plt.axis('equal')  # Garante que o gráfico seja escalado corretamente
    plt.show()  # Exibe o gráfico gerado

# Função para calcular a área do quadrilátero


def calculate_area(laterals):
    # Obtém as coordenadas dos pontos do quadrilátero
    A, B, C, D = calculate_coordinates(laterals)

    # A fórmula usada é a de área de um trapézio (superior e
    # inferior paralelos)

    # A fórmula assume que as linhas superiores e inferiores são paralelas
    area = 0.5 * (laterals[0] + laterals[2]) * abs(D[1] - A[1])
    return area  # Retorna o valor da área calculada

# Função principal que gerencia a entrada do usuário e controla o
# fluxo do programa


def main():
    print("Bem-vindo ao programa de cálculo de quadriláteros!")

    # Coleta as medidas das 4 laterais fornecidas pelo usuário
    # Lateral superior
    lateral_A = float(input("Informe a distância da lateral A (superior): "))
    # Lateral direita
    lateral_B = float(input("Informe a distância da lateral B (direita): "))
    # Lateral inferior
    lateral_C = float(input("Informe a distância da lateral C (inferior): "))
    # Lateral esquerda
    lateral_D = float(input("Informe a distância da lateral D (esquerda): "))

    # Armazena as medidas das laterais em uma lista
    laterals = [lateral_A, lateral_B, lateral_C, lateral_D]

    # Calcula a área com base nas laterais fornecidas
    area = calculate_area(laterals)

    # Exibe as medidas informadas e a área calculada
    print("\nMedidas informadas:")
    for i, lateral in enumerate(laterals, 1):
        print(f"Lateral {i}: {lateral:.2f}")

    print(f"Área aproximada: {area:.2f}")

    # Chama a função para desenhar o quadrilátero com as laterais e a área
    plot_quadrilateral(laterals, area)


# Verifica se o script é executado diretamente e chama a função principal
if __name__ == "__main__":
    main()
