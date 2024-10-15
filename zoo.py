#Imports Fauna and Flora to hold the data
from fauna import Fauna
from flora import Flora
#imports csv to save data to csv
import csv

#gathers the fauna data based on the number of fauna entered
def getFaunaInput(faunaNum):
    faunaList = []
    for i in range(faunaNum):
        print(f"Fauna number: {i+1}")
        name = input("Please enter the fauna's name: ")
        kingdom = input("Please enter the fauna's kingdom: ")
        phylum = input("Please input the fauna's phylum: ")
        order = input("Please input the fauna's order: ")
        family = input("Please input the fauna's family: ")
        genus = input("Please input the fauna's genus: ")
        species = input("Please input the fauna's species: ")
        #instance of the class Fauna named theFauna
        theFauna = Fauna(name,kingdom,phylum,order,family,genus,species)
        #append fauna object to the list.
        faunaList.append(theFauna)
    return faunaList

#gathers the flora data based on the number of flora entered
def getFloraInput(floraNum):
    floraList = []
    for i in range(floraNum):
        print(f"New flora number: {i+1}")
        areas = input("Please enter the areas this flora inhabits: ")
        periods = input("Please input the periods in which this flora grows: ")
        climate = input("Please input the climate conditions for this flora: ")
        specialConditions = input("Please input any special conditions for this flora: ")
        #instance of the class Flora named theFlora
        theFlora = Flora(areas,periods,climate,specialConditions)
        #append flora object to the list
        floraList.append(theFlora)
    return floraList

#prints list to a text file
def printText(list,toNameFile):
    #checks to see if the named file is flora fauna
    if toNameFile == "flora": #if its flora write the appropriate data to the file
        with open(toNameFile+".txt", "w") as myFile:
            myFile.write(f"Areas Periods Climate SpecialConditions\n")
            for i in list:
                myFile.write(f"{i.areas}\t{i.periods}\t{i.climate}\t{i.specialConditions}")
    elif toNameFile == "fauna": #if its fauna write the appropriate data to the file
        with open(toNameFile+".txt", "w") as myFile:
            myFile.write(f"Name Kingdom Phylum Order Family Genus Species\n")
            for i in list: #for each object in the list write the object with all its sub properties
                myFile.write(f"{i.name}\t{i.kingdom}\t{i.phylum}\t{i.order}\t{i.family}\t{i.genus}\t{i.species}")

def printCsv(list,toNameFile):
    csvFile = toNameFile + ".csv"
    with open(csvFile, 'w', newline='') as myFile:
        writer = csv.writer(myFile)
        if toNameFile == "fauna":
            writer.writerow(["Name","Kingdom","Phylum","Order","Family","Genus","Species"]) #print headers
            for i in range(len(list)): #for each object in the list write the object with all its sub properties
                writer.writerow([list[i].name,list[i].kingdom,list[i].phylum,list[i].order,list[i].family,list[i].genus,list[i].species])
        elif toNameFile == "flora":
            writer.writerow(["Area","Period","Climate","Special Conditions"]) #print headers
            for i in range(len(list)): #for each object in the list write the object with all its sub properties
                writer.writerow([list[i].areas,list[i].periods, list[i].climate, list[i].specialConditions])
#returns the entire list of flora in a nice print statement        
def getFloraList(floraList):
    print("Here are all the Flora in your zoo: \n")
    for i in floraList: #for each object in the flora list print the table
        print(f"Areas this plant grows: {i.areas}", end="\t")
        print(f"The periods the plant grows: {i.periods}", end="\t")
        print(f"The climate the plant grows in: {i.climate}", end="\t")
        print(f"Special conditions concerning the plant: {i.specialConditions}", end="\t")
        print("\n")

#returns the entire list of flora in a nice print statement        
def getFaunaList(faunaList):
        print("Here are all the fauna in your zoo: \n")
        for i in faunaList: #for each object in the fauna list, print the table
            print(f"Name: {i.name}", end="\t")
            print(f"Kingdom: {i.kingdom}", end="\t")
            print(f"Phylum: {i.phylum}", end="\t")
            print(f"Order: {i.order}", end="\t")
            print(f"Family: {i.family}", end="\t")
            print(f"Genus: {i.genus}", end="\t")
            print(f"Species: {i.species}", end="\t")
            print("\n")

#checks to see if there is data for fauna, flora, or if both have valid data
def checkLength(faunaData,floraData):
    if len(faunaData) >=1 and len(floraData) >=1:
        return "both"
    elif len(faunaData) >=1:
        return "fauna"
    elif len(floraData) >= 1:
        return "flora"

#main function do the stuff
def main():
    faunaData = [] #placeholder
    floraData = [] #placeholder
    #user input for initial setup
    faunaSize = input("How many fauna live in your zoo?: ")
    floraSize = input("How many flora live in your zoo?: ")
    if faunaSize.isdigit() and floraSize.isdigit(): #check to see if the faunasize and flora size given were integers
        if int(faunaSize) > 0: #if number is bigger than one gather data
            faunaData = getFaunaInput(int(faunaSize))
        if int(floraSize) > 0: #if number is bigger than one gather data
            floraData = getFloraInput(int(floraSize))
    else:
        if not faunaSize.isdigit(): #if its not a digit...
            print("Please use a number for the fauna size") #print error
            main() #call main function
        elif not floraSize.isdigit():#if its not a digit...
            print("Please use a number for the flora size")
            main()#call main function
        elif not faunaSize.isdigit() and floraSize.isdigit(): #if neither is digit
            print("Please use numerical inputs for fauna and flora")
            main()#call main function
    #get input from user asking how they want the output formatted
    printSelection = input("How would you like to save the data? Select between csv, text, or both?: ")
    #checks the length of fauna and flora to see what data gets saved
    check = checkLength(faunaData,floraData)

    match printSelection:
        case "csv": #if its a csv....
           match check:
                case "fauna": #if its fauna...
                    printCsv(faunaData,"fauna")
                case "flora": #if its flora...
                    printCsv(floraData,"flora")
                case "both":#if its both...
                    printCsv(faunaData,"both")
                    printCsv(floraData,"both")
                case _:#if the cat jumped on the keyboard and spammed the input
                    print("invalid selection")                   
        case "text":  #if its a text....
            match check:
                case "fauna":#if its fauna...
                    printText(faunaData,"fauna")
                case "flora":#if its flora...
                    printText(floraData, "flora")
                case "both":#if its both...
                    printText(faunaData,"both")
                    printText(floraData, "both")
                case _:
                    print("invalid selection")                    
        case "both":  #if its both....
            match check:
                case "fauna":#if its fauna...
                    printCsv(faunaData, "fauna")
                    printText(faunaData, "fauna")
                case "flora":#if its flora...
                    printCsv(floraData, "flora")
                    printText(floraData, "flora")
                case "both":#if its both...
                    printCsv(faunaData, "fauna")
                    printText(faunaData, "fauna")                    
                    printCsv(floraData, "flora")
                    printText(floraData, "flora")
                case _: #if the you had an animal friend give the input
                    print("invalid selection")
        case _: #i'm running out of animal jokes but meh lets be real any animal would cause this error
            print("invalid selection")
main() #start your engine and initiate scope