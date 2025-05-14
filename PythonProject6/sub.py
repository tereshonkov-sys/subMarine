import pygame
import random
from val import lore1, loreh, his, bed, good, location,subst
pygame.init()
pygame.display.set_caption('субкрафт')
window_surface = pygame.display.set_mode((600, 600))

inventory = [[0.5,'startw'],[2.0,'tw'],]
eqip = [0.1,'для смены снаряда q']
hh=0
antposy = -300
ant = pygame.image.load('ant.jpg')
current_color_index = 0
pole = []
lor1 = pygame.image.load('lor1.jpeg')
lor2 = pygame.image.load('gun.jpg')
lor3 = pygame.image.load('lor3.jpg')
lor4 = pygame.image.load('lor4.jpg')
lor5 = pygame.image.load('lor5.jpg')
lor6 = pygame.image.load('llor.jpg')
hs1 = pygame.image.load('hs1.jpg')
hs2 = pygame.image.load('hs2.jpg')
hs3 = pygame.image.load('hs3.jpg')
hs4 = pygame.image.load('hs4.jpg')
hs5 = pygame.image.load('hs5.jpg')
hs6 = pygame.image.load('hs6.jpg')
bg= pygame.image.load('panel.jpg')
hscor = pygame.image.load('hscor.jpg')
lorim=[[lor2,1],[lor3,4],[lor4,2],[lor5,9],[lor6,16],]
hsim = [[hs1,7],[hscor,16],[hs2,15],[hs3,9],[hs4,9],[hs5,6],[hs6,14]]
endim = pygame.image.load('end.jpg')


lasts =0
vib1 = pygame.image.load('vib1.jpg')
vib2 = pygame.image.load('2vib.jpg')
vib3 = pygame.image.load('vib3.jpg')
vib4 = pygame.image.load('vib4.jpg')

subim = [[vib1,(0,0)],[vib2,(300,0)],[vib3,(0,300)],[vib4,(300,300)]]

#имя,множетель времени,множетель урона,множетель скросоти врагов,скорость радара

