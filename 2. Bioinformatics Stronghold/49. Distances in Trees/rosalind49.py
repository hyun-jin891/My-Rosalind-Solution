from collections import deque

def construct_tree(original):
    str1 = ""
    res = []
    
    for i in range(len(original)):
        if original[i] == '(' or original[i] == ')':
            if len(str1) != 0:
                res.append(str1)
                str1 = ""
            res.append(original[i])
        elif original[i] == ',':
            if len(str1) != 0:
                res.append(str1)
                str1 = ""
            res.append(original[i])
        elif original[i] == " ":
            continue
        else:
            str1 += original[i]
    if len(str1) != 0:
        res.append(str1)
    return res
            
def cal_dist(tree, target1, target2):
    targets = (target1, target2)
    stack = deque()
    res = 0
    flag = False
    complete_flag = False
    
    for i in range(len(tree)):
        current_str = tree[i]
        
        if current_str in targets and flag == False:
            flag = True
            continue
        
        if flag:
            if current_str == '(':
                stack.append(current_str)
            elif current_str == ')':
                if len(stack) == 0 and complete_flag == True:
                    res += 1
                    return res
                elif len(stack) == 0:
                    res += 1
                else:
                    stack.pop()
            else:
                if current_str in targets:
                    if len(stack) == 0 and tree[i - 1] != ',':
                        return res
                    res += len(stack)
                    res += 1
                    complete_flag = True  
            

ori_trees = []

name = input()
f = open(name, 'r')

flag = False
ori_tree = ""
target_nodes = []
tree_flag = False

for line in f.readlines():
    if line == '\n':
        continue
    if line[-2] == ';':
        flag = True
        ori_tree += line[:-2]
        ori_trees.append(ori_tree)
        tree_flag = True
        ori_tree = ""
        continue
    if flag == False:
        ori_tree += line[:-1]
    if tree_flag:
        tree_flag = False
        flag = False
        target_nodes.append(tuple(line[:-1].split()))

for i in range(len(ori_trees)):
    current_ori_tree = ori_trees[i]
    current_target1 = target_nodes[i][0]
    current_target2 = target_nodes[i][1]
    
    current_tree = construct_tree(current_ori_tree)
    print(cal_dist(current_tree, current_target1, current_target2), end=' ')    





        