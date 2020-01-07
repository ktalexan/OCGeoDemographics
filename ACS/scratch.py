import os, arcpy


os.chdir(r"E:\Dev\Repos\OCGeoDemographics\ACS")

from TableVars import *



#################### DEF __INIT___ ##########################

basepath = os.environ["OneDriveConsumer"]
prjPath = os.path.join(basepath, r"Professional\Projects\OCPW\OCGeodemographics\OCACS\OCACS2017")

dataIn = os.path.join(prjPath, "Original")
dataOut = os.path.join(prjPath, "Processed")


arcpy.env.workspace = dataIn
arcpy.env.overwriteOutput = True

# Read the file geodatabase workspaces in the input folder, and obtain a list of geodatabase names
wrkspListIn = arcpy.ListWorkspaces("ACS*", "FileGDB")
gdbListIn = [os.path.split(w)[1] for w in wrkspListIn]

# Get all the prefixes and geo-levels from the geodatabase list
prodList = [i.split(".gdb")[0].split("_")[0] for i in gdbListIn]
yearList = [i.split(".gdb")[0].split("_")[1] for i in gdbListIn]
estList = [i.split(".gdb")[0].split("_")[2] for i in gdbListIn]
geoList = [i.split(".gdb")[0].split("_")[3] for i in gdbListIn]

if prodList.count(prodList[0]) == len(prodList): # check if all items in list are the same
    prod = f"OC{prodList[0]}"
    if yearList.count(yearList[0]) == len(yearList): # check if all years are the same
        year = int(yearList[0])
        if estList.count(estList[0]) == len(estList): # check if all estimate years are the same
            est = estList[0]
            prefix = f"{prod}{year}"

# Compute the US Congress number based on the year of the ACS survey:
cdn = int(113 + (year - 2012) * 0.5)

# Lookup geo-reference table
geolookup = {
    "COUNTY": ("CO", "Orange County"),
    "COUSUB": ("CS", "County Subdivisions"),
    "PLACE": ("PL", "Cities/Places"),
    "ZCTA": ("ZC", "ZIP Code Tabulation Areas"),
    "CD": ("CD", f"Congressional Districts of the {cdn}th US Congress"),
    "SLDL": ("LL", "State Assembly Legislative Districts"),
    "SLDU": ("UL", "State Senate Legislative Districts"),
    "SDE": ("ED", "Elementary School Districts"),
    "SDS": ("SD", "Secondary School Districts"),
    "SDU": ("UD", "Unified School Districts"),
    "UA": ("UA", "Urban Areas"),
    "PUMA": ("PU", "Public Use Microdata Areas"),
    "BG": ("BG", "Block Groups"),
    "TRACT": ("TR", "Census Tracts")
    }

# Dictionary containing codes and aliases for each of the project's geography levels
geoNames = {}
if "COUNTY" in geoList:
    geoNames["CO"] = "Orange County"
if "COUSUB" in geoList:
    geoNames["CS"] = "County Subdivisions"
if "PLACE" in geoList:
    geoNames["PL"] = "Cities/Places"
if "ZCTA" in geoList:
    geoNames["ZC"] = "ZIP Code Tabulation Areas"
if "CD" in geoList:
    geoNames["CD"] = f"Congressional Disticts, {cdn}th US Congress"
if "SLDL" in geoList:
    geoNames["LL"] = "State Assembly Legislative Districts"
if "SLDU" in geoList:
    geoNames["UL"] = "State Senate Legislative Districts"
if "SDE" in geoList:
    geoNames["ED"] = "Elementary School Districts"
if "SDS" in geoList:
    geoNames["SD"] = "Secondary School Districts"
if "SDU" in geoList:
    geoNames["UD"] = "Unified School Districts"
if "UA" in geoList:
    geoNames["UA"] = "Urban Areas"
if "PUMA" in geoList:
    geoNames["PU"] = "Public Use Microdata Areas"
if "BG" in geoList:
    geoNames["BG"] = "Block Groups"
if "TRACT" in geoList:
    geoNames["TR"] = "Census Tracts"


geoLevels = [key for key in geoNames.keys()]


acsCategory = {
    "D": "Demographic Characteristics",
    "S": "Social Characteristics",
    "E": "Economic Characteristics",
    "H": "Housing Characteristics"
    }


################## ocacsGdbStructure #####################

print("\nSTEP 1: RESTRUCTURING ORIGINAL GEODATABASES")
arcpy.env.workspace = dataIn
arcpy.env.overwriteOutput = True

print(f"\tDefining a list of new geodatabase geographies...")

