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
