import csv 
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)    

data.pop(0)

new_data = []

for i in range(len(data)):
    num = data[i][1]
    new_data.append(float(num))

n = len(new_data)
new_data.sort()
if n%2 = 0:
    median = float(new_data[n//2])
    median1 = float(new_data[n//2-1])
    median2 = (median+median1)/2

else:
    median2 = new_data[n//2]

print('the median is '+ str(median2))
