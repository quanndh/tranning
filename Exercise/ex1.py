districts = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
population = [150300, 247100, 333300, 266800, 420900, 318000]
matdo = []

max = 0
min = 0
indexMax = 0
indexMin = 0

for i in range(len(population)):
    if population[i] > max:
        max = population[i]
        indexMax = i
    if population[i] < min:
        min = population[i]
        indexMin = i

for i in range(len(districts)):
    matdo.append(population[i] / area[i])

print(indexMax, indexMin)
print("It nhat:" , districts[indexMin], "nhieu nhat:", districts[indexMax])
print(matdo)