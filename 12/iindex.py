import csv

def csv_dict(file):
    l = []
    f = open(file)
    csv_dict_reader = csv.DictReader(f)
    for line in csv_dict_reader:
        l.append(line)
    f.close()
    return l

def find_word(dict,word):
    fw = {}
    for name_of_cat in dict:
        statement = name_of_cat['Last Statement']
        if word in statement:   
            execute = name_of_cat['Execution #']
            fw.setdefault(word,[])
            fw[word].append(execute)   
    return fw
        
    
    

print(find_word(csv_dict('offenders.csv'),'bless'))
        
        