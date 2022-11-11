import glob, os, shutil
from time import sleep

#Warning agreement
print("Please open the python file to modify the values following my instructions to make sure this works. Then open your command prompt and change your directory to where you store the .py file and type the following: pip install pyinstaller and then pyinstaller --onefile HPBWMM.py")
sleep(5)
os.system("pause")
print("Please notice that you need ModThatIsNotMod, Player Models and CustomMaps already installed, and also have started the game at least once so MelonLoader creates the folders.")
sleep(3.5)
os.system("pause")

print("Detecting your files and installing them...")
print("Please wait...")
#Copies all mod files and paste them in the respective folders
#Custom Items
files = glob.iglob(os.path.join("C:\Users\Usuario\Downloads\userdata", "*.melon"))
for file in files:  #Modify the folder above to select where you store your mods without installing them
    if os.path.isfile(file):
        shutil.copy2(file, "C:\Program Files\VRGAMES\BONEWORKS\UserData\CustomItems")
    else:           #Modify the folder above to select your Boneworks Directory
        print("There are no Custom Items Mods in this folder")

#Player Models
files1 = glob.iglob(os.path.join("C:\Users\Usuario\Downloads\userdata", "*.body"))
for file in files1:  #Modify the folder above to select where you store your mods without installing them
    if os.path.isfile(file):
        shutil.copy2(file, "C:\Program Files\VRGAMES\BONEWORKS\UserData\PlayerModels")
    else:           #Modify the folder above to select your Boneworks Directory
        print("There are no Player Models Mods in this folder")

#Maps
#.bcm maps
files2 = glob.iglob(os.path.join("C:\Users\Usuario\Downloads\userdata", "*.bcm"))
for file in files2:  #Modify the folder above to select where you store your mods without installing them
    if os.path.isfile(file):
        shutil.copy2(file, "C:\Program Files\VRGAMES\BONEWORKS\UserData\CustomMaps")
    else:           #Modify the folder above to select your Boneworks Directory
        print("There are no .bcm Custom Maps Mods in this folder")
#.cma maps
files3 = glob.iglob(os.path.join("C:\Users\Usuario\Downloads\userdata", "*.cma"))
for file in files3:  #Modify the folder above to select where you store your mods without installing them
    if os.path.isfile(file):
        shutil.copy2(file, "C:\Program Files\VRGAMES\BONEWORKS\UserData\CustomMaps")
    else:           #Modify the folder above to select your Boneworks Directory
        print("There are no .cma Custom Maps Mods in this folder")