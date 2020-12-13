import pygame
import sys
list_hard = [1,3,3,1,1,24,0]
SHU = 1    # 数独难度1，2，3
NUM_SINGLE = 0    # 悔棋次数
HARD_WZY = 1   # 2048难度1，2，3
HARD_SWEEPER = 1
RESULT = 'white'
NUM = 1   # 24点的结果
NUM_FL = 1   # flappy bird的结果
import mainshudu
# 初始化主界面
def start_screean():
    pygame.init()
    size = width , height = 1080,720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("来者何人")
    begin_image1 = pygame.image.load("./pic/xu1.jpg")
    screen.blit(begin_image1,(0,0))
    pygame.display.update()

    n1 = True
    n = 1
    while n1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                first(screen,n)
                n = n + 1
            if n == 7 :
                n1 = False
    n2 = True
    while n2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                (x,y) = event.pos
                # 数独困难选择
                if x >= 78 and x <= 349  and y >=592 and y <= 620:
                    list_hard[1] = 1
                    first(screen,7)

                    n2 = False
                if x >= 450 and x <= 643 and y >= 592 and y <= 620:
                    list_hard[1] = 2
                    first(screen,8)

                    n2 = False
                if x >= 770 and x <= 1018 and y >= 592 and y <= 620:
                    list_hard[1] = 3
                    first(screen,9)
                    n2 = False
                print(list_hard[1])

    n3 = True
    while n3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 调用数独
                pygame.quit()
                mainshudu.main(list_hard)
# 序章和第一关数独引入
def first(screen,n):
    if n == 1:
        gamebg = pygame.image.load(r"./pic/xu2.ppm")
    if  n <= 5 and n > 1:
        m = n-1
        gamebg = pygame.image.load("./pic/shudu%s.ppm"%m)
    if n == 6:
        gamebg = pygame.image.load("./pic/shudubutton.ppm")
    if n == 7:
        gamebg = pygame.image.load("./pic/shudueasy.ppm")
    if n == 8:
        gamebg = pygame.image.load("./pic/shudumid.ppm")
    if n == 9:
        gamebg = pygame.image.load("./pic/shuduhard.ppm")


    screen.blit(gamebg,(0,0))
    pygame.display.update()

import testfile
import flappy
import wzy2048

import dian

import minesweeperHD
import minesweeperEZ
import minesweeperMD

# 插入背景介绍图
def inset_img(screen,name,n):
    game_img = pygame.image.load("./pic/"+name+str(n)+".ppm")
    screen.blit(game_img,(0,0))
    pygame.display.update()

def inset_img2(screen,name,n):
    game_img = pygame.image.load("./pic/"+name+str(n)+".jpg")
    screen.blit(game_img,(0,0))
    pygame.display.update()

