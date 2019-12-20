import os, arcpy, shutil, csv, pandas
from datetime import datetime, timedelta
from time import time

class ocacs(object):
    """
    OCACS Python Class. Processes and analyzes census data for the American Community Survey products for the geographies in Orange County, California.
    
    Inputs:
        year: the ACS year (integer)
        est: the year-estimates of the data (1 or 5, integers)
        dataOrigin: the path to the original ACS Census datasets (geodatabases) downloaded from Tiger/Line Census website (one for each geography). The path does not have to be inside the project directory.
        prjDir: the current project directory. That's where all the processed data will be saved and stored.

    Notes:
        1. The class uses 14 ACS geographies: Block Groups (BG), Congressional Districts, 115th US Congress (CD115), Orange County (COUNTY), County Subdivisions (COUSUB), Census Cities/Places (PLACE), Public Use Microdata Areas (PUMA), Elementary/Secondary/Unified School Districts (SDE/SDS/SDU), State Assembly/Senate Legislative Districts (SLDL/SLDU), Census Tracts (TRACT), Urban Areas (UA), and ZIP Code Tabulation Areas (ZCTA).
        2. The original geodatabases must exist in the <dataOrigin> directory folder. If other geodatabases exist in the folder (e.g., additional geographies such as MSA, METDIV, CSA), the python processing script will ignore them.
        3. The output geodatabase structure is created inside an empty folder in the <prjDir> (ignoring other files and directories).

    Credits:
        Script created by Dr. Kostas Alexandridis, GISP, OC Public Works, OC Survey/Geospatial Services, December 2019. Version 2.0.
    """

    def __init__(self, dataIn, dataOut):
        """
        Class instantiation function. See class notes
        """
        self.dataIn = dataIn
        self.dataOut = dataOut

        # Read the geodatabases, and obtain the Census product, the year, and the year-estimate
        arcpy.env.workspace = self.dataIn
        arcpy.env.overwriteOutput = True

        # Read the file geodatabase workspaces in the input folder, and obtain a list of geodatabase names.
        self.wrkspListIn = arcpy.ListWorkspaces("ACS*", "FileGDB")
        self.gdbListIn = [os.path.split(w)[1] for w in self.wkspListIn]

        # Get all the prefixes and geo-levels from the geodatabase list.
        prodList = [i.split(".gdb")[0].split("_")[0] for i in self.gdbListIn]
        yearList = [i.split(".gdb")[0].split("_")[1] for i in self.gdbListIn]
        estList = [i.split(".gdb")[0].split("_")[2] for i in self.gdbListIn]
        geoList = [i.split(".gdb")[0].split("_")[3] for i in self.gdbListIn]

        if prodList.count(prodList[0]) == len(prodList):
            self.prod = f"OC{prodList[0]}"
            if yearList.count(yearList[0]) == len(yearList):
                self.year = yearList[0]
                if estList.count(estList[0]) == len(estList):
                    self.est = estList[0]
                    self.prefix = f"{self.prod}_{self.year}_{self.est}"
        
        # Compute the US Congress number based on the year of the ACS survey
        cdn = int(113 + (self.year - 2012) * 0.5)


        # Dictionary containing codes and aliases for each of the project's geography levels
        self.geoNames = {}

        if "COUNTY" in geoList:
            self.geoNames["COUNTY"] = "Orange County"
        if "COUSUB" in geoList:
            self.geoNames["COUSUB"] = "County Subdivisions"
        if "PLACE" in geoList:
            self.geoNames["PLACE"] = "Cities/Places"
        if "ZCTA" in geoList:
            self.geoNames["ZCTA"] = "ZIP Code Tabulation Areas"
        if "CD" in geoList:
            self.geoNames[f"CD{cdn}"] = f"Congressional Disticts, {cdn}th US Congress"
        if "SLDL" in geoList:
            self.geoNames[f"SLDL"] = "State Assembly Legislative Districts"
        if "SLDU" in geoList:
            self.geoNames[f"SLDU"] = "State Senate Legislative Districts"
        if "SDE" in geoList:
            self.geoNames["SDE"] = "Elementary School Districts"
        if "SDS" in geoList:
            self.geoNames["SDS"] = "Secondary School Districts"
        if "SDU" in geoList:
            self.geoNames["SDU"] = "Unified School Districts"
        if "UA" in geoList:
            self.geoNames["UA"] = "Urban Areas"
        if "PUMA" in geoList:
            self.geoNames["PUMA"] = "Public Use Microdata Areas"
        if "BG" in geoList:
            self.geoNames["BG"] = "Block Groups"
        if "TRACT" in geoList:
            self.geoNames["TRACT"] = "Census Tracts"


        # List of all the geographic code levels
        self.geoLevels = [key for key in self.geoNames.keys()]

        return super().__init__()


    def ocacsGdbStructure(self):
        """
        """
        print("\nSTEP 1: RESTRUCTURING ORIGINAL GEODATABASES")
        arcpy.env.workspace = self.dataIn
        arcpy.env.overwriteOutput = True

        print(f"\tDefining a list of new geodatabase geographies...")


        gdbListOut = {level: f"{self.prefix}_{level}.gdb" for level in self.geoLevels}


        # Create new geodatabases for census geographies (delete if they exist)
        print(f"\tCreating new geodatabaes for ACS geographies:")
        if os.path.exists(os.path.join(self.prjOut)) is False:
            os.md