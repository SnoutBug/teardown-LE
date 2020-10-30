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
    for file in glob.glob("vehicles\*.vox"):
        print("#" + str(num) + " " + file)
        vFiles.append(file)
        num = num + 1
    print("_"*10)
    print("What vehicle do you want to add?")
    i = input("Type the name: ")
    if i in vFiles:
        print('Did you want to select "'+i+'"?')
    else:
        contin = False
            
    yn = input("(Y/N): ")
    if yn.lower() == "y":
        contin = True
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
            nV = ElementTree.Element("vehicle")
            nV.set('name',i[:-4])
            nV.set('pos', x +' '+y +' '+z)
            #default sportscar, will edit l8er
            #this is nothing someone should code in python, i would rather do that in c# with the unity engine but i dont know how to do that.
            #also i would rather use presets LOL GREAT IDEA
            nV.set('rot', '0 0 0')
            nV.set('driven', 'false')
            nV.set('sound', 'sportscar')
            nV.set('spring', '1.2')
            nV.set('damping', '1.0')
            nV.set('topspeed', '120')
            nV.set('acceleration', '12')
            nV.set('strength', '8')
            nV.set('antispin', '0')
            nV.set('antiroll', '0.1')
            nV.set('difflock', '0.1')
            nV.set('steerassist', '0.3')
            nV.set('friction', '1.9')
            bod = ElementTree.Element("body")
            bod.set('pos', '-0.05002 0.35 0.25')
            bod.set('rot', '0.0 0.0 0.0')
            bod.set('dynamic', 'true')
            vox = ElementTree.Element("vox")
            vox.set('pos', '0.05 -0.15 -0.25')
            vox.set('rot', '0 180 0')
            vox.set('density', '2')
            vox.set('file', "LEVEL/vehicles/"+i)
            vox.set('object', 'body')
            locE = ElementTree.Element("location")
            locE.set('tags', 'exhaust')
            locE.set('pos', '0.5 0.1 -2.1')
            locE.set('rot', '-180.0 360.0 -180.0')
            locV = ElementTree.Element("location")
            locV.set('tags', 'vital')
            locV.set('pos', '0.05 0.55 -1.4')
            locV.set('rot', '-180.0 360.0 -180.0')
            locP = ElementTree.Element("location")
            locP.set('tags', 'player')
            locP.set('pos', '0.4 0.75 0.15')
            locP.set('rot', '0.0 0.0 0.0')
            wBL = ElementTree.Element("wheel")
            wBL.set('name', 'bl')
            wBL.set('pos', '-0.64999 -0.0 1.2')
            wBL.set('drive', '1')
            wBL.set('travel', '-0.1 0.1')
            voxBL = ElementTree.Element("vox")
            voxBL.set('pos', '-0.1 -0.35 -0.05')
            voxBL.set('rot', '0.0 -180.0 0.0')
            voxBL.set('file', "LEVEL/vehicles/"+i)
            voxBL.set('object', 'wheel_bl')   
            wBR = ElementTree.Element("wheel")
            wBR.set('name', 'br')
            wBR.set('pos', '0.65001 -0.0 1.2')
            wBR.set('drive', '1')
            wBR.set('travel', '-0.1 0.1')
            voxBR = ElementTree.Element("vox")
            voxBR.set('pos', '0.2 -0.35 -0.05')
            voxBR.set('rot', '0.0 180.0 0.0')
            voxBR.set('file', "LEVEL/vehicles/"+i)
            voxBR.set('object', 'wheel_br') 
            wFL = ElementTree.Element("wheel")
            wFL.set('name', 'fl')
            wFL.set('pos', '-0.64999 -0.0 -1.4')
            wFL.set('drive', '1')
            wFL.set('steer', '0.7')
            wFL.set('travel', '-0.1 0.1')
            voxFL = ElementTree.Element("vox")
            voxFL.set('pos', '-0.1 -0.35 -0.05')
            voxFL.set('rot', '0.0 180.0 0.0')
            voxFL.set('file', "LEVEL/vehicles/"+i)
            voxFL.set('object', 'wheel_fl') 
            wFR = ElementTree.Element("wheel")
            wFR.set('name', 'fr')
            wFR.set('pos', '0.65001 -0.0 -1.4')
            wFR.set('drive', '1')
            wFR.set('steer', '0.7')
            wFR.set('travel', '-0.1 0.1')
            voxFR = ElementTree.Element("vox")
            voxFR.set('pos', '0.2 -0.35 -0.05')
            voxFR.set('rot', '0.0 -180.0 0.0')
            voxFR.set('file', "LEVEL/vehicles/"+i)
            voxFR.set('object', 'wheel_fr')             
            #YES I WILL USE PRESETS STOP COMPLAINING!
            vox.append(locE)
            vox.append(locV)
            vox.append(locP)
            bod.append(vox)
            wBL.append(voxBL)
            wBR.append(voxBR)
            wFL.append(voxFL)
            wFR.append(voxFR)
            bod.append(wBL)
            bod.append(wBR)
            bod.append(wFL)
            bod.append(wFR)
            nV.append(bod)
            customRoot.append(nV)
            customXML.write(path + '\create\custom.xml')
            print("Your vehicle has been placed!")
        else:
             print("[i] Let's retry!\n")        
    
def main():
    ModPath = path + "\create\custom"
    os.chdir(ModPath)
    print("\n[i] .vox files available to be placed: ")
    
    while True:
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
                #removeVehicle()
                print("Implementing vehicles is sooo much work pepehands, maybe later\n\n")
print("Place the objects you want to have in your map inside of the create\custom folder!")        
print("Create a new folder called 'vehicles' and place them there.")
print("CTRL + C to exit.")
main()