def next_screen(list_hardS,n):
    # 进入第二关flappy bird表哥
    if n == 2:
        pygame.quit()
        pygame.init()
        screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("来者何人")
        print(list_hardS[1])
        if list_hardS[1]== 1:
            begin_image1 = pygame.image.load("./pic/shudueasywin.ppm")
            screen.blit(begin_image1, (0, 0))
            pygame.display.update()
        else:
            list_hard[6] = list_hard[6] + 1
            if list_hardS[1]== 2:
                begin_image1 = pygame.image.load("./pic/shudumidwin.ppm")
            if list_hardS[1] == 3:
                begin_image1 = pygame.image.load("./pic/shuduhardwin.ppm")

            screen.blit(begin_image1, (0, 0))
            pygame.display.update()
        count = 1
        n1 = True
        while n1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if list_hardS[1] == 2 and count == 1:
                        inset_img(screen,"shudumidwin",1)
                        count = count + 1
                    elif list_hardS[1] == 3 and count == 1:
                        inset_img(screen,"shuduhardwin",1)
                        count = count + 1
                    else:
                        if count == 1:
                            inset_img(screen,"fp",count)
                            count = count +1
                            if count == 7:
                                n1 = False
                        if count > 1:
                            inset_img(screen, "fp", count-1)
                            count = count + 1
                            if count == 8:
                                n1 = False


        n2 = True
        while n2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    # 调用flappy bird
                    flappy.main()

    # 进入第三关白王2048
    if n == 3:
        pygame.quit()
        pygame.init()
        screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("主界面")
        if list_hard[2] == 1:
            fp_image1 = pygame.image.load("./pic/fpwin20.ppm")
        else:
            fp_image1 = pygame.image.load("./pic/fpwin40.ppm")
        screen.blit(fp_image1, (0, 0))
        pygame.display.update()
        count = 1
        n1 = True
        while n1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if count <= 3:
                        inset_img(screen, "2048", count)
                        count = count + 1
                    else:
                        inset_img(screen, "48xuan", count-3)
                        count = count + 1

                if count == 5:
                    n1 = False
        n2 = True
        while n2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(event.pos)
                    (x, y) = event.pos
                    # 2048困难选择
                    if  x >= 666 and x <= 802 and y >= 582 and y <= 644:
                        inset_img(screen,"48xuan",1.5)
                        list_hard[3] = 1
                        n2 = False
                        test_fiel(3)
                        # n3(list_hard,3)

                    if x >= 245 and x <= 296 and y >= 585 and y <= 630 :
                        # list_hard[3] = 2
                        inset_img(screen,"48xuan",2)
                        n2 = False
                    print(list_hard[3])

        n4 = True
        while n4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    inset_img(screen,"48xuan",3)
                    n4 = False
        n5 = True
        while n5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    (x, y) = event.pos
                    # 2048困难选择
                    if x >= 245 and x <= 296 and y >= 585 and y <= 644:
                        inset_img(screen, "48mid", 1)
                        list_hard[3] = 2
                        n5 = False
                        test_fiel(3)
                        # n3(list_hard,3)
                    if x >= 666 and x <= 802 and y >= 582 and y <= 630:
                        inset_img(screen, "48hard", 1)
                        list_hard[3] = 3
                        # n3(list_hard,3)
                        n5 = False
                        test_fiel(3)


    # 进入第四关扫雷
    elif n == 4:
        pygame.quit()
        pygame.init()
        screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("来者何人")
        if list_hard[3] == 1:
            begin_image1 = pygame.image.load("./pic/48easywin.jpg")
            screen.blit(begin_image1, (0, 0))
            pygame.display.update()
        if list_hard[3] == 2:
            begin_image1 = pygame.image.load("./pic/48midwin.jpg")
            screen.blit(begin_image1, (0, 0))
            pygame.display.update()
            state = True
            add = 1
            while state:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        inset_img(screen, "add", add)
                        add = add + 1
                    if add == 7:
                        state = False
        if list_hard[3] == 3:
            begin_image1 = pygame.image.load("./pic/48hardwin.ppm")
            screen.blit(begin_image1, (0, 0))
            pygame.display.update()
            state = True
            add = 0
            while state:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        inset_img(screen, "add", 20 + add)
                        add = add + 1
                    if add == 3:
                        state = False
        count = 1
        n1 = True
        while n1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if count< 4 and  event.type == pygame.MOUSEBUTTONDOWN:
                    inset_img2(screen, "saolei", count)
                    count = count + 1
                if count == 4 and event.type == pygame.MOUSEBUTTONDOWN:
                    inset_img2(screen,"saoleixuan",0)
                    n1 = False
        n2 = True
        while n2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    (x, y) = event.pos
                    if x >= 187 and x <= 365 and y >= 590 and y <= 630:
                        inset_img2(screen, "saoleieasy", 0)
                        list_hard[4] = 1
                        n2 = False
                        test_fiel(4)
                        # n3(list_hard,4)
                    if x >= 625 and x <= 820 and y >= 590 and y <= 630:
                        inset_img2(screen, "saoleixuan", 1)
                        n2 = False
        n4 = True
        while n4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    inset_img2(screen, "saoleibutton",0 )
                    n4 = False
        n5 = True
        while n5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = event.pos
                    if x >= 245 and x <= 296 and y >= 585 and y <= 644:
                        inset_img2(screen, "saoleimid",1 )
                        list_hard[4] = 2
                        n5 = False
                        # n3(list_hard,4)
                        test_fiel(4)
                    if x >= 666 and x <= 802 and y >= 582 and y <= 630:
                        inset_img(screen, "saoleihard",1 )
                        list_hard[4] =3
                        n5 = False
                        test_fiel(4)
                        # n3(list_hard,4)



    # 解开封印24点
    elif n == 5:
        pygame.quit()
        pygame.init()
        screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("主界面")
        print(list_hard[4])
        # print(list_hardS[4])
        if list_hard[4] == 1:
            begin_image1 = pygame.image.load("./pic/saoleieasywin.jpg")
            screen.blit(begin_image1, (0, 0))
            pygame.display.update()
        else:
            if list_hard[4] == 2:
                begin_image1 = pygame.image.load("./pic/saoleimidwin.jpg")
            if list_hard[4] == 3:
                begin_image1 = pygame.image.load("./pic/saoleihardwin.ppm")

            screen.blit(begin_image1, (0, 0))
            pygame.display.update()
            count = 1
            n1 = True
            while n1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        inset_img(screen, "saolei2win", count)
                        count = count + 1
                    if count == 11:
                        n1 = False
        n2 = True
        num = 0
        while n2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    inset_img2(screen,"dian",num)
                    num = num + 1
                if num == 3:
                    n2 = False
        n4 = True
        while n4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    dian.main()

    elif n == 6:
        pygame.quit()
        pygame.init()
        screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("主界面")
        if list_hard[5] > 24 :
            begin_image1 = pygame.image.load("./pic/dianwinlarge.ppm")
            screen.blit(begin_image1, (0, 0))
            pygame.display.update()
        else:
            if list_hard[4] == 1:
                inset_img(screen, "dianwinlose", 0)
            else:
                inset_img(screen,"dianwinwin",0)
            count = 1
            n1 = True
            while n1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if list_hard[5] == 24 and list_hard[4] == 1:
                            inset_img(screen, "dianwinlose", count)
                            count = count + 1
                            if count == 2:
                                n3(list_hard,5)
                        if list_hard[5] == 24 and list_hard[4] != 1:
                            inset_img(screen, "dianwinwin", count)
                            count = count + 1
                    if count == 2:
                        n1 = False
        n2 = True
        k = 1
        while n2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    inset_img(screen,"wu",k)
                    k = k+1
                if k == 4:
                    n2 = False
                    n3(list_hard,5)


