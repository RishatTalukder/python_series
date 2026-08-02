def power(num, powe):
    #local scope
    # print(num**powe)
    
    return num**powe

def name_format(first_name, last_name):
    full = f"{first_name.title()} {last_name.title()}"
    
    return {
        "first" : first_name.title(),
        "last" : last_name.title(),
        'full': full
    }