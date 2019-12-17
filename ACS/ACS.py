import os, arcpy

year = 2017
est = 5

prefix = f"ACS{year}Y{est}"
prjDir = os.getcwd()
dataOrigin = r"E:\ACS2017"

from ocacs import ocacs

acs17 = ocacs(year, est, dataOrigin, prjDir)

acs17.acsCreateGdbStructure()

arcpy.env.workspace = dataOrigin
arcpy.env.overwriteOutput = True

workspaces = {l: sorted(arcpy.ListWorkspaces(f"ACS*_{l}*", "FileGDB"))[i] for i, l in enumerate(geoLevels)}

workspaces = {}
for level in geoLevels:
    workspaces = {level: arcpy.ListWorkspaces(f"ACS*_{level}*", "FileGDB")[0]}

workspaces = {l: arcpy.ListWorkspaces(f"ACS*_{l}*", "FileGDB")[0] for l in geoLevels}