def lose_screen(n):
    pygame.quit()
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    if n == 1:
        img = pygame.image.load("./pic/loseshudu.ppm")
    if n == 2 :
        img = pygame.image.load("./pic/losefp.ppm")
    if n == 3:
        img = pygame.image.load("./pic/lose48.jpg")
    if n == 4:
        if list_hard[4] == 1:
            img = pygame.image.load("./pic/saoleieasylose.jpg")
        if list_hard[4] == 2:
            img = pygame.image.load("./pic/saoleimidlose.jpg")
        if list_hard[4] == 3:
            img = pygame.image.load("./pic/saoleihardlose.jpg")
    if n == 5:
        img = pygame.image.load("./pic/losedian.jpg")
    pygame.display.set_caption("主界面")
    screen.blit(img, (0, 0))
    pygame.display.update()
    ln = True
    while ln:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ln = False
                start_screean()

        pygame.display.update()

def test_fiel(n):
    n4 = True
    while n4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                if n == 3:
                    testfile.maintest_3()
                if n == 4:
                    testfile.maintest_4()
                if n == 5:
                    testfile.maintest_5()

def n3(list,n):
    n4 = True
    while n4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                if n == 3:
                    wzy2048.main()
                if n == 4:
                    print(list[4])
                    if list[4] == 1:
                        minesweeperEZ.main()
                    if list[4] == 2:
                        minesweeperMD.main()
                    if list[4] == 3:
                        minesweeperHD.main()
                if n == 5:
                    if list[4] == 1 and list[5] == 24:
                        start_screean()
                    else:
                        pygame.quit()
                        SinglePlayerGameB.main_singleplayer()

import SinglePlayerGameB
import minesweeperHD
import minesweeperMD
# 五子棋主界面
def Win_screen():
    pygame.init()
    screen = pygame.display.set_mode((1620,1080))
    pygame.display.set_caption("来者何人")
    if RESULT == "white":
        begin_image1 = pygame.image.load(r"D:/Agame/gamebox/游戏总文件/pic/losewu.ppm")  # 要加完路径，因为是从五子棋文件跳回
    else:
        begin_image1 = pygame.image.load(r"D:/Agame/gamebox/游戏总文件/pic/wuwin.ppm")
    screen.blit(begin_image1,(0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pygame.quit()
            #     sys.exit()





if __name__ == '__main__':
    start_screean()