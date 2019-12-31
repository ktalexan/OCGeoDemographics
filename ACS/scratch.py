import os, arcpy




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
            prefix = f"{prod}_{year}_{est}"

# Compute the US Congress number based on the year of the ACS survey:
cdn = int(113 + (year - 2012) * 0.5)

# Dictionary containing codes and aliases for each of the project's geography levels
geoNames = {}
if "COUNTY" in geoList:
    geoNames["COUNTY"] = "Orange County"
if "COUSUB" in geoList:
    geoNames["COUSUB"] = "County Subdivisions"
if "PLACE" in geoList:
    geoNames["PLACE"] = "Cities/Places"
if "ZCTA" in geoList:
    geoNames["ZCTA"] = "ZIP Code Tabulation Areas"
if "CD" in geoList:
    geoNames[f"CD{cdn}"] = f"Congressional Disticts, {cdn}th US Congress"
if "SLDL" in geoList:
    geoNames[f"SLDL"] = "State Assembly Legislative Districts"
if "SLDU" in geoList:
    geoNames[f"SLDU"] = "State Senate Legislative Districts"
if "SDE" in geoList:
    geoNames["SDE"] = "Elementary School Districts"
if "SDS" in geoList:
    geoNames["SDS"] = "Secondary School Districts"
if "SDU" in geoList:
    geoNames["SDU"] = "Unified School Districts"
if "UA" in geoList:
    geoNames["UA"] = "Urban Areas"
if "PUMA" in geoList:
    geoNames["PUMA"] = "Public Use Microdata Areas"
if "BG" in geoList:
    geoNames["BG"] = "Block Groups"
if "TRACT" in geoList:
    geoNames["TRACT"] = "Census Tracts"


geoLevels = [key for key in geoNames.keys()]




################## ocacsGdbStructure #####################

arcpy.env.workspace = dataIn
arcpy.env.overwriteOutput = True

gdbListOut = {level: f"{prefix}_{level}.gdb" for level in geoLevels}

# Create new geodatabases for census geographies (delete if they exist)
if os.path.exists(dataOut) is False:
    os.mkdir(dataOut)

for level, gdb in gdbListOut.items():
    pathGdb = os.path.join(dataOut, gdb)
    if arcpy.Exists(pathGdb):
        arcpy.Delete_management(pathGdb)
    arcpy.CreateFileGDB_management(dataOut, gdb)

# Changing the arcpy environment (dataOut)
arcpy.env.workspace = dataOut
arcpy.env.overwriteOutput = True

# Starting with the COUNTY geodatabase
print(f"\nSTEP")







arcpy.env.workspace = r"d:\OneDrive\Professional\Projects\OCPW\OCGeodemographics\OCACS\OCACS2017\Original\ACS_2017_5YR_BG_06_CALIFORNIA.gdb"



hcGR = {}
hcGRPI = {}
dhSA = {}

with arcpy.da.SearchCursor("BG_METADATA_2017", ["Short_Name", "Full_Name"]) as cursor:
    for row in cursor:
        if "e" in row[0]:

            if "B25063" in row[0]:
                hcGR[row[0]] = row[1].replace(strEst, "")

            if "B25070" in row[0]:
                hcGRPI[row[0]] = row[1].replace(strEst, "")

            if "B01001e1" in row[0]:
                dhSA[row[0]] = row[1].replace(strEst, "")
            if "B01001e2" in row[0]:
                dhSA[row[0]] = row[1].replace(strEst,"")
            if "B01001e26" in row[0]:
                dhSA[row[0]] = 


strEst = " -- (Estimate)"
dSexAge = {}
dRace = {}
dRaceAloneCombination = {}
with arcpy.da.SearchCursor("BG_METADATA_2017", ["Short_Name", "Full_Name"]) as cursor:
    for row in cursor:
        if "e" in row[0]:
            if "B01001" in row[0]:
                dSexAge[row[0]] = row[1].replace(strEst, "").replace("SEX BY AGE: ", "")
            if "B02001" in row[0]:
                dRace[row[0]] = row[1].replace(strEst, "").replace("RACE: ", "")
            for var in ["B02001e1", "B02008e1", "B02009e1", "B02010e1", "B02011e1", "B02012e1", "B02013e1"]:
                if var in row[0] and "B02001e10" not in row[0]:
                    dRaceAloneCombination[row[0]] = row[1].replace(strEst, "")




arcpy.CreateFileGDB_management(dataOut,"OCACS2017Y5_DH_SEXBYAGE")



