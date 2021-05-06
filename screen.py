import random
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen_width = 640
screen_height = 480

# dred = 255
# dgreen = 50
# dblue = 102

x_snake = int(screen_width / 2)
y_snake = int(screen_height / 2)
w_snake = 10
h_snake = 10

x_apple = random.randint(10, 630)
y_apple = random.randint(50, 470)

# musica de fundo
pygame.mixer.music.set_volume(1)
background_music = pygame.mixer.music.load('sound/Ras G - Into Infinity _ear_ loop.mp3')
pygame.mixer.music.play(-1)

# todos os arquivos de som tirando a musica de fundo deverão estar em .wav se nao havera um erro
eat_apple = pygame.mixer.Sound('sound/smw_power-up.wav')

fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

relogio = pygame.time.Clock()

score = 0
speed = 1
snake_body = []
snake_lenght = 10
x_controller = speed
y_controller = 0
die = False

'''
def randomApple():
    cx = random.randint(0, 640 + 1);
    cy = random.randint(0, 480);
    print(random.randint(0, 640+1));
    print(random.randint(0, 480+1))
'''


def grow_snake(snake_body):
    for XeY in snake_body:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 10, 10))


def restart_game():
    global score, snake_lenght, x_snake, y_snake, snake_body, snake_head, x_apple, y_apple, die
    score = 0
    snake_lenght = 10
    x_snake = int(screen_width / 2)
    y_snake = int(screen_height / 2)
    snake_body = []
    snake_head = []
    x_apple = random.randint(10, 630)
    y_apple = random.randint(50, 470)
    die = False


play = True
while play:
    relogio.tick(60)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {score}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''    
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x_snake -= 10
                cx -= 10
            if event.key == K_RIGHT:
                x_snake += 10
                cx += 10
            if event.key == K_UP:
                y_snake -= 10
                cy -= 10
            if event.key == K_DOWN:
                y_snake += 10
                cy += 10
        '''

    # ------------Circulo
    # if cy >= screen_height:
    #     cy = 0
    # elif cy <= 0:
    #     cy = screen_height
    # if cx > screen_width:
    #     cx = 0
    # elif cx <= 0:
    #     cx = screen_width

    # ------------Retangulo
    if x_snake >= screen_width:
        x_snake = 0
    elif x_snake <= 0:
        x_snake = screen_width
    if y_snake >= screen_height:
        y_snake = 0
    elif y_snake <= 0:
        y_snake = screen_height

    if pygame.key.get_pressed()[K_LEFT]:
        if x_controller == speed:
            pass
        else:
            x_controller = -speed
            y_controller = 0

    if pygame.key.get_pressed()[K_RIGHT]:
        if x_controller == -speed:
            pass
        else:
            x_controller = speed
            y_controller = 0

    if pygame.key.get_pressed()[K_UP]:
        if y_controller == speed:
            pass
        else:
            y_controller = -speed
            x_controller = 0

    if pygame.key.get_pressed()[K_DOWN]:
        if y_controller == -speed:
            pass
        else:
            y_controller = speed
            x_controller = 0

    x_snake += x_controller
    y_snake += y_controller

    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, w_snake, h_snake))
    apple = pygame.draw.circle(tela, (255, 0, 0), (x_apple, y_apple), 5)

    if apple.collidepoint(x_snake, y_snake) or snake.collidepoint(apple.x, apple.y):
        eat_apple.play()
        snake_lenght += 1
        x_apple = random.randint(10, 630)
        y_apple = random.randint(50, 470)
        score += 1 + int((len(snake_body) * speed) / (len(snake_body) + speed))
        speed += 0.05
        print(score)

    snake_head = [x_snake, y_snake]

    snake_body.append(snake_head)

    if snake_body.count(snake_head) > 1:
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
        rect_text = texto_formatado.get_rect()
        die = True
        while die:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()
            rect_text.center = (screen_width // 2, screen_height // 2)
            tela.blit(texto_formatado, rect_text)
            pygame.display.update()

    if len(snake_body) > snake_lenght:
        del snake_body[0]

    grow_snake(snake_body)

    # linha x verde
    # pygame.draw.line(tela, (0, 255, 50), (10, 4), (640, 4), 10)
    # #linha y amarelo
    # pygame.draw.line(tela, (255, 255, 25), (4, 10), (4, 480), 10)
    # #ponto vermelho
    # pygame.draw.line(tela, (255, 0, 0), (0, 4), (10, 4), 10)

    tela.blit(texto_formatado, (10, 10))
    pygame.display.update()
