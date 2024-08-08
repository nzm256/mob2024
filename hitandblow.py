import random

answer = [random.randint(0,9),random.randint(0,9),random.randint(0,9)]
print(answer)

for i in range(10):
    usr_input = str(input())
    hit = 0
    blow = 0
    #answerの各要素がhitもしくはblowに使われたかどうか
    matched = [False]*3
    #hitしなかったusr_inputのindex
    checkBlow = []

    #先にhitを確認
    for i in range(3):
        if(answer[i] == int(usr_input[i])):
            hit+= 1
            matched[i] = True #使用済みにする
        else:#hitしなかった場合blowの要確認
            checkBlow.append(i) 
    #blowの確認
    for i in checkBlow:
        for j in range(3):
            if(matched[j]):#すでに使われていたら飛ばす
                continue
            if(answer[j] == int(usr_input[i])):#blowした
                blow += 1
                matched[j] = True #使用済みにする
                break  #これ以上の探索はしてはいけないのでbreak
    
    print("Hit="+str(hit)+",Blow="+str(blow))
    if(hit == 3):
        print("正解です！")
        break