import random

def hReturn(name):
    return "Shut up " + name

def handle_response(user):
    if user == 'tarantula0':
        return hReturn("Joseph")
    elif user == 'zenith.edu':
        return hReturn("Josh")
    elif user == 'buzzybees':
        return hReturn("Jack")
    elif user == 'cnm4211':
        return hReturn("Cooper")
    elif user == 'snowbeanboy':
        return hReturn("Sean")
    elif user == 'awayy.':
        return hReturn("Yonas")
    elif user == 'turkey0438':
        return hReturn("Bella")
    elif user == '_hyyper':
        return hReturn("Jacob")
    elif user == 'rob_7203':
        return hReturn("Lib")
    elif user == 'senpainero':
        return hReturn("Zach")
    elif user == 'thatlittleanna':
        return hReturn("Anne")
    elif user == 'pjter':
        return hReturn("Peej")
    elif user == 'fable.exe':
        return hReturn("Jordan")
    elif user == 'freecarpets':
        return hReturn("Rome")
    elif user == 'alithaya':
        return hReturn("Germany")
    elif user == '.kwamkwam':
        with open('fat.txt', 'r') as file:
            lines = file.read()
        linearray = lines.split(',')
        print(linearray[:10])
        random.shuffle(linearray)
        processed_lines = []
        for line in linearray:
            line = line.replace('\n', ', ')
            processed_lines.append(line)
        result = ''.join(processed_lines)
        return hReturn(result)
    elif user == 'danoferth1':
        return hReturn("Daniel")
    elif user == 'theroheryn':
        return hReturn("Stephen")
    elif user == 'pizzakingi':
        return hReturn("Caleb")
    elif user == 'crunk.exe':
        return hReturn("Paul")
    elif user == 'stacey#3106':
        return hReturn("Stacey")
    elif user == 'tamtam9758':
        return hReturn("Tamia")
    elif user == 'dwayne5440':
        return hReturn("Dwayne")
    elif user == 'krp7038':
        return hReturn("Ben")
    else:
        return 'seans alt lol'