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








# 1. SOCIAL CHARACTERISTICS
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
scMaritalStatus = {
    "B": "Males, 15 years and over",
    "B": "Males, 15 years and over, never married",
    "B": "Males, 15 years and over, now married, except separated",
    "B": "Males, 15 years and over, separated",
    "B": "Males, 15 years and over, widowed",
    "B": "Males, 15 years and over, divorced",
    "B": "Females, 15 years and over",
    "B": "Females, 15 years and over, never married",
    "B": "Females, 15 years and over, now married, except separated",
    "B": "Females, 15 years and over, separated",
    "B": "Females, 15 years and over, widowed",
    "B": "Females, 15 years and over, divorced"
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
    "B": "Population 3 years and over enrolled in school",
    "B": "Nursery school, preschool",
    "B": "Kindergarten",
    "B": "Elementary school (grades 1-8)",
    "B": "High school (grades 9-12)",
    "B": "College or graduate school"
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
    "B": "Workers 16 years and over",
    "B": "Car, truck, or van - drove alone",
    "B": "Car, truck, or van - carpooled",
    "B": "Public transportation (excluding taxicab)",
    "B": "Walked",
    "B": "Other means",
    "B": "Worked at home",
    "B": "Mean travel time to work (minutes)"
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



# 4. DEMOGRAPHIC AND HOUSING ESTIMATES

# 4.1. Sex and Age (Universe: Total population)
dhSexAge = {
    "B01001e1": "Total population",
    "B01001e2": "Male",
    "B01001e26": "Female",
    "B": "Sex ratio (males per 100 females)",
    "B": "Under 5 years",
    "B": "10 to 14 years",
    "B": "15 to 19 years",
    "B": "20 to 24 years",
    "B": "25 tp 34 years",
    "B": "35 to 44 years",
    "B": "45 to 54 years",
    "B": "55 to 59 years",
    "B": "60 to 64 years",
    "B": "65 to 74 years",
    "B": "75 to 84 years",
    "B": "85 years and over",
    "B01002e1": "Median age (years)",
    "B": "Under 18 years",
    "B": "16 years and over",
    "B": "18 years and over",
    "B": "18 years and over, male",
    "B": "18 years and over, female",
    "B": "18 years and over, sex ratio (males per 100 females)",
    "B": "21 years and over",
    "B": "65 years and over",
    "B": "65 years and over, male",
    "B": "65 years and over, female",
    "B": "65 years and over, sex ratio (males per 100 females)"
    }


# 4.2. Race (Universe: Total population)
dhRace = {
    "B": "Total population",
    "B": "One race",
    "B": "One race, White",
    "B": "One race, Black or African American",
    "B": "One race, American Indian and Alaska Native",
    "B": "One race, American Indian and Alaska Native, Cherokee tribal grouping",
    "B": "One race, American Indian and Alaska Native, Chippewa tribal grouping",
    "B": "One race, American Indian and Alaska Native, Navajo tribal grouping",
    "B": "One race, American Indian and Alaska Native, Sioux tribal grouping",
    "B": "One race, Asian",
    "B": "One race, Asian, Asian Indian",
    "B": "One race, Asian, Chinese",
    "B": "One race, Asian, Filipino",
    "B": "One race, Asian, Japanese",
    "B": "One race, Asian, Korean",
    "B": "One race, Asian, Vietnamese",
    "B": "One race, Asian, Other Asian",
    "B": "One race, Native Hawaiian and Other Pacific Islander",
    "B": "One race, Native Hawaiian and Other Pacific Islander, Native Hawaiian",
    "B": "One race, Native Hawaiian and Other Pacific Islander, Guamanian or Chamorro",
    "B": "One race, Native Hawaiian and Other Pacific Islander, Samoan",
    "B": "One race, Native Hawaiian and Other Pacific Islander, Other Pacific Islander",
    "B": "One race, Some other race",
    "B": "Two or more races",
    "B": "Two or more races, White and Black or African American",
    "B": "Two or more races, White and American Indian and Alaska Native",
    "B": "Two or more races, White and Asian",
    "B": "Two or more races, Black or African American and American Indian and Alaska Native"
    }


# 4.3. Race Alone or in Combination with One or More Other Races (Universe: Total population)
dhRaceAloneOrCombinations = {
    "B": "Total population",
    "B": "White",
    "B": "Black or African American",
    "B": "American Indian and Alaska Native",
    "B": "Asian",
    "B": "Native Hawaiian and Other Pacific Islander",
    "B": "Some other race"
    }


# 4.4. Hispanic or Latino and Race (Universe: Total population)
dhHispanicRace = {
    "B": "Total population",
    "B": "Hispanic or Latino (of any race)",
    "B": "Hispanic or Latino, Mexican",
    "B": "Hispanic or Latino, Puerto Rican",
    "B": "Hispanic or Latino, Cuban",
    "B": "Hispanic or Latino, Other Hispanic or Latino",
    "B": "Not Hispanic or Latino",
    "B": "Not Hispanic or Latino, White alone",
    "B": "Not Hispanic or Latino, Black or African American alone",
    "B": "Not Hispanic or Latino, American Indian and Alaska Native alone",
    "B": "Not Hispanic or Latino, Asian alone",
    "B": "Not Hispanic or Latino, Native Hawaiian and Other Pacific Islander alone",
    "B": "Not Hispanic or Latino, Some other race alone",
    "B": "Two or more races",
    "B": "Two races including some other race",
    "B": "Two races excluding some other race, and three or more races"
    }


# 4.5. Citizen Voting Age Population (Universe: Citizen, 18 and over population)
dhCitizen = {
    "B": "Citizen, 18 and over population",
    "B": "Citizen, Male",
    "B": "Citize, Female"
    }



arcpy.env.workspace = r"d:\OneDrive\Professional\Projects\OCPW\OCGeodemographics\OCACS\OCACS2017\Original\ACS_2017_5YR_BG_06_CALIFORNIA.gdb"


strEst = " -- (Estimate)"

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


dhSexAge = {
    "B01001e1": "Total population",
    "B01001e2": "Male",
    "B01001e26": "Female",
    "B": "Sex ratio (males per 100 females)",
    "B": "Under 5 years",
    "B": "10 to 14 years",
    "B": "15 to 19 years",
    "B": "20 to 24 years",
    "B": "25 tp 34 years",
    "B": "35 to 44 years",
    "B": "45 to 54 years",
    "B": "55 to 59 years",
    "B": "60 to 64 years",
    "B": "65 to 74 years",
    "B": "75 to 84 years",
    "B": "85 years and over",
    "B01002e1": "Median age (years)",
    "B": "Under 18 years",
    "B": "16 years and over",
    "B": "18 years and over",
    "B": "18 years and over, male",
    "B": "18 years and over, female",
    "B": "18 years and over, sex ratio (males per 100 females)",
    "B": "21 years and over",
    "B": "65 years and over",
    "B": "65 years and over, male",
    "B": "65 years and over, female",
    "B": "65 years and over, sex ratio (males per 100 females)"
    }

