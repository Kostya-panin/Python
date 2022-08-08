#парам пам пам
def numbervowels(s):
    kol=0
    for symbol in s:
        if symbol in 'аеёиоуэюя':
            kol=kol+1
    return kol
string="пара-ра-рам рам-пам-папам па-ра-па-дам"
kol=set([numbervowels(i) for i in string.split(" ")])
if len(kol)==1:
    print("Парам пам-пам")
else:
    print("Пам парам")