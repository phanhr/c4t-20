districtNames = ['ST', 'BD', 'BTL', 'CG','DD', 'HBT']
totalPopulation = [150300, 247100, 333300, 266800, 420900, 318000]
districtArea = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
populationDensity = []  
endIndex = len(totalPopulation)
for i in range(endIndex):
    populationDensity.append(totalPopulation[i]/districtArea[i])
print(*populationDensity,sep=', ')
averagePDensity = []
districtSum = len(districtNames)
for a in range(districtSum):
    averagePDensity.append(populationDensity[a]/districtSum)
print(*averagePDensity, sep=' ')