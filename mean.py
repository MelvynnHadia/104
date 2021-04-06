import csv 
with open('SOCR-HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

new_data = []

for i in range(len(data)):
    num = data[i][1]
    new_data.append(float(num))

n = len(new_data)
total = 0
for x in new_data: 
    total+=x

mean = total/n

print("mean is "+str(mean))