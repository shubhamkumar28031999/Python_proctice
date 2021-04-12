from functools import cmp_to_key


class Player:
    def __init__(self, name, score, dic=None):
        self.name = name
        self.score = score
        if score in dic:
            dic[score].append(name)

        else:
            li=[]
            li.append(name)
            dic[score] = li
    def display(self,dic=None):
        print(dic)
    #
    # def __repr__(self):
    #
    # def comparator(a, b):


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
Player.display()
# data = sorted(data, key=cmp_to_key(Player.comparator))
# for i in data:
#     print(i.name, i.score)
# amy 100
# david 100
# heraldo 50
# aakansha 75