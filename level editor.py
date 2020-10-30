import xml.etree.ElementTree as ElementTree
import glob, os
path = "C:\Program Files (x86)\Steam\steamapps\common\Teardown"

customXML = ElementTree.parse(path + '\create\custom.xml')
customRoot = customXML.getroot()
BodyList = []

def getObjects():
    for body in customRoot.iter('body'):
        BodyList.append(body)
        for object in body:
            if object.tag == "vox":
                print(object.get('file') + " at (" + object.get('pos') + ")")
    return BodyList

def getConfirmation(files, i):
    if i in files:
        print('Did you want to select "'+i+'"?')
    else:
        return False

    yn = input("(Y/N): ")
    if yn.lower() == "y":
        return True
    else:
        return False

def addObject():
    os.chdir(path + "\create\custom")
    files = []
    num = 0
    for file in glob.glob("*.vox"):
        print("#" + str(num) + " " + file)
        files.append(file)
        num = num + 1
    print("_"*10)

    confirm = False
    x = 0
    y = 0
    z = 0
    print("Enter the file name of the object you want to place: ")
    print('Eg: "tree.vox"')
    i = input("Enter Name: ")
    confirm = getConfirmation(files, i)

    if confirm:
        print("[i] Confirmed!\n\n")
        print("Please enter the coordinates now.")
        x = input("X-Coordinate          : ")
        y = input("Y-Coordinate (Height) : ")
        z = input("Z-Coordinate          : ")
        print('Your object "'+ i +'" will be placed at:', x, y, z)
        yn = input("Do you want to place it?(Y/N): ")
        if yn.lower() == "y":
            newBody = ElementTree.Element("body")
            vox = ElementTree.Element("vox")
            vox.set('pos', x +' '+y +' '+z)
            vox.set('file', "LEVEL/"+i)
            newBody.append(vox)
            customRoot.append(newBody)
            customXML.write(path + '\create\custom.xml')
            print("Your object has been placed!")
        else:
             print("[i] Let's retry!\n")
    else:
        print("[i] Let's retry!\n")

def removeObject():
    print("\n"*2)
    for body in customRoot.iter('body'):
        for vox in body:
            if vox.tag == "vox":
                print(vox.get('file') + " at: " + vox.get('pos'))

    print("Enter the file name of the object you want to REMOVE: ")
    print('Eg: "tree.vox"')
    i = input("Enter Name: ")
    for body in customRoot.iter('body'):
        for vox in body:
            if vox.tag == "vox":
                if i in vox.get('file'):
                    print('You are about to delete "' + vox.get('file') + '" at: '+ vox.get('pos'))
                    yn = input("Are you sure? (Y/N): ").lower()
                    if yn == "y":
                        customRoot.remove(body)
                        customXML.write(path + '\create\custom.xml')
                        print("Object has been removed!")

def addVehicle():
    print("\n"*2)
    vFiles = []
    num = 0
    os.chdir(path + "\create\custom\\vehicles")
    print("\n[i] .vox files available to be placed: ")
    for vehicle in glob.glob("*.xml"):
        print("#" + str(num) + " " + vehicle)
        vFiles.append(vehicle)
        num = num + 1
    print("_"*10)
    print("What vehicle do you want to add?")
    i = input("Type the name: ")
    if i in vFiles:
        print('Did you want to select "'+i+'"?')
        yn = input("(Y/N): ")
        if yn.lower() == "y":
            contin = True
        else:
            contin = False
    else:
        contin = False

    if contin:
        print("[i] Confirmed!\n\n")
        print("Please enter the coordinates now.")
        x = input("X-Coordinate         : ")
        y = input("Y-Coordinate (Height): ")
        z = input("Z-Coordinate         : ")
        print('Your vehicle "'+ i +'" will be placed at:', x, y, z)
        yn = input("Do you want to place it?(Y/N): ")
        if yn.lower() == "y":
            vehicleXML = ElementTree.parse(path + '\create\custom\\vehicles\\'+i)
            vehicleRoot = vehicleXML.getroot()
            vehicleRoot.set('pos',  x +' '+y +' '+z)

            customRoot.append(vehicleRoot)
            customXML.write(path + '\create\custom.xml')
            print("Your vehicle has been placed!")
        else:
             print("[i] Let's retry!\n")

def removeVehicle():
    for vehicle in customRoot.iter('vehicle'):
        print(vehicle.get('name') + " at: " + vehicle.get('pos'))

    print("Enter the file name of the vehicle you want to REMOVE: ")
    print('Eg: "sportscar"')
    i = input("Enter Name: ")
    for vehicle in customRoot.iter('vehicle'):
        if i == vehicle.get('name'):
                    print('You are about to delete "' + vehicle.get('name') + '" at: '+ vehicle.get('pos'))
                    yn = input("Are you sure? (Y/N): ").lower()
                    if yn == "y":
                        customRoot.remove(vehicle)
                        customXML.write(path + '\create\custom.xml')
                        print("Object has been removed!")

def main():
    ModPath = path + "\create\custom"
    while True:
        print("\n"*2)
        print("Do you want to edit Vehicles or Objects?")
        vo = input("(V/O): ").lower()
        if vo == "o":
            print("Do you want to add or remove?")
            ar = input("(A/R): ").lower()
            if ar == "a":
                addObject()
            elif ar == "r":
                removeObject()

        elif vo == "v":
            # getVehicles()
            print("Do you want to add or remove?")
            ar = input("(A/R): ").lower()
            if ar == "a":
                addVehicle()
            elif ar == "r":
                removeVehicle()

print("Place the objects you want to have in your map inside of the create\custom folder!")
print("Create a new folder called 'vehicles' and place them there.")
print("CTRL + C to exit.")
main()
