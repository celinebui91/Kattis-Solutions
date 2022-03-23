import sys

var_names_dict = {}  # 'name' --> 'number'

values_of_var = {} # 'number' --> 'name'


for line in sys.stdin:
    lines = line.split()
    
    starting_word = lines[0]
    
    
    if starting_word == 'def':
        
        var_name = lines[1]
        var_value = lines[2]

        if var_name in var_names_dict.keys():
            del values_of_var[int(var_names_dict[var_name])]
            

        var_names_dict[var_name] = var_value
        values_of_var[int(var_value)] = var_name

    elif starting_word == 'calc':
        
        if len(list(filter(lambda key: key in var_names_dict.keys(), lines[1::2]))) != len(lines[1::2]):
            print(" ".join(lines[1:]), 'unknown')
            
        else:
            val = eval(" ".join(map(lambda key: var_names_dict[key] if key in var_names_dict.keys() else key, lines[1:-1])))
            if val in values_of_var.keys():
                print(" ".join(lines[1:]), values_of_var[val])
            else:
                print(" ".join(lines[1:]), 'unknown')
                
    else:
        var_names_dict.clear()
        values_of_var.clear()
