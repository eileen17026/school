#1到100中的所有奇數和

sum = 0
for x in range(1, 101):
    if x % 2 != 0:
        sum += x

print(sum)