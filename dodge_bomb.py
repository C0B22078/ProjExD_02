import sys
import random
import pygame as pg



WIDTH, HEIGHT = 1500, 800
delta = {
pg.K_UP: (0,-5),
pg.K_DOWN: (0,+5),
pg.K_LEFT: (-5,0),
pg.K_RIGHT: (+5,0),
}

def window_judge(rct:pg.rect) -> tuple[bool,bool]:
    """
    こうかとんRect,爆弾Rectが画面外or 画面内かを判定する関数
    引数:こうかとんRect or 爆弾Rect
    戻り値;横方向,縦方向の判定結果タプル 
    """


    yoko,tate = True,True  #画面内であればTrue
    if rct.left < 0 or WIDTH <rct.right :
        yoko = False 
    if rct.top < 0 or HEIGHT <rct.bottom:
        tate = False
    return yoko,tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")#backgroundimage
    kk_img = pg.image.load("ex02/fig/3.png")#koukaton_image
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    #こうかとんSurface (kk_img)からこうかとんRect(kk_rct)を抽出する　
    kk_rct =kk_img.get_rect()
    kk_rct.center=900,400
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
        if kk_rct.colliderect(bomb_rect):
            print("game over")
            return  #ガメオベラ
        key_lst = pg.key.get_pressed()
        sum_mv = [0,0] #合計移動量

        for k,mv in delta.items():
            if key_lst[k] :
                sum_mv[0]+= mv[0]
                sum_mv[1]+= mv[1]
                
        kk_rct.move_ip(sum_mv[0],sum_mv[1])
        if window_judge(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bomb_rect.move_ip(vx,vy) #練習2
        yoko,tate = window_judge(bomb_rect)
        if not yoko: #横方向に画面外だったら
            vx *= -1
        if not tate : #縦方向に範囲外であれば
            vy *= -1 
        screen.blit(bomb_img,bomb_rect)
    
        pg.display.update()
        tmr += 1
        clock.tick(50)


    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()