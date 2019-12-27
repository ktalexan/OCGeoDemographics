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





# D: DEMOGRAPHIC AND HOUSING ESTIMATES

# D01: Sex and Age (Universe: Total population)
d01_SexAndAge = {
    "B01001e1": "Total population",
    "B01001e2": "Male",
    "B01001e3": "Male, under 5 years",
    "B01001e4": "Male, 5 to 9 years",
    "B01001e5": "Male, 10 to 14 years",
    "B01001e6": "Male, 15 to 17 years",
    "B01001e7": "Male, 18 and 19 years",
    "B01001e8": "Male, 20 years",
    "B01001e9": "Male, 21 years",
    "B01001e10": "Male, 22 to 24 years",
    "B01001e11": "Male, 25 to 29 years",
    "B01001e12": "Male, 30 to 34 years",
    "B01001e13": "Male, 35 to 39 years",
    "B01001e14": "Male, 40 to 44 years",
    "B01001e15": "Male, 45 to 49 years",
    "B01001e16": "Male, 50 to 54 years",
    "B01001e17": "Male, 55 to 59 years",
    "B01001e18": "Male, 60 and 61 years",
    "B01001e19": "Male, 62 to 64 years",
    "B01001e20": "Male, 65 and 66 years",
    "B01001e21": "Male, 67 to 69 years",
    "B01001e22": "Male, 70 to 74 years",
    "B01001e23": "Male, 75 to 79 years",
    "B01001e24": "Male, 80 to 84 years",
    "B01001e25": "Male, 85 years and over",
    "B01001e26": "Female",
    "B01001e27": "Female, under 5 years",
    "B01001e28": "Female, 5 to 9 years",
    "B01001e29": "Female, 10 to 14 years",
    "B01001e30": "Female, 15 to 17 years",
    "B01001e31": "Female, 18 and 19 years",
    "B01001e32": "Female, 20 years",
    "B01001e33": "Female, 21 years",
    "B01001e34": "Female, 22 to 24 years",
    "B01001e35": "Female, 25 to 29 years",
    "B01001e36": "Female, 30 to 34 years",
    "B01001e37": "Female, 35 to 39 years",
    "B01001e38": "Female, 40 to 44 years",
    "B01001e39": "Female, 45 to 49 years",
    "B01001e40": "Female, 50 to 54 years",
    "B01001e41": "Female, 55 to 59 years",
    "B01001e42": "Female, 60 and 61 years",
    "B01001e43": "Female, 62 to 64 years",
    "B01001e44": "Female, 65 and 66 years",
    "B01001e45": "Female, 67 to 69 years",
    "B01001e46": "Female, 70 to 74 years",
    "B01001e47": "Female, 75 to 79 years",
    "B01001e48": "Female, 80 to 84 years",
    "B01001e49": "Female, 85 years and over"
    }

# D02: Median Age by Sex and Age (Universe: Total population)
d02_MedianAgeSexRace = {
    "B01002e1": "Median age (years)",
    "B01002e2": "Male, median age (years)",
    "B01002e3": "Female, median age (years)",
    "B01002Ae1": "White alone, median age (years)",
    "B01002Be1": "Black or African American alone, median age (years)",
    "B01002Ce1": "American Indian and Alaska Native alone, median age (years)",
    "B01002De1": "Asian alone, median age (years)",
    "B01002Ee1": "Native Hawaiian and Other Pacific Islander alone, median age (years)",
    "B01002Fe1": "Some other race alone, median age (years)",
    "B01002Ge1": "Two or more races, median age (years)",
    "B01002He1": "White alone, not Hispanic or Latino, median age (years)",
    "B01002Ie1": "Hispanic or Latino, median age (years)"
    }




# D03: Race (Universe: Total population)
d03_Race = {
    "B02001e1": "Total population",
    "B02001e2": "White alone",
    "B02001e3": "Black or African American alone",
    "B02001e4": "American Indian and Alaska Native alone",
    "B02001e5": "Asian alone",
    "B02001e6": "Native Hawaiian and Other Pacific Islander alone",
    "B02001e7": "Some other race alone",
    "B02001e8": "Two or more races"
    }


# D04: Race Alone or in Combination with One or More Other Races (Universe: Total population)
d04_RaceCombinations = {
    "B02001e1": "Total population",
    "B02008e1": "White",
    "B02009e1": "Black or African American",
    "B02010e1": "American Indian and Alaska Native",
    "B02011e1": "Asian",
    "B02012e1": "Native Hawaiian and Other Pacific Islander",
    "B02013e1": "Some other race"
    }


# D05: Hispanic or Latino and Race (Universe: Total population)
d05_HispanicOrLatinoRace = {
    "B03002e1": "Total population",
    "B03002e2": "Not Hispanic or Latino",
    "B03002e3": "Not Hispanic or Latino, White alone",
    "B03002e4": "Not Hispanic or Latino, Black or African American alone",
    "B03002e5": "Not Hispanic or Latino, American Indian and Alaska Native alone",
    "B03002e6": "Not Hispanic or Latino, Asian alone",
    "B03002e7": "Not Hispanic or Latino, Native Hawaiian and Other Pacific Islander alone",
    "B03002e8": "Not Hispanic or Latino, Some other race alone",
    "B03002e9": "Not Hispanic or Latino, Two or more races",
    "B03002e10": "Not Hispanic or Latino, Two races including some other race",
    "B03002e11": "Not Hispanic or Latino, Two races excluding some other race, and three or more races",
    "B03002e12": "Hispanic or Latino",
    "B03002e13": "Hispanic or Latino, White alone",
    "B03002e14": "Hispanic or Latino, Black or African American alone",
    "B03002e15": "Hispanic or Latino, American Indian and Alaska Native alone",
    "B03002e16": "Hispanic or Latino, Asian alone",
    "B03002e17": "Hispanic or Latino, Native Hawaiian and Other Pacific Islander alone",
    "B03002e18": "Hispanic or Latino, Some other race alone",
    "B03002e19": "Hispanic or Latino, Two or more races",
    "B03002e20": "Hispanic or Latino, Two races including some other race",
    "B03002e21": "Hispanic or Latino, Two races excluding some other race, and three or more races"
    }




# D06: Citizen Voting Age Population (Universe: Citizen, 18 and over population)
d06_CitizenVotingAge = {
    "B": "Citizen, 18 and over population",
    "B": "Citizen, Male",
    "B": "Citize, Female"
    }





# S: SOCIAL CHARACTERISTICS
# S01: Households by Type (Universe: Total households)

s01_HouseholdsType = {
    "B11001e1": "Total households",
    "B11001e2": "Family households (families)",
    "B11003e1": "Family households with own children of the householder under 18 years",
    "B11001e3": "Married-couple family households",
    "B11003e3": "Married-couple family households with own children of the householder under 18 years",
    "B11001e5": "Male householder, no wife present, family households",
    "B11003e10": "Male householder, no wife present, family households with own children of the householder under 18 years",
    "B11001e6": "Female householder, no husband present, family households",
    "B11003e16": "Female householder, no husband present, family households with own children of the householder under 18 years",
    "B11001e7": "Nonfamily households",
    "B11001e8": "Nonfamily households, householder living alone",
    "B11005e2": "Households with one or more people under 18 years",
    "B11007e2": "Households with one or more people 65 years and over",
    "B": "Average household size",
    "B": "Average family size"
    }


# S02: Relationship (Universe: Population in households)
s02_Relationship = {
    "B09019e2": "Population in households",
    "B09019e4": "Householder",
    "B09019e7": "Spouse",
    "B09019e8": "Child",
    "B09019e9": "Child, biological",
    "B09019e10": "Child, adopted",
    "B09019e11": "Child, stepchild",
    "B09019e12": "Grandchild",
    "B09019e13": "Brother or sister",
    "B09019e14": "Parent",
    "B09019e15": "Parent in law",
    "B09019e16": "Son in law or daughter in law",
    "B09019e17": "Other relatives",
    "B09019e18": "Non-relatives",
    "B09019e19": "Non-relatives, roomer or boarder",
    "B09019e20": "Non-relatives, housemate or roomate",
    "B09019e21": "Non-relatives, unmarried partner",
    "B09019e22": "Non-relatives, foster child",
    "B09019e23": "Non-relatives, other"
    }


# S03: Marital Status (Universe: Males or Females 15 years and over)
s03_MaritalStatus = {
    "B12001e1": "Total population, 15 years and over",
    "B12001e2": "Males, 15 years and over",
    "B12001e3": "Males, 15 years and over, never married",
    "B12001e5": "Males, 15 years and over, now married, except separated",
    "B12001e7": "Males, 15 years and over, separated",
    "B12001e9": "Males, 15 years and over, widowed",
    "B12001e10": "Males, 15 years and over, divorced",
    "B12001e11": "Females, 15 years and over",
    "B12001e12": "Females, 15 years and over, never married",
    "B12001e14": "Females, 15 years and over, now married, except separated",
    "B12001e16": "Females, 15 years and over, separated",
    "B12001e18": "Females, 15 years and over, widowed",
    "B12001e19": "Females, 15 years and over, divorced"
    }


# S04: Fertility (Universe: Number of women 15 to 50 years old who had a birth in the past 12 months)
s04_Fertility = {
    "B": "Number of women 15 to 50 years old who had a birth in the past 12 months",
    "B": "Unmarried (widowed, divorced, and never married)",
    "B": "Unmarried, per 1,000 unmarried women",
    "B": "Per 1,000 women 15 to 50 years old",
    "B": "Per 1,000 women 15 to 19 years old",
    "B": "Per 1,000 women 20 to 34 years old",
    "B": "Per 1,000 women 35 to 50 years old"
    }

# S05: Grandparents (Universe: Number of grandparents living or responsible for own grandchildren under 18 years)
s05_Grandparents = {
    "B": "Number of grandparents living with own grandchildren under 18 years",
    "B": "Number of grandparents living with own grandchildren under 18 years, responsible for grandchildren",
    "B": "Number of grandparents living with own grandchildren under 18 years, years responsible for grandchildren",
    "B": "Number of grandparents living with own grandchildren under 18 years, less than 1 year responsible for grandchildren",
    "B": "Number of grandparents living with own grandchildren under 18 years, 1 or 2 years responsible for grandchildren",
    "B": "Number of grandparents living with own grandchildren under 18 years, 3 or 4 years responsible for grandchildren",
    "B": "Number of grandparents living with own grandchildren under 18 years, 5 or more years responsible for grandchildren",
    "B": "Number of grandparents responsible for own grandchildren under 18 years",
    "B": "Number of grandparents responsible for own grandchildren under 18 years who are female",
    "B": "Number of grandparents responsible for own grandchildren under 18 years, who are married"
    }


# S06: School Enrollment (Universe: Population 3 years and over enrolled in school)
s06_SchoolEnrollment = {
    "B14007e2": "Population 3 years and over enrolled in school",
    "B14007e3": "Nursery school, preschool",
    "B14007e4": "Kindergarten",
    "B14007e5": "Elementary school, grade 1",
    "B14007e6": "Elementary school, grade 2",
    "B14007e7": "Elementary school, grade 3",
    "B14007e8": "Elementary school, grade 4",
    "B14007e9": "Elementary school, grade 5",
    "B14007e10": "Elementary school, grade 6",
    "B14007e11": "Elementary school, grade 7",
    "B14007e12": "Elementary school, grade 8",
    "B14007e13": "High school, grade 9",
    "B14007e14": "High school, grade 10",
    "B14007e15": "High school, grade 11",
    "B14007e16": "High school, grade 12",
    "B14007e17": "College, undergraduate years",
    "B14007e18": "Graduate or professional school"
    }


# S07: Educational Attainment (Universe: Population 25 years and over)
s07_EducationalAttainment = {
    "B15003e1": "Population 25 years and over",
    "B15003e2": "No schooling completed",
    "B15003e3": "Nursery school",
    "B15003e4": "Kindergarten",
    "B15003e5": "1st grade",
    "B15003e6": "2nd grade",
    "B15003e7": "3rd grade",
    "B15003e8": "4th grade",
    "B15003e9": "5th grade",
    "B15003e10": "6th grade",
    "B15003e11": "7th grade",
    "B15003e12": "8th grade",
    "B15003e13": "9th grade",
    "B15003e14": "10th grade",
    "B15003e15": "11th grade",
    "B15003e16": "12th grade",
    "B15003e17": "High school diploma",
    "B15003e18": "GED or alternative credential",
    "B15003e19": "Some college, less than 1 year",
    "B15003e20": "Some college, 1 or more years, no degree",
    "B15003e21": "Associate's degree",
    "B15003e22": "Bachelor's degree",
    "B15003e23": "Master's degree",
    "B15003e24": "Professional school degree",
    "B15003e25": "Doctorate degree"
    }


# S08: Veteran Status (Universe: Civilian population 18 years and over)
s08_VeteranStatus = {
    "B21001e1": "Civilian population 18 years and over",
    "B21001e2": "Civilian veterans"
    }


# S09: Disability Status (Universe: Total civilian non-institutionalized population)
s09_DisabilityStatus = {
    "B": "Total civilian non-institutionalized population",
    "B": "Total civilian non-institutionalized population, with a disability",
    "B": "Under 18 years",
    "B": "Under 18 years, with a disability",
    "B": "18 to 64 years",
    "B": "18 to 64 years, with a disability",
    "B": "65 years and over",
    "B": "65 years and over, with a disability"
    }


# S10: Residence 1 Year Ago (Universe: Population 1 year and over)
s10_Residence = {
    "B": "Population 1 year and over",
    "B": "Same house",
    "B": "Different house in the US",
    "B": "Different house in the US, same county",
    "B": "Different house in the US, different county",
    "B": "Different house in the US, different county, same state",
    "B": "Different house in the US, different county, different state",
    "B": "Abroad"
    }


# S11: Place of Birth (Universe: Total population)
s11_PlaceOfBirth = {
    "B00001e1": "Total population",
    "B": "Native population",
    "B": "Native population, born in US",
    "B": "Native population, born in US, state of residence",
    "B": "Native population, born in US, different state",
    "B": "Native population, born in PR, USVI, or born abroad to American parent(s)",
    "B": "Foreign born"
    }


# S12: US Citizenship Status (Universe: Foreign-born population)
s12_CitizenshipStatus = {
    "B": "Foreign born population",
    "B": "Naturalized US citizen",
    "B": "Not a US citizen"
    }


# S13: Year of Entry (Universe: Population born outside the United States)
s13_YearOfEntry = {
    "B": "Population born outside the US",
    "B": "Native",
    "B": "Native, entered 2010 or later",
    "B": "Native, entered before 2010",
    "B": "Foreign born",
    "B": "Foreign born, entered 2010 or later",
    "B": "Foreign born, entered before 2010"
    }


# S14: World Region of Birth of Foreign Born Population (Universe: Foreign-born population, escluding population born at sea)
s14: BirthRegion = {
    "B": "Foreign born population, excluding population born at sea",
    "B": "Europe",
    "B": "Asia",
    "B": "Africa",
    "B": "Oceania",
    "B": "Latin America",
    "B": "Northern America"
    }


# S15: Language Spoken in Households (Universe: Total households)
s15_LanguageSpokenHouseholds = {
    "C16002e1": "Total households",
    "C16002e2": "English only households",
    "C16002e3": "Spanish households",
    "C16002e6": "Other Indo-European languages households",
    "C16002e9": "Asian and Pacific Island languages households",
    "C16002e12": "Other languages households"
    }

