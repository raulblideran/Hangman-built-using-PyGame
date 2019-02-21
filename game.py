import pygame
import random

pygame.init()
pygame.font.init()
pygame.display.set_caption('Hangman')
pygame.mouse.set_visible(True)

#image imports

bg_game = pygame.image.load("bg.jpg")
win = pygame.image.load('win.png')
head = pygame.image.load('head.png')
body = pygame.image.load('body.png')
r_arm = pygame.image.load('r_arm.png')
l_arm = pygame.image.load('l_arm.png')
r_leg = pygame.image.load('r_leg.png')
l_leg = pygame.image.load('l_leg.png')
dead_g = pygame.image.load('dead.png')
start = pygame.image.load('start.jpg')

screen = pygame.display.set_mode((1050, 500))

def start_screen():
    screen.blit(start, (0, 0))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                if event.key == pygame.K_q:
                    waiting = False
                elif event.key == pygame.K_s:
                    waiting = False
                    game()
            if event.type == pygame.QUIT:
                waiting = False

def passed():
    screen.blit(win, (0, 0))
    pygame.display.flip()
    pygame.mixer.music.load('win.mp3')
    pygame.mixer.music.play(0)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                if event.key == pygame.K_q:
                    waiting = False
                if event.key == pygame.K_r:
                    waiting = False
                    game()
                if event.key == pygame.K_m:
                    waiting = False
                    start_screen()
            if event.type == pygame.QUIT:
                waiting = False

def dead():
    screen.blit(dead_g, (0, 0))
    pygame.display.flip()
    pygame.mixer.music.load('dead.mp3')
    pygame.mixer.music.play(0)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                if event.key == pygame.K_q:
                    waiting = False
                if event.key == pygame.K_r:
                    waiting = False
                    game()
                if event.key == pygame.K_m:
                    waiting = False
                    start_screen()
            if event.type == pygame.QUIT:
                waiting = False


def game():
    clock = pygame.time.Clock()
    screen.blit(bg_game, (0,0))
    font = pygame.font.SysFont("comicsansms", 65)
    with open("words.txt", "r") as words:
        list = words.read().splitlines()
    a = random.choice(list)
    x = 440
    for letter in range(len(a)):
        pygame.draw.rect(screen, (0,0,0), [x, 350, 25, 3])
        x = x+60
    new_list = [it for it in a]
    hang = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_a:
                    b = 450
                    if 'a' in new_list:
                        while 'a' in new_list:
                            k = new_list.index('a')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head,(185,45))
                        if hang == 2:
                            screen.blit(body,(185,155))
                        if hang == 3:
                            screen.blit(l_arm,(230,180))
                        if hang == 4:
                            screen.blit(r_arm,(135,180))
                        if hang == 5:
                            screen.blit(l_leg,(230,320))
                        if hang == 6:
                            screen.blit(r_leg,(135,320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_b:
                    b = 450
                    if 'b' in new_list:
                        while 'b' in new_list:
                            k = new_list.index('b')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_c:
                    b = 450
                    if 'c' in new_list:
                        while 'c' in new_list:
                            k = new_list.index('c')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_d:
                    b = 450
                    if 'd' in new_list:
                        while 'd' in new_list:
                            k = new_list.index('d')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_e:
                    b = 450
                    if 'e' in new_list:
                        while 'e' in new_list:
                            k = new_list.index('e')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                            dead()
                            done = True
                if event.key == pygame.K_f:
                    b = 450
                    if 'f' in new_list:
                        while 'f' in new_list:
                            k = new_list.index('f')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_g:
                    b = 450
                    if 'g' in new_list:
                        while 'g' in new_list:
                            k = new_list.index('g')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_h:
                    b = 450
                    if 'h' in new_list:
                        while 'h' in new_list:
                            k = new_list.index('h')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_i:
                    b = 450
                    if 'i' in new_list:
                        while 'i' in new_list:
                            k = new_list.index('i')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_j:
                    b = 450
                    if 'j' in new_list:
                        while 'j' in new_list:
                            k = new_list.index('j')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_k:
                    b = 450
                    if 'k' in new_list:
                        while 'k' in new_list:
                            k = new_list.index('k')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_l:
                    b = 450
                    if 'l' in new_list:
                        while 'l' in new_list:
                            k = new_list.index('l')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_m:
                    b = 450
                    if 'm' in new_list:
                        while 'm' in new_list:
                            k = new_list.index('m')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_n:
                    b = 450
                    if 'n' in new_list:
                        while 'n' in new_list:
                            k = new_list.index('n')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_o:
                    b = 450
                    if 'o' in new_list:
                        while 'o' in new_list:
                            k = new_list.index('o')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_p:
                    b = 450
                    if 'p' in new_list:
                        while 'p' in new_list:
                            k = new_list.index('p')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_q:
                    b = 450
                    if 'q' in new_list:
                        while 'q' in new_list:
                            k = new_list.index('q')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_r:
                    b = 450
                    if 'r' in new_list:
                        while 'r' in new_list:
                            k = new_list.index('r')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_s:
                    b = 450
                    if 's' in new_list:
                        while 's' in new_list:
                            k = new_list.index('s')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_t:
                    b = 450
                    if 't' in new_list:
                        while 't' in new_list:
                            k = new_list.index('t')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_u:
                    b = 450
                    if 'u' in new_list:
                        while 'u' in new_list:
                            k = new_list.index('u')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_v:
                    b = 450
                    if 'v' in new_list:
                        while 'v' in new_list:
                            k = new_list.index('v')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_w:
                    b = 450
                    if 'w' in new_list:
                        while 'w' in new_list:
                            k = new_list.index('w')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_x:
                    b = 450
                    if 'x' in new_list:
                        while 'x' in new_list:
                            k = new_list.index('x')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_y:
                    b = 450
                    if 'y' in new_list:
                        while 'y' in new_list:
                            k = new_list.index('y')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
                if event.key == pygame.K_z:
                    b = 450
                    if 'z' in new_list:
                        while 'z' in new_list:
                            k = new_list.index('z')
                            t = font.render(new_list[k], True, (0, 0, 0))
                            screen.blit(t, (b + 45 * k + 15 * k - t.get_width() // 2, 315 - t.get_height() // 2))
                            new_list[k] = 1
                    else:
                        hang = hang + 1
                        if hang == 1:
                            screen.blit(head, (185, 45))
                        if hang == 2:
                            screen.blit(body, (185, 155))
                        if hang == 3:
                            screen.blit(l_arm, (230, 180))
                        if hang == 4:
                            screen.blit(r_arm, (135, 180))
                        if hang == 5:
                            screen.blit(l_leg, (230, 320))
                        if hang == 6:
                            screen.blit(r_leg, (135, 320))
                        if hang == 7:
                            dead()
                            done = True
            if len(set(new_list)) == 1:
                done = True
                passed()
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()
        clock.tick(60)
start_screen()
pygame.quit()
