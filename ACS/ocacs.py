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

    def __init__(self, year, est, dataOrigin, prjDir):
        """
        Class instantiation function.
        See class notes.
        """
        self.step = 0 # step enumeration to be used throughout the class for documentation.
        self.prefix = f"ACS{year}Y{est}"
        self.prjDir = prjDir
        self.dataOrigin = dataOrigin
        self.xlsxMetadata = os.path.join(self.prjDir, "Metadata and Documentation", "MasterMetadata.xlsx")

        # Dictionary containing codes and aliases for each of the project's geography levels.
        self.geoNames = {
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
        self.geoLevels = [key for key in self.geoNames.keys()]

        # Increment the initialization step (from 0 to 1, so that the first function calling the intialized object has initial step = 1.
        self.step += 1
        #return
        return super().__init__()






    def acsCreateGdbStructure(self):
        """
        Creates the main geodatabase structure for ACS geographies in Orange County.

        Notes:
            1. The function inherits the path to the project structure and the ACS bundle prefix (e.g., 'OCACS16Y5') from the class instantiation function.
            2. The function also inherits the 14 ACS geographies from the class instantiation function.
        """
        try:
            print(f"\nSTEP {self.step}: RESTRUCTURING ORIGINAL GEODATABASES")
            arcpy.env.workspace = self.dataOrigin
            arcpy.env.overwriteOutput = True

            print(f"\tObtaining workspaces for original census ACS data...")
            # List all file geodatabases in the current workspace
            workspaces = {l: arcpy.ListWorkspaces(f"ACS*{l}*", "FileGDB")[0] for l in self.geoLevels}

            print(f"\tObtaining original geodatabase lists...")
            origGdb = {i: os.path.split(j)[1] for i, j in workspaces.items()}

            print(f"\tDefining a list of new geodatabase geographies...")
            newGdb = {level: f"{self.prefix}_{level}.gdb" for level in self.geoLevels}

            # Create new geodatabases for census geographies (delete if they exist)

            print(f"\tCreating new geodatabases for census ACS geographies:")
            if os.path.exists(os.path.join(self.dataOrigin, self.prefix)) is False:
                os.mkdir(os.path.join(self.dataOrigin, self.prefix))

            for level, gdb in newGdb.items():
                print(f"\t\tGeography Level {level}: {gdb}")
                pathGdb = os.path.join(self.dataOrigin, self.prefix, gdb)
                if arcpy.Exists(pathGdb):
                    print(f"\t\t\tGeodatabase for {level} exists. Deleting geodatabase: {gdb}")
                    arcpy.Delete_management(pathGdb)
                print(f"\t\t\tCreating new geodatabase: {gdb}")
                arcpy.CreateFileGDB_management(os.path.join(self.dataOrigin, self.prefix), gdb)

            self.step += 1

            print(f"\nSTEP {self.step}: CREATING BASE GEOGRAPHIES IN GEODATABASES")

            # COUNTY Geodatabase
            print("\tSetting up geography for County Level:")
            # Create a temporary layer of the original County data (national)
            print("\t\tDefining workspace...")
            curWorkspace = workspaces["COUNTY"]

            print("\t\tDefining output geodatabase")
            outGdbLyr = os.path.join(self.dataOrigin, self.prefix, newGdb["COUNTY"], newGdb["COUNTY"][:-4])
        
            print("\t\tSetting ArcPy environment...")
            arcpy.env.workspace = curWorkspace
            arcpy.env.overwriteOutput = True
        
            print("\t\tCreating temporary layer from original geography...")
            fcIn = arcpy.ListFeatureClasses()[0]
            arcpy.MakeFeatureLayer_management(fcIn, "lyrIn")

            # Select only the Orange County polygon
            print("\t\tSelecting polygon for Orange County...")
            lyrOut = arcpy.SelectLayerByAttribute_management("lyrIn", "NEW_SELECTION", "GEOID = '06059'")

            # Place the resulting Orange COunty polygon into the new project geodatabase
            print("\t\tPlacing resulting polygon into new County geodatabase...")
            arcpy.CopyFeatures_management(lyrOut, outGdbLyr)

            # Delete the temporary layers
            print("\t\tDeleting temporary layers...")
            arcpy.Delete_management("lyrIn", "lyrOut")

            # Add feature class alias
            print(f"\t\tAdding feature class alias: {self.geoNames['COUNTY']}")
            arcpy.AlterAliasName(outGdbLyr, f"{self.geoNames['COUNTY']}")

            # Create a feature layer for the new County layer - will not delete this until the end
            arcpy.MakeFeatureLayer_management(outGdbLyr, "lyrCounty")

            # Remaining geographic levels processing
            print("\tSetting up remaining geographies (looping):")
            for level, gdb in newGdb.items():
                if "COUNTY" not in level:
                    print(f"\n\t\tProcessing level {level}: {gdb}")
                    curWorkspace = workspaces[level]

                    print(f"\t\t\tCurrent workspace: {curWorkspace}")
                    outGdbLyr = os.path.join(self.dataOrigin, self.prefix, gdb, gdb[:-4])
                
                    print(f"\t\t\tNew geodatabase feature class: {outGdbLyr}")
                    print("\t\t\tSetting ArcPy environment...")
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
                    print(f"\t\t\tAdding feature class alias: {self.geoNames[level]}")
                    arcpy.AlterAliasName(outGdbLyr, f"{self.geoNames[level]}")

            # Delete county feature layer after geoprocessing operations
            print("\n\tDeleting temporary layer for County.")
            arcpy.Delete_management("lyrCounty")

            print("\nScript Finished. Exiting.")

        except arcpy.ExecuteError:
            # Print geoprocessing exception messages
            print(arcpy.GetMessages(2))
        except Exception as ex:
            # Print the exception message
            print(ex.args[0])

        return




    def acsAddGdbAlias(self, theme=None):
        """
        Function generating alias for fields in each geodatabase's census tables from a metadata excel file.
        
        Notes:
            1. gdbPath is the path to the geodatabase for whom the table field aliases will be updated.
            2. xlsxMetadata is the excel file containing the metadata (two columns: Field, and Alias)
        """
        try:
            startTime = time()
            print(f"\tScript started on: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")

            arcpy.env.workspace = self.dataOrigin
            arcpy.env.overwriteOutput = True

            workspaces = {l: arcpy.ListWorkspaces(f"ACS*{l}*", "FileGDB")[0] for l in self.geoLevels}

            for level in self.geoLevels:
                print(f"\nProcessing Level: {level}")
                gdbPath = workspaces[level]

                os.chdir(gdbPath)
                arcpy.env.workspace = gdbPath
                arcpy.env.overwiteOutput = True

                # Read metadata into an array
                print("\t\tReading metadata excel file into an array...")
                metaArray = pandas.read_excel(self.xlsxMetadata, sheet_name = "Metadata")
                if theme == None:
                    inTables = arcpy.ListTables("X*")
                elif isinstance(theme, list):
                    inTables = theme
                elif isinstance(theme, str):
                    inTables = [f"{theme}"]

                endTime = time()
                execTime = str(timedelta(seconds = round(endTime - startTime)))
                print(f"\t\tEnd of preliminaries session. Total execution time: {execTime}\n")


                for table in inTables:
                    fieldList = [t.name for t in arcpy.ListFields(table)]
                    metaList = [s for s in metaArray.values if s[0] in fieldList]
                    countList = len(metaList)

                    # Change fields and aliases for the table
                    print(f"\t\tChanging field aliases for the table: {table}")
                    startTime1 = time()

                    for i, row in enumerate(metaList):
                        if row[0] in fieldList:
                            print(f"\t\t\t[{level}] {table}: Alias ({i+1} of {countList}) field {row[0]}: {row[1]}")
                            arcpy.AlterField_management(table, row[0], row[0], row[1])
                    endTime = time()
                    execTime = str(timedelta(seconds = round(endTime - startTime)))
                    execTime1 = str(timedelta(seconds = round(endTime - startTime1)))
                    print(f"\t\tCompleted table {table}. Total execution time: {execTime1} ({execTime} since script started)\n")

            endTime = time()
            execTime = str(timedelta(seconds = round(endTime - startTime)))
            print(f"\t\tTotal execution time: {execTime}\n")


        except arcpy.ExecuteError:
            # Print geoprocessing exception messages
            print(arcpy.GetMessages(2))
        except Exception as ex:
            # Print the exception message
            print(ex.args[0])

        return

    # Returns the text prefix of the data tables
    def removePrefix(self, text, textprefix):
        if text.startswith(textprefix):
            return text[len(textprefix):]
        return text



    # Function for looping all tables
    #def acsCreateFc(self, geoLevel):
    #    """
    #    Function for looping all geodatabase tables.
    #    Creating geodatabase feature classes (for a single geography) by thematic census table and adds alias from metadata fields.
    #    """
    #    try:
    #        startTime = time()
    #        print("\nScript started on {0}".format(datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
    #        print("\n\tBeginning general operations:")

    #        # Define levels, names, workspaces, etc.
    #        print("\tSetting up operational definitions...")
    #        acrpy.env.workspace = self.prjDir
    #        inGdb = arcpy.ListWorkspaces("*_{0}*".format(geoLevel), "FileGDB")[0]
    #        arcpy.env.workspace = inGdb
    #        inTables = arcpy.ListTables("X*")
    #        arcpy.env.workspace = os.path.join(self.dataOrigin, self.prefix)