# S16: Language Spoken at Home (Universe: Population 5 years and over)
s16_LanguageSpokenHome = {
    "B16004e1": "Population 5 years and over",
    "B16004e2": "5 to 17 years",
    "B16004e3": "5 to 17 years, speak only English",
    "B16004e4": "5 to 17 years, speak Spanish",
    "B16004e5": "5 to 17 years, speak Spanish, speak English 'very well'",
    "B16004e6": "5 to 17 years, speak Spanish, speak English 'well'",
    "B16004e7": "5 to 17 years, speak Spanish, speak English 'not well'",
    "B16004e8": "5 to 17 years, speak Spanish, speak English 'not at all'",
    "B16004e9": "5 to 17 years, speak other Indo-European languages",
    "B16004e10": "5 to 17 years, speak other Indo-European languages, speak English 'very well'",
    "B16004e11": "5 to 17 years, speak other Indo-European languages, speak English 'well'",
    "B16004e12": "5 to 17 years, speak other Indo-European languages, speak English 'not well'",
    "B16004e13": "5 to 17 years, speak other Indo-European languages, speak English 'not at all'",
    "B16004e14": "5 to 17 years, speak Asian and Pacific Island languages",
    "B16004e15": "5 to 17 years, speak Asian and Pacific Island languages, speak English 'very well'",
    "B16004e16": "5 to 17 years, speak Asian and Pacific Island languages, speak English 'well'",
    "B16004e17": "5 to 17 years, speak Asian and Pacific Island languages, speak English 'not well'",
    "B16004e18": "5 to 17 years, speak Asian and Pacific Island languages, speak English 'not at all'",
    "B16004e19": "5 to 17 years, speak other languages",
    "B16004e20": "5 to 17 years, speak other languages, speak English 'very well'",
    "B16004e21": "5 to 17 years, speak other languages, speak English 'well'",
    "B16004e22": "5 to 17 years, speak other languages, speak English 'not well'",
    "B16004e23": "5 to 17 years, speak other languages, speak English 'not at all'",
    "B16004e24": "18 to 64 years",
    "B16004e25": "18 to 64 years, speak only English",
    "B16004e26": "18 to 64 years, speak Spanish",
    "B16004e27": "18 to 64 years, speak Spanish, speak English 'very well'",
    "B16004e28": "18 to 64 years, speak Spanish, speak English 'well'",
    "B16004e29": "18 to 64 years, speak Spanish, speak English 'not well'",
    "B16004e30": "18 to 64 years, speak Spanish, speak English 'not at all'",
    "B16004e31": "18 to 64 years, speak other Indo-European languages",
    "B16004e32": "18 to 64 years, speak other Indo-European languages, speak English 'very well'",
    "B16004e33": "18 to 64 years, speak other Indo-European languages, speak English 'well'",
    "B16004e34": "18 to 64 years, speak other Indo-European languages, speak English 'not well'",
    "B16004e35": "18 to 64 years, speak other Indo-European languages, speak English 'not at all'",
    "B16004e36": "18 to 64 years, speak Asian and Pacific Island languages",
    "B16004e37": "18 to 64 years, speak Asian and Pacific Island languages, speak English 'very well'",
    "B16004e38": "18 to 64 years, speak Asian and Pacific Island languages, speak English 'well'",
    "B16004e39": "18 to 64 years, speak Asian and Pacific Island languages, speak English 'not well'",
    "B16004e40": "18 to 64 years, speak Asian and Pacific Island languages, speak English 'not at all'",
    "B16004e41": "18 to 64 years, speak other languages",
    "B16004e42": "18 to 64 years, speak other languages, speak English 'very well'",
    "B16004e43": "18 to 64 years, speak other languages, speak English 'well'",
    "B16004e44": "18 to 64 years, speak other languages, speak English 'not well'",
    "B16004e45": "18 to 64 years, speak other languages, speak English 'not at all'",
    "B16004e46": "65 years and over",
    "B16004e47": "65 years and over, speak only English",
    "B16004e48": "65 years and over, speak Spanish",
    "B16004e49": "65 years and over, speak Spanish, speak English 'very well'",
    "B16004e50": "65 years and over, speak Spanish, speak English 'well'",
    "B16004e51": "65 years and over, speak Spanish, speak English 'not well'",
    "B16004e52": "65 years and over, speak Spanish, speak English 'not at all'",
    "B16004e53": "65 years and over, speak other Indo-European languages",
    "B16004e54": "65 years and over, speak other Indo-European languages, speak English 'very well'",
    "B16004e55": "65 years and over, speak other Indo-European languages, speak English 'well'",
    "B16004e56": "65 years and over, speak other Indo-European languages, speak English 'not well'",
    "B16004e57": "65 years and over, speak other Indo-European languages, speak English 'not at all'",
    "B16004e58": "65 years and over, speak Asian and Pacific Island languages",
    "B16004e59": "65 years and over, speak Asian and Pacific Island languages, speak English 'very well'",
    "B16004e60": "65 years and over, speak Asian and Pacific Island languages, speak English 'well'",
    "B16004e61": "65 years and over, speak Asian and Pacific Island languages, speak English 'not well'",
    "B16004e62": "65 years and over, speak Asian and Pacific Island languages, speak English 'not at all'",
    "B16004e63": "65 years and over, speak other languages",
    "B16004e64": "65 years and over, speak other languages, speak English 'very well'",
    "B16004e65": "65 years and over, speak other languages, speak English 'well'",
    "B16004e66": "65 years and over, speak other languages, speak English 'not well'",
    "B16004e67": "65 years and over, speak other languages, speak English 'not at all'"
    }


# S17: Ancestry (Universe: Total population)
s17_Ancestry = {
    "B00001e1": "Total population",
    "B": "American population",
    "B": "Arab population",
    "B": "Czech population",
    "B": "Danish population",
    "B": "Dutch population",
    "B": "English population",
    "B": "French (except Basque) population",
    "B": "French Canadian population",
    "B": "German population",
    "B": "Greek population",
    "B": "Hungarian population",
    "B": "Irish population",
    "B": "Italian population",
    "B": "Lithuanian population",
    "B": "Norwegian population",
    "B": "Polish population",
    "B": "Portugese population",
    "B": "Russian population",
    "B": "Scotch-Irish population",
    "B": "Scottish population",
    "B": "Slovak population",
    "B": "Subsaharan African population",
    "B": "Swedish population",
    "B": "Swiss population",
    "B": "Ukranian population",
    "B": "Welsh population",
    "B": "West Indian (excluding Hispanic origin groups) population"
    }


# S18: Computers and Internet Use (Universe: Total households)
s18_ComputersInternet = {
    "B": "Total households",
    "B": "Households with a computer",
    "B": "Households with a broadband internet connection"
    }


# E. ECONOMIC CHARACTERISTICS

# E01: Employment Status (Universe: Population 16 years and over)
e01_EmploymentStatus = {
    "B23025e1": "Population 16 years and over",
    "B23025e2": "Population 16 years and over in labor force",
    "B23025e3": "Population 16 years and over in labor force, civilian labor force",
    "B23025e4": "Population 16 years and over in labor force, civilian labor force, employed",
    "B23025e5": "Population 16 years and over in labor force, civilian labor force, unemployed",
    "B23025e6": "Population 16 years and over in labor force, armed forces",
    "B23025e7": "Population 16 years and over not in labor force",
    

    "B": "Civilian labor force",
    "B": "Civilian labor force, unemployment rate",
    "B": "Females 16 years and over",
    "B": "Females 16 years and over in labor force",
    "B": "Females 16 years and over in labor force, civilian labor force",
    "B": "Females 16 years and over in labor force, civilian labor force, employed",
    "B": "Females 16 years and over in labor force, civilian labor force, unemployed",
    "B": "Own children of the householder under 6 years",
    "B": "Own children of the householder under 6 years, all parents in family in labor force",
    "B": "Own children of the householder 6 to 17 years",
    "B": "Own children of the householder 6 to 17 years, all parents in family in labor force"
    }

# E02: Work Status by Age of workers (Universe: population 16 years and over)
e02_WorkStatus = {
    "B23027e1": "Total population, 16 years and over",
    "B23027e2": "16 to 19 years",
    "B23027e3": "16 to 19 years, worked in the past 12 months",
    "B23027e4": "16 to 19 years, worked full-time, year-round for the past 12 months",
    "B23027e5": "16 to 19 years, worked less than full time, year-round for the past 12 months",
    "B23027e6": "16 to 19 years, did not work for the past 12 months",
    "B23027e7": "20 to 24 years",
    "B23027e8": "20 to 24 years, worked in the past 12 months",
    "B23027e9": "20 to 24 years, worked full-time, year-round for the past 12 months",
    "B23027e10": "20 to 24 years, worked less than full time, year-round for the past 12 months",
    "B23027e11": "20 to 24 years, did not work for the past 12 months",
    "B23027e12": "25 to 44 years",
    "B23027e13": "25 to 44 years, worked in the past 12 months",
    "B23027e14": "25 to 44 years, worked full-time, year-round for the past 12 months",
    "B23027e16": "25 tp 44 years, worked less than full time, year-round for the past 12 months",
    "B23027e16": "25 to 44 years, did not work for the past 12 months",
    "B23027e17": "45 to 54 years",
    "B23027e18": "45 to 54 years, worked in the past 12 months",
    "B23027e19": "45 to 54 years, worked full-time, year-round for the past 12 months",
    "B23027e20": "45 to 54 years, worked less than full time, year-round for the past 12 months",
    "B23027e21": "45 to 54 years, did not work for the past 12 months",
    "B23027e22": "55 to 64 years",
    "B23027e23": "55 to 64 years, worked in the past 12 months",
    "B23027e24": "55 to 64 years, worked full-time, year-round for the past 12 months",
    "B23027e25": "55 to 64 years, worked less than full time, year-round for the past 12 months",
    "B23027e26": "55 to 64 years, did not work for the past 12 months",
    "B23027e27": "65 to 69 years",
    "B23027e28": "65 to 69 years, worked in the past 12 months",
    "B23027e29": "65 to 69 years, worked full-time, year-round for the past 12 months",
    "B23027e30": "65 to 69 years, worked less than full time, year-round for the past 12 months",
    "B23027e31": "65 to 69 years, did not work for the past 12 months",
    "B23027e32": "70 years and over",
    "B23027e33": "70 years and over, worked in the past 12 months",
    "B23027e34": "70 years and over, worked full-time, year-round for the past 12 months",
    "B23027e35": "70 years and over, worked less than full time, year-round for the past 12 months",
    "B23027e36": "70 years and over, did not work for the past 12 months"
    }


# E03: Commuting to Work (Universe: Workers 16 years and over)
e03_Commuting = {
    "B08301e1": "Workers 16 years and over",
    "B08301e3": "Car, truck, or van - drove alone",
    "B08301e4": "Car, truck, or van - carpooled",
    "B08301e10": "Public transportation (excluding taxicab)",
    "B08301e19": "Walked",
    "B08301e20": "Other means",
    "B08301e21": "Worked at home",
    "B08135e1": "Aggregate travel time to work (minutes)"
    }


# E04: Occupation (Universe: Civilian employed population 16 years and over)
e04_Occupation = {
    "C24010e1": "Civilian employed population 16 years and over",
    "C24010e2": "Male",
    "C24010e5": "Male, management occupations",
    "C24010e6": "Male, business and financial operations occupations",
    "C24010e8": "Male, computer and mathematical occupations",
    "C24010e9": "Male, architecture and engineering occupations",
    "C24010e10": "Male, life, physical, and social science occupations",
    "C24010e12": "Male, community and social service occupations",
    "C24010e13": "Male, legal occupations",
    "C24010e14": "Male, education, training, and library occupations",
    "C24010e15": "Male, arts, design, entertainment, sports, and media occupations",
    "C24010e17": "Male, health diagnosing and treating practitioners and other technical occupations",
    "C24010e18": "Male, health technologists and technicians occupations",
    "C24010e20": "Male, healthcare support occupations",
    "C24010e22": "Male, fire fighting and prevention, and other protective service occupations",
    "C24010e23": "Male, law enforcement occupations",
    "C24010e24": "Male, food preparation and serving related occupations",
    "C24010e25": "Male, building and grounds cleaning and meintanence occupations",
    "C24010e26": "Male, personal care and service occupations",
    "C24010e28": "Male, sales and related occupations",
    "C24010e29": "Male, office and administrative support occupations",
    "C24010e31": "Male, farming, fishing, and forestry occupations",
    "C24010e32": "Male, construction and extraction occupations",
    "C24010e33": "Male, installation, maintenance and repair occupations",
    "C24010e35": "Male, production occupations",
    "C24010e36": "Male, transportation occupations",
    "C24010e37": "Male, material moving occupations",
    "C24010e38": "Female",
    "C24010e41": "Female, management occupations",
    "C24010e42": "Female, business and financial operations occupations",
    "C24010e44": "Female, computer and mathematical occupations",
    "C24010e45": "Female, architecture and engineering occupations",
    "C24010e46": "Female, life, physical, and social science occupations",
    "C24010e48": "Female, community and social service occupations",
    "C24010e49": "Female, legal occupations",
    "C24010e50": "Female, education, training, and library occupations",
    "C24010e51": "Female, arts, design, entertainment, sports, and media occupations",
    "C24010e53": "Female, health diagnosing and treating practitioners and other technical occupations",
    "C24010e54": "Female, health technologists and technicians occupations",
    "C24010e56": "Female, healthcare support occupations",
    "C24010e58": "Female, fire fighting and prevention, and other protective service occupations",
    "C24010e59": "Female, law enforcement occupations",
    "C24010e60": "Female, food preparation and serving related occupations",
    "C24010e61": "Female, building and grounds cleaning and meintanence occupations",
    "C24010e62": "Female, personal care and service occupations",
    "C24010e64": "Female, sales and related occupations",
    "C24010e65": "Female, office and administrative support occupations",
    "C24010e67": "Female, farming, fishing, and forestry occupations",
    "C24010e68": "Female, construction and extraction occupations",
    "C24010e69": "Female, installation, maintenance and repair occupations",
    "C24010e71": "Female, production occupations",
    "C24010e72": "Female, transportation occupations",
    "C24010e73": "Female, material moving occupations"
    }


# E05: Industry (Universe: Civilian employed population 16 years and over)
e05_Industry = {
    "C24030e1": "Civilian employed population 16 years and over",
    "C24030e2": "Male",
    "C24030e4": "Male, agriculture, forestry, fishing and hunting",
    "C24030e5": "Male, mining, quarrying, and oil and gas extraction",
    "C24030e6": "Male, construction",
    "C24030e7": "Male, manufacturing",
    "C24030e8": "Male, wholesale trade",
    "C24030e9": "Male, retail trade",
    "C24030e11": "Male, transportation and warehousing",
    "C24030e12": "Male, utilities",
    "C24030e13": "Male, information",
    "C24030e15": "Male, finance and insurance",
    "C24030e16": "Male, real estate and rental and leasing",
    "C24030e18": "Male, professional, scientific and technical services",
    "C24030e19": "Male, management of companies and enterprises",
    "C24030e20": "Male, administrative and support and waste management services",
    "C24030e22": "Male, educational services",
    "C24030e23": "Male, health care and social assistance",
    "C24030e25": "Male, arts, entertainment, and recreation",
    "C24030e26": "Male, accommodation and food services",
    "C24030e27": "Male, other services, except public administration",
    "C24030e28": "Male, public administration",
    "C24030e29": "Female",
    "C24030e31": "Female, agriculture, forestry, fishing and hunting",
    "C24030e32": "Female, mining, quarrying, and oil and gas extraction",
    "C24030e33": "Female, construction",
    "C24030e34": "Female, manufacturing",
    "C24030e35": "Female, wholesale trade",
    "C24030e36": "Female, retail trade",
    "C24030e38": "Female, transportation and warehousing",
    "C24030e39": "Female, utilities",
    "C24030e40": "Female, information",
    "C24030e42": "Female, finance and insurance",
    "C24030e43": "Female, real estate and rental and leasing",
    "C24030e45": "Female, professional, scientific and technical services",
    "C24030e46": "Female, management of companies and enterprises",
    "C24030e47": "Female, administrative and support and waste management services",
    "C24030e49": "Female, educational services",
    "C24030e50": "Female, health care and social assistance",
    "C24030e52": "Female, arts, entertainment, and recreation",
    "C24030e53": "Female, accommodation and food services",
    "C24030e54": "Female, other services, except public administration",
    "C24030e55": "Female, public administration"
    }


# E06: Class of Worker (Universe: Civilian employed population 16 years and over)
e06_ClassOfWorker = {
    "B24080e1": "Civilian employed population 16 years and over",
    "B24080e2": "Male",
    "B24080e4": "Male, employee of private company workers",
    "B24080e5": "Male, self-employed in own incorporated business workers",
    "B24080e6": "Male, private not-for-profit wage and salary workers",
    "B24080e7": "Male, local government workers",
    "B24080e8": "Male, state government workers",
    "B24080e9": "Male, federal government workers",
    "B24080e10": "Male, self-employed in own not incorporated business workers",
    "B24080e11": "Male, unpaid family workers",
    "B24080e12": "Female",
    "B24080e14": "Female, employee of private company workers",
    "B24080e15": "Female, self-employed in own incorporated business workers",
    "B24080e16": "Female, private not-for-profit wage and salary workers",
    "B24080e17": "Female, local government workers",
    "B24080e18": "Female, state government workers",
    "B24080e19": "Female, federal government workers",
    "B24080e20": "Female, self-employed in own not incorporated business workers",
    "B24080e21": "Female, unpaid family workers"
    }


# E07: Income and Benefits (Universe: Total households, families, nonfamilies, workers)
e07_IncomeAndBenefits = {
    "B19001e1": "Total households",
    "B19001e2": "Households, less than $10,000",
    "B19001e3": "Households, $10,000 to $14,999",
    "B19001e4": "Households, $15,000 to $19,999",
    "B19001e5": "Households, $20,000 to $24,999",
    "B19001e6": "Households, $25,000 to $29,999",
    "B19001e7": "Households, $30,000 to $34,999",
    "B19001e8": "Households, $35,000 to $39,999",
    "B19001e9": "Households, $40,000 to $44,999",
    "B19001e10": "Households, $45,000 to $49,999",
    "B19001e11": "Households, $50,000 to $59,999",
    "B19001e12": "Households, $60,000 to $74,999",
    "B19001e13": "Households, $75,000 to $99,999",
    "B19001e14": "Households, $100,000 to $124,999",
    "B19001e15": "Households, $125,000 to $149,999",
    "B19001e16": "Households, $150,000 to $199,999",
    "B19001e17": "Households, $200,000 or more",
    "B19013e1": "Median household income (dollars)",
    "B19025e1": "Aggregate household income (dollars)",


    "B": "Mean household income (dollars)",
    "B19051e2": "Households with earnings",
    "B": "Households with earnings, mean earnings (dollars)",
    "B": "Households with social security",
    "B": "Households with social security, mean social security income (dollars)",
    "B": "Households with retirement income",
    "B": "Households with retirement income, mean retirement income (dollars)",
    "B": "Households with supplemental security income",
    "B": "Households with supplemental security income, mean supplemental security income (dollars)",
    "B": "Households with food stamp/SNAP benefits in the past 12 months",
    "B": "Families",
    "B": "Families, less than $10,000",
    "B": "Families, $10,000 to $14,999",
    "B": "Families, $15,000 to $24,999",
    "B": "Families, $25,000 to $34,999",
    "B": "Families, $35,000 to $49,999",
    "B": "Families, $50,000 to $74,999",
    "B": "Families, $75,000 to $99,9999",
    "B": "Families, $100,000 to $149,999",
    "B": "Families, $150,000 to $199,999",
    "B": "Families, $200,000 or more",
    "B": "Median family income (dollars)",
    "B": "Mean family income (dollars)",
    "B": "Per capita income (dollars)",
    "B": "Nonfamily households",
    "B": "Median nonfamily income (dollars)",
    "B": "Mean nonfamily income (dollars)",
    "B": "Median earnings for workers (dollars)",
    "B": "Median earnings for male full-time, year-round workers (dollars)",
    "B": "Median earnings for female full-time, year-round workers (dollars)"
    }

# E08: Earnings in the past 12 months for households (Universe: Households)
e08_EarningsHouseholds = {
    "B19051e1": "Total households",
    "B19051e2": "Househols with earnings",
    "B19051e3": "Households without earnings",
    "B19052e2": "Households with wage or salary income",
    "B19053e2": "Households with self-employment income",
    "B19054e2": "Households with interest, dividents, or net rental income",
    "B19055e2": "Households with social security income",
    "B19056e2": "Households with supplemental security income",
    "B19057e2": "Households with public assistance income",
    "B19059e2": "Households with retirement income",
    "B19060e2": "Households with other types of income",
    "B22010e2": "Households received food stamps/SNAP income"
    }

# E09: Earnings and Income in Dollars (Universe: Aggregate earnings in households in inflation-adjusted dollars)
e09_EarningsIncomeDollars = {
    "B19061e1": "Aggregate earnings in households",
    "B19062e1": "Aggregate wage or salary income in households",
    "B19063e1": "Aggregate self-employment income in households",
    "B19064e1": "Aggregate interest, dividents, or net rental income in households",
    "B19065e1": "Aggregate social security income in households",
    "B19066e1": "Aggregate supplemental security income in households",
    "B19067e1": "Aggregate public assistance income in households",
    "B19069e1": "Aggregate retirement income in households",
    "B19069e1": "Aggregate other types of income in household",
    "B19113e1": "Median family income",
    "B19202e1": "Median nonfamily household income",
    "B19214e1": "Aggregate nonfamily household income",
    "B19301e1": "Per capita income (total population)",
    "B19301Ae1": "Per capita income, White alone",
    "B19301Be1": "Per capita income, Black or African American alone",
    "B19301Ce1": "Per capita income, American Indian and Alaska Native alone",
    "B19301De1": "Per capita income, Asian alone",
    "B19301Ee1": "Per capita income, Native Hawaiian and Other Pacific Islander alone",
    "B19301Fe1": "Per capita income, some other race alone",
    "B19301Ge1": "Per capita income, two or more races",
    "B19301He1": "Per capita income, White alone, not Hispanic or Latino",
    "B19301Ie1": "Per capita income, Hispanic or Latino",
    "B19313e1": "Aggregate income (total population)",
    "B20002e1": "Median earnings (total population)",
    "B20002e2": "Median earnings, male population",
    "B20002e3": "Median earnings, female population",
    "B20003e1": "Aggregate earnings (total population)",
    "B20003e2": "Aggregate earnings, male population",
    "B20003e3": "Aggregate earnings, male, worked full-time",
    "B20003e5": "Aggregate earnings, female population",
    "B20003e6": "Aggregate earnings, female, worked full-time"
    }

# E10: Family Income in Dollars (Universe: Families)
e10_FamilyIncome = {
    "B19101e1": "Total families",
    "B19101e2": "Families, less than $10,000",
    "B19101e3": "Families, $10,000 to $14,999",
    "B19101e4": "Families, $15,000 to $19,999",
    "B19101e5": "Families, $20,000 to $24,999",
    "B19101e6": "Families, $25,000 to $29,999",
    "B19101e7": "Families, $30,000 to $34,999",
    "B19101e8": "Families, $35,000 to $39,999",
    "B19101e9": "Families, $40,000 to $44,999",
    "B19101e10": "Families, $45,000 to $49,999",
    "B19101e11": "Families, $50,000 to $59,999",
    "B19101e12": "Families, $60,000 to $74,999",
    "B19101e13": "Families, $75,000 to $99,999",
    "B19101e14": "Families, $100,000 to $124,999",
    "B19101e15": "Families, $125,000 to $149,999",
    "B19101e16": "Families, $150,000 to $199,999",
    "B19101e17": "Families, $200,000 or more"
    }

# E11: Health Insurance Coverage (Universe: Civilian non-institutionalized population, families, total population)
e11_HealthInsurance = {
    "B27010e1": "Civilian non-institutionalized population",
    "B27010e2": "Under 19 years",
    "B27010e3": "Under 19 years, with one type of health insurance coverage",
    "B27010e10": "Under 19 years, with two or more types of health insurance coverage",
    "B27010e17": "Under 19 years, without health insurance coverage",
    "B27010e18": "19 to 34 years",
    "B27010e19": "19 to 34 years, with one type of health insurance coverage",
    "B27010e26": "19 to 34 years, with two or more types of health insurance coverage",
    "B27010e33": "19 to 34 years, without health insurance coverage",
    "B27010e34": "35 to 64 years",
    "B27010e35": "35 to 64 years, with one type of health insurance coverage",
    "B27010e42": "35 to 64 years, with two or more types of health insurance coverage",
    "B27010e50": "35 to 64 years, without health insurance coverage",
    "B27010e51": "65 years and over",
    "B27010e52": "65 years and over, with one type of health insurance coverage",
    "B27010e58": "65 years and over, with two or more types of health insurance coverage",
    "B27010e66": "65 years and over, without health insurance coverage"
    }


# E12: Ratio of income to poverty level (Universe: total population for whom poverty level is determined)
e12_RatioIncomePoverty = {
    "C17002e1": "Total population (for whom poverty status id determined)",
    "C17002e2": "Under 0.50",
    "C17002e3": "0.50 to 0.99",
    "C17002e4": "1.00 to 1.24",
    "C17002e5": "1.25 to 1.49",
    "C17002e6": "1.50 to 1.84",
    "C17002e7": "1.84 to 1.99",
    "C17002e8": "2.00 and over"
    }


# E13: Poverty in Population in the past 12 months (Universe: Total population for whom poverty level is determined)
e13_BelowPovertyPopulation = {
    "B17021e1": "Total population (for whom poverty status is determined)",
    "B17021e2": "Population below poverty level",
    "B17021e3": "Population in family households below poverty level",
    "B17021e4": "Population in married couple family households below poverty level",
    "B17021e8": "Population in male householder, no wife present households below poverty level",
    "B17021e11": "Population in female householder, no husband present households below poverty level",
    "B17021e14": "Population in nonfamily households below poverty level"
    }

# E14: Poverty in Households in the past 12 months (Universe: Total households)
e14_BelowPovertyHouseholds = {
    "B17017e1": "Total households",
    "B17017e2": "All households below poverty level",
    "B17017e3": "Family households below poverty level",
    "B17017e4": "Married couple family households below poverty level",
    "B17017e10": "Male householder, no wife present households below poverty level",
    "B17017e15": "Female householder, no husband present households below poverty level",
    "B17017e20": "Nonfamily households below poverty level",
    "B17017e21": "Nonfamily households, male householder below poverty level",
    "B17017e26": "Nonfamily households, female householder below poverty level"
    }


# E15: Percentage of families and people whose income in the past 12 months is below the poverty level (Universe: families, population)
e15_BelowPovertyFamilies = {
    "B17010e1": "All families",
    "B17010e2": "All families below poverty level",
    "B17010e3": "Married couple families below poverty level",
    "B17010e4": "Married couple families with related children under 18 years below poverty level",
    "B17010e10": "Male householder, no wife present families below poverty level",
    "B17010e11": "Male householder, no wife present families with related children under 18 years below poverty level",
    "B17010e16": "Female householder, no husband present families below poverty level",
    "B17010e17": "Female householder, no husband present families with related children under 18 years below poverty level"
    }


# E16: Poverty and income deficit (dollars) in the past 12 months for families (Universe: Families with income below poverty level in the past 12 months)
e16_BelowPovertyIncomeDeficit = {
    "B17011e1": "Families below poverty: aggregate income deficit (past 12 months)",
    "B17011e2": "Married couple families below poverty: aggregate income deficit",
    "B17011e4": "Male householder, no wife present below poverty: aggregrate income deficit",
    "B17011e5": "Female householder, no husband present below poverty: aggregate income deficit"
    }





# H. HOUSING CHARACTERISTICS

# H01: Housing Occupancy (Universe: Total housing units)
h01_HousingOccupancy = {
    "B25002e1": "Total housing units",
    "B25002e2": "Occupied housing units",
    "B25002e3": "Vacant housing units",
    "B": "Homeowner vacancy rate",
    "B": "Rental vacancy rage"
    }


# H02: Units in Structure (Universe: Total housing units)
h02_UnitsInStructure = {
    "B25024e1": "Total housing units",
    "B25024e2": "1-unit, detatched",
    "B25024e3": "1-unit, attached",
    "B25024e4": "2-units",
    "B25024e5": "3 or 4 units",
    "B25024e6": "5 to 9 units",
    "B25024e7": "10 to 19 units",
    "B25024e8": "20 to 49 units",
    "B25024e9": "50 or more units",
    "B25024e10": "Mobile home",
    "B25024e11": "Boat, RV, van, etc"
    }

# H03: Population in occupied housing units by tenure by units in structure (Universe: total population in occupied housing units)
h03_PopulationByHousingOccupancy = {
    "B25033e1": "Total population in occupied housing units",
    "B25033e2": "Population in owner-occupied housing units",
    "B25033e3": "Population in owner-occupied 1 detached or attached housing units",
    "B25033e4": "Population in owner-occupied 2 to 4 housing units",
    "B25033e5": "Population in owner-occupied 5 or more housing units",
    "B25033e6": "Population in owner-occupied mobile home",
    "B25033e7": "Population in owner-occupied boat, RV, van, etc",
    "B25033e8": "Population in renter-occupied housing units",
    "B25033e9": "Population in renter-occupied 1 detached or attached housing units",
    "B25033e10": "Population in renter-occupied 2 to 4 housing units",
    "B25033e11": "Population in renter-occupied 5 or more housing units",
    "B25033e12": "Population in renter-occupied mobile home",
    "B25033e13": "Population in renter-occupied boat, RV, van, etc"
    }

