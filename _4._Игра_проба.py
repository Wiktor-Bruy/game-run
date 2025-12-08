from email.mime import image
from re import X
import pygame

clock = pygame.time.Clock()

pygame.init()
ekran = pygame.display.set_mode((600, 360))
pygame.display.set_caption('Моя первая игра.')
fon = pygame.image.load('image/fon.jpg').convert()
fon2 = pygame.image.load('image/fon2.jpg').convert()
fx = 0
icon = pygame.image.load('image/icon.png').convert()
pygame.display.set_icon(icon)

font = pygame.font.Font('fonts.ttf', 60)
text = font.render('Game Over!', False, (0, 0, 0))
text2 = font.render('Play', False, (235, 231, 30))
text_rect = text2.get_rect(topleft = (210, 200))

fon_muz = pygame.mixer.Sound('muz/bg.mp3')
fon_muz.play()
jsound = pygame.mixer.Sound('muz/jump.mp3')
botmuz = pygame.mixer.Sound('muz/bots.mp3')
botkill = pygame.mixer.Sound('muz/kill.mp3')
game_over = pygame.mixer.Sound('muz/Over.mp3')
shot = pygame.mixer.Sound('muz/shot.mp3')

rr = [pygame.image.load('image/rr1.png').convert_alpha(),
      pygame.image.load('image/rr1.png').convert_alpha(),
      pygame.image.load('image/rr1.png').convert_alpha(),
      pygame.image.load('image/rr2.png').convert_alpha(),
      pygame.image.load('image/rr2.png').convert_alpha(),
      pygame.image.load('image/rr2.png').convert_alpha(),
      pygame.image.load('image/rr3.png').convert_alpha(),
      pygame.image.load('image/rr3.png').convert_alpha(),
      pygame.image.load('image/rr3.png').convert_alpha(),
      pygame.image.load('image/rr4.png').convert_alpha(),
      pygame.image.load('image/rr4.png').convert_alpha(),
      pygame.image.load('image/rr4.png').convert_alpha()]
plx = 150
ply = 130
pls = 5
num = 0

bot1 = pygame.image.load('image/bot1.png').convert_alpha()
bots1 = []
bot1_t = pygame.USEREVENT +1
pygame.time.set_timer(bot1_t, 7000)

bot2 = pygame.image.load('image/bot2.png').convert_alpha()
bots2 = []

bulet = []
bul = pygame.image.load('image/bul.png').convert_alpha()
bt = True
bt1 = 0

jump = False
jumps = 8
bjump = False
bjumps = 4

Game = True
Play = True

while Game:

    
    if Play:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and plx > 70:
            plx -= pls
        elif keys[pygame.K_RIGHT] and plx < 240:
            plx += pls

        if not jump:
            if keys[pygame.K_UP]:
                jump = True
                jsound.play()
        else:
            if jumps >= -8:
                if jumps > 0:
                    ply -= (jumps**2)/2
                else:
                    ply += (jumps**2)/2
                jumps -= 1
            else:
                 jumps = 8
                 jump = False

        ekran.blit(fon, (fx, 0))
        ekran.blit(fon, (fx+600, 0))
        fx -= 1
        if fx == -600:
            fx =0

        ekran.blit(rr[num], (plx, ply))
        rr_rect = rr[0].get_rect(topleft = (plx, ply))
        if num == 11:
            num =0
        else:
            num += 1

        if keys[pygame.K_b] and bt:
            bulet.append(bul.get_rect(topleft = (plx+130, ply+70)))
            bt = False
            shot.play()

        if bulet:
            for (a, b) in enumerate(bulet):
                ekran.blit(bul, b)
                b.x += 8
                if b.x > 620:
                    bulet.pop(a)
                if bots1:
                    for (c, d) in enumerate(bots1):
                        if b.colliderect(d):
                            bulet.pop(a)
                            bots1.pop(c)
                if bots2:
                    for(n, m) in enumerate(bots2):
                        if b.colliderect(m):
                            bulet.pop(a)
                            bots2.pop(n)

        if bots2:
            for (e, f) in enumerate(bots2):
                ekran.blit(bot2, f)
                f.x -= 7
                if f.x == 600:
                    botmuz.play()
                if rr_rect.colliderect(f):
                    Play = False
                    game_over.play()

        if bots1:
            for (i, el) in enumerate(bots1):
                ekran.blit(bot1, el)
                el.x -= 6
                if el.x == 600:
                    botmuz.play()
                if el.x < -30:
                    bots1.pop(i)
                if rr_rect.colliderect(el):
                    if ply+128 <= el.y+10:
                        botkill.play()
                        bots1.pop(i)
                        bjump = True
                    else:
                        Play = False
                        game_over.play()

        if bjump:
            if bjumps >= -4:
                if bjumps > 0:
                    ply -= (bjumps**2)/2
                else:
                    ply += (bjumps**2)/2
                bjumps -= 1
            else:
                 bjumps = 4
                 bjump = False

    else:
        
        ekran.blit(fon2, (-12, -50))
        ekran.blit(text, (120, 70))
        ekran.blit(text2, text_rect)

        mouse = pygame.mouse.get_pos()
        if text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            Play = True
            plx = 150
            ply = 130
            bots1.clear()
            bots2.clear()
            bulet.clear()
            bt = True
            bt1 = 0
            bjumps = 4
            bjump = False
            jumps = 8
            jump = False

    pygame.display.update()
    
    if not bt:
        if bt1 > 40:
            bt = True
            bt1 = 0
        bt1 +=1

    clock.tick(25)

    for sob in pygame.event.get():
        if sob.type == pygame.QUIT:
            Game = False
            pygame.quit()
            exit()
        if sob.type == bot1_t:
            bots1.append(bot1.get_rect(topleft = (620, 195)))
            bots2.append(bot2.get_rect(topleft = (920, 165)))