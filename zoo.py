#Imports 
from fauna import Fauna
from flora import Flora
import csv
import numpy as np
import os

#Check for existing files
def checkForExistingFiles():
    existingFiles = []
    if os.path.exists("fauna.txt"):
        existingFiles.append("fauna.txt")
    if os.path.exists("fauna.csv"):
        existingFiles.append("fauna.csv")
    if os.path.exists("flora.txt"):
        existingFiles.append("flora.txt")
    if os.path.exists("flora.csv"):
        existingFiles.append("flora.csv")
    return existingFiles

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
def printText(list,toNameFile,existing):
    #checks to see if the named file is flora fauna
    if toNameFile == "flora": #if its flora write the appropriate data to the file
        with open(toNameFile+".txt", "a") as myFile:
            if existing == False:
                myFile.write("Areas Periods Climate SpecialConditions\n")
            for i in list:
                myFile.write(f"{i.areas}\t{i.periods}\t{i.climate}\t{i.specialConditions}\n")
    elif toNameFile == "fauna": #if its fauna write the appropriate data to the file
        with open(toNameFile+".txt", "a") as myFile:
            if existing == False:
                myFile.write("Name Kingdom Phylum Order Family Genus Species\n")
            for i in list: #for each object in the list write the object with all its sub properties
                myFile.write(f"{i.name}\t{i.kingdom}\t{i.phylum}\t{i.order}\t{i.family}\t{i.genus}\t{i.species}\n")

def printCsv(list,toNameFile,existing):
    csvFile = toNameFile + ".csv"
    with open(csvFile, 'a', newline='') as myFile:
        writer = csv.writer(myFile)
        if toNameFile == "fauna":
            if existing == False:
                writer.writerow(["Name","Kingdom","Phylum","Order","Family","Genus","Species"]) #print headers
            for i in range(len(list)): #for each object in the list write the object with all its sub properties
                writer.writerow([list[i].name,list[i].kingdom,list[i].phylum,list[i].order,list[i].family,list[i].genus,list[i].species])
        elif toNameFile == "flora":
            if existing == False:
                writer.writerow(["Area","Period","Climate","Special Conditions"]) #print headers
            for i in range(len(list)): #for each object in the list write the object with all its sub properties
                writer.writerow([list[i].areas,list[i].periods, list[i].climate, list[i].specialConditions])

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
    hasExisting = False #Flag stating if there are existing files
    existingFiles = checkForExistingFiles() #existingFiles becomes a list of files that exist
    if len(existingFiles) > 0: #if there are existing files...
        hasExisting = True #flag true
        for i in existingFiles: #check existing files
            if ".csv" in i: #see if any are csv and read in using np
                with open(i, 'r') as file:#open file
                    reader = csv.reader(file)#read file
                    data = list(reader)#make the data into a list
                    if i == "fauna.csv": #if its fauna
                        faunaData = np.array(data) #update faunaData with new information
                    elif i == "flora.csv":
                        floraData = np.array(data) #otherwise update floraData
            elif ".txt" in i:#if csv doesn't exist but existing files do exist the only other file to check for is a text file
                with open(i, 'r') as file:
                    if i == "fauna.txt": # if fauna read lines in
                        faunaData = file.readlines()
                    elif i == "flora.txt": # if flora reads lines in
                        floraData = file.readlines()                   
    else: 
        print("No existing files") 
 
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
                    if "fauna.txt" in existingFiles:
                        printText(faunaData,"fauna",hasExisting)
                    printCsv(faunaData,"fauna",hasExisting)
                case "flora": #if its flora...
                    if "flora.txt" in existingFiles:
                        printText(floraData,"flora",hasExisting)
                    printCsv(floraData,"flora",hasExisting)
                case "both":#if both have a valid length...
                    if "flora.txt" in existingFiles:
                        printText(faunaData,"fauna",hasExisting)
                    if "fauna.txt" in existingFiles:
                        printText(floraData,"flora",hasExisting)
                    printCsv(faunaData,"fauna",hasExisting)
                    printCsv(floraData,"flora",hasExisting)
                case _:#if the cat jumped on the keyboard and spammed the input
                    print("invalid selection")                   
        case "text":  #if its a text....
            match check:
                case "fauna":#if its fauna...
                    if "fauna.csv" in existingFiles:
                        printCsv(faunaData,"fauna", hasExisting)
                    printText(faunaData,"fauna", hasExisting)
                case "flora":#if its flora...
                    if "flora.csv" in existingFiles:
                        printCsv(faunaData,"fauna", hasExisting)
                    printText(floraData, "flora", hasExisting)
                case "both":#if its both...
                    if "flora.csv" in existingFiles:
                        printCsv(floraData,"flora", hasExisting)
                    if "fauna.csv" in existingFiles:
                        printCsv(faunaData,"fauna",hasExisting)
                    printText(faunaData,"fauna", hasExisting)
                    printText(floraData, "flora", hasExisting)
                case _:
                    print("invalid selection")                    
        case "both":  #if its both in print selection....
            printCsv(faunaData, "fauna", hasExisting)
            printText(faunaData, "fauna", hasExisting)                    
            printCsv(floraData, "flora", hasExisting)
            printText(floraData, "flora", hasExisting)

        case _: #i'm running out of animal jokes but meh lets be real any animal would cause this error
            print("invalid selection")
    print("Output saved and updated, have a great day!")
main() #start your engine and initiate scope