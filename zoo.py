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
        print(f"New fauna number: {i+1}")
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
        name = input("Please give me the flora's name: ")
        areas = input("Please enter the areas this flora inhabits: ")
        periods = input("Please input the periods in which this flora grows: ")
        climate = input("Please input the climate conditions for this flora: ")
        specialConditions = input("Please input any special conditions for this flora: ")
        #instance of the class Flora named theFlora
        theFlora = Flora(name,areas,periods,climate,specialConditions)
        #append flora object to the list
        floraList.append(theFlora)
    return floraList

#prints list to a text file
def printText(faunaData,floraData):
    existingFiles = checkForExistingFiles()
    #checks to see if the named file is flora fauna
    with open("flora.txt", "a") as myFile:
        if "flora.txt" not in existingFiles:
            myFile.write("Name Areas Periods Climate SpecialConditions\n")
        for i in floraData:
            myFile.write(f"{i.name}\t{i.areas}\t{i.periods}\t{i.climate}\t{i.specialConditions}\n")
    with open("fauna.txt", "a") as myFile:
        if "fauna.txt" not in existingFiles:
            myFile.write("Name Kingdom Phylum Order Family Genus Species\n")
        for i in faunaData: #for each object in the list write the object with all its sub properties
            myFile.write(f"{i.name}\t{i.kingdom}\t{i.phylum}\t{i.order}\t{i.family}\t{i.genus}\t{i.species}\n")

def printCsv(faunaData,floraData):
    existingFiles = checkForExistingFiles()
    with open("fauna.csv", 'a', newline='') as faunaFile:
        writer = csv.writer(faunaFile)
        if "fauna.csv" not in existingFiles:
            writer.writerow(["Name","Kingdom","Phylum","Order","Family","Genus","Species"]) #print headers
        for i in range(len(faunaData)): #for each object in the list write the object with all its sub properties
            writer.writerow([faunaData[i].name,faunaData[i].kingdom,faunaData[i].phylum,faunaData[i].order,faunaData[i].family,faunaData[i].genus,faunaData[i].species])
    with open("flora.csv",'a', newline='') as floraFile:
        writer = csv.writer(floraFile)    
        if "flora.csv" not in existingFiles:
            writer.writerow(["Name","Area","Period","Climate","SpecialConditions"]) #print headers
        for i in range(len(floraData)): #for each object in the list write the object with all its sub properties
            writer.writerow([floraData[i].name,floraData[i].areas,floraData[i].periods, floraData[i].climate, floraData[i].specialConditions])

#main function do the stuff
def main():
    faunaData = [] #placeholder
    floraData = [] #placeholder
    existingFiles = checkForExistingFiles() #existingFiles becomes a list of files that exist
    if len(existingFiles) > 0: #if there are existing files...
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
        elif not floraSize.isdigit():#if its not a digit...
            print("Please use a number for the flora size")
        elif not faunaSize.isdigit() and floraSize.isdigit(): #if neither is digit
            print("Please use numerical inputs for fauna and flora")

    printCsv(faunaData,floraData)
    printText(faunaData, floraData,)                    

    print("Output saved and updated, have a great day!")
main() #start your engine and initiate scope