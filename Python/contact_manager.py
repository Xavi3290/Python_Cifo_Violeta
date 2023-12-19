d = {}

def add_contact(name, number):
    if name in d.keys():
        return "Contact already exists."
    #for key in d.keys():   #La manera en if es mas rapida i mas eficiente y te hace lo mismo
    #    if key == name:
    #       return "Contact already exists."
    d[name] = number
    return f"Contact {name} added."

def delete_contact(name):
    find = False
    for key in d.keys():
        if key == name:
            find = True
    if find:     
        d.pop(name)
        return f"Contact {name} deleted."
    else: 
        return "Contact not found."  

def search_contact(name):
    for key, value in d.items():
        if key == name:
            return value
    return "Contact not found."