# H04: Year Structure Built (Universe: Total housing units)
h04_YearStructureBuilt = {
    "B25034e1": "Total housing units",
    "B25034e2": "Built 2014 or later",
    "B25034e3": "Built 2010 to 2013",
    "B25034e4": "Built 2000 to 2009",
    "B25034e5": "Built 1990 to 1999",
    "B25034e6": "Built 1980 to 1989",
    "B25034e7": "Built 1970 to 1979",
    "B25034e8": "Built 1960 to 1969",
    "B25034e9": "Built 1950 to 1959",
    "B25034e10": "Built 1940 to 1949",
    "B25034e11": "Built 1939 or earlier",
    "B25035e1": "Median year structure built",
    "B25037e1": "Median year structure built, occupied housing units",
    "B25037e2": "Median year structure built, owner-occupied housing units",
    "B25037e3": "Median year structure built, renter-occupied housing units"
    }

# H05: Rooms (Universe: Total housing units)
h05_Rooms = {
    "B25017e1": "Total housing units",
    "B25017e2": "1 room",
    "B25017e3": "2 rooms",
    "B25017e4": "3 rooms",
    "B25017e5": "4 rooms",
    "B25017e6": "5 rooms",
    "B25017e7": "6 rooms",
    "B25017e8": "7 rooms",
    "B25017e9": "8 rooms",
    "B25017e10": "9 rooms or more",
    "B25018e1": "Median number of rooms",
    "B25019e1": "Aggregate number of rooms",
    "B25021e1": "Median number of rooms in occupied housing units",
    "B25021e2": "Median number of rooms in owner-occupied housing units",
    "B25021e3": "Median number of rooms in renter-occupied housing units",
    "B25022e1": "Aggregate number of rooms in occupied housing units",
    "B25022e2": "Aggregate number of rooms in owner-occupied housing units",
    "B25022e3": "Aggregate number of rooms in renter-occupied housing units",
    }


# H06: Bedrooms (Universe: Total housing units)
h06_Bedrooms = {
    "B25041e1": "Total housing units",
    "B25041e2": "No bedroom",
    "B25041e3": "1 bedroom",
    "B25041e4": "2 bedrooms",
    "B25041e5": "3 bedrooms",
    "B25041e6": "4 bedrooms",
    "B25041e7": "5 or more bedrooms",
    "B25042e": "Owner-occupied housing units",
    "B25042e3": "Owner-occupied, no bedroom",
    "B25042e4": "Onwer-occupied, 1 bedroom",
    "B25042e5": "Owner-occupied, 2 bedrooms",
    "B25042e6": "Owner-occupied, 3 bedrooms",
    "B25042e7": "Owner-occupied, 4 bedrooms",
    "B25042e8": "Owner-occupied, 5 or more bedrooms",
    "B25042e9": "Renter-occupied housing units",
    "B25042e10": "Renter-occupied, no bedroom",
    "B25042e11": "Onwer-occupied, 1 bedroom",
    "B25042e12": "Renter-occupied, 2 bedrooms",
    "B25042e13": "Renter-occupied, 3 bedrooms",
    "B25042e14": "Renter-occupied, 4 bedrooms",
    "B25042e15": "Renter-occupied, 5 or more bedrooms"
    }


# H07: Housing tenure by race of householder (Universe: Occupied housing units)
h07_HousingTenureRaceAge = {
    "B25003e1": "Occupied houging units",
    "B25003e2": "Owner-occupied",
    "B25003e3": "Renter-occuped",
    "B25003Ae1": "Occupied housing units with a householder who is White alone",
    "B25003Ae2": "Owner-occupied housing units with a householder who is White alone",
    "B25003Ae3": "Renter-occupied housing units with a householder who is White alone",
    "B25003Be1": "Occupied housing units with a householder who is Black or African American alone",
    "B25003Be2": "Owner-occupied housing units with a householder who is Black or African American alone",
    "B25003Be3": "Renter-occupied housing units with a householder who is Black or African American alone",
    "B25003Ce1": "Occupied housing units with a householder who is American Indian and Alaska Native alone",
    "B25003Ce2": "Owner-occupied housing units with a householder who is American Indian and Alaska Native alone",
    "B25003Ce3": "Renter-occupied housing units with a householder who is American Indian and Alaska Native alone",
    "B25003De1": "Occupied housing units with a householder who is Asian alone",
    "B25003De2": "Owner-occupied housing units with a householder who is Asian alone",
    "B25003De3": "Renter-occupied housing units with a householder who is Asian alone",
    "B25003Ee1": "Occupied housing units with a householder who is Native Hawaiian and Other Pacific Islander alone",
    "B25003Ee2": "Owner-occupied housing units with a householder who is Native Hawaiian and Other Pacific Islander alone",
    "B25003Ee3": "Renter-occupied housing units with a householder who is Native Hawaiian and Other Pacific Islander alone",
    "B25003Fe1": "Occupied housing units with a householder who is other race alone",
    "B25003Fe2": "Owner-occupied housing units with a householder who is other race alone",
    "B25003Fe3": "Renter-occupied housing units with a householder who is other race alone",
    "B25003Ge1": "Occupied housing units with a householder who is two or more races",
    "B25003Ge2": "Owner-occupied housing units with a householder who is two or more races",
    "B25003Ge3": "Renter-occupied housing units with a householder who is two or more races",
    "B25003He1": "Occupied housing units with a householder who is White alone, not Hispanic or Latino",
    "B25003He2": "Owner-occupied housing units with a householder who is White alone, not Hispanic or Latino",
    "B25003He3": "Renter-occupied housing units with a householder who is White alone, not Hispanic or Latino",
    "B25003Ie1": "Occupied housing units with a householder who is Hispanic or Latino",
    "B25003Ie2": "Owner-occupied housing units with a householder who is Hispanic or Latino",
    "B25003Ie3": "Renter-occupied housing units with a householder who is Hispanic or Latino",
    "B25007e3": "Owner-occupied, householder 15 to 24 years",
    "B25007e4": "Owner-occupied, householder 25 to 34 years",
    "B25007e5": "Owner-occupied, householder 35 to 44 years",
    "B25007e6": "Owner-occupied, householder 45 to 54 years",
    "B25007e7": "Owner-occupied, householder 55 to 59 years",
    "B25007e8": "Owner-occupied, householder 60 to 64 years",
    "B25007e9": "Owner-occupied, householder 65 to 74 years",
    "B25007e10": "Owner-occupied, householder 75 to 84 years",
    "B25007e11": "Owner-occupied, householder 85 years and over",
    "B25007e13": "Renter-occupied, householder 15 to 24 years",
    "B25007e14": "Renter-occupied, householder 25 to 34 years",
    "B25007e15": "Renter-occupied, householder 35 to 44 years",
    "B25007e16": "Renter-occupied, householder 45 to 54 years",
    "B25007e17": "Renter-occupied, householder 55 to 59 years",
    "B25007e18": "Renter-occupied, householder 60 to 64 years",
    "B25007e19": "Renter-occupied, householder 65 to 74 years",
    "B25007e20": "Renter-occupied, householder 75 to 84 years",
    "B25007e21": "Renter-occupied, householder 85 years and over",
    "B25010e1": "Average household size of occupied housing units",
    "B25010e2": "Average household size of owner-occupied housing units",
    "B25010e3": "Average household size of renter-occupied houding units"
    }

# H08: Total population in occupied housing units by tenure (Universe: total population in occupied housing units)
h08_PopulationTenure = {
    "B25008e1": "Total population in occupied housing units",
    "B25008e2": "Population in owner-occupied housing units",
    "B25008e3": "Population in renter-occupied housing units"
    }

# H09: Vacancy Status (Universe: vacand housing units)
h09_VacancyStatus = {
    "B25004e1": "Total vacant housing units",
    "B25004e2": "For rent",
    "B25004e3": "Rented, not occupied",
    "B25004e4": "For sale only",
    "B25004e5": "Sold, not occupied",
    "B25004e6": "For seasonal, recreational, or occassional use",
    "B25004e7": "For migrant workers",
    "B25004e8": "Other vacant units"
    }


# H10: Occupied housing units by race of householder (Universe: occupied housing units)
h10_HouseholderRace = {
    "B25006e1": "Occupied housing units",
    "B25006e2": "Units with White alone householder",
    "B25006e3": "Units with Black or Afican American alone householder",
    "B25006e4": "Units with American Indian and Alaska Native alone householder",
    "B25006e5": "Units with Asian alone householder",
    "B25006e6": "Units with Native Hawaiian and Other Pacific Islander alone householder",
    "B25006e7": "Units with some other race alone householder",
    "B25006e8": "Units with two or more races householder"
    }


# H11: Year Householder Moved into Unit (Universe: Occupied housing units)
h11_YearMovedIntoUnit = {
    "B25038e1": "Occupied housing units",
    "B25038e2": "Owner-occupied housing units",
    "B25038e3": "Owner-occupied, moved in 2015 or later",
    "B25038e4": "Owner-occupied, moved in 2010 to 2014",
    "B25038e5": "Owner-occupied, moved in 2000 to 2009",
    "B25038e6": "Owner-occupied, moved in 1990 to 1999",
    "B25038e7": "Owner-occupied, moved in 1980 to 1989",
    "B25038e8": "Owner-occupied, moved in 1979 or earlier",
    "B25038e9": "Renter-occupied housing units",
    "B25038e10": "Renter-occupied, moved in 2015 or later",
    "B25038e11": "Renter-occupied, moved in 2010 to 2014",
    "B25038e12": "Renter-occupied, moved in 2000 to 2009",
    "B25038e13": "Renter-occupied, moved in 1990 to 1999",
    "B25038e14": "Renter-occupied, moved in 1980 to 1989",
    "B25038e15": "Renter-occupied, moved in 1979 or earlier",
    "B25039e1": "Median year householder moved into occupied housing unit",
    "B25039e2": "Median year householder moved into owner-occupied unit",
    "B25039e3": "Median year householder moved into renter-occupied unit"
    }


# H12: Vehicles Available (Universe: Occupied housing units)
h12_VehiclesAvailable = {
    "B25044e1": "Occupied housing units",
    "B25044e2": "Owner-occupied housing units",
    "B25044e3": "Owner-occupied, no vehicles available",
    "B25044e4": "Owner-occupied, 1 vehicle available",
    "B25044e5": "Owner-occupied, 2 vehicles available",
    "B25044e6": "Owner-occupied, 3 vehicles available",
    "B25044e7": "Owner-occupied, 4 vehicles available",
    "B25044e8": "Owner-occupied, 5 or more vehicles available",
    "B25044e9": "Renter-occupied housing units",
    "B25044e10": "Renter-occupied, no vehicles available",
    "B25044e11": "Renter-occupied, 1 vehicle available",
    "B25044e12": "Renter-occupied, 2 vehicles available",
    "B25044e13": "Renter-occupied, 3 vehicles available",
    "B25044e14": "Renter-occupied, 4 vehicles available",
    "B25044e15": "Renter-occupied, 5 or more vehicles available",
    "B25046e1": "Aggregate number of vehicles available in occupied housing units",
    "B25046e2": "Aggregate number of vehicles available in owner-occupied housing units",
    "B25046e3": "Aggregate number of vehicles available in renter-occupied housing units"
    }


# H13: House Heating Fuel (Universe: Occupied housing units)
h13_HouseHeatingFuel = {
    "B25040e1": "Occupied housing units",
    "B25040e2": "Utility gas",
    "B25040e3": "Bottled, tank, or LP gas",
    "B25040e4": "Electricity",
    "B25040e5": "Fuel oil, kerosene, etc",
    "B25040e6": "Coal or coke",
    "B25040e7": "Wood",
    "B25040e8": "Solar energy",
    "B25040e9": "Other fuel",
    "B25040e10": "No fuel used"
    }


# H14: Selected Characteristics (Universe: Occupied housing units)
h14_SelectedCharacteristics = {
    "B25016e1": "Occupied housing units",
    "B25016e2": "Onwer-occupied housing units",
    "B25016e11": "Renter-occupied housing units",
    "B25016e7": "Onwer-occupied, lacking complete plumbing facilities",
    "B25016e16": "Renter-occupied, lacking complete plumbing facilities",
    "B25043e7": "Owner-occupied, no telephone service available",
    "B25043e16": "Renter-occupied, no telephone service available",
    "B25053e4": "Owner-occupied, lacking complete kitchen facilities",
    "B25053e7": "Renter-occupied, lacking complete kitchen facilities"
    }


# H15: Occupants Per Room (Universe: Occupied housing units)
h15_OccupantsPerRoom = {
    "B25014e1": "Occupied housing units",
    "B25014e2": "Owner-occupied housing units",
    "B25014e3": "Owner-occupied housing units, 0.5 or less occupants per room",
    "B25014e4": "Owner-occupied housing units, 0.51 to 1.00 occupants per room",
    "B25014e5": "Owner-occupied housing units, 1.01 to 1.50 occupants per room",
    "B25014e6": "Owner-occupied housing units, 1.51 to 2.00 occupants per room",
    "B25014e7": "Owner-occupied housing units, 2.01 or more occupants per room",
    "B25014e8": "Renter-occupied housing units",
    "B25014e9": "Renter-occupied housing units, 0.5 or less occupants per room",
    "B25014e10": "Renter-occupied housing units, 0.51 to 1.00 occupants per room",
    "B25014e11": "Renter-occupied housing units, 1.01 to 1.50 occupants per room",
    "B25014e12": "Renter-occupied housing units, 1.51 to 2.00 occupants per room",
    "B25014e13": "Renter-occupied housing units, 2.01 or more occupants per room"
    }


# H16: Housing Value (Universe: Owner-occupied units)
h16_HousingValue = {
    "B25075e1": "Owner-occupied units",
    "B25075e2": "Less than $10,000",
    "B25075e3": "$10,000 to $14,999",
    "B25075e4": "$15,000 to $19,999",
    "B25075e5": "$20,000 to $24,999",
    "B25075e6": "$25,000 to $29,999",
    "B25075e7": "$30,000 to $34,999",
    "B25075e8": "$35,000 to $39,999",
    "B25075e9": "$40,000 to $49,999",
    "B25075e10": "$50,000 to $59,999",
    "B25075e11": "$60,000 to $69,999",
    "B25075e12": "$70,000 to $79,999",
    "B25075e13": "$80,000 to $89,999",
    "B25075e14": "$90,000 to $99,999",
    "B25075e15": "$100,000 to $124,999",
    "B25075e16": "$125,000 to $149,999",
    "B25075e17": "$150,000 to $174,999",
    "B25075e18": "$175,000 to $199,999",
    "B25075e19": "$200,000 to $249,999",
    "B25075e20": "$250,000 to $299,999",
    "B25075e21": "$300,000 to $399,999",
    "B25075e22": "$400,000 to $499,999",
    "B25075e23": "$500,000 to $749,999",
    "B25075e24": "$750,000 to $999,999",
    "B25075e25": "$1,000,000 to $1,499,999",
    "B25075e26": "$1,500,000 to $1,999,999",
    "B25075e27": "$2,000,000 or more",
    "B25076e1": "Lower value quartile (dollars)",
    "B25077e1": "Median value (dollars)",
    "B25078e1": "Upper value quartile (dollars)",
    "B25079e1": "Aggregate value (dollars)",
    "B25083e1": "Median value (dollars) for mobile homes"
    }


# H17: Price asked for vacant for-sale only and sold, not occupied housing units (Universe: vacant for sale only and sold, not occupied housing units)
h17_HousingPriceAsked = {
    "B25085e1": "Total vacant for-sale only and sold, not occupied housing units",
    "B25085e2": "Less than $10,000",
    "B25085e3": "$10,000 to $14,999",
    "B25085e4": "$15,000 to $19,999",
    "B25085e5": "$20,000 to $24,999",
    "B25085e6": "$25,000 to $29,999",
    "B25085e7": "$30,000 to $34,999",
    "B25085e8": "$35,000 to $39,999",
    "B25085e9": "$40,000 to $49,999",
    "B25085e10": "$50,000 to $59,999",
    "B25085e11": "$60,000 to $69,999",
    "B25085e12": "$70,000 to $79,999",
    "B25085e13": "$80,000 to $89,999",
    "B25085e14": "$90,000 to $99,999",
    "B25085e15": "$100,000 to $124,999",
    "B25085e16": "$125,000 to $149,999",
    "B25085e17": "$150,000 to $174,999",
    "B25085e18": "$175,000 to $199,999",
    "B25085e19": "$200,000 to $249,999",
    "B25085e20": "$250,000 to $299,999",
    "B25085e21": "$300,000 to $399,999",
    "B25085e22": "$400,000 to $499,999",
    "B25085e23": "$500,000 to $749,999",
    "B25085e24": "$750,000 to $999,999",
    "B25085e25": "$1,000,000 to $1,499,999",
    "B25085e26": "$1,500,000 to $1,999,999",
    "B25085e27": "$2,000,000 or more",
    "B25086e1": "Aggregate price asked (dollars)"
    }

# H18: Mortgage Status (Universe: Owner-occupied units)
h18_MortgageStatus = {
    "B25081e1": "Owner-occupied units",
    "B25081e2": "Housing units with a mortgage",
    "B25081e7": "Housing units with a mortgage only",
    "B25081e4": "Housing units with a mortgage and a second mortgage",
    "B25081e5": "Housing units with a mortgage and a home equity loan",
    "B25081e6": "Housing units with a mortgage and both a second mortgage and a home equity loan",
    "B25081e8": "Housing units without a mortgage",
    "B25082e1": "Aggregate value (dollars) of owner-occupied units",
    "B25082e2": "Aggregate value (dollars) of housing units with a mortgage",
    "B25082e3": "Aggregate value (dollars) of housing units without a mortgage"
    }