sub =[]
start_ticks=pygame.time.get_ticks()
mouseClicked = False
fize = False
lr =0
seconds = 0
r = 0
vibor = True
k_ent = 0
lk_ent =0
dr =0
lh=0
f1 = pygame.font.Font(None, 22)
f2 = pygame.font.Font(None, 24)
eq = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                fize = not fize
            if event.key == pygame.K_RETURN:
                if len(hsim) > 0:
                    k_ent += 1
            elif event.key == pygame.K_w:
                if fize == True:
                    if eq == len(inventory):
                        eq = 0
                    else:
                        eq += 1
                    eqip.clear()
                    eqip.extend(inventory[eq - 1].copy())
            elif event.key == pygame.K_s:
                if fize == True:
                    if eq == 0:
                        eq = len(inventory)
                    else:
                        eq -= 1
                    eqip.clear()
                    eqip.extend(inventory[eq - 1].copy())
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseClicked = False
    mouse = pygame.mouse.get_pos()

    while vibor == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    k_ent +=1
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouseClicked = False
        if  lr < len(lore1) and k_ent>lk_ent:
            window_surface.blit(lor1, (0, 0))
            for i in range(lr,lr+15):
                text1 = f1.render(lore1[lr], True,(180, 0, 0))
                lr+=1
                dr += 15
                window_surface.blit(text1, (180, 250+ dr))
            dr=0
            lk_ent+=1
        elif  k_ent>lk_ent and len(lorim)>0:
            if lorim[0][1] > 0:
                lorim[0][1]-=1
                lh+=1
                window_surface.blit(lorim[0][0], (0, 0))
                text1 = f2.render(loreh[lh], True, (180, 0, 0))
                window_surface.blit(text1, (0, 550))
                lk_ent += 1
            else:
                lorim.pop(0)
        elif len(lorim)==0:
            mouse = pygame.mouse.get_pos()
            if  mouseClicked == True:
                if mouse[0] < 300 and mouse[1] <300: #если элементов было бы больше 5 я бы сделал цыклом
                    sub.extend(subst[0])
                elif mouse[0] > 300 and mouse[1] < 300:
                    sub.extend(subst[1])
                elif mouse[0] < 300 and mouse[1] > 300:
                    sub.extend(subst[2])
                elif mouse[0] > 300 and mouse[1] > 300:
                    sub.extend(subst[3])
            if len(sub)!= 0:
                vibor = False
            for i in range(len(subim)):
                window_surface.blit(subim[i][0],subim[i][1])
        pygame.display.update()
        pygame.time.Clock().tick(240)
    f1 = pygame.font.SysFont('serif', 31)
    text2 = f1.render(f'название снаряда:{eqip[1]}', False, (255, 0, 50))
    if fize == False and antposy <150 :
        seconds += 0.00416666 * sub[1]
        if seconds > 90:
            seconds= 91.0
            antposy += 1
        print(seconds)  # print how many seconds
        if seconds > (10 + lasts):
            lasts +=10
            inventory.append(location[lasts//10][-1])

        if len(pole) < location[int(seconds) % 10][0]:
            pole.append(location[int(seconds) % 10][1].copy())
            pole[-1][0]= random.randint(0,240)
            score = 0

        for i in range(len(pole)):
            if pole[i][0] >= 150:
                pole[i][1] += pole[i][3]*sub[3]
                pole[i][0] -= pole[i][3]*sub[3]
            elif pole[i][0]<150:
               pole[i][0] += pole[i][3]*sub[3]
               pole[i][1] += pole[i][3]*sub[3]
            if pole[i][1] >= 150:
                pygame.quit()
                exit()
        print(pole)
        button_color = pygame.Color("gray")
        button_rect = pygame.Rect(pole[0][0], pole[0][1], 30, 30)
        if len(pole)>1:
            button2_color = pygame.Color("gray")
            button2_rect = pygame.Rect(pole[1][0], pole[1][1], 30, 30)
        mouse = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse) and mouseClicked ==  True:
            pole[0][2]-=eqip[0]*sub[2]
        if len(pole) > 1:
            if button2_rect.collidepoint(mouse) and mouseClicked ==  True:
                pole[1][2] -=eqip[0]
        for i in range(len(pole)):
            if pole[i][2]<0:
                pole.pop(i)
                break
        r += 2* sub[4]
        window_surface.blit(bg, (0, 0))
        pygame.draw.rect(window_surface, (0,0,0), (0, 0, 300, 300))
        pygame.draw.rect(window_surface, button_color, button_rect)
        if len(pole) > 1:
            pygame.draw.rect(window_surface, button_color, button2_rect)
        pygame.draw.arc(window_surface, (0, 0, 0), (0, 0, 300, 300), ((0 + r) / 57), ((180 + r) / 57), 150)
        pygame.draw.arc(window_surface, (0, 255, 0), (0, 0, 300, 300), ((0 + r) / 57), ((3 + r) / 57), 150)
        j=150
        while j > 0:
            if j%50==0:
                pygame.draw.circle(window_surface, (0, 255, 0), (150, 150), j, 3)
            else:
                pygame.draw.circle(window_surface, (0, 255, 0), (150, 150), j, 1)
            j-=25


        pygame.draw.circle(window_surface, (0, 0, 0), (150, 150), 200, 50)
        window_surface.blit(ant, (0, antposy))
        window_surface.blit(text2, (0, 400))
    elif antposy < 150:

        print(eqip)

        window_surface.blit(bg, (0, 0))
        pi = 3.14
        pygame.draw.rect(window_surface, (0, 0, 0), (0, 0, 300, 300))
        j = 150
        while j > 0:
            if j % 50 == 0:
                pygame.draw.circle(window_surface, (0, 255, 0), (150, 150), j, 3)
            else:
                pygame.draw.circle(window_surface, (0, 255, 0), (150, 150), j, 1)
            j -= 25
        window_surface.blit(text2, (0, 400))
    else:
        if k_ent > lk_ent:
            if len(hsim) > 0:
                if hsim[0][1] > 0:
                    hsim[0][1] -= 1
                    window_surface.blit(hsim[0][0], (0, 0))
                    text1 = f2.render(his[hh], True, (180, 0, 0))
                    window_surface.blit(text1, (0, 550))
                    hh += 1
                    lk_ent += 1

                else:
                    hsim.pop(0)
            if len(hsim) == 0:
                his.clear()
                hh = 0
                if mouseClicked == True:
                    if mouse[0] < 300 :
                        hsim.append([endim, 17])
                        his.extend(bed)
                    if mouse[0] > 300 :
                        hsim.append([endim, 4])
                        his.extend(good)
    pygame.display.update()
    pygame.time.Clock().tick(240)