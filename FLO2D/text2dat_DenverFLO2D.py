#! python3

# text2dat.py

# Created by: Jake Ursetta
# ICON Engineering

# Date Created: 5/25/2016
# Date Modified: 6/15/2016

############################################## Function Definition ###########################################################
# WARNING: Do not change this section unless you have saved a previous version.

import xlrd, re, sys, os

def text2dat(path):
	# Opens work book and sheet and finds how many lines there are

	# Save project folder path and filename for saving purposes
	project,fileName = os.path.split(os.path.abspath(path))

	if "DS" in fileName or "US" in fileName:
		suffixIndex = fileName.find("DS")
		if suffixIndex == -1:
			suffixIndex = fileName.find("US")
		saveSuffix = fileName[suffixIndex:]
		saveSuffix = saveSuffix[:saveSuffix.find(".")]
	else:
		saveSuffix = input("\n Please enter a suffix to textfile name.\n ex: 'US_50yr' would result in INFLOW_US_50yr.dat\n \n")


	book = xlrd.open_workbook(path)
	sheet = book.sheet_by_name("HYDROGRAPHS")
	numCol = sheet.ncols
	numRow = sheet.nrows

	# Creates text file name and opens the text file
	savefile = project + "\\" +  "INFLOW_" + str(saveSuffix) + ".dat"
	file = open(savefile,"w")

	for sr in range(0,10):
		if (sheet.cell(sr,0).value == 0 and sheet.cell(sr,1).value == 0) or (sheet.cell(sr,0).value == "0" and sheet.cell(sr,1).value == "0"):
			surfaceRow = sr
			break

	# Reads in text for each column if the surface flow number exists
	for j in range (0,numCol):
		if sheet.cell(surfaceRow - 1,j).value != '':
			file.write('{}	{}	{:.0f}'.format("F",0,float(sheet.cell(surfaceRow - 1,j).value)) + "\n")
			for i in range (surfaceRow, 58):
				# Insures empty rows are not read in
				if sheet.cell(i,1).value != '':
					file.write('{}	{:.2f}	{:.2f}'.format("H",float(sheet.cell(i,2).value),float(sheet.cell(i,j).value)) + "\n")
	# Closes the file
	file.close


#################################################### Execution ################################################################
# WARNING: Do not change this section unless you know what you are doing and have saved a previous version.

path = input("\n Please drag and drop the data file and then press enter.\n")

text2dat(path)
