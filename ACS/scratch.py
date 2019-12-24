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
d01 = {
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

# D02: Median Age (Universe: Total population)
d02 = {
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
d03 = {
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
d04 = {
    "B02001e1": "Total population",
    "B02008e1": "White",
    "B02009e1": "Black or African American",
    "B02010e1": "American Indian and Alaska Native",
    "B02011e1": "Asian",
    "B02012e1": "Native Hawaiian and Other Pacific Islander",
    "B02013e1": "Some other race"
    }


# D05: Hispanic or Latino and Race (Universe: Total population)
d05 = {
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




# 4.5. Citizen Voting Age Population (Universe: Citizen, 18 and over population)
dhCitizen = {
    "B": "Citizen, 18 and over population",
    "B": "Citizen, Male",
    "B": "Citize, Female"
    }





# S: SOCIAL CHARACTERISTICS
# 1.1. Households by Type (Universe: Total households)

scHouseholds = {
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
    "B": "Nonfamily households, householder living alone, 65 years and over",
    "B11005e2": "Households with one or more people under 18 years",
    "B11007e2": "Households with one or more people 65 years and over",
    "B": "Average household size",
    "B": "Average family size"
    }


# 1.2. Relationship (Universe: Population in households)
scRelationship = {
    "B11002e1": "Population in households",
    "B": "Householder",
    "B": "Spouse",
    "B": "Child",
    "B": "Other relatives",
    "B": "Non-relatives",
    "B": "Non-relatives, unmarried partner"
    }


# 1.3. Marital Status (Universe: Males or Females 15 years and over)
sMaritalStatus = {
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


# 1.4. Fertility (Universe: Number of women 15 to 50 years old who had a birth in the past 12 months)
scFertility = {
    "B": "Number of women 15 to 50 years old who had a birth in the past 12 months",
    "B": "Unmarried (widowed, divorced, and never married)",
    "B": "Unmarried, per 1,000 unmarried women",
    "B": "Per 1,000 women 15 to 50 years old",
    "B": "Per 1,000 women 15 to 19 years old",
    "B": "Per 1,000 women 20 to 34 years old",
    "B": "Per 1,000 women 35 to 50 years old"
    }

# 1.5. Grandparents (Universe: Number of grandparents living or responsible for own grandchildren under 18 years)
scGrandparents = {
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


# 1.6. School Enrollment (Universe: Population 3 years and over enrolled in school)
scSchoolEnrollment = {
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


# 1.7. Educational Attainment (Universe: Population 25 years and over)
scEducationalAttainment = {
    "B": "Population 25 years and over",
    "B": "Less than 9th grade",
    "B": "9th to 12th grade",
    "B": "High school graduate (includes equivalency)",
    "B": "Some college, no degree",
    "B": "Associate's degree",
    "B": "Bachelor's degree",
    "B": "Graduate or professional degree",
    "B": "High school graduate or higher",
    "B": "Bachelor's degree or higher"
    }


# 1.8. Veteran Status (Universe: Civilian population 18 years and over)
scVeteranStatus = {
    "B": "Civilian population 18 years and over",
    "B": "Civilian veterans"
    }


# 1.9. Disability Status (Universe: Total civilian non-institutionalized population)
scDisabilityStatus = {
    "B": "Total civilian non-institutionalized population",
    "B": "Total civilian non-institutionalized population, with a disability",
    "B": "Under 18 years",
    "B": "Under 18 years, with a disability",
    "B": "18 to 64 years",
    "B": "18 to 64 years, with a disability",
    "B": "65 years and over",
    "B": "65 years and over, with a disability"
    }


# 1.10. Residence 1 Year Ago (Universe: Population 1 year and over)
scResidence = {
    "B": "Population 1 year and over",
    "B": "Same house",
    "B": "Different house in the US",
    "B": "Different house in the US, same county",
    "B": "Different house in the US, different county",
    "B": "Different house in the US, different county, same state",
    "B": "Different house in the US, different county, different state",
    "B": "Abroad"
    }


# 1.11. Place of Birth (Universe: Total population)
scPlaceOfBirth = {
    "B00001e1": "Total population",
    "B": "Native population",
    "B": "Native population, born in US",
    "B": "Native population, born in US, state of residence",
    "B": "Native population, born in US, different state",
    "B": "Native population, born in PR, USVI, or born abroad to American parent(s)",
    "B": "Foreign born"
    }


# 1.12. US Citizenship Status (Universe: Foreign-born population)
scCitizenshipStatus = {
    "B": "Foreign born population",
    "B": "Naturalized US citizen",
    "B": "Not a US citizen"
    }


# 1.13. Year of Entry (Universe: Population born outside the United States)
scYearOfEntry = {
    "B": "Population born outside the US",
    "B": "Native",
    "B": "Native, entered 2010 or later",
    "B": "Native, entered before 2010",
    "B": "Foreign born",
    "B": "Foreign born, entered 2010 or later",
    "B": "Foreign born, entered before 2010"
    }


# 1.14. World Region of Birth of Foreign Born Population (Universe: Foreign-born population, escluding population born at sea)
scBirthRegion = {
    "B": "Foreign born population, excluding population born at sea",
    "B": "Europe",
    "B": "Asia",
    "B": "Africa",
    "B": "Oceania",
    "B": "Latin America",
    "B": "Northern America"
    }


# 1.15. Language Spoken at Home (Universe: Population 5 years and over)
scLanguageSpoken = {
    "B": "Population 5 years and over",
    "B": "English only",
    "B": "language other than English",
    "B": "Language other than English, speak English less than 'very well'",
    "B": "Spanish",
    "B": "Spanish, speak English less than 'very well'",
    "B": "Other Indo-European languages",
    "B": "Other Indo-European languages, speak English less than 'very well'",
    "B": "Asian and Pacific Islander languages",
    "B": "Asian and Pacific Islander languages, speak English less than 'very well'",
    "B": "Other languages",
    "B": "Other languages, speak English less than 'very well'"
    }


# 1.16. Ancestry (Universe: Total population)
scAncestry = {
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


# 1.17. Computers and Internet Use (Universe: Total households)
scComputersInternet = {
    "B": "Total households",
    "B": "Households with a computer",
    "B": "Households with a broadband internet connection"
    }


# 2. ECONOMIC CHARACTERISTICS

# 2.1. Employment Status (Universe: Population 16 years and over)
ecEmploymentStatus = {
    "B": "Population 16 years and over",
    "B": "Population 16 years and over in labor force",
    "B": "Population 16 years and over in labor force, civilian labor force",
    "B": "Population 16 years and over in labor force, civilian labor force, employed",
    "B": "Population 16 years and over in labor force, civilian labor force, unemployed",
    "B": "Population 16 years and over in labor force, armed forces",
    "B": "Population 16 years and over not in labor force",
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


# 2.2. Commuting to Work (Universe: Workers 16 years and over)
ecCommuting = {
    "B08301e1": "Workers 16 years and over",
    "B08301e3": "Car, truck, or van - drove alone",
    "B08301e4": "Car, truck, or van - carpooled",
    "B08301e10": "Public transportation (excluding taxicab)",
    "B08301e19": "Walked",
    "B08301e20": "Other means",
    "B08301e21": "Worked at home",
    "B08135e1": "Aggregate travel time to work (minutes)"
    }


# 2.3. Occupation (Universe: Civilian employed population 16 years and over)
ecOccupation = {
    "B": "Civilian employed population 16 years and over",
    "B": "Management, business, science and arts occupations",
    "B": "Service occupations",
    "B": "Sales and office occupations",
    "B": "Natural resources, construction, and maintenance occupations",
    "B": "Production, transportation, and material moving occupations"
    }


# 2.4. Industry (Universe: Civilian employed population 16 years and over)
ecIndustry = {
    "B": "Civilian employed population 16 years and over",
    "B": "Agriculture, forestry, fishing and hunting, and mining",
    "B": "Construction",
    "B": "Manufacturing",
    "B": "Wholesale trade",
    "B": "Retail trade",
    "B": "Transportation and warehousing, and utilities",
    "B": "Information",
    "B": "Finance and insurance, and real estate and rental and leasing",
    "B": "Professional, scientific, and management, and administrative, and waste management services",
    "B": "Educational services, and health care and social assistance",
    "B": "Arts, entertainment, and recreation, and accommodation and food services",
    "B": "Other services, except public administration",
    "B": "Public administration"
    }


# 2.5. Class of Worker (Universe: Civilian employed population 16 years and over)
ecClassOfWorker = {
    "B": "Civilian employed population 16 years and over",
    "B": "Private wage and salary workers",
    "B": "Government workers",
    "B": "Self-employed in own incorporated business workers",
    "B": "Unpaid family workers"
    }


# 2.6. Income and Benefits (Universe: Total households, families, nonfamilies, workers)
ecIncomeAndBenefits = {
    "B": "Total households",
    "B": "Households, less than $10,000",
    "B": "Households, $10,000 to $14,999",
    "B": "Households, $15,000 to $24,999",
    "B": "Households, $25,000 to $34,999",
    "B": "Households, $35,000 to $49,999",
    "B": "Households, $50,000 to $74,999",
    "B": "Households, $75,000 to $99,9999",
    "B": "Households, $100,000 to $149,999",
    "B": "Households, $150,000 to $199,999",
    "B": "Households, $200,000 or more",
    "B": "Median household income (dollars)",
    "B": "Mean household income (dollars)",
    "B": "Households with earnings",
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


# 2.7. Health Insurance Coverage (Universe: Civilian non-institutionalized population, families, total population)
ecHealthInsurance = {
    "B": "Civilian non-institutionalized population",
    "B": "With health insurance coverage",
    "B": "With private health insurance coverage",
    "B": "With public health insurance coverage",
    "B": "No health insurance coverage",
    "B": "19 to 64 years",
    "B": "19 to 64 years in labor force",
    "B": "19 to 64 years in labor force, employed",
    "B": "19 to 64 years in labor force, employed with health insurance coverage",
    "B": "19 to 64 years in labor force, employed with private health insurance coverage",
    "B": "19 to 64 years in labor force, employed with public health insurance coverage",
    "B": "19 to 64 years in labor force, employed with no health insurance coverage",
    "B": "19 to 64 years in labor force, unemployed",
    "B": "19 to 64 years in labor force, unemployed with health insurance coverage",
    "B": "19 to 64 years in labor force, unemployed with private health insurance coverage",
    "B": "19 to 64 years in labor force, unemployed with public health insurance coverage",
    "B": "19 to 64 years in labor force, unemployed with no health insurance coverage",
    "B": "19 to 64 years not in labor force",
    "B": "19 to 64 years not in labor force, with health insurance coverage",
    "B": "19 to 64 years not in labor force, with private health insurance coverage",
    "B": "19 to 64 years not in labor force, with public health insurance coverage",
    "B": "19 to 64 years not in labor force, with no health insurance coverage"
    }

# 2.8. Percentage of families and people whose income in the past 12 months is below the poverty level (Universe: families, population)
ecBelowPovertyLevel = {
    "B": "All families",
    "B": "Families with related children of the householder under 18 years",
    "B": "Families with related children of the householder under 5 years only",
    "B": "Married couple families",
    "B": "Married couple families with related children of the householder under 18 years",
    "B": "Married couple families with related children of the householder under 5 years only",
    "B": "Female householder, no husband present families",
    "B": "Female householder, no husband present families with related children of the householder under 18 years",
    "B": "Female householder, no husband present families with related children of the householder under 5 years only",
    "B": "All people",
    "B": "Under 18 years",
    "B": "Under 18 years, related children of the householder under 18 years",
    "B": "Under 18 years, related children of the householder under 5 years",
    "B": "Under 18 years, related children of the householder 5 to 17 years",
    "B": "18 years and over",
    "B": "18 to 64 years",
    "B": "65 years and over",
    "B": "People in families",
    "B": "Unrelated individuals 15 years and over"
    }


# 3. HOUSING CHARACTERISTICS

# 3.1. Housing Occupancy (Universe: Total housing units)
hcHousingOccupancy = {
    "B": "Total housing units",
    "B": "Occupied housing units",
    "B": "Vacant housing units",
    "B": "Homeowner vacancy rate",
    "B": "Rental vacancy rage"
    }


# 3.2. Units in Structure (Universe: Total housing units)
hcUnitsInStructure = {
    "B": "Total housing units",
    "B": "1-unit, detatched",
    "B": "1-unit, attached",
    "B": "2-units",
    "B": "3 or 4 units",
    "B": "5 to 9 units",
    "B": "10 to 19 units",
    "B": "20 or more units",
    "B": "Mobile home",
    "B": "Boat, RV, van, etc"
    }

# 3.3. Year Structure Built (Universe: Total housing units)
hcYearStructureBuilt = {
    "B": "Total housing units",
    "B": "Built 2014 or later",
    "B": "Built 2010 to 2013",
    "B": "Built 2000 to 2009",
    "B": "Built 1990 to 1999",
    "B": "Built 1980 to 1989",
    "B": "Built 1970 to 1979",
    "B": "Built 1960 to 1969",
    "B": "Built 1950 to 1959",
    "B": "Built 1940 to 1949",
    "B": "Built 1939 or earlier"
    }

# 3.4. Rooms (Universe: Total housing units)
hcRooms = {
    "B": "Total housing units",
    "B": "1 room",
    "B": "2 rooms",
    "B": "3 rooms",
    "B": "4 rooms",
    "B": "5 rooms",
    "B": "6 rooms",
    "B": "7 rooms",
    "B": "8 rooms",
    "B": "9 rooms or more",
    "B": "Median rooms"
    }


# 3.5. Bedrooms (Universe: Total housing units)
hcBedrooms = {
    "B": "Total housing units",
    "B": "No bedroom",
    "B": "1 bedroom",
    "B": "2 bedrooms",
    "B": "3 bedrooms",
    "B": "4 bedrooms",
    "B": "5 or more bedrooms"
    }


# 3.6. Housing Tenure (Universe: Occupied housing units)
hcHousingTenure = {
    "B": "Occupied houging units",
    "B": "Owner-occupied",
    "B": "Renter-occuped",
    "B": "Average household size of owner-occupied unit",
    "B": "Average household size of renter-occupied unit"
    }


# 3.7. Year Householder Moved into Unit (Universe: Occupied housing units)
hcYearMovedIntoUnit = {
    "B": "Occupied housing units",
    "B": "Moved in 2017 or later",
    "B": "Moved in 2015 to 2016",
    "B": "Moved in 2000 to 2014",
    "B": "Moved in 1990 to 1999",
    "B": "Moved in 1989 and earlier"
    }


# 3.8. Vehicles Available (Universe: Occupied housing units)
hcVehiclesAvailable = {
    "B": "Occupied housing units",
    "B": "No vehicles available",
    "B": "1 vehicle available",
    "B": "2 vehicles available",
    "B": "3 or more vehicles available"
    }


# 3.9. House Heating Fuel (Universe: Occupied housing units)
hcHouseHeatingFuel = {
    "B": "Occupied housing units",
    "B": "Utility gas",
    "B": "Bottled, tank, or LP gas",
    "B": "Electricity",
    "B": "Fuel oil, kerosene, etc",
    "B": "Coal or coke",
    "B": "Wood",
    "B": "Solar energy",
    "B": "Other fuel",
    "B": "No fuel used"
    }


# 3.10. Selected Characteristics (Universe: Occupied housing units)
hcSelectedCharacteristics = {
    "B": "Occupied housing units",
    "B": "Lacking complete plumbing facilities",
    "B": "Lacking complete kitchen facilities",
    "B": "No telephone service available"
    }


# 3.11. Occupants Per Room (Universe: Occupied housing units)
hcOccupantsPerRoom = {
    "B": "Occupied housing units",
    "B": "1.00 or less",
    "B": "1.01 to 1.50",
    "B": "1.51 or more"
    }


# 3.12. Housing Value (Universe: Owner-occupied units)
hcHousingValue = {
    "B": "Owner-occupied units",
    "B": "Less than $50,000",
    "B": "$50,000 to $99,000",
    "B": "$100,000 to $149,999",
    "B": "$150,000 to $199,999",
    "B": "$200,000 to $299,999",
    "B": "$300,000 to $499,999",
    "B": "$500,000 to $999,999",
    "B": "$1,000,000 or more",
    "B": "Median value (dollars)"
    }


# 3.13. Mortgage Status (Universe: Owner-occupied units)
hcMortgageStatus = {
    "B": "Owner-occupied units",
    "B": "Housing units with a mortgage",
    "B": "Housing units without a mortgage"
    }


# 3.14. Selected Monthly Owner Costs (SMOC) (Universe: Housing units with or without a mortgage)
hcSMOC = {
    "B": "Housing units with a mortgage",
    "B": "With mortgage, less than $500",
    "B": "With mortgage, $500 to $999",
    "B": "With mortgage, $1,000 to $1,499",
    "B": "With mortgage, $1,500 to $1,999",
    "B": "With mortgage, $2,000 to $2,499",
    "B": "With mortgage, $2,500 to $2,999",
    "B": "With mortgage, $3,000 or more",
    "B": "With mortgage, Median monthly owner costs (dollars)",
    "B": "Housing units without a mortgage",
    "B": "Without mortgage, less than $250",
    "B": "Without mortgage, $250 to $399",
    "B": "Without mortgage, $400 to $599",
    "B": "Without mortgage, $600 to $799",
    "B": "Without mortgage, $800 to $999",
    "B": "Without mortgage, $1,000 or more",
    "B": "Without mortgage, Median monthly owner costs (dollars)"
    }


# 3.15. Selected Monthly Owner Costs as a Percentage of Household Income (SMOCAPI) (Universe: Housing units with or without a mortgage)
hcSMOCAPI = {
    "B": "Housing units with a mortgage",
    "B": "With mortgage, less than 20.0 percent",
    "B": "With mortgage, 20.0 to 24.9 percent",
    "B": "With mortgage, 25.0 to 29.9 percent",
    "B": "With mortgage, 30.0 to 34.9 percent",
    "B": "With mortgage, 35.0 percent or more",
    "B": "With mortgage, not computed",
    "B": "Housing units without a mortgage",
    "B": "Without mortgage, less than 10.0 percent",
    "B": "Without mortgage, 10.0 to 14.9 percent",
    "B": "Without mortgage, 15.0 to 19.9 percent",
    "B": "Without mortgage, 20.0 to 24.9 percent",
    "B": "Without mortgage, 25.0 to 29.9 percent",
    "B": "Without mortgage, 30.0 to 34.9 percent",
    "B": "Without mortgage, 35.0 percent or more",
    "B": "Without mortgage, not computed"
    } 


# 3.16. Gross Rent (Universe: Occupied units paying rent)
hcGrossRent = {
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
    "B": "$500 to $999",
    "B": "$1,000 to $1,499",
    "B": "$1,500 to $1,999",
    "B": "$2,000 to $2,499",
    "B": "$2,500 to $2,999",
    "B": "$3,000 or more",
    "B": "Median gross rent (dollars)",
    "B": "No rent paid"
    }


# 3.17. Gross Rent as Percentage of Household Income (Universe: Occupied units paying rent)
hcGrossRentPercentageIncome = {
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