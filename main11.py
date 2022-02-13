import math
from urllib.request import Request, urlopen
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

x = str(data)

list_1 = x.split(",")  #xwrizw se kommatia

y = list_1[0].split(":")

number = y[1]

number = int(number)

z = list_1[1].split(":")

number2 = z[1]   #metablhth gia na ekxwrhsw to noumero toy randomness kai na to kanw 16diko

number2 = str(number2)

number2 = number2.encode("utf-8")

number2_hex = number2.hex()

txt = number2_hex

for i in range(1,20):
    number = number - 1

    req = Request('https://drand.cloudflare.com/public/' + str(number),headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})

    x = str(data)

    list_1 = x.split(",")

    z = list_1[1].split(":")

    number2 = z[1]

    number2 = str(number2)

    number2 = number2.encode("utf-8")

    number2_hex = number2.hex()

    txt += number2_hex

w = [ float(txt.count(a)) / len(txt) for a in dict.fromkeys(str(txt)) ]

entropy = -sum([ b * math.log(b) / math.log(2.0) for b in w])

print("THE RESULT OF ENTROPY IS :")

print(entropy)