# List of geodatabases to be created
gdbListOut = {level: f"{prefix}{level}.gdb" for level in acsCategory}

# Create new geodatabases for census geographies (delete if they exist)
if os.path.exists(dataOut) is False:
    os.mkdir(dataOut)

print(f"\tCreating new geodatabases for ACS geographies:")
for level, gdb in gdbListOut.items():
    print(f"\t\tCategory: {acsCategory[level]}")
    pathGdb = os.path.join(dataOut, gdb)
    if arcpy.Exists(pathGdb):
        print(f"\t\t...geodatabase exists. Deleting...")
        arcpy.Delete_management(pathGdb)
    print(f"\t\t...Creating geodatabase: {gdb}")
    arcpy.CreateFileGDB_management(dataOut, gdb)


print(f"\nSTEP 2: CREATING BASE GEOGRAPHIES IN GEODATABASE DIRECTORY")

# Changing the arcpy environment (dataOut)
arcpy.env.workspace = dataOut
arcpy.env.overwriteOutput = True

# Starting with the COUNTY geodatabase
print("\tSetting up geography for County level:")

# Create a temporary layer of the original County data (national)
print("\t\tDefining workspace")
curWorkspace = [str for str in wrkspListIn if "COUNTY" in os.path.split(str)[1]][0]

print("\t\tDefining output geodatabase")
#outGdbLyr = os.path.join(dataIn, )

print("\t\tSetting ArcPy environment...")
arcpy.env.workspace = curWorkspace
arcpy.env.overwriteOutput = True

fcIn = arcpy.ListFeatureClasses()[0]
arcpy.MakeFeatureLayer_management(fcIn, "lyrIn")

# Select only the Orange County polygon
print("\t\tSelecting polygon for Orange County...")
lyrOut = arcpy.SelectLayerByAttribute_management("lyrIn", "NEW_SELECTION", "GEOID = '06059'")

# Place the resulting Orange County polygon into each of the category geodatabases
print("\t\tPlacing resulting polygon into geodatabases...")
for cat in gdbListOut.keys():
    outGdbLyr = os.path.join(dataOut, gdbListOut[cat], f"{prefix}CO{cat}")
    arcpy.CopyFeatures_management(lyrOut, outGdbLyr)


# Delete the temporary layers
print("\t\tDeleting temporary layers...")
arcpy.Delete_management("lyrIn", "lyrOut")

# Add feature class alias
print("\t\tAdding feature class alias: {")
for cat in gdbListOut.keys():
    outGdbLyr = os.path.join(dataOut, gdbListOut[cat], f"{prefix}CO{cat}")
    arcpy.AlterAliasName(outGdbLyr, f"{acsCategory[cat]} for {geoNames['CO']}")

    # Create a feature layer for the new county layer - will not delete this until the end:
    arcpy.MakeFeatureLayer_management(outGdbLyr, "lyrCounty")

    # Remaining geographic levels processing
    print("\tSetting up remaining geographies (looping):")
    workspaceOut = os.path.join(dataOut, gdbListOut[cat])

    for level, (code, alias) in geolookup.items():
        if "COUNTY" not in level:
            print(f"\n\t\tProcessing level {code}: {alias}")
            curWorkspace = [str for str in wrkspListIn if level in os.path.split(str)[1]][0]

            print(f"\t\t\tCurrent workspace: {curWorkspace}")
            outGdbLyr = os.path.join(dataOut, gdbListOut[cat], f"{prefix}{code}{cat}")

            print(f"\t\t\tNew geodatabase feature class: {outGdbLyr}")
            print(f"\t\t\tSetting ArcPy environment...")
            arcpy.env.workspace = curWorkspace
            arcpy.env.overwriteOutput = True

            fcIn = arcpy.ListFeatureClasses()[0]
            print(f"\t\t\tFeature classes to be copied: {fcIn}")

            # Create a temporary layer for the original data (national)
            print("\t\t\tCreating temporary layer...")
            arcpy.MakeFeatureLayer_management(fcIn, "lyrIn")

            # Select features from original that are within a distance (-1000 feet) of the Orange County polygon (all are selected)
            print("\t\t\tSelecting features within distance (1,000 feet) from County layer...")
            lyrOut = arcpy.SelectLayerByLocation_management("lyrIn", "WITHIN_A_DISTANCE", "lyrCounty", "-1000 Feet", "NEW_SELECTION", "NOT_INVERT")

            # Place the selected features into the new feature class in the project geodatabase
            print("\t\t\tCopying selected features to the new geodatabase feature class...")
            arcpy.CopyFeatures_management(lyrOut, outGdbLyr)

            # Delete the temporary layers
            print("\t\t\tDeleting temporary layers...")
            arcpy.Delete_management("lyrIn", "lyrOut")

            # Add feature class alias
            print(f"\t\t\tAdding feature class alias: {alias}")
            arcpy.AlterAliasName(outGdbLyr, f"{acsCategory[cat]} for {alias}")

    # Delete county feature layer after geoprocessing operations
    print("\n\tDeleting temporary layer for County.")
    arcpy.Delete_management("lyrCounty")
    

tableLevels = getTableVars()

tableMatch = {
    "D": {"D01":"X01", "D02":"X01", "D03":"X02", "D04":"X02", "D05":"X03", "D06":"X05"},
    "S": {"S01":["X11", "X25"], "S02":"X09", "S03":"X12", "S04":"X13", "S05":"X10", "S06":"X14", "S07":"X15", "S08":"X21", "S09":"X18", "S10":"X18", "S11":"X07", "S12":"X05", "S13":"X05", "S14":"X05", "S15":"X05", "S16":"X16", "S17":"X16", "S18":"X04", "S19":"X28"},
    "E": {"E01":"X23", "E02":"X23", "E03":"X08", "E04":"X08", "E05":"X08", "E06":"X08", "E07":"X08", "E08":"X24", "E09":"X24", "E10":"X24", "E11":["X19", "X22"], "E12":["X19", "X20"], "E13":"X19", "E14":"X27", "E15":"X17", "E16":"X17", "E17":"X17", "E18":"X17", "E19":"X17"},
    "H": {"H01":"X25", "H02":"X25", "H03":"X25", "H04":"X25", "H05":"X25", "H06":"X25", "H07":"X25", "H08":"X25", "H09":"X25", "H10":"X25", "H11":"X25", "H12":"X25", "H13":"X25", "H14":"X25", "H15":"X25", "H16":"X25", "H17":"X25", "H18":"X25", "H19":"X25", "H20":"X25", "H21":"X25", "H22":"X25", "H23":"X25"}
    }




for cat in gdbListOut.keys():
    dlist = tableMatch[cat]
    for level, (code, alias) in geolookup.items():
        print(f"\nProcessing level {code}: {alias}")
        inWorkspace = [str for str in wrkspListIn if level in os.path.split(str)[1]][0]
        outWorkspace = os.path.join(dataOut, gdbListOut[cat])
        fc = os.path.join(f"{prefix}{code}{cat}")
        joinField1 = "GEOID_Data"
        joinField2 = "GEOID"

        print("\tSetting arcpy environment to input...")
        arcpy.env.workspace = inWorkspace
        arcpy.env.overwriteOutput = True


        print("\tObtaining original list of tables...")
        inTables = arcpy.ListTables("X*")

        print("\tChanging arcpy environment to output...")
        arcpy.env.workspace = outWorkspace
        arcpy.env.overwriteOutput = True

        for dno, tno in dlist.items():
            print(f"\n\tProcessing group {dno} for table(s) {tno}")

            if isinstance(tno, str):
                for tname in inTables:
                    if tno in tname:
                        inTable = tname
                        joinTable = os.path.join(inWorkspace, inTable)
                        levelfields = [key for key in tableLevels[cat][dno].keys()]
                        arcpy.JoinField_management(fc, joinField1, joinTable, joinField2, levelfields)
                        print("\t...Adding aliases to feature class")
                    aliases = [alias for alias in tableLevels[cat][dno].items()]
                    for field, alias in aliases:
                        newfield = f"{dno}{field}"
                        print(f"\t\t...adding alias {dno}: {alias}")
                        arcpy.AlterField_management(fc, field, newfield, f"{dno}: {alias}")

            elif isinstance(tno, list):
                for t in tno:
                    for tname in inTables:
                        if t in tname:
                            inTable = tname
                            joinTable = os.path.join(inWorkspace, inTable)
                            levelfields = [key for key in tableLevels[cat][dno].keys() if key[1:3] == t[1:3]]
                            arcpy.JoinField_management(fc, joinField1, joinTable, joinField2, levelfields)                    
                    print("\t...Adding aliases to feature class")
                    aliases = [alias for alias in tableLevels[cat][dno].items()]
                    for field, alias in aliases:
                        newfield = f"{dno}{field}"
                        print(f"\t\t...adding alias {dno}: {alias}")
                        arcpy.AlterField_management(fc, field, newfield, f"{dno}: {alias}")


