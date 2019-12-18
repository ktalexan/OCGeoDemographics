# OCGeoDemographics
## OC Survey GeoDemographics Repository
Dr. Kostas Alexandridis, GISP. OC Public Works, OC Survey/Geospatial Services, 2019.

### Description
---
This repository contains basic code for processing, customizing and displaying geodatabases containing the spatially-explicit data of the US Census American Community Survey (ACS), 5-year estimates for the Orange County, California.

### Census Data
---
The original data are downloaded from the US Census TIGER/Line dataset with linked ACS demographic tables.

**Data source**: [US Census TIGER/Line with Selected Demographic and Economic Data.](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-data.html)



### Geographies included
---
The dataset incude 14 separate geographies, and 25 data tables per geography in each geodatabase. Specifically, the included geographies are:

Geography | Abbrev | Description
---|---|---
State | STATE | State of California Population/Housing ACS 5-year estimates.
County | COUNTY |  County of Orange Population/Housing ACS 5-year estimates.
County Subdivisions | COUSUB | County subdivision ACS 5-year estimates.
Cities/Places | PLACE | Incorporated cities/places for ACS 5-year estimates.
Block Groups | BG | Census block groups for Orange County.
Census Tract | TRACT | Census tracts for Orange County.
Congressional Disticts (115th) | CD115 | US Congressional districts (115th US Congress) for Orange County. Exceed county geographic boundaries.
State Legislative Districts (Lower) | SLDL | California State Assembly Legislative Districts for Orange County. Exceed county geographic boundaries.
State Legislative Ditricts (Upper) | SLDU | California State Senate Legislative Districts for Orange County. Exceed county geographic boundaries.
Elementary School Districts | SDE | California Elementary School Districts for Orange County.
Secondary School Districts | SDS | California Secondary School Districts for Orange County.
Unified School Districts | SDU | California Unified School Districts for Orange County.
Public Use Microdata Areas | PUMA | US Census Public Use Microdata Areas for Orange County.
ZIP Code Tabulation Areas | ZCTA | ZIP Code Tabulation Areas for Orange County.



### ACS Demographic Tables
---
The following ACS demographic tables are included in each of the geographic levels below inside earch geography's geodatabase:

Table | Name | Description
---|---|---
X01 | Sex by Age | Sex by age and age group; Median age by sex, race and ethnic groups, Hispanic/Latino. 
X02 | Race | Race, single/multiple races, ethnic groups, and detailed race determination.
X03 | Hispanic or Latino Orgin | Hispanic/Latino origin by race and race groups, single/multiple races.
X04 | Migration | Geographical mobility in the past year for current residence in US, Puerto Rico, metropolitan/micropolitan or other statistical areas,.
X05 | Foreign Born Citizenship | Citizenship and place of birth information tables.
X06 | Place of Birth |
X07 | Migration |
X08 | Commuting |
X09 | Children Household Relationship |
X10 | Grandparents/Grandchildren |
X11 | Household Family/Subfamilies |
X12 | Marital Status and History |
X13 | Fertility |
X14 | School Enrollment |
X15 | Educational Attainment |
X16 | Language Spoken at Home |
X17 | Poverty |
X18 | Disability |
X19 | Income |
X20 | Earnings |
X21 | Veteran Status |
X22 | Food Stamps |
X23 | Employment Status |
X24 | Industry and Occupation |
X25 | Housing Characteristics |
X26 | Group Quarters |
X27 | Health Insurance |


