import random

class Card:
    color=''
    value=0
    def printString(self):
        strValue = ''
        if self.value==1:
            strValue = "A"
        elif self.value==11:
            strValue = "J"
        elif self.value ==12:
            strValue = "Q"
        elif self.value==13:
           strValue = "K"
        else:
           strValue = str(self.value)
        return self.color+strValue

class Poke:
    colors = ["红桃", "黑桃", "方片", "草花"]
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    cards={}
    def __init__(self):
        # 生成52张扑克，印刷扑克
        index = 0
        for i in range(4):
            for j in range(13):
                self.cards[index] = Card()
                self.cards[index].value=self.values[j]
                self.cards[index].color=self.colors[i]
                index+=1
    def outputCards(self):
        index2 = 0;
        for i in self.cards:
            if index2 % 13 == 0:
                print()
            print(self.cards[i].printString(),end=" ")
            index2 += 1
        print()
    def shuffle(self):
        random.shuffle(self.cards)

    # 一手牌
    def getOneHands(self):
        cardHands = {}
        for i in range(5):
            cardHands[i] = self.cards[i]
        return cardHands
    def judgeHandType(self,hands):
        bIsSameColor = False
        bIsShunzi = False
        colorSets=set()
        for i in hands:
            colorSets.add(hands[i].color)
        if len(colorSets) == 1:
            bIsSameColor = True  #同花
        valueSets=set()
        valueLists=[]
        for i in hands:
            valueSets.add(hands[i].value)
            valueLists.append(hands[i].value)
        valueLists.sort()
        diff = valueLists[4] - valueLists[0]
        if diff == 4 & len(valueSets) == 5:
            bIsShunzi = True
        if bIsSameColor & bIsShunzi:
            print("同花顺")
        elif bIsSameColor:
            print("同花")
        elif bIsShunzi:
            print("顺子")
        elif len(valueSets) == 5: #这5张牌不是顺子，并且值都不同
            print("杂牌")
        elif len(valueSets) == 4:
            print("一对")
        else:
            #map的key保存的是牌的值，map的值保存的是同样值的牌的列表
            map = {}
            #将一手牌的数据，从数组结构，转变成map结构
            for i in hands:
            #看card这张牌的值是否在map的key中存在
                if hands[i].value in map: #如果存在
                    lst = map[hands[i].value]
                    lst.append(hands[i])
                else: #不存在
                    lst = []
                    lst.append(hands[i])
                    map.update({hands[i].value:lst})
            if len(map) == 2: #4带1, 3带2
                bIsFourWithOne = False
                for obj in map.items():
                    #entry的值是一个List
                    if len(obj[1]) == 4:
                        bIsFourWithOne = True
                        break
                if bIsFourWithOne:
                    print("四带一")
                else:
                    print("三带二")
            elif len(map) == 3: #221, 311
                bIsThreeOneOne = False
                for obj in map.items():
                    if len(obj[1])==3:
                        bIsThreeOneOne = True
                        break
                if bIsThreeOneOne:
                    print("三条")
                else:
                    print("两对")

pock=Poke()
pock.outputCards()
pock.shuffle()
print()
print("\n洗牌后")
pock.outputCards()

hands=pock.getOneHands()
print()
print("分到的一手好牌是")
print()
for i in hands:
    print(hands[i].color,hands[i].value,end=' ')
print('\n\n牌型是：')
pock.judgeHandType(hands)
