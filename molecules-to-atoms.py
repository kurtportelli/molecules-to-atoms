def parse_molecule (formula):
    import re
    
    #change all brackets to same type - curly because of regex
    formula = formula.replace('(', '{').replace(')', '}').replace('[', '{').replace(']', '}')
    
    #find all elements and create a dict with them
    elements = re.findall(r'[A-Z][a-z]*', formula)
    result = {element: 0 for element in elements}
    
    #convert the formula to a list for easier access
    formula_list = re.findall(r'[A-Z][a-z]*|\d+|{|}', formula)
    
    #convert all numbers to integers
    for i in range(len(formula_list)):
        try:
            formula_list[i] = int(formula_list[i])
        except:
            pass
            
    #add a 1 after elements and brackets without a number
    index = 0
    while index < len(formula_list):
        if (formula_list[index] in result or formula_list[index] == '}') and index + 1 == len(formula_list):
            formula_list.insert(index + 1, 1)
        if (formula_list[index] in result or formula_list[index] == '}') and not isinstance(formula_list[index + 1], int):
            formula_list.insert(index + 1, 1)
        index += 1
    
    #count the number of bracket pairs
    brackets = formula.count('}')
    
    #for every bracket pair
    for each in range(brackets):
        end_index = formula_list.index('}')
        multiplier = formula_list[end_index+1]
        
        #search for numbers up to start bracket and multiply them by the multiplier
        index = end_index - 1
        while formula_list[index] != '{':
            if isinstance(formula_list[index], int):
                formula_list[index] *= multiplier
            index -= 1
        
        #remove the brackets and multiplier from list
        del formula_list[end_index+1]
        del formula_list[end_index]
        del formula_list[index]
    
    #prepare lists to be added to dict
    element_list = formula_list[::2]
    amount_list = formula_list[1::2]
    zipped_lists = zip(element_list, amount_list)
    
    #add lists to dict
    for element, amount in zipped_lists:
        result[element] += amount
    
    return result