# H19: Selected Monthly Owner Costs (SMOC) (Universe: owner-occupied housing units with or without a mortgage)
h19_SMOC = {
    "B25087e1": "Total owner-occupied housing units",
    "B25087e2": "Housing units with a mortgage",
    "B25087e3": "With mortgage, less than $200",
    "B25087e4": "With mortgage, $200 to $299",
    "B25087e5": "With mortgage, $300 to $399",
    "B25087e6": "With mortgage, $400 to $499",
    "B25087e7": "With mortgage, $500 to $599",
    "B25087e8": "With mortgage, $600 to $699",
    "B25087e9": "With mortgage, $700 to $799",
    "B25087e10": "With mortgage, $800 to $899",
    "B25087e11": "With mortgage, $900 to $999",
    "B25087e12": "With mortgage, $1,000 to $1,249",
    "B25087e13": "With mortgage, $1,250 to $1,499",
    "B25087e14": "With mortgage, $1,500 to $1,999",
    "B25087e15": "With mortgage, $2,000 to $2,499",
    "B25087e16": "With mortgage, $2,500 to $2,999",
    "B25087e17": "With mortgage, $3,000 to $3,499",
    "B25087e18": "With mortgage, $3,500 to $3,999",
    "B25087e19": "With mortgage, $4,000 or more",
    "B25087e20": "Housing units without a mortgage",
    "B25087e21": "Without mortgage, less than $100",
    "B25087e22": "Without mortgage, $100 to $149",
    "B25087e23": "Without mortgage, $150 to $199",
    "B25087e24": "Without mortgage, $200 to $249",
    "B25087e25": "Without mortgage, $250 to $299",
    "B25087e26": "Without mortgage, $300 to $349",
    "B25087e27": "Without mortgage, $350 to $399",
    "B25087e28": "Without mortgage, $400 to $499",
    "B25087e29": "Without mortgage, $500 to $599",
    "B25087e30": "Without mortgage, $600 to $699",
    "B25087e31": "Without mortgage, $700 to $799",
    "B25087e32": "Without mortgage, $800 to $899",
    "B25087e33": "Without mortgage, $900 to $999",
    "B25087e34": "Without mortgage, $1,000 to $1,099",
    "B25087e35": "Without mortgage, $1,100 to $1,199",
    "B25087e36": "Without mortgage, $1,200 to $1,299",
    "B25087e37": "Without mortgage, $1,300 to $1,399",
    "B25087e38": "Without mortgage, $1,400 to $1,499",
    "B25087e39": "Without morrgage, $1,500 or more",
    "B25088e1": "Median selected monthly owner costs (dollars) for all owner-occupied housing units",
    "B25088e2": "Median selected monthly owner costs (dollars) for units with a mortgage",
    "B25088e3": "Median selected monthly owner costs (dollars) for units without a mortgage",
    "B25089e1": "Aggregate selected monthly owner costs (dollars) for all owner-occupied housing units",
    "B25089e2": "Aggregate selected monthly owner costs (dollars) for units with a mortgage",
    "B25089e3": "Aggregate selected monthly owner costs (dollars) for units without a mortgage"
    }


# H20: Selected Monthly Owner Costs as a Percentage of Household Income (SMOCAPI) (Universe: Housing units with or without a mortgage)
h20_SMOCAPI = {
    "B25091e1": "Owner-occupied housing units",
    "B25091e2": "Housing units with a mortgage",
    "B25091e3": "With mortgage, less than 10.0 percent",
    "B25091e4": "With mortgage, 10.0 to 14.9 percent",
    "B25091e5": "With mortgage, 15.0 to 19.9 percent",
    "B25091e6": "With mortgage, 20.0 to 24.9 percent",
    "B25091e7": "With mortgage, 25.0 to 29.9 percent",
    "B25091e8": "With mortgage, 30.0 to 34.9 percent",
    "B25091e9": "With mortgage, 35.0 to 39.9 percent",
    "B25091e10": "With mortgage, 40.0 to 49.9 percent",
    "B25091e11": "With mortgage, 50.0 percent or more",
    "B25091e12": "With mortgage, not computed",
    "B25091e13": "Housing units without a mortgage",
    "B25091e14": "Without mortgage, less than 10.0 percent",
    "B25091e15": "Without mortgage, 10.0 to 14.9 percent",
    "B25091e16": "Without mortgage, 15.0 to 19.9 percent",
    "B25091e17": "Without mortgage, 20.0 to 24.9 percent",
    "B25091e18": "Without mortgage, 25.0 to 29.9 percent",
    "B25091e19": "Without mortgage, 30.0 to 34.9 percent",
    "B25091e20": "Without mortgage, 35.0 to 39.9 percent",
    "B25091e21": "Without mortgage, 40.0 to 49.9 percent",
    "B25091e22": "Without mortgage, 50.0 percent or more",
    "B25091e23": "Without mortgage, not computed",
    "B25092e1": "Median selected monthly owner costs (dollars) as percentage of household income for all units",
    "B25092e2": "Median selected monthly owner costs (dollars) as percentage of household income for units with a mortgage",
    "B25092e3": "Median selected monthly owner costs (dollars) as percentage of household income for units without a mortgage"
    }


# H21: Contract rent distribution in dollars (Universe: renter-occupied housing units paying cash rent) and 
# Rent asked distribution in dollars (Universe: vacant and for-rent and rented, not occupied housing units)
h21_RentContractAsked = {
    "B25056e2": "renter-occupied housing units paying cash rent",
    "B25057e1": "Lower contract rent quartile",
    "B25058e1": "Median contract rent",
    "B25059e1": "Upper contract rent quartile",
    "B25060e1": "Aggregate contract rent",
    "B25061e1": "Vacant for rent and rented, not occupied housing units",
    "B25062e1": "Aggregate rent asked"
    }

# H22: Gross Rent (Universe: Occupied units paying rent)
h22_GrossRent = {
    "B25063e2": "Occupied units paying rent",
    "B25063e3": "Less than $500",
    "B25063e4": "$100 to $149",
    "B25063e5": "$150 to $199",
    "B25063e6": "$200 to $249",
    "B25063e7": "$250 to $299",
    "B25063e8": "$300 to $349",
    "B25063e9": "$350 to $399",
    "B25063e10": "$400 to $449",
    "B25063e11": "$450 to $499",
    "B25063e12": "$500 to $549",
    "B25063e13": "$550 to $599",
    "B25063e14": "$600 to #649",
    "B25063e15": "$650 to $699",
    "B25063e16": "$700 to $749",
    "B25063e17": "$750 to $799",
    "B25063e18": "$800 to $899",
    "B25063e19": "$900 to $999",
    "B25063e20": "$1,000 to $1,249",
    "B25063e21": "$1,250 to $1,499",
    "B25063e22": "$1,500 to $1,999",
    "B25063e23": "$2,000 to $2,499",
    "B25063e24": "$2,500 to $2,999",
    "B25063e25": "$3,000 to $3,499",
    "B25063e26": "$3,500 or more",
    "B25063e27": "No cash rent",
    "B25064e1": "Median gross rent (dollars)",
    "B25065e1": "Aggregate gross rent (dollars)"
    }


# H23: Gross Rent as Percentage of Household Income (Universe: Occupied units paying rent)
h23_GrossRentPercentageIncome = {
    "B25070e1": "Occupied units paying rent",
    "B25070e2": "Less than 10.0 percent",
    "B25070e3": "10.0 to 14.9 percent",
    "B25070e4": "15.0 to 19.9 percent",
    "B25070e5": "20.0 to 24.9 percent",
    "B25070e6": "25.0 to 29.9 percent",
    "B25070e7": "30.0 to 34.9 percent",
    "B25070e8": "35.0 to 39.9 percent",
    "B25070e9": "40.0 to 49.9 percent",
    "B25070e10": "50.0 percent or more",
    "B25070e11": "Not computed"
    }




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

tableLevels = {
    "D01": "SexAge",
    "D02": "Race",
    "D03": "RaceCombinations",
    "D04": "HispanicLatinoRace",
    "D05": "CitizenVoting",
    "S01": "HouseholdsByType",
    "S02": "Relationship",
    "S03": "MaritalStatus",
    "S04": "Fertility",
    "S05": "Grandparents",
    "S06": "SchoolEnrollment",
    "S07": "EducationalAttainment",
    "S08": "VeteranStatus",
    "S09": "DisabilityStatus",
    "S10": "Residence",
    "S11": "PlaceOfBirth",
    "S12": "CitizenshipStatus",
    "S13": "YearOfEntry",
    "S14": "WorldRegionBirth",
    "S15": "LanguageSpokenAtHome",
    "S16": "Ancestry",
    "S17": "ComputersInternet",
    "E01": "EmploymentStatus",
    "E02": "Commuting",
    "E03": "Occupation",
    "E04": "Industry",
    "E05": "ClassOrWorker",
    "E06": "IncomeBenefits",
    "E07": "HealthInsurance",
    "E08": "BelowPovertyLevel",
    "H01": "HousingOccupancy",
    "H02": "UnitsInStructure",
    "H03": "YearStructureBuilt",
    "H04": "Rooms",
    "H05": "Bedrooms",
    "H06": "HousingTenure",
    "H07": "YearMovedIntoUnit",
    "H08": "VehiclesAvailable",
    "H09": "HouseHeatingFuel",
    "H10": "SelectedCharacteristics",
    "H11": "OccupantsPerRoom",
    "H12": "HousingValue",
    "H13": "MortgageStatus",
    "H14": "OwnerCostsDollars",
    "H15": "OwnerCostsPercentage",
    "H16": "GrossRentDollars",
    "H17": "GrossRentPerecentage"
    }