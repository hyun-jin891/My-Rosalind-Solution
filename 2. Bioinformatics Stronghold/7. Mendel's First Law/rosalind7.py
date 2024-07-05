def probability(k, m, n):
    total = k + m + n
    pair1 = (k / total) * ((k - 1) / (total - 1))
    pair2 = (k / total) * (m / (total - 1))
    pair3 = (k / total) * (n / (total - 1))
    pair4 = (m / total) * ((m - 1) / (total - 1)) * 0.75
    pair5 = (m / total) * (n / (total - 1)) * 0.5
    pair6 = (m / total) * (k / (total - 1))
    pair7 = (n / total) * (k / (total - 1))
    pair8 = (n / total) * (m / (total - 1)) * 0.5
    
    return pair1 + pair2 + pair3 + pair4 + pair5 + pair6 + pair7 + pair8


file_name = input()
f = open(file_name, 'r')

line = f.readline()

k, m, n = map(int, line.split())

print(probability(k, m, n))
f.close()