import os, arcpy

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
        return super().__init__()






    def acsCreateGdbStructure(self):
        """
        Creates the main geodatabase structure for ACS geographies in Orange County.

        Notes:
            1. The function inherits the path to the project structure and the ACS bundle prefix (e.g., 'OCACS16Y5') from the class instantiation function.
            2. The function also inherits the 14 ACS geographies from the class instantiation function.
        """
        return


