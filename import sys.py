import sys
import random
import pygame as pg

WIDTH, HEIGHT = 1500, 800
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}

def window_judge(rct: pg.rect) -> tuple[bool, bool]:
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko, tate

def img_ch():
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 1.0)
    kk_img_rv = pg.transform.flip(kk_img, True, False)
    img_change = {}
    for acc in range(1, 11):
        kk_img_acc = pg.transform.rotozoom(kk_img_rv, 0, 2.0 * acc)
        img_change[(0, 0, acc)] = kk_img_acc
    return img_change

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_imgs = img_ch()
    
    kk_rct = kk_imgs[(0, 0, 1)].get_rect()
    kk_rct.center = 900, 400
    
    bomb_imgs = []
    for r in range(1, 11):
        bomb_img = pg.Surface((20 * r, 20 * r))
        pg.draw.circle(bomb_img, (255, 0, 0), (10 * r, 10 * r), 10 * r)
        bomb_imgs.append(bomb_img)
    
    bomb_rect = bomb_imgs[0].get_rect()
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bomb_rect.center = x, y
    
    clock = pg.time.Clock()
    tmr = 0
    vx, vy = 5, 5
    accs = [a for a in range(1, 11)]
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        if kk_rct.colliderect(bomb_rect):
            print("Game Over")
            pg.quit()
            sys.exit()
        
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        
        if window_judge(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_imgs[(sum_mv[0], sum_mv[1], 1)], kk_rct)
        
        acc = min(tmr // 500, 9)
        bomb_rect.move_ip(vx * accs[acc], vy * accs[acc])
        yoko, tate = window_judge(bomb_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bomb_imgs[acc], bomb_rect)
        
        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
