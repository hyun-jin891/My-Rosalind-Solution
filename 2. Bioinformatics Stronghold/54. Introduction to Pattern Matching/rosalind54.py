#다수의 motif 정리를 위한 사전으로서 trie를 사용


class Node:
    def __init__(self, base, num, data=None):
        self.base = base
        self.data = data
        self.child = {}
        self.num = num

class Trie:
    def __init__(self, head=None):
        self.head = head
        self.fin_n = 1
    
    def insert(self, motif):
        current_node = self.head
        
        for i in range(len(motif)):
            if motif[i] not in current_node.child:
                print(current_node.num, end=" ")
                self.fin_n += 1
                if i == len(motif) - 1:
                    newNode = Node(motif[i], self.fin_n, motif)
                else:
                    newNode = Node(motif[i], self.fin_n)
                
                print(self.fin_n, motif[i])
                current_node.child[motif[i]] = newNode
            
            current_node = current_node.child[motif[i]]
        

name = input()
f = open(name, 'r')
head = Node("", 1)

pattern_Trie = Trie(head)

for seq in f.readlines():
    seq = seq[:-1]
    pattern_Trie.insert(seq)

        
        
        
f.close() 