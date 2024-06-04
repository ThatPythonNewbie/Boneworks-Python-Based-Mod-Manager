import os, time

while True:
    source_path = input("Input the path where your files are: ")
    if os.path.exists(source_path):
        break
    else:
        print("Invalid path.")
        continue
while True:
    root_game_dir = input("What is the path to your game install (root dir of the game, leave blank to use deault steam path)? ")
    if root_game_dir == "":
        root_game_dir = r"C:\Program Files (x86)\Steam\steamapps\common\BONEWORKS"
    else:
        if os.path.exists(root_game_dir):
            break
        else:
            print("Invalid path")
            continue
start = time.time()
print("Fetching files...")
CustomItems = []
PlayerModels = []
CustomMaps = []
ScriptMods = []
cic = 0
pmc = 0
cmc = 0
smc = 0
for file in os.listdir(source_path):
    if ".melon" in file:
        print(f"Custom Item found ({file}) adding to list...")
        CustomItems.append(file)
        cic += 1
    elif ".body" in file:
        print(f"Player Model found ({file}) adding to list...")
        PlayerModels.append(file)
        pmc += 1
    elif ".bcm" in file or ".cma" in file:
        print(f"Custom Map found ({file}) adding to list...")
        CustomMaps.append(file)
        cmc += 1
    elif ".dll" in file:
        confirm = "1 possible script mod found (dll) Would you like to add it too? [Y/n]"
        if confirm == "Y" or confirm == "y":
            ScriptMods.append(file)
            smc += 1
        else:
            pass

if cic == 0:
    print("No custom items found.")
elif pmc == 0:
    print("No player models found.")
elif cmc == 0:
    print("No custom maps found.")
elif cic == 0 and pmc == 0 and cmc == 0:
    print("No files found. Are you sure this is the correct path?")
else:
    print(f"""
{str(cic)} Custom Items found\n
{str(pmc)} Player Models found\n
{str(cmc)} Custom Maps found\n
{str(smc)} Script Mods found
""")
print("Proceeding with copying...")
for f in CustomItems:
    with open(f, "rb") as file:
        data = file.read()
    path_to_file = os.path.join(root_game_dir, r"\UserData\CustomItems\\" + f)
    try:
        open(path_to_file, "x")
    except FileExistsError:
        while True:
            ñ = input(f"File {f} already exists in {path_to_file}, would you like to overwrite? [Y/n] ")
            if ñ == "Y" or ñ == "y":
                break
            elif ñ == "N" or ñ == "n":
                pass
        with open(path_to_file, "wb") as file_to_copy_to:
            file_to_copy_to.write(data)

for f in PlayerModels:
    with open(f, "rb") as file:
        data = file.read()
    path_to_file = os.path.join(root_game_dir, r"\UserData\PlayerModels\\" + f)
    try:
        open(path_to_file, "x")
    except FileExistsError:
        while True:
            ñ = input(f"File {f} already exists in {path_to_file}, would you like to overwrite? [Y/n] ")
            if ñ == "Y" or ñ == "y":
                break
            elif ñ == "N" or ñ == "n":
                pass
        with open(path_to_file, "wb") as file_to_copy_to:
            file_to_copy_to.write(data)

for f in CustomMaps:
    with open(f, "rb") as file:
        data = file.read()
    path_to_file = os.path.join(root_game_dir, r"\UserData\CustomMaps\\" + f)
    try:
        open(path_to_file, "x")
    except FileExistsError:
        while True:
            ñ = input(f"File {f} already exists in {path_to_file}, would you like to overwrite? [Y/n] ")
            if ñ == "Y" or ñ == "y":
                break
            elif ñ == "N" or ñ == "n":
                pass
        with open(path_to_file, "wb") as file_to_copy_to:
            file_to_copy_to.write(data)

for f in ScriptMods:
    with open(f, "rb") as file:
        data = file.read()
    path_to_file = os.path.join(root_game_dir, r"\Mods\\" + f)
    try:
        open(path_to_file, "x")
    except FileExistsError:
        while True:
            ñ = input(f"File {f} already exists in {path_to_file}, would you like to overwrite? [Y/n] ")
            if ñ == "Y" or ñ == "y":
                break
            elif ñ == "N" or ñ == "n":
                pass
        with open(path_to_file, "wb") as file_to_copy_to:
            file_to_copy_to.write(data)
end = time.time()
print(f"Operation finished in {str(end - start)} seconds")
