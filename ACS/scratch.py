import os, arcpy

os.chdir(r"E:\Dev\Repos\OCGeoDemographics\ACS")
from ocacs import ocacs

basepath = os.environ["OneDriveConsumer"]
folderpath = r"Professional\Projects\OCPW\OCGeodemographics\OCACS"
years = ['2017', '2016', '2015', '2014', '2013']

prjPathList = [os.path.join(basepath, folderpath, f"OCACS{year}") for year in years]

ocacs(prjPathList[0])


for prjPath in prjPathList:
    print(f"\n\nPROCESSING YEAR: {prjPath[-4:]}\n")
    ocacs(prjPath)





