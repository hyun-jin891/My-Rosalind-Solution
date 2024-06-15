import re
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

regularExpression = "(?=" + "N[^P][ST][^P]" + ")"
compiler = re.compile(regularExpression)


name = input()
f = open(name, 'r')
ID_list = []
result_ID_list = []
res = []

for line in f.readlines():
    result_ID_list.append(line[:-1])
    end_index = line.find("_")
    if end_index == -1:
        ID_list.append(line[:-1])
    else:
        ID_list.append(line[:end_index])
f.close()

for i in range(len(ID_list)):
    currentID = ID_list[i]
    
    driver = webdriver.Chrome()
    driver.get("https://www.uniprot.org/uniprotkb/" + currentID)
    time.sleep(2)
    
    History_button = driver.find_element(By.LINK_TEXT, "History")
    History_button.click()
    
    time.sleep(3)
    
    fasta_file = driver.find_elements(By.LINK_TEXT, "(fasta)")[0]
    fasta_file.send_keys(Keys.CONTROL + 't')

    time.sleep(2)
    
    url = fasta_file.get_attribute('href')
    driver.get(f"{url}")
    txt = driver.find_element(By.TAG_NAME, "pre").text
    #time.sleep(1)
    driver.close()
    
    temp = txt.split("\n")
    seq = ""
    
    for j in range(1, len(temp)):
        if temp[j] == "":
            continue
        seq += temp[j]
        
    motifs = compiler.finditer(seq)
    
    count = 0
    res_element = ""
    for motif in motifs:
        if count == 0:
            res_element += result_ID_list[i] + '\n'
            count += 1
        res_element += str(motif.span()[0] + 1) + " "
    
    res.append(res_element[:-1])
    

for i in range(len(res)):
    if len(res[i]) == 0:
        continue
    print(res[i])       
   
    
    
        
















while (True):
    seq = input()
    
    if seq == "0":
        break
    else:
        motifs = compiler.finditer(seq)
        
        for motif in motifs:
            print(motif.span()[0] + 1, end=" ")
        
        print()


