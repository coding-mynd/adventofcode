with open(".\\input.txt","r") as f:
    lines = f.readlines()


calories = 0
highest = [0,0,0]
total = 0
count = -1

for line in lines:
    count += 1
    try:
        calories += int(line.strip())
    except:
        for i,s in enumerate(highest):
            if calories > highest[i]:
                if i == len(highest)-1:
                    highest[i] = calories
                    break
                else:
                    highest[i+1] = highest[i]
                    highest[i] = calories
                    break
        calories = 0


for i in highest:
    total += i
print(total)

