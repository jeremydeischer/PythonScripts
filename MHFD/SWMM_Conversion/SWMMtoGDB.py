# SWMMtoGDB.py
# Programmer: Cody Garcia
# Date: 4/27/2021
# Description: This script will create a project file geodatabase, project features to
#   NAD 83 State Plane Colorado Central, import shapefiles from a folder containing geometries
#   exported from a SWIMM model, add the required fields to JOIN to the existing and future
#   discharge CSVs, allow the user to fill in project specific fields, and delete autopopulated
#   fields created by the SWIMM export

# Inputs:
    # Output location: location where geodatabase will be created
    # SWIMM folder: folder containing geometries (shapefiles) exported from SWIMM model
    # Source: project name (string)
    # Study year: project year (string)
    # SWIMM model: SWIMM model name (e.g. LCM.inp)
    # CUHP version: (string)

# Output: file geodatabase containing shapefiles exported from SWIMM model with the required fields

######################################################################################################

import arcpy, os
arcpy.env.overwriteOutput = True

outGDBLoc = arcpy.GetParameterAsText(0)
inSWMMfolder = arcpy.GetParameterAsText(1)
source = arcpy.GetParameterAsText(2)
studyYear = arcpy.GetParameterAsText(3)
SWMMinput = arcpy.GetParameterAsText(4)
SWMMver = arcpy.GetParameterAsText(5)
CUHPversion = arcpy.GetParameterAsText(6)



# Create a project file geodatabase
GDBname = os.path.basename(inSWMMfolder)
arcpy.CreateFileGDB_management(outGDBLoc, GDBname)
GDB = os.path.join(outGDBLoc,GDBname + ".gdb")
arcpy.AddMessage("\nCreated project file geodatabase\n")

# Feed tool a folder from the model output that has the shapefiles
# For each shapefile in the folder, define projection, and import into project GDB
arcpy.env.workspace = inSWMMfolder
shapes = arcpy.ListFeatureClasses()
arcpy.AddMessage("Defining projection and importing to file geodatabase for all features in {0}\n".format(inSWMMfolder))

for shape in shapes:
    # 102654 is the code for:
    # NAD 1983 StatePlane Colorado Central FIPS 0502 Feet
    sr = arcpy.SpatialReference(102654)
    arcpy.DefineProjection_management(shape, sr)
    # Import each shape into GDB
    out_name = os.path.basename(shape[:-4])
    # Import each shape into a the file geodatabase
    arcpy.FeatureClassToFeatureClass_conversion (shape, GDB, out_name)

arcpy.env.workspace = GDB
features = arcpy.ListFeatureClasses()
dropFields = ["TREATMENT","BASEPATTRN","TIMESERIES","SCALEFACTR","AVGVALUE","PATTERN1","PATTERN2",
              "PATTERN3","PATTERN4","HYDROGRAPH","SSAREA","TOTCONAREA","IMPCONAREA","UNITFLOW",
              "AVGDEPTH","MAXDEPTH","MAXHGL","TIMEMAXHGL","REMAXDEPTH","MAXLATFLOW","MAXTOTFLOW",
              "TOTLATFLOW","TOTINFLOW","CULVRTCODE","CTRLRULES","MAXSPREAD","TOTCONAREA",
              "IMPCONAREA","UNITFLOW","MAXFLOW","TIMEMAXFLW","MAXVELOCIT","CAPFLOW","CAPDEPTH", "MAXVOLUME",
              "FULLBOTH","HRSFULLUP", "FULLDOWN","FULLNORMAL","HRSLIMITED","LENGTHFACT","DRY","SUBCRIT",
              "SUPERCRIT","NORMALLTD","INLETCNTRL","SEEPAGE","OPENRATE","ENDCONTRCT","ENDCOEFF",
              "SURCHARGE","COEFFCURVE","ROADWIDTH","ROADSURF","BASEFLOW","FLOWERROR","HRSSURCHAR","MAXSURCHAR",
              "MINDEPTHBR","HOURSFLOOD","MAXFLOODR","TOTFLDVOL","MAXPONDED","OUTLET","FLOWFREQ","AVGFLOW",
              "TOTALFLOW","PONDEDAREA","SUCTHEAD","CONDUCT","INITDEFICT","AVGVOLUME","AVGPERCENT","EVAPLOSS",
              "INFILLOSS","PCNTLOSS","MAXPERCENT","MAXOUTFLOW"]

arcpy.AddMessage("Adding required fields and feild calculating project fields for all features in {0}\n".format(GDB))

# Go through each record to add fields and calculate the user input entries
for feature in features:
    featureName = os.path.join(GDB, feature)
    arcpy.AddMessage("Required fields added to " + featureName)
    # Add required fields to each shape
    arcpy.AddField_management(featureName,"SOURCE","TEXT","","","255")
    arcpy.CalculateField_management(featureName, "SOURCE",'"'+ source + '"', "PYTHON_9.3")
    arcpy.AddField_management(featureName,"STUDY_YR","TEXT","","","4")
    arcpy.CalculateField_management(featureName, "STUDY_YR", '"'+ studyYear + '"', "PYTHON_9.3")
    arcpy.AddField_management(featureName,"MODEL","TEXT","","","50")
    arcpy.CalculateField_management(featureName, "MODEL", '"'+ SWMMinput + '"', "PYTHON_9.3")
    arcpy.AddField_management(featureName,"SWMM_VER","TEXT","","","50")
    arcpy.CalculateField_management(featureName, "SWMM_VER", '"'+ SWMMver + '"', "PYTHON_9.3")
    arcpy.AddField_management(featureName,"CUHP_VER","TEXT","","","10")
    arcpy.CalculateField_management(featureName, "CUHP_VER", '"'+ CUHPversion + '"', "PYTHON_9.3")
    arcpy.AddField_management(featureName,"MHFDBASIN","DOUBLE",10,2)
    # Add field DESIGNPT to selected features
    if feature == "Dividers" or feature == "Junctions" or feature == "Outfalls" or feature == "Storages":
        arcpy.AddField_management(featureName,"DESIGNPT","TEXT","","","10")
    arcpy.AddField_management(featureName,"Q_Ex_WQ","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Ex_001","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Ex_002","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Ex_005","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Ex_010","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Ex_025","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Ex_050","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Ex_100","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Ex_500","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Fut_WQ","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Fut_001","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Fut_002","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Fut_005","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Fut_010","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Fut_025","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Fut_050","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Fut_100","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"Q_Fut_500","DOUBLE",10,2)
    arcpy.AddField_management(featureName,"LASTEDITOR","TEXT","","","255")
    arcpy.AddField_management(featureName,"LAST_DATE","TEXT","","","10")
    if feature == "Outlets":
        arcpy.DeleteField_management(featureName, "COEFF")
    # Delete non-deliverable fields
    arcpy.DeleteField_management(featureName, dropFields)


arcpy.Delete_management("Subcatchments")
