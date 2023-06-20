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

def img_ch():
        kk_img = pg.image.load("ex02/fig/3.png")#koukaton_image
        kk_img = pg.transform.rotozoom(kk_img, 0, 1.0)
        kk_img_rv = pg.transform.flip(kk_img, True, False)
        img_change =  {
            (-5,-5):pg.transform.rotozoom(kk_img,-45,2.0),
            (-5,0):pg.transform.rotozoom(kk_img,0,2.0),
            (-5,+5):pg.transform.rotozoom(kk_img, 45, 2.0),
            (+5,-5):pg.transform.rotozoom(kk_img_rv,45,2.0),
            (+5,0):pg.transform.rotozoom(kk_img_rv,0,2.0),
            (+5,+5):pg.transform.rotozoom(kk_img_rv,-45,2.0),
            (0,-5):pg.transform.rotozoom(kk_img_rv,90,2.0),
            (0,+5):pg.transform.rotozoom(kk_img_rv,-90,2.0),
            (0,0):pg.transform.rotozoom(kk_img_rv,0,2.0),
        }
        
        return img_change

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")#backgroundimage
    kk_imgs = img_ch() #画像の挿入
    
    

    
    #こうかとんSurface (kk_img)からこうかとんRect(kk_rct)を抽出する　
    kk_rct =kk_imgs[(0,0)].get_rect()
    kk_rct.center=900,400
    bomb_imgs= []
    for r in range(1, 11):
        bomb_img = pg.Surface((20 * r, 20 * r)) #爆弾サーフェスの作成
        #関数を用いて、円と色の変更
        pg.draw.circle(bomb_img, (255, 0, 0), (10 * r, 10 * r), 10 * r)
        bomb_img.set_colorkey((0,0,0))

        bomb_imgs.append(bomb_img)#異なるサイズの爆弾画像を格納するために使用
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    #爆弾Surface(bomb_img)
    bomb_rect = bomb_img.get_rect()
    #bomb_rectの中心座標を乱数指定
    bomb_rect.center = x,y 
    clock = pg.time.Clock()
    tmr = 0
    vx,vy = +5,+5
    accs = [a for a in range(1, 11)]

    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bomb_rect):
            print("game over")
            return  #ゲームオーバー
        
        key_lst = pg.key.get_pressed()
        sum_mv = [0,0] #合計移動量

        for k,mv in delta.items():
            if key_lst[k] :
                kk_rct.move_ip(mv)
                sum_mv[0]+= mv[0]
                sum_mv[1]+= mv[1]
                
        

        if window_judge(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_imgs[tuple(sum_mv)], kk_rct)
        #爆弾の移動時間ごとに大きさを変化させる変数の追加
        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]

        bomb_img = bomb_imgs[min(tmr//500,9)]
        bomb_rect.move_ip(avx,avy) #練習2
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