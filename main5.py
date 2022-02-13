from collections import Counter
from collections import defaultdict
f = open("tc.txt", "r")
x = f.read()

f.close()
mikra = x.lower()

mikra = ''.join([i for i in mikra if not i.isdigit()])#sbhnei olous tous aritmous

mikra = ''.join([e for e in mikra if e.isalnum() or e == ' '])#sbnei ola ta sumbola

s = mikra.split()
Counter = Counter(s)
most_freq = Counter.most_common(10)
print("ΔΕΚΑ ΔΗΜΟΦΙΛΕΣΤΕΡΕΣ ΛΕΞΕΙΣ ΕΙΝΑΙ:")
print('\n')
print(most_freq)


list1 = [word[:2] for word in mikra.split()]

print('\n')
print('\n')
print('\n')
list1 = list(dict.fromkeys(list1))
temp = defaultdict(int)
print("ΟΙ ΤΡΕΙΣ ΠΡΩΤΟΙ ΣΥΝΔΙΑΣΜΟΙ ΤΩΝ ΠΡΩΤΩΝ ΔΥΟ ΓΡΑΜΜΑΤΩΝ ΠΟΥ ΑΡΧΙΖΟΥΝ ΟΙ ΠΕΡΙΣΣΟΤΕΡΕΣ ΛΕΞΕΙΣ ΕΙΝΑΙ: ")
print('\n')
for i in range(3):
    for sub in list1:
        for wrd in sub.split():
            temp[wrd] +=1
            res = max(temp, key = temp.get)
    print(str(res))
    list1.remove(res)


list2 = [word[:3] for word in mikra.split()]

print('\n')
print('\n')
print('\n')
list2 = list(dict.fromkeys(list2))
temp = defaultdict(int)
print("ΟΙ ΤΡΕΙΣ ΠΡΩΤΟΙ ΣΥΝΔΙΑΣΜΟΙ ΤΩΝ ΠΡΩΤΩΝ ΤΡΙΩΝ ΓΡΑΜΜΑΤΩΝ ΠΟΥ ΑΡΧΙΖΟΥΝ ΟΙ ΠΕΡΙΣΣΟΤΕΡΕΣ ΛΕΞΕΙΣ ΕΙΝΑΙ: ")
print('\n')
for i in range(3):
    for sub in list2:
        for wrd in sub.split():
            temp[wrd] +=1
            res = max(temp, key = temp.get)
    print(str(res))
    list2.remove(res)

















