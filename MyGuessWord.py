from random import randint

# 函数：打印新的字符串
def printWords(wordNow):
    for w in wordNow:
        print(w,end='')
    print()
words = ('static','abstract','extends','implements','throw','orange','student','select','group','interface')
# print(len(words))
n=randint(0,9)
selectWord=words[n]  #随机选中猜测单词
print(selectWord)

wordnow=[]#定义用户猜测的列表
# 初始化用户猜测的列表
for i in range(len(selectWord)):
    wordnow.append('-')
# 打印开始没猜的列表
for w in wordnow:
    print(w,end='')
print()
userTimes = 5;#用户可以猜5次

while True:
    strGuess=input('请输入猜测的字母：')
    findIndex=selectWord.find(strGuess)
    # print(findIndex)测试打印查找位置
    if findIndex<0:
        userTimes-=1
        if userTimes==0:
            break
        print('还剩'+str(userTimes)+'次机会')
        printWords(wordnow)
    else:
        for i in range(len(selectWord)):
            tempC=selectWord[i]
            if(tempC==strGuess):
                wordnow[i]=tempC
        printWords(wordnow)
        # 如果wordNow数组中不在包含 -，说明所有的字符全部被猜出来了
        if '-' not in wordnow:
            break
if userTimes>0:
    print('恭喜，你猜对了')
else:
    print('你输了，正确答案是')
    print(selectWord)