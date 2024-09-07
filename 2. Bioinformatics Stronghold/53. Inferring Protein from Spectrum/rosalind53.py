mass_table = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E"  : 129.04259, "F"  : 147.06841, "G"  : 57.02146, "H"  : 137.05891, "I"  : 113.08406, "K"  : 128.09496, "L"  : 113.08406, "M"  : 131.04049, "N"  : 114.04293, "P"  : 97.05276, "Q"  : 128.05858, "R"  : 156.10111, "S"  : 87.03203, "T"  : 101.04768, "V"  : 99.06841, "W"  : 186.07931, "Y"  : 163.06333}

name = input()
f = open(name, 'r')
prefix_spectrum = []

for line in f.readlines():
    prefix_spectrum.append(float(line[:-1]))

res = ""

for i in range(1, len(prefix_spectrum)):
    extra_mass = prefix_spectrum[i] - prefix_spectrum[i - 1]
    candidate = []
    for aa in mass_table.keys():
        if abs(extra_mass - mass_table[aa]) < 1:
            candidate.append((aa, abs(extra_mass - mass_table[aa])))
    minMass = candidate[0][1]
    minAA = candidate[0][0]
    for aa, mass in candidate:
        if minMass > mass:
            minAA = aa
            minMass = mass
    
    res += minAA
            

print(res)
        
f.close()