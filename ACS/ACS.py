import os, arcpy

year = 2017
est = 5

prefix = f"ACS{year}Y{est}"
prjDir = r"E:\Dev\Repos\OCGeoDemographics\ACS"
dataOrigin = r"E:\ACS2017"

os.chdir(prjDir)

from ocacs import ocacs

acs17 = ocacs(year, est, dataOrigin, prjDir)

acs17.acsCreateGdbStructure()
acs17.acsAddGdbAlias()


xlsxMetadata = os.path.join(prjDir, "Metadata and Documentation", "MasterMetadata.xlsx")

# Dictionary containing codes and aliases for each of the project's geography levels.
geoNames = {
    "BG": "Block Groups",
    "CD115": "Congressional Districts, 115th US Congress",
    "COUNTY": "Orange County",
    "COUSUB": "County Subdivisions",
    "PLACE": "Cities",
    "PUMA": "Public Use Microdata Areas",
    "SDE": "Elementary School Districts",
    "SDS": "Secondary School Districts",
    "SDU": "Unified School Districts",
    "SLDL": "State Assembly Legislative Districts",
    "SLDU": "State Senate Legislative Districts",
    "TRACT": "Census Tracts",
    "UA": "Urban Areas",
    "ZCTA": "ZIP Code Tabulation Areas"
    }
# List of all the geographic code levels
geoLevels = [key for key in geoNames.keys()]

arcpy.env.workspace = dataOrigin
arcpy.env.overwriteOutput = True

workspaces = {l: arcpy.ListWorkspaces(f"ACS*{l}*", "FileGDB")[0] for l in geoLevels}

for layer in workspaces:
    print(workspaces[layer])