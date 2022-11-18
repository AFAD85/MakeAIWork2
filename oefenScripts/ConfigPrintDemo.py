from configparser import ConfigParser

config = ConfigParser()
config.read("appel_config.ini")

username = input("Wie bende gij? : ")

if username == "Amad69":
    password = input("Doe maar ff bewijzen met je password: ")
    if password != "RijbewijsYes15112022":
        print("NEE DAS FOUT SNODAARD!")
        exit(0)
        
        
if username == "AntonSoixanteNeuf":
    password = input("Doe maar ff bewijzen met je password: ")
    if password != "RUSTAAAGH123":
        print("NEE DAS FOUT SNODAARD!")
        exit(0)
        
if username == "default":
    password = input("Doe maar ff bewijzen met je password: ")
    if password != "blah":
        print("NEE DAS FOUT SNODAARD!")
        exit(0)
    

try:
    config_data = config[username]
except:
    print("User not found")
    exit(0)
    
welkomsboodschap = config_data["WelkomsBoodschap"]
print(welkomsboodschap)
