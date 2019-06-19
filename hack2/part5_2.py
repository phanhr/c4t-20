districtNames = ['ST', 'BD', 'BTL', 'CG','DD', 'HBT']
population = [150300, 247100, 333300, 266800, 420900, 318000]
indexMax = population.index(max(population))
indexMin = population.index(min(population))
print('District has highest population: ', districtNames[indexMax])
print('District has lowest population: ', districtNames[indexMin])