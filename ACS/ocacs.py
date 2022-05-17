################################# OCACS Main Programming Class #################################

import csv
import os
import shutil
from datetime import datetime, timedelta
from time import timedelta

import arcpy
import import
import pandas

###### MAIN OCACS CLASS ######


class ocacs(object):
    """
    OCACS Python Class. Processes and analyzes census data for the American Community Survey products for the geographies in Orange County, California.

    Args:
        Inputs:
            year(integer): The ACS year.
            est(1 or 5, integers): the year-estimates of the data.
            dataOrigin(path): the path to the original ACS Census datasets (geodatabases) downloaded from Tiger/Line Census website (one for each geography). The path does not have to be inside the project directory.
            prjDir(path): the current project directory. THat's where all the processed data will be saved and stored.       
        Notes:
            1. The class uses 14 ACS Geographies:
                1.1. Block Groups (BG)
                1.2. Congressional Districts xxxth US Congress (CD)
                1.3. Orange County (COUNTY)
                1.4. County Subdivisions (COUSUB)
                1.5. Census Cities/Places (PLACE)
                1.6. Public Use Microadata Areas (PUMA)
                1.7. Elementary School Districts (SDE)
                1.8. Secondary School Districts (SDS)
                1.9. Unified School Districts (SDU)
                1.10. State Assembly Legislative Districts (SLDL)
                1.11. State Senate Legislative Districts (SLDU)
                1.12. Census Tracts (TRACT)
                1.13. Urban Areas (UA)
                1.14. ZIP Code Tabulation Areas (ZCTA)
            2. The original geodatabases must exist in the <dataOrigin> directory folder. If other geodatabases exist in the folder, (e.g., additional geographies usch as MSA, METDIV, CSA), the python processing script will ignore them.
            3. The output geodatabase structure is created inside an empty folder in the <prjDir> (ignoring other files and directories).
        Credits:
            Script created by Dr. Kostas Alexandridis, GISP, OC Public Works, OC Survey/Geospatial Services, December 2019-2022, Version 2.0
    """


###### Function: Class Initialization ######

    def __init__(self, prjPath):
        """Class instantiation function. See class notes.

        Args:
            prjPath(path): the path to the project directory.
        """

        # Creates path for the "original" and "processed" versions of the dataset.
        self.dataIn = os.path.join(prjPath, "Original")
        self.dataOut = os.path.join(prjPath, "Processed")

        # Read the geodatabases, and obtain the Census product, the year, and the year-estimates
        arcpy.env.workspace = self.dataIn
        arcpy.env.overwriteOutput = True

        # Read the file geodatabase workspaces in the input folder, and obtain a list of geodatabase names
        self.wrkspListIn = arcpy.ListWorkspaces("ACS*", "FileGDB")
        self.gdbListIn = [os.path.split(w)[1] for w in self.wrkspListIn]

        # Get all the prefixes and geo-levels from the geodatabase list
        # table of product list (e.g., ACS)
        prodList = [i.split(".gdb")[0].split("_")[0] for i in self.gdbListIn]
        # table of the year(s)
        yearList = [i.split(".gdb")[0].split("_")[1] for i in self.gdbListIn]
        # table of the estimates (e.g., 1% or 5%)
        estList = [i.split(".gdb")[0].split("_")[2] for i in self.gdbListIn]
        # table of the geographic level (one of 14 geographies)
        geoList = [i.split(".gdb")[0].split("_")[3] for i in self.gdbListIn]

        # Calculate and check counts (to make sure uniquiness), and fill relevant data
        if prodList.count(prodList[0]) == len(prodList):
            self.prod = f"{prodList[0]}"
            if yearList.count(yearList[0]) == len(yearList):
                self.year = int(yearList[0])
                if estList.count(estList[0]) == len(estList):
                    self.est = estList[0]
                    self.prefix = f"OC{self.prod}{self.year}"

        # Compute the US Congress number based on the year of the ACS survey and
        cdn = int(113 + (self.year - 2012) * 0.5)

        # Geo-reference lookup table
        self.geolookup = {
            "COUNTY": ("CO", "Orange County"),
            "COUSUB": ("CS", "County Subdivisions"),
            "PLACE": ("PL", "Cities/Places"),
            "ZCTA": ("ZC, ZIP Code Tabluation Areas"),
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
        self.geoNames = {}

        if "COUNTY" in geoList:
            self.geoNames["CO"] = "Orange County"
        if "COUSUB" in geoList:
            self.geoNames["CS"] = "County Subdivisions"
        if "PLACE" in geoList:
            self.geoNames["PL"] = "Cities/Places"
        if "ZCTA" in geoList:
            self.geoNames["ZC"] = "ZIP Code Tabulation Areas"
        if "CD" in geoList:
            self.geoNames["CD"] = f"Congressional Districts, {cdn}th US Congress"
        if "SLDL" in geoList:
            self.geoNames["LL"] = "State Assembly Legislantive Districts"
        if "SLDU" in geoList:
            self.geoNames["UL"] = "State Senate Legislative Districts"
        if "SDE" in geoList:
            self.geoNames["ED"] = "Elementary School Districts"
        if "SDS" in geoList:
            self.geoNames["SD"] = "Secondary School Districts"
        if "SDU" in geoList:
            self.geoNames["UD"] = "Unified School Districts"
        if "UA" in geoList:
            self.geoNames["UA"] = "Urban Areas"
        if "PUMA" in geoList:
            self.geoNames["PU"] = "Public Use Microdata Areas"
        if "BG" in geoList:
            self.geoNames["BG4"] = "Block Groups"
        if "TRACT" in geoList:
            self.geoNames["Census Tracts"]

        # List of all the geographic code levels
        self.geoLevels = [key for key in self.geoNames.keys()]

        # List of four ACS category characteristics
        self.acsCategory = {
            "D": "Demographic Characteristics",
            "S": "Social Characteristics",
            "E": "Economic Characteristics",
            "H": "Housing Characteristics"
        }

        # Close initialization Function
        return super().__init__()

    ################ FUNCTION: PROCESSING GEODATABASE TABLES ################

    def processTables(self):
        """Processing Geodatabase Tables Function
        """
