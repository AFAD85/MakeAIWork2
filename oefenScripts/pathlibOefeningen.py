import pathlib
from pathlib import Path


# huidige bestand
# LET OP!! __file__ werkt niet in jupyter... geen idee waarom, en teveel tijd aan besteed om er nog verder naar te willen zoeken
p = Path(__file__)
print(p)

#directory van huidige bestand
pDir = Path(__file__).parent



# iets in de shell/terminal voegt de eerste regel die begint met $ toe de p variabele heeft enkel de bestandsnaame+locatie (in linux notatie, dus misschien nodig om \ weer in / te veranderen?)

# even duidelijk maken waar de probeerseltjes worden geprint :
print('Liesje leerde lotje lopen')
# object (variabele) p printen
print(p)
print(pDir)
# working directory printen :
print("working directory : ", p.cwd())

# bestandsnaam van huidige bestand printen : 
print("filename : ", p.name)

# windoos home directory printen : 
print("Home directory : ", p.home())

# subdirectory aanspreken
huidigeDirectory = p.cwd() / 'oefenScripts'
print(huidigeDirectory)

# iets doen voor alle bestanden in map of alle bestanden die x zijn (bijvoorbeeld alle jpegies ofzo)
print('alle bestanden in map')
for files in huidigeDirectory.iterdir():
    print(files)

# alleen de txt bestanden
print('alle txt bestanden in map')
for files in huidigeDirectory.iterdir():
    if files.suffix == ".txt":
        print(files)
        
# nieuwe directory maken in directory (exist_ok=True zorgt er voor dat je geen error krijgt als de map al bestaat)
nDir = Path(__file__).parent / 'testBlah'
Path.mkdir(nDir, exist_ok=True)

# alle bestanden printen uit de map INCLUSIEF de submappen
print('alle bestanden en mappen in map en submappen')
for file in pDir.rglob("*"):
    print(file)

# alle .txt bestanden printen uit de map INCLUSIEF de submappen
print('alle .TXT bestanden in map en submappen')
for file in pDir.rglob("*.txt"):
    print(file)

# alle bestandsnamen zonder suffix(txt enzo)
print('alle .TXT bestanden in map en submappen ZONDER het type')
for file in pDir.rglob("*.txt"):
    print(file.stem)
