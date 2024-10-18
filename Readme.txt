Zoo Data Management

This project provides a command-line interface for managing and saving data about zoo fauna and flora. The user can input data, and choose output formats (CSV, text, or both) it will automatically save the data in a JSON format, and save this data in structured files.

Features
	Input data for fauna (animals) and flora (plants) including various biological classifications.
	Save data in multiple formats: JSON, CSV, and text files.
	Automatically checks for existing data files and appends new data.
	Handles user input with validation.
Requirements
	Required libraries: numpy, os, json, and csv.
	Code Structure
	Imports: The code imports necessary libraries and modules.
	from fauna import Fauna
	from flora import Flora
	import csv
	import numpy as np
	import os
	import json
	
Check for Existing Files: This function checks if data files exist in the directory.
	def checkForExistingFiles():
Gathering Fauna Data: Prompts the user for input to create a list of fauna data.
	def getFaunaInput(faunaNum):
Gathering Flora Data: Prompts the user for input to create a list of flora data.
	def getFloraInput(floraNum):
Output Functions: Functions to write data to JSON, text files, and CSV files.
	def printJSON(list, toNameFile, existing):
	def printText(list, toNameFile, existing):
	def printCsv(list, toNameFile, existing):

Check Data Length: Validates the presence of fauna and flora data.
	def checkLength(faunaData, floraData):
Main Function: Orchestrates user interaction, data collection, and saving operations.
	def main():
Usage
	Clone or download the repository.
	Navigate to the project directory.
	Execute python3 zoo.py in terminal
Run the script:
	Follow the prompts to input fauna and flora data.
	Choose your desired output format.
Data Model
	Fauna Class: Represents an animal with attributes like name, kingdom, phylum, order, family, genus, and species.
	Flora Class: Represents a plant with attributes like name, areas, periods, climate, and special conditions.
Output Files
	Fauna data can be saved in fauna.txt, fauna.csv, and JSON in MasterData.json.
	Flora data can be saved in flora.txt, flora.csv, and MasterData.json.
