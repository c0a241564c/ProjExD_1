import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #Surface
    kk_img=pg.image.load("fig/3.png")

    kk_img=pg.transform.flip(kk_img, True ,False)
    bg_img2=pg.transform.flip(bg_img, True ,False)
    kk_rct=kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        a=0
        b=0
        Key_lst=pg.key.get_pressed()
        if Key_lst[pg.K_UP]:
            a-=1
        if Key_lst[pg.K_DOWN]:
            a+=1
        if Key_lst[pg.K_LEFT]:
            b-=1
        if Key_lst[pg.K_RIGHT]:
            b+=1
        else:
            b-=1
        kk_rct.move_ip(b,a)
        x=tmr%3200
        screen.blit(bg_img, [-x, 0]) #一枚目
        screen.blit(bg_img2, [-x+1600, 0]) #二枚目
        screen.blit(bg_img, [-x+3200, 0]) #三枚目
        # screen.blit(kk_img, [300, 200])
        screen.blit(kk_img,kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200) #FPS


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()