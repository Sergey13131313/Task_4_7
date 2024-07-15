# hexata = 'AA'
# print(type(hexata))
# hexata = int(hexata, 16)
# print(hexata)
# print(type(hexata))
# hexata = int(hexata)
# print(hexata)
# print(type(hexata))
# hexata = bin(hexata)
# print(hexata)
# print(type(hexata))

mac = "AAAA:BBBB:CCCC"

mac = mac.split(':')
print(mac)
mac1 = []
for x in mac:
    mac1.append(x[:2])
    mac1.append(x[2:])
print(mac1)
mac2 = []
for x in mac1:
    x = int(x, 16)
    x = bin(x)
    mac2.append(x)
print(mac2)
mac3 = ''
mac3 = mac3.join(mac2)
print(mac3)

