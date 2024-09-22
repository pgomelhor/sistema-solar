import pygame
import math
from datetime import datetime, timedelta

pygame.init()

largura = 1440
altura = 1024
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sistema Solar")

cor_fundo = (0, 0, 0)
cor_sol = (255, 255, 0)
cor_terra = (0, 0, 255)
cor_mercurio = (200, 200, 200)
cor_venus = (255, 165, 0)
cor_marte = (255, 0, 0)  # Cor para Marte
cor_saturno = (255, 215, 0)  # Cor para Saturno
cor_jupiter = (255, 140, 0)  # Cor para Júpiter
cor_urano = (0, 191, 255)  # Cor para Urano
cor_netuno = (0, 0, 128)  # Cor para Netuno

raio_orbita_terra = 200
raio_orbita_mercurio = 100
raio_orbita_venus = 150
raio_orbita_marte = 250  # Defina o raio da órbita de Marte
raio_orbita_saturno = 350  # Defina o raio da órbita de Saturno
raio_orbita_jupiter = 450  # Defina o raio da órbita de Júpiter
raio_orbita_urano = 550  # Defina o raio da órbita de Urano
raio_orbita_netuno = 650  # Defina o raio da órbita de Netuno

angulo_terra = 0
angulo_mercurio = 0
angulo_venus = 0
angulo_marte = 0
angulo_saturno = 0
angulo_jupiter = 0
angulo_urano = 0
angulo_netuno = 0

# Variável para controlar o tempo de translação (em meses)
tempo_translacao_meses = 0
meses_por_volta = 12

# Fator de conversão de dias terrestres para ângulo de órbita
dias_por_clique = 30
dias_por_volta_mercurio = 59
dias_por_volta_venus = 243
dias_por_volta_terra = 365
dias_por_volta_marte = 687
dias_por_volta_saturno = 10752.9
dias_por_volta_jupter = 4333
dias_por_volta_urano = 30663.65
dias_por_volta_netuno = 60148.35
# Contador de tempo (inicia em 01/01/2001)
data_atual = datetime(2001, 1, 1)
dias_por_volta_ano = 365
angulo_por_dia = 2 * math.pi / dias_por_volta_ano

def avancar_tempo():
    global angulo_terra, angulo_mercurio, angulo_venus, angulo_marte, angulo_saturno, angulo_jupiter, angulo_urano, angulo_netuno, data_atual
    angulo_terra += 2 * math.pi  * (dias_por_clique/dias_por_volta_terra)
    angulo_mercurio += 2 * math.pi  * (dias_por_clique/dias_por_volta_mercurio)
    angulo_venus += 2 * math.pi * (dias_por_clique/dias_por_volta_venus)
    angulo_marte += 2 * math.pi * (dias_por_clique/dias_por_volta_marte)
    angulo_saturno += 2 * math.pi * (dias_por_clique/dias_por_volta_saturno)
    angulo_jupiter += 2 * math.pi * (dias_por_clique/dias_por_volta_jupter)
    angulo_urano += 2 * math.pi * (dias_por_clique/dias_por_volta_urano)
    angulo_netuno += 2 * math.pi * (dias_por_clique/dias_por_volta_netuno)
    data_atual += timedelta(days=30)  # Adiciona 30 dias (1 mês)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                avancar_tempo()

    x_terra = largura // 2 + raio_orbita_terra * math.cos(angulo_terra)
    y_terra = altura // 2 + raio_orbita_terra * math.sin(angulo_terra)
    x_mercurio = largura // 2 + raio_orbita_mercurio * math.cos(angulo_mercurio)
    y_mercurio = altura // 2 + raio_orbita_mercurio * math.sin(angulo_mercurio)
    x_venus = largura // 2 + raio_orbita_venus * math.cos(angulo_venus)
    y_venus = altura // 2 + raio_orbita_venus * math.sin(angulo_venus)
    x_marte = largura // 2 + raio_orbita_marte * math.cos(angulo_marte)
    y_marte = altura // 2 + raio_orbita_marte * math.sin(angulo_marte)
    x_saturno = largura // 2 + raio_orbita_saturno * math.cos(angulo_saturno)
    y_saturno = altura // 2 + raio_orbita_saturno * math.sin(angulo_saturno)
    x_jupiter = largura // 2 + raio_orbita_jupiter * math.cos(angulo_jupiter)
    y_jupiter = altura // 2 + raio_orbita_jupiter * math.sin(angulo_jupiter)
    x_urano = largura // 2 + raio_orbita_urano * math.cos(angulo_urano)
    y_urano = altura // 2 + raio_orbita_urano * math.sin(angulo_urano)
    x_netuno = largura // 2 + raio_orbita_netuno * math.cos(angulo_netuno)
    y_netuno = altura // 2 + raio_orbita_netuno * math.sin(angulo_netuno)

    # Desenhe os planetas (adapte os tamanhos conforme desejado)
    janela.fill(cor_fundo)
    pygame.draw.circle(janela, cor_sol, (largura // 2, altura // 2), 20)  # Sol
    pygame.draw.circle(janela, cor_terra, (x_terra, y_terra), 5)  # Terra
    pygame.draw.circle(janela, cor_mercurio, (x_mercurio, y_mercurio), 3)  # Mercúrio
    pygame.draw.circle(janela, cor_venus, (x_venus, y_venus), 4)  # Vênus
    pygame.draw.circle(janela, cor_marte, (x_marte, y_marte), 4)  # Marte
    pygame.draw.circle(janela, cor_saturno, (x_saturno, y_saturno), 8)  # Saturno
    pygame.draw.circle(janela, cor_jupiter, (x_jupiter, y_jupiter), 10)  # Júpiter
    pygame.draw.circle(janela, cor_urano, (x_urano, y_urano), 6)  # Urano
    pygame.draw.circle(janela, cor_netuno, (x_netuno, y_netuno), 6)  # Netuno
    
    # Desenhe a caixa branca para a data
    caixa_data = pygame.Rect(largura - 160, 10, 150, 30)
   
    pygame.draw.rect(janela, (255, 255, 255), caixa_data)
    fonte_data = pygame.font.Font(None, 24)
    texto_data = fonte_data.render(data_atual.strftime("%d/%m/%Y"), True, (0, 0, 0))
    janela.blit(texto_data, (20, 20))
    posicao_texto = texto_data.get_rect(center=caixa_data.center)
    janela.blit(texto_data, posicao_texto)
    
    pygame.draw.rect(janela, (255, 255, 255), (10, 10, 80, 30))
    fonte = pygame.font.Font(None, 24)
    texto_botao = fonte.render("1 mês", True, (0, 0, 0))
    janela.blit(texto_botao, (20, 20))

    pygame.display.flip()