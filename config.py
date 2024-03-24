from configparser import ConfigParser

def config(filename="database.ini", section="postgresql"):
    #create a pareser
    parser= ConfigParser()
    #read config gile
    parser.read(filename)
    db= {}

    if parser.has_section(section): #verification, else raise Exception
        params= parser.items(section)
        for param in params:
            db[param[0]]= param[1] #key and value assignment
    else:
        raise Exception('Section{0} is not found in the {1} file.'.format(section,filename))
    
    #print(db)
    return db

config()
