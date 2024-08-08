answer = 'apple'
opened = [False]*len(answer)
#開けた回数
count = 0

while(count < len(answer)):
    print("文字を入力してください:",end='')
    #標準入力
    user_input = input()
    for i in range(0,len(answer)):
        #一致し、かつ未開の場合
        if(answer[i] == user_input and (not opened[i])):
            opened[i] = True
            count+=1
        
        if(opened[i]):
            print(answer[i]+' ',end = '')
        else:
            print('_ ',end='')
    print()
print("正解です！")