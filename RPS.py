import random

usr_win = 0
comp_win = 0
hand = {'g':'グー','c':'チョキ','p':'パー'}
#乱数を手に変えるための配列
num_tohand = ['g','c','p']
#キーの手が勝つ場合の相手の手
judge = {'g':'c','c':'p','p':'g'}
play = 1

while(usr_win<3 and comp_win<3):
    print(str(play) +'回戦')
    print("グー(g)、チョキ(c)、パー(p)のいずれかを入力してください：",end="")
    #標準入力
    usr =  input()
    #例外(書かなくてもいい)
    if (not(usr in hand)):
        continue
    #乱数生成(0以上2以下)
    r = random.randint(0,2)
    comp = num_tohand[r]

    print("コンピュータ："+str(hand[comp])+" ユーザー："+str(hand[usr]))

    if (usr == comp):
        print("あいこ")
    elif (judge[usr] == comp):
        usr_win += 1
        print("ユーザーの勝ち")
    else:
        comp_win += 1
        print("コンピュータの勝ち")

    print("コンピュータ："+str(comp_win)+"勝, ユーザー："+str(usr_win)+"勝")
    play+=1

if(usr_win >= 3):
    print("ユーザーが"+str(usr_win)+"回勝ちました!")
elif(comp_win >= 3):
    print("コンピュータが"+str(comp_win)+"回勝ちました!")