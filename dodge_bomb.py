import sys
import random
import pygame as pg



WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")#backgroundimage
    kk_img = pg.image.load("ex02/fig/3.png")#koukaton_image
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bomb_img = pg.Surface((20,20))
    bomb_img.set_colorkey((0,0,0)) #黒い部分を透明に
    pg.draw.circle(bomb_img,(255,0,0),(10,10),10)
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    #爆弾Surface(bomb_img)
    bomb_rect = bomb_img.get_rect()
    #bomb_rectの中心座標を乱数指定
    bomb_rect.center = x,y 

    clock = pg.time.Clock()
    tmr = 0
    vx,vy = +5,+5
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bomb_rect.move_ip(vx,vy) #練習2
        screen.blit(bomb_img,bomb_rect)
        pg.display.update()
        
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()