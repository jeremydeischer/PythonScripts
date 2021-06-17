# PopulateHydrologicResults.py
# Programmer: Cody Garcia - GIS Analyst; Icon Engineering, Inc.
# Date: 4/27/2021
# Description: This script will autopopulate discharge fields for existing and future conditions
#   from link and node CSV files. Make sure to delete the last 5 fields in the CSV files that are
#   completely blank (H through L). For some reason SWIMM has those as fields but they are blank.
#   The links CSVs were used to populate discharge values for the conduits and outlets features.
#   The nodes CSVs were used to populate discharges for the junctions, storages, dividers, and
#   outfalls features.
#   JOIN fields for links (in features "NAME", in CSVs "Link")
#   JOIN fields for nodes (in features "NAME", in CSVs "Node")


# Inputs:
    # Existing link conditions: input existing link CSV
    # Future link conditions: input future link CSV
    # Existing node conditions: input existing node CSV
    # Future lnode conditions: input future node CSV
    # Project GDB: project GDB created with SWIMM to GDB tool

# Output: populated discharge fields for all feautres within project GDB, and tables added to the
#   project GDB from the CSV files

######################################################################################################
import arcpy, os
arcpy.env.overwriteOutput = True

inLinkExisting = arcpy.GetParameterAsText(0)
tblName0 = os.path.basename(inLinkExisting[:-4])
inLinkFuture = arcpy.GetParameterAsText(1)
tblName1 = os.path.basename(inLinkFuture[:-4])
inNodeExisting = arcpy.GetParameterAsText(2)
tblName2 = os.path.basename(inNodeExisting[:-4])
inNodeFuture = arcpy.GetParameterAsText(3)
tblName3 = os.path.basename(inNodeFuture[:-4])
GDB = arcpy.GetParameterAsText(4)   #Project GDB created in SWIMM to GDB script

# Set environments workspace
arcpy.env.workspace = GDB

# Import all CSVs into project GDB, and make table views to call later
arcpy.AddMessage("\nImporting CSVs into project geodatabase \n")
arcpy.TableToTable_conversion (inLinkExisting, GDB, tblName0)
tbl0 = os.path.join(GDB,tblName0)
arcpy.MakeTableView_management(tbl0, "tbl0_view")

arcpy.TableToTable_conversion (inLinkFuture, GDB, tblName1)
tbl1 = os.path.join(GDB,tblName1)
arcpy.MakeTableView_management(tbl1, "tbl1_view")

arcpy.TableToTable_conversion (inNodeExisting, GDB, tblName2)
tbl2 = os.path.join(GDB,tblName2)
arcpy.MakeTableView_management(tbl2, "tbl2_view")

arcpy.TableToTable_conversion (inNodeFuture, GDB, tblName3)
tbl3 = os.path.join(GDB,tblName3)
arcpy.MakeTableView_management(tbl3, "tbl3_view")

# Start with Links existing and future CSVs;
# JOIN Conduits to tbl0 (exisitng), field calculate fields, then delete non-required fields
arcpy.AddMessage("Updating existing and future discharges for Conduits and Outlets\n")
arcpy.JoinField_management("Conduits", 'NAME',"tbl0_view", 'LINK')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Ex_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Ex_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Ex_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Ex_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Ex_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Ex_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Ex_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Ex_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Link","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Conduits", dropFields)

# JOIN Conduits to tbl1 (future), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Conduits", 'NAME',"tbl1_view", 'LINK')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Fut_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Fut_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Fut_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Fut_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Fut_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Fut_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Fut_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Conduits",
                                "Q_Fut_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Link","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Conduits", dropFields)


# JOIN Outlets to tbl0 (existing), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Outlets", 'NAME',"tbl0_view", 'LINK')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Ex_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Ex_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Ex_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Ex_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Ex_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Ex_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Ex_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Ex_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Link","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR","F500YR"]
arcpy.DeleteField_management("Outlets", dropFields)

# JOIN Outlets to tbl1 (future), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Outlets", 'NAME',"tbl1_view", 'LINK')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Fut_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Fut_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Fut_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Fut_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Fut_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Fut_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Fut_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Outlets",
                                "Q_Fut_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Link","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Outlets", dropFields)

# Junctions, storages, dividers, outfalls join to Nodes existing and future, then feild calculate
# JOIN Junctions to tbl0 (existing), field calculate fields, then delete non-required fields
arcpy.AddMessage("Updating existing and future discharges for Junctions, Storages, Dividers, Outfalls\n")
arcpy.JoinField_management("Junctions", 'NAME',"tbl2_view", 'Node')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Ex_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Ex_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Ex_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Ex_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Ex_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Ex_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Ex_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Ex_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Node","Type","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Junctions", dropFields)

# JOIN Junctions to tbl1 (future), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Junctions", 'NAME',"tbl3_view", 'Node')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Fut_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Fut_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Fut_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Fut_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Fut_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Fut_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Fut_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Junctions",
                                "Q_Fut_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Node","Type","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Junctions", dropFields)

# JOIN Storages to tbl0 (existing), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Storages", 'NAME',"tbl2_view", 'Node')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Ex_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Ex_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Ex_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Ex_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Ex_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Ex_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Ex_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Ex_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Node","Type","F1YR","F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Storages", dropFields)

# JOIN Junctions to tbl1 (future), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Storages", 'NAME',"tbl3_view", 'Node')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Fut_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Fut_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Fut_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Fut_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Fut_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Fut_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Fut_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Storages",
                                "Q_Fut_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Node","Type","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Storages", dropFields)

# JOIN Dividers to tbl0 (existing), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Dividers", 'NAME',"tbl2_view", 'Node')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Ex_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Ex_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Ex_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Ex_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Ex_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Ex_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Ex_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Ex_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Node","Type_1","F1YR","F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Dividers", dropFields)

# JOIN Dividers to tbl1 (future), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Dividers", 'NAME',"tbl3_view", 'Node')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Fut_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Fut_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Fut_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Fut_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Fut_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Fut_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Fut_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Dividers",
                                "Q_Fut_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Node","Type_1","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Dividers", dropFields)

# JOIN Outfalls to tbl0 (existing), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Outfalls", 'NAME',"tbl2_view", 'Node')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Ex_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Ex_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Ex_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Ex_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Ex_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Ex_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Ex_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Ex_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Node","Type_1","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Outfalls", dropFields)

# JOIN Outlets to tbl1 (future), field calculate fields, then delete non-required fields
arcpy.JoinField_management("Outfalls", 'NAME',"tbl3_view", 'Node')

exp001 = "!F1YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Fut_001", exp001, "PYTHON_9.3")
exp002 = "!F2YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Fut_002", exp002, "PYTHON_9.3")
exp005 = "!F5YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Fut_005", exp005, "PYTHON_9.3")
exp010 = "!F10YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Fut_010", exp010, "PYTHON_9.3")
exp025 = "!F25YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Fut_025", exp025, "PYTHON_9.3")
exp050 = "!F50YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Fut_050", exp050, "PYTHON_9.3")
exp100 = "!F100YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Fut_100", exp100, "PYTHON_9.3")
exp500 = "!F500YR!"
arcpy.CalculateField_management("Outfalls",
                                "Q_Fut_500", exp500, "PYTHON_9.3")

# Delete fields after Join
dropFields = ["Node","Type_1","F1YR", "F2YR", "F5YR", "F10YR", "F25YR", "F50YR", "F100YR", "F500YR"]
arcpy.DeleteField_management("Outfalls", dropFields)
