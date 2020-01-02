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

<table>
    <thead>
        <tr>
            <th>Category</th>
            <th>Level</th>
            <th>Abbrev</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>Administrative</td>
            <td>County</td>
            <td>COUNTY</td>
            <td>County of Orange</td>
        </tr>
        <tr>
            <td>County Subdivisions</td>
            <td>COUSUB</td>
            <td>Orange County subdivisions</td>
        </tr>
        <tr>
            <td>Cities/Places</td>
            <td>PLACE</td>
            <td>Orange County Cities</td>
        </tr>
        <tr>
            <td>ZIP Codes</td>
            <td>ZCTA</td>
            <td>ZIP Code Tabulation Areas for Orange County</td>
        </tr>
        <tr>
            <td rowspan = 3>Political</td>
            <td>Congressional Districts</td>
            <td>CD11X</td>
            <td>Congressional Districts, 113th-116th US Congress for Orange County</td>
        </tr>
        <tr>
            <td>State Assembly</td>
            <td>SLDL</td>
            <td>State Assembly Legislative Districts (Lower) for Orange County</td>
        </tr>
        <tr>
            <td>State Senate</td>
            <td>SLDU</td>
            <td>State Senate Legislative Districts (Upper) for Orange County</td>
        </tr>
        <tr>
            <td rowspan = 3>Education</td>
            <td>Elementary</td>
            <td>SDE</td>
            <td>Elementary School Districts for Orange County</td>
        </tr>
        <tr>
            <td>Secondary</td>
            <td>SDS</td>
            <td>Secondary School Districts for Orange County</td>
        </tr>
        <tr>
            <td>Unified</td>
            <td>SDU</td>
            <td>Unified School Districts for Orange County</td>
        </tr>
        <tr>
            <td rowspan = 4>Census</td>
            <td>Urban Areas</td>
            <td>UA</td>
            <td>Urban Areas for Orange and Los Angeles Counties</td>
        </tr>
        <tr>
            <td>Public Use Microdata Areas</td>
            <td>PUMA</td>
            <td>Census Public Use Microdata Areas for Orange County</td>
        </tr>
        <tr>
            <td>Block Groups</td>
            <td>BG</td>
            <td>Census Block Groups for Orange County</td>
        </tr>
        <tr>
            <td>Census Tracts</td>
            <td>TRACT</td>
            <td>Census Tracts for Orange County</td>
        </tr>
    </tbody>
</table>


<br/><br/>



### Geodemographic Tables by group
<br>


#### Demographic Characteristics (6 groups, 105 fields)

Code|Name|Universe|Table|Fields|Count
---|---|---|---|---|---:
D01|Sex and age|total population|X1|B01001|49
D02|Median age by sex and race|total population|X1|B01002|12
D03|Race|total population|X2|B02001|8
D04|Race alone or in combination with one or more other races|total population|X2|B02001,B02008-13|7
D05|Hispanic or Latino and race|total population|X3|B03002|21
D06|Citizen voting age population|citizen, 18 and over|X5|B05003|8

<br>

#### Social Characteristics (19 groups, 500 fields)

Code|Name|Universe|Table|Fields|Count
---|---|---|---|---|---:
S01|Households by type|total households|X11|B11001, B11003, B11007, B25010|17
S02|Relationship|population in households|X9|B09019|19
S03|Marital status|population 15 years and over|X12|B12001|13
S04|Fertility|women 15 to 50 years old who had birth in the past 12 months|X13|B13002, B13016|11
S05|Grandparents|grandparents living or responsible for own grandchildren under 18 years|X10|B10050, B10056-57|18
S06|School enrollment|population 3 years old and over enrolled in school|X14|B14007|17
S07|Educational attainment|population 25 years and over|X15|B15003|25
S08|Veteran status|civilian population 18 years and over|X21|B21001|2
S09|Disability sttus and type by sex and age|total civilian non-institutionalized population|X18|B18101-107|77
S10|Disability status by age and health insurance coverage|civilian non-institutionalized population|X18|B18135|16
S11|Residence 1 year ago|population 1 year and over|X7|B07001|6
S12|Place of birth|total population|X5|B05002|27
S13|Citizenship status by nativity in the US|total population|X5|B05001|6
S14|Year of entry|population born outside the US|X5|B05005|21
S15|World region of birth of foreign born population|foreign-born population, excluding population born at sea|X5|B05006|25
S16|Language spoken in households|total households|X16|C16002|6
S17|Language spoken at home|population 5 years and over|X16|B16004|67
S18|Ancestry|total population reporting ancestry|X4|B04006-7|114
S19|Computers and internet use|total population in households and total households|X28|B28008, B28010-11|13

<br>

#### Economic Characteristics (19 groups, 397 fields)

Code|Name|Universe|Table|Fields|Count
---|---|---|---|---|---:
E01|Employment status|population 16 years and over|X23|B23025|7
E02|Work status by age of worker|population 16 years and over|x23|B23027|36
E03|Commuting to work|workers 16 years and over|X8|B08301, B08135|8
E04|Travel time to work|workers 16 years and over who did not work at home|X8|B08012-13|14
E05|Number of vehicles available for workers|workers 16 years and over in households|X8|B08014-15|8
E06|Median age by means of transportation to work|median age, workers 16 years and over)|X8|B01103|7
E07|Means of transportation to work by race|workers 16 years and over|X8|B08105|64
E08|Occupation|civilian employed population 16 years and over|X24|C24010|53
E09|Industry|civilian employed population 16 years and over|X24|C24030|43
E10|Class of worker|civilian employed population 16 years and over|X24|B24080|19
E11|Household income and earnings in the past 12 months|total households|X19|B19001, B19013, B19025, B19081, B19083, B19051-60, B22010|37
E12|Income and earnings in dollars|inflation-adjusted dollars|X19, X20|B19061-69, B19113, B19202, B19214, B19301, B19313, B20002|31
E13|Family income in dollars|total families|X19|B19101|17
E14|Health insurance coverage|civilian non-instutionalized population|X27|B27010|17
E15|Ratio of income to poverty level|total population for whom poverty level is determined|X17|C17002|8
E16|Poverty in population in the past 12 months|total population for whom poverty is determined|X17|B17021|7
E17|Poverty in households in the past 12 months|total households|X17|B17017|9
E18|Percentage of families and people whose income in the past 12 months is below the poverty level|families, population|X17|B17010|8
E19|Poverty and income deficit (dollars) in the past 12 months for families|families with income below poverty level in the past 12 months|X17|B17011|4

<br>

#### Housing Characteristics (23 groups, 406 fields)

Code|Name|Universe|Table|Fields|Count
---|---|---|---|---|---:
H01|Housing occupancy|total housing units|X25|B25002|3
H02|Units in structure|total housing units|X25|B25024|11
H03|Population in occupied housing units by tenure by units in structure|total population in occupied housing units|X25|B25033|13
H04|Year structure built|total housing units|X25|B25034-35, B25037|15
H05|Rooms|total housing units|X25|B25017-19, B25021-22|18
H06|Bedrooms|total housing units|X25|B25041-42|21
H07|Housing tenure by race of householder|occupied housing units|X25|B25003, B25007, B25010|51
H08|Total population in occupied housing units by tenure|total population in occupied housing units|X25|B25008|3
H09|Vacancy status|vacant housing units|X25|B25004|8
H10|Occupied housing units by race of householder|occupied housing units|X25|B25006|8
H11|Year householder moved into unit|occupied housing units|X25|B25038|18
H12|Vehicles available|occupied housing units|X25|B25044, B25046|18
H13|House heating fuel|occupied housing units|X25|B25040|10
H14|Selected characteristics|occupied housing units|X25|B25016, B25043, B25053|9
H15|Occupants per room|occupied housing units|X25|B25014|13
H16|Housing value|owner-occupied units|X25|B25075-79, B25083|32
H17|Price asked for vacant for-sale only, and sold, not occupied housing units|vacant for slae only, and sold, not occupied housing units|X25|B25085-86|28
H18|Mortgage status|owner-occupied units|X25|B25081-82|10
H19|Selected monthly owner costs (SMOC)|owner-occupied housing units with or without a mortgage|X25|B25087-89|45
H20| Selected monthly owner costs as a percentage of household income (SMOCAPI)|owner-occupied housing units with or without a mortgage|X25|B25091-92|26
H21|Contract rent distribution and rent asked distribution in dollars|renter-occupied housing units paying cash rent and vacant, for rent, and rented, not occupied housing units|X25|B25056-62|7
H22|Gross rent|occupied units paying rent|X25|B25063-65|28
H23|Gross rent as percentage of household income|occupied units paying rent|X25|B25070|11

<br><br>

### Detailed Description
<br>

<h4 id="d">Demographic Characteristics</h4>

<h5 id="d01">D01: Sex and Age</h5>

Name|ACS2017_BG_D01
:---|:---
Tags|geodemographics; Orange County; California; US Census; ACS; American Community Survey; demographics; block groups; age and sex
Summary|Age and Sex characteristics by Census Block Groups of the 2017 American Community Survey (ACS), 5-year estimates for Orange County, California. The purpose of the dataset is to assist spatial visualization and analysis of basic demographic statistical information in the county. Universe: Total population.
Description | US Census American Community Survey (ACS) 2017, 5-year estimates of the key Age and Sex demographic characteristics for Orange County, California. The layer contains demographic data for table X01: Age and Sex of the ACS 2017 (5-year) dataset for Block Groups in Orange County, fields B01002 (Universe: Total population). The US Census geodemographic data are based on the 2017 TigerLines across multiple census geographies. The spatial geographies were merged with ACS demographic data tables.
Terms of Use | Original datasets from US Census [TigerLine Geography](https://www.census.gov/geo/maps-data/data/tiger-line.html), and [American FactFinder](https://factfinder.census.gov) for the X01: Age and Sex Tables of the American Community Survey (ACS, 2017). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey/Geospatial Services, Dr. Kostas Alexandridis, GISP, on December 2019.

<br>
<h5 id="d02">D02: Median age by sex and race</h5>

Name|ACS2017_BG_D02
:---|:---
Tags|geodemographics; Orange County; California; US Census; ACS; American Community Survey; demographics; block groups; sex; race; median age
Summary|Median age by sex and race characteristics by Census Block Groups of the 2017 American Community Survey (ACS), 5-year estimates for Orange County, California. The purpose of the dataset is to assist spatial visualization and analysis of basic demographic statistical information in the county. Universe: Total population.
Description | US Census American Community Survey (ACS) 2017, 5-year estimates of the key Age and Sex demographic characteristics for Orange County, California. The layer contains demographic data for table X01: Age and Sex of the ACS 2017 (5-year) dataset for Block Groups in Orange County, fields B01002 (Universe: Total population). The US Census geodemographic data are based on the 2017 TigerLines across multiple census geographies. The spatial geographies were merged with ACS demographic data tables.
Terms of Use | Original datasets from US Census [TigerLine Geography](https://www.census.gov/geo/maps-data/data/tiger-line.html), and [American FactFinder](https://factfinder.census.gov) for the X01: Age and Sex Tables of the American Community Survey (ACS, 2017). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey/Geospatial Services, Dr. Kostas Alexandridis, GISP, on December 2019.


<h5 id="d03">D03: Race</h5>

* Universe: total population
* Census table: X02
* Fields: B02001 (8 fields)


