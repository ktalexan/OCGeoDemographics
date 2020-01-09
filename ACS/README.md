# OCGeoDemographics: American Community Survey (ACS) Data for Orange County
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


|Category|Level|Abbrev|Description|
|:---|:---|:---:|:---|
|Administrative|County|CO|County of Orange|
|^|County Subdivisions|CS|Orange County Subdivisions|
|^|Cities/Places|PL|Orange Couny Cities|
|^|ZIP Codes|ZC|ZIP Code Tabulation Areas for Orange County|
|Political|Congressional Districts|CD|Congressional Districts, 113th-116th US Congress for Orange County|
|^|State Assembly|LL|State Assembly Legislative Districts (Lower) for Orange County|
|^|State Senate|UL|State Senate Legislative Districts (Upper) for Orange County|
|Education|Elementary|ED|Elementary School Districts for Orange County|
|^|Secondary|SD|Secondary School Districts for Orange County|
|^|Unified|UD|Unified School Districts for Orange County|
|Census|Urban Areas|UA|Urban Areas for Orange and Los Angeles Counties|
|^|Public Use Microdata Areas|PU|Census Public Use Microdata Areas (PUMA) for Orange County|
|^|Block Groups|BG|Census Block Groups for Orange County|
|^|Census Tracts|TR|Census Tracts for Orange County|

<br><br>



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
            <td>CO</td>
            <td>County of Orange</td>
        </tr>
        <tr>
            <td>County Subdivisions</td>
            <td>CS</td>
            <td>Orange County subdivisions</td>
        </tr>
        <tr>
            <td>Cities/Places</td>
            <td>PL</td>
            <td>Orange County Cities</td>
        </tr>
        <tr>
            <td>ZIP Codes</td>
            <td>ZC</td>
            <td>ZIP Code Tabulation Areas for Orange County</td>
        </tr>
        <tr>
            <td rowspan = 3>Political</td>
            <td>Congressional Districts</td>
            <td>CD</td>
            <td>Congressional Districts, 113th-116th US Congress for Orange County</td>
        </tr>
        <tr>
            <td>State Assembly</td>
            <td>LL</td>
            <td>State Assembly Legislative Districts (Lower) for Orange County</td>
        </tr>
        <tr>
            <td>State Senate</td>
            <td>UL</td>
            <td>State Senate Legislative Districts (Upper) for Orange County</td>
        </tr>
        <tr>
            <td rowspan = 3>Education</td>
            <td>Elementary</td>
            <td>ED</td>
            <td>Elementary School Districts for Orange County</td>
        </tr>
        <tr>
            <td>Secondary</td>
            <td>SD</td>
            <td>Secondary School Districts for Orange County</td>
        </tr>
        <tr>
            <td>Unified</td>
            <td>UD</td>
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
            <td>PU</td>
            <td>Census Public Use Microdata Areas for Orange County</td>
        </tr>
        <tr>
            <td>Block Groups</td>
            <td>BG</td>
            <td>Census Block Groups for Orange County</td>
        </tr>
        <tr>
            <td>Census Tracts</td>
            <td>TR
</td>
            <td>Census Tracts for Orange County</td>
        </tr>
    </tbody>
</table>


<br/><br/>



### Geodemographic Tables by group

For each of the 14 geographies described in the previous section four categories of geodemographic characteristics are linked:

1. Demographic characteristics (6 groups, 105 fields)
2. Social characteristics (19 groups, 500 fields)
3. Economic characteristics (19 groups, 397 fields)
4. Housing characteristics (23 groups, 406 fields)

Each of the geographies is represented by a separate geodatabase structure. Within of each of the geographic level geodatabases, each of the four characteristics is represented by a _feature class_ respectively. In order to easily identify each of the sub-groups within each category, the name of the original census table field was adjusted by prepending to it the subgroup identification code. For example, the original field B01001e1 would become D01_B01001e1 in the new feature class for the demographic characteristics.

A more detailed description of each sub-group within each of the four feature classes representing the ACS table characteristics is provided below. The table's columns represent: the subgroup's code; its descriptive name;the universe (summative) level of the reference; the ACS cenus table in which the original fields are located; the fields/variables of the data, and; how many fields are included in the subgroup.

<br>

#### D: Demographic Characteristics (6 groups, 105 fields)

The demographic characteristics selected for spatial representation can be found in ACS data tables X1-X5. They are devided in 6 subgroups: sex and age, median age distribution, single race determination, race in combination with other races, Hispanic or Latino determination, and the citizen voting age population estimates.

Code|Name|Universe|Table|Fields|Count
---|---|---|---|---|---:
D01|Sex and age|total population|X1|B01001|49
D02|Median age by sex and race|total population|X1|B01002|12
D03|Race|total population|X2|B02001|8
D04|Race alone or in combination with one or more other races|total population|X2|B02001,B02008-13|7
D05|Hispanic or Latino and race|total population|X3|B03002|21
D06|Citizen voting age population|citizen, 18 and over|X5|B05003|8

<br>

The following fields are included for each of the demographic groups:

* __D01:__ B01001e1 (Total population); B01001e2 (Male); B01001e3 (Male, under 5 years); B01001e4 (Male, 5 to 9 years); B01001e5 (Male, 10 to 14 years); B01001e6 (Male, 15 to 17 years); B01001e7 (Male, 18 and 19 years); B01001e8 (Male, 20 years); B01001e9 (Male, 21 years); B01001e10 (Male, 22 to 24 years); B01001e11 (Male, 25 to 29 years); B01001e12 (Male, 30 to 34 years); B01001e13 (Male, 35 to 39 years); B01001e14 (Male, 40 to 44 years); B01001e15 (Male, 45 to 49 years); B01001e16 (Male, 50 to 54 years); B01001e17 (Male, 55 to 59 years); B01001e18 (Male, 60 and 61 years); B01001e19 (Male, 62 to 64 years); B01001e20 (Male, 65 and 66 years); B01001e21 (Male, 67 to 69 years); B01001e22 (Male, 70 to 74 years); B01001e23 (Male, 75 to 79 years); B01001e24 (Male, 80 to 84 years); B01001e25 (Male, 85 years and over); B01001e26 (Female); B01001e27 (Female, under 5 years); B01001e28 (Female, 5 to 9 years); B01001e29 (Female, 10 to 14 years); B01001e30 (Female, 15 to 17 years); B01001e31 (Female, 18 and 19 years); B01001e32 (Female, 20 years); B01001e33 (Female, 21 years); B01001e34 (Female, 22 to 24 years); B01001e35 (Female, 25 to 29 years); B01001e36 (Female, 30 to 34 years); B01001e37 (Female, 35 to 39 years); B01001e38 (Female, 40 to 44 years); B01001e39 (Female, 45 to 49 years); B01001e40 (Female, 50 to 54 years); B01001e41 (Female, 55 to 59 years); B01001e42 (Female, 60 and 61 years); B01001e43 (Female, 62 to 64 years); B01001e44 (Female, 65 and 66 years); B01001e45 (Female, 67 to 69 years); B01001e46 (Female, 70 to 74 years); B01001e47 (Female, 75 to 79 years); B01001e48 (Female, 80 to 84 years); B01001e49 (Female, 85 years and over).

* __D02:__ B01002e1 (Median age (years)); B01002e2 (Male, median age (years)); B01002e3 (Female, median age (years)); B01002Ae1 (White alone, median age (years)); B01002Be1 (Black or African American alone, median age (years)); B01002Ce1 (American Indian and Alaska Native alone, median age (years)); B01002De1 (Asian alone, median age (years)); B01002Ee1 (Native Hawaiian and Other Pacific Islander alone, median age (years)); B01002Fe1 (Some other race alone, median age (years)); B01002Ge1 (Two or more races, median age (years)); B01002He1 (White alone, not Hispanic or Latino, median age (years)); B01002Ie1 (Hispanic or Latino, median age (years)).

* __D03:__ B02001e1 (Total population); B02001e2 (White alone); B02001e3 (Black or African American alone); B02001e4 (American Indian and Alaska Native alone); B02001e5 (Asian alone); B02001e6 (Native Hawaiian and Other Pacific Islander alone); B02001e7 (Some other race alone); B02001e8 (Two or more races).

* __D04:__ B02001e1 (Total population); B02008e1 (White); B02009e1 (Black or African American); B02010e1 (American Indian and Alaska Native); B02011e1 (Asian); B02012e1 (Native Hawaiian and Other Pacific Islander); B02013e1 (Some other race).

* __D05:__ B03002e1 (Total population); B03002e2 (Not Hispanic or Latino); B03002e3 (Not Hispanic or Latino, White alone); B03002e4 (Not Hispanic or Latino, Black or African American alone); B03002e5 (Not Hispanic or Latino, American Indian and Alaska Native alone); B03002e6 (Not Hispanic or Latino, Asian alone); B03002e7 (Not Hispanic or Latino, Native Hawaiian and Other Pacific Islander alone); B03002e8 (Not Hispanic or Latino, Some other race alone); B03002e9 (Not Hispanic or Latino, Two or more races); B03002e10 (Not Hispanic or Latino, Two races including some other race); B03002e11 (Not Hispanic or Latino, Two races excluding some other race, and three or more races); B03002e12 (Hispanic or Latino); B03002e13 (Hispanic or Latino, White alone); B03002e14 (Hispanic or Latino, Black or African American alone); B03002e15 (Hispanic or Latino, American Indian and Alaska Native alone); B03002e16 (Hispanic or Latino, Asian alone); B03002e17 (Hispanic or Latino, Native Hawaiian and Other Pacific Islander alone); B03002e18 (Hispanic or Latino, Some other race alone); B03002e19 (Hispanic or Latino, Two or more races); B03002e20 (Hispanic or Latino, Two races including some other race); B03002e21 (Hispanic or Latino, Two races excluding some other race, and three or more races).

* __D06:__ B05003e8 (Male, 18 years and over); B05003e9 (Male, Native US Citizen, 18 years and over); B05003e11 (Male, Foreign-born Naturalized US Citizen, 18 years and over); B05003e12 (Male, Foreign-born, not a US Citizen, 18 years and over); B05003e19 (Female, 18 years and over); B05003e20 (Female, Native US Citizem, 18 years and over); B05003e22 (Female, Foreign-born, Naturalized US Citizen, 18 years and over); B05003e23 (Female, Foreign-born, not a US Citizen, 18 years and over).



<br><br>


#### S: Social Characteristics (19 groups, 500 fields)

The social characteristics selected for spatial representation can be found in ACS data tables X5-X18 and X28. They are devided in 19 subgroups: household types, relationships, marital status, fertility, grandparents, school enrollment, educational attainment, veteran status, disability characteristics, residence, place of birth, citizenship status, language (in households and at home), ancestry, and computers/internet use estimates.

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

The following fields are included for each of the social groups:

* __S01:__ B11001e1 (Total households); B11001e2 (Family households (families)); B11003e1 (Family households with own children of the householder under 18 years); B11001e3 (Married-couple family households); B11003e3 (Married-couple family households with own children of the householder under 18 years); B11001e5 (Male householder, no wife present, family households); B11003e10 (Male householder, no wife present, family households with own children of the householder under 18 years); B11001e6 (Female householder, no husband present, family households); B11003e16 (Female householder, no husband present, family households with own children of the householder under 18 years); B11001e7 (Nonfamily households); B11001e8 (Nonfamily households, householder living alone); B11005e2 (Households with one or more people under 18 years); B11007e2 (Households with one or more people 65 years and over); B25010e1 (Average household size for total occupied housing units); B25010e2 (Average household size for owner-occupied housing units); B25010e3 (Average household size for renter-occupied housing units); B11003e1 (Total families).

* __S02:__ B09019e2 (Population in households); B09019e4 (Householder); B09019e7 (Spouse); B09019e8 (Child); B09019e9 (Child, biological); B09019e10 (Child, adopted); B09019e11 (Child, stepchild); B09019e12 (Grandchild); B09019e13 (Brother or sister); B09019e14 (Parent); B09019e15 (Parent in law); B09019e16 (Son in law or daughter in law); B09019e17 (Other relatives); B09019e18 (Non-relatives); B09019e19 (Non-relatives, roomer or boarder); B09019e20 (Non-relatives, housemate or roomate); B09019e21 (Non-relatives, unmarried partner); B09019e22 (Non-relatives, foster child); B09019e23 (Non-relatives, other).

* __S03:__ B12001e1 (Total population, 15 years and over); B12001e2 (Males, 15 years and over); B12001e3 (Males, 15 years and over, never married); B12001e5 (Males, 15 years and over, now married, except separated); B12001e7 (Males, 15 years and over, separated); B12001e9 (Males, 15 years and over, widowed); B12001e10 (Males, 15 years and over, divorced); B12001e11 (Females, 15 years and over); B12001e12 (Females, 15 years and over, never married); B12001e14 (Females, 15 years and over, now married, except separated); B12001e16 (Females, 15 years and over, separated); B12001e18 (Females, 15 years and over, widowed); B12001e19 (Females, 15 years and over, divorced)

* __S04:__ B13002e1 (Women 15 to 50 years); B13002e2 (Women 15 to 50 years old who had a birth in the past 12 months); B13002e3 (Now married (including separated and spouse absent) women 15 to 50 years old who had a birth in the past 12 months); B13002e7 (Unmarried (never married, widowed, and divorced) women 15 to 50 years old who had a birth in the past 12 months); B13016e3 (Women 15 to 19 years old who had a birth in the past 12 months); B13016e4 (Women 20 to 24 years old who had a birth in the past 12 months); B13016e5 (Women 25 to 29 years old who had a birth in the past 12 months); B13016e6 (Women 30 to 34 years old who had a birth in the past 12 months); B13016e7 (Women 35 to 39 years old who had a birth in the past 12 months); B13016e8 (Women 40 to 44 years old who had a birth in the past 12 months); B13016e9 (Women 45 to 50 years old who had a birth in the past 12 months).

* __S05:__ B10050e1 (Population 30 years and over); B10050e2 (Number of grandparents living with own grandchildren under 18 years); B10050e3 (Number of grandparents living with own grandchildren under 18 years, responsible for grandchildren); B10050e4 (Number of grandparents living with own grandchildren under 18 years, less than 6 months responsible for grandchildren); B10050e5 (Number of grandparents living with own grandchildren under 18 years, less than 1 year responsible for grandchildren); B10050e6 (Number of grandparents living with own grandchildren under 18 years, 1 or 2 years responsible for grandchildren); B10050e7 (Number of grandparents living with own grandchildren under 18 years, 3 or 4 years responsible for grandchildren); B10050e8 (Number of grandparents living with own grandchildren under 18 years, 5 or more years responsible for grandchildren); B10050e9 (Number of grandparents living with own grandchildren under 18 years, not responsible for grandchildren); B10050e10 (Number of grandparents not living with own grandchildren under 18 years); B10056e2 (Male grandparents living with own grandchildren under 18 years); B10056e3 (Male grandparents living with own grandchildren under 18 years, responsible for grandchildren); B10056e7 (Female grandparents living with own grandchildren under 18 years); B10056e8 (Female grandparents living with own grandchildren under 18 years, responsible for grandchildren); B10057e2 (Married grandparents living with own grandchildren under 18 years); B10057e3 (Married grandparents living with own grandchildren under 18 years, responsible for grandchildren); B10057e7 (Unmarried grandparents living with own grandchildren under 18 years); B10057e8 (Unmarried grandparents living with own grandchildren under 18 years, responsible for grandchildren).

* __S06:__ B14007e2 (Population 3 years and over enrolled in school); B14007e3 (Nursery school, preschool); B14007e4 (Kindergarten); B14007e5 (Elementary school, grade 1); B14007e6 (Elementary school, grade 2); B14007e7 (Elementary school, grade 3); B14007e8 (Elementary school, grade 4); B14007e9 (Elementary school, grade 5); B14007e10 (Elementary school, grade 6); B14007e11 (Elementary school, grade 7); B14007e12 (Elementary school, grade 8); B14007e13 (High school, grade 9); B14007e14 (High school, grade 10); B14007e15 (High school, grade 11); B14007e16 (High school, grade 12); B14007e17 (College, undergraduate years); B14007e18 (Graduate or professional school).

* __S07:__ B15003e1 (Population 25 years and over); B15003e2 (No schooling completed); B15003e3 (Nursery school); B15003e4 (Kindergarten); B15003e5 (1st grade); B15003e6 (2nd grade); B15003e7 (3rd grade); B15003e8 (4th grade); B15003e9 (5th grade); B15003e10 (6th grade); B15003e11 (7th grade); B15003e12 (8th grade); B15003e13 (9th grade); B15003e14 (10th grade); B15003e15 (11th grade); B15003e16 (12th grade); B15003e17 (High school diploma); B15003e18 (GED or alternative credential); B15003e19 (Some college, less than 1 year); B15003e20 (Some college, 1 or more years, no degree); B15003e21 (Associate's degree); B15003e22 (Bachelor's degree); B15003e23 (Master's degree); B15003e24 (Professional school degree); B15003e25 (Doctorate degree).

* __S08:__ B21001e1 (Civilian population 18 years and over); B21001e2 (Civilian veterans).

* __S09:__ B18101e1 (Total civilian non-institutionalized population); B18101e2 (Male); B18101e4 (Male, under 5 years, with disability); B18102e4 (Male, under 5 years, with hearing difficulty); B18103e4 (Male, under 5 years, with vision difficulty); B18101e7 (Male, 5 to 17 years, with disability); B18102e7 (Male, 5 to 17 years, with hearing difficulty); B18103e7 (Male, 5 to 17 years, with vision difficulty); B18104e4 (Male, 5 to 17 years, with cognitive difficulty); B18105e4 (Male, 5 to 17 years, with ambulatory difficulty); B18106e4 (Male, 5 to 17 years, with self-care difficulty); B18101e10 (Male, 18 to 34 years, with disability); B18102e10 (Male, 18 to 34 years, with hearing difficulty); B18103e10 (Male, 18 to 34 years, with vision difficulty); B18104e7 (Male, 18 to 34 years, with cognitive difficulty); B18105e7 (Male, 18 to 34 years, with ambulatory difficulty); B18106e7 (Male, 18 to 34 years, with self-care difficulty); B18107e4 (Male, 18 to 34 years, with independent living difficulty); B18101e13 (Male, 35 to 64 years, with disability); B18102e13 (Male, 35 to 64 years, with hearing difficulty); B18103e13 (Male, 35 to 64 years, with vision difficulty); B18104e10 (Male, 35 to 64 years, with cognitive difficulty); B18105e10 (Male, 35 to 64 years, with ambulatory difficulty); B18106e10 (Male, 35 to 64 years, with self-care difficulty); B18107e7 (Male, 35 to 64 years, with independent living difficulty); B18101e16 (Male, 65 to 74 years, with disability); B18102e16 (Male, 65 to 74 years, with hearing difficulty); B18103e16 (Male, 65 to 74 years, with vision difficulty); B18104e13 (Male, 65 to 74 years, with cognitive difficulty); B18105e13 (Male, 65 to 74 years, with ambulatory difficulty); B18106e13 (Male, 65 to 74 years, with self-care difficulty); B18107e10 (Male, 65 to 74 years, with independent living difficulty); B18101e19 (Male, 75 years and over, with disability); B18102e19 (Male, 75 years and over, with hearing difficulty); B18103e19 (Male, 75 years and over, with vision difficulty); B18104e16 (Male, 75 years and over, with cognitive difficulty); B18105e16 (Male, 75 years and over, with ambulatory difficulty); B18106e16 (Male, 75 years and over, with self-care difficulty); B18107e13 (Male, 75 years and over, with independent living difficulty); B18101e21 (Female); B18101e23 (Female, under 5 years, with disability); B18102e23 (Female, under 5 years, with hearing difficulty); B18103e23 (Female, under 5 years, with vision difficulty); B18101e26 (Female, 5 to 17 years, with disability); B18102e26 (Female, 5 to 17 years, with hearing difficulty); B18103e26 (Female, 5 to 17 years, with vision difficulty); B18104e20 (Female, 5 to 17 years, with cognitive difficulty); B18105e20 (Female, 5 to 17 years, with ambulatory difficulty); B18106e20 (Female, 5 to 17 years, with self-care difficulty); B18101e29 (Female, 18 to 34 years, with disability); B18102e29 (Female, 18 to 34 years, with hearing difficulty); B18103e29 (Female, 18 to 34 years, with vision difficulty); B18104e23 (Female, 18 to 34 years, with cognitive difficulty); B18105e23 (Female, 18 to 34 years, with ambulatory difficulty); B18106e23 (Female, 18 to 34 years, with self-care difficulty); B18107e17 (Female, 18 to 34 years, with independent living difficulty); B18101e32 (Female, 35 to 64 years, with disability); B18102e32 (Female, 35 to 64 years, with hearing difficulty); B18103e32 (Female, 35 to 64 years, with vision difficulty); B18104e26 (Female, 35 to 64 years, with cognitive difficulty); B18105e26 (Female, 35 to 64 years, with ambulatory difficulty); B18106e26 (Female, 35 to 64 years, with self-care difficulty); B18107e20 (Female, 35 to 64 years, with independent living difficulty); B18101e35 (Female, 65 to 74 years, with disability); B18102e35 (Female, 65 to 74 years, with hearing difficulty); B18103e35 (Female, 65 to 74 years, with vision difficulty); B18104e29 (Female, 65 to 74 years, with cognitive difficulty); B18105e29 (Female, 65 to 74 years, with ambulatory difficulty); B18106e29 (Female, 65 to 74 years, with self-care difficulty); B18107e23 (Female, 65 to 74 years, with independent living difficulty); B18101e38 (Female, 75 years and over, with disability); B18102e38 (Female, 75 years and over, with hearing difficulty); B18103e38 (Female, 75 years and over, with vision difficulty); B18104e32 (Female, 75 years and over, with cognitive difficulty); B18105e32 (Female, 75 years and over, with ambulatory difficulty); B18106e32 (Female, 75 years and over, with self-care difficulty); B18107e26 (Female, 75 years and over, with independent living difficulty

* __S10:__ B18135e1 (Total civilian non-institutionalized population); B18135e2 (Under 19 years); B18135e3 (Under 19 years with a disability); B18135e5 (Under 19 years with a disability, with private health insurance); B18135e6 (Under 19 years with a disability, with public health insurance); B18135e7 (Under 19 years with a disability, without health insurance); B18135e13 (19 to 64 years); B18135e14 (19 to 64 years with a disability); B18135e16 (19 to 64 years with a disability, with private health insurance); B18135e17 (19 to 64 years with a disability, with public health insurance); B18135e18 (19 to 64 years with a disability, without health insurance); B18135e24 (65 years and over); B18135e25 (65 years and over with a disability); B18135e27 (65 years and over with a disability, with private health insurance); B18135e28 (65 years and over with a disability, with public health insurance); B18135e29 (65 years and over with a disability, without health insurance); 

* __S11:__ B07001e1 (Population 1 year and over); B07001e17 (Same house 1 year ago); B07001e33 (Moved within same county); B07001e49 (Moved from different county, within same state); B07001e65 (Moved from different state); B07001e81 (Moved from abroad).

* __S12:__ B05002e1 (Total population); B05002e2 (Native population); B05002e3 (Native population, born in US, state of residence); B05002e4 (Native population, born in US, different state); B05002e5 (Native population, born in US, different state, Northeast); B05002e6 (Native population, born in US, different state, Midwest); B05002e7 (Native population, born in US, different state, South); B05002e8 (Native population, born in US, different state, west); B05002e9 (Native population, born outside the US); B05002e10 (Native population, born outside the US, Puerto Rico); B05002e11 (Native population, born outside the US, US Islands); B05002e12 (Native population, born outside the US, abroad to American parent(s)); B05002e13 (Foreign-born population); B05002e14 (Foreign-born population, naturalized US citizen); B05002e15 (Foreign-born population, naturalized US citizen, Europe); B05002e16 (Foreign-born population, naturalized US citizen, Asia); B05002e17 (Foreign-born population, naturalized US citizen, Africa); B05002e18 (Foreign-born population, naturalized US citizen, Oceania); B05002e19 (Foreign-born population, naturalized US citizen, Latin America); B05002e20 (Foreign-born population, naturalized US citizen, Northern America); B05002e21 (Foreign-born population, not a US citizen); B05002e22 (Foreign-born population, not a US citizen, Europe); B05002e23 (Foreign-born population, not a US citizen, Asia); B05002e24 (Foreign-born population, not a US citizen, Africa); B05002e25 (Foreign-born population, not a US citizen, Oceania); B05002e26 (Foreign-born population, not a US citizen, Latin America); B05002e27 (Foreign-born population, not a US citizen, Northern America).

* __S13:__ B05001e1 (Total population); B05001e2 (US citizen, born in the US); B05001e3 (US citizen, born in Puerto Rico or US island areas); B05001e4 (US citizen, born abroad of American parent(s)); B05001e5 (Us citizen by naturalization); B05001e6 (Not a US citizen).

* __S14:__ B05005e1 (Population born outside the US); B05005e2 (Entered 2010 or later); B05005e3 (Entered 2010 or later, native); B05005e4 (Entered 2010 or later, foreign-born); B05005e5 (Entered 2010 or later, foreign-born, naturalized US citizen); B05005e6 (Entered 2010 or later, foreign-born, not a US citizen); B05005e7 (Entered 2000 to 2009); B05005e8 (Entered 2000 to 2009, native); B05005e9 (Entered 2000 to 2009, foreign-born); B05005e10 (Entered 2000 to 2009, foreign-born, naturalized US citizen); B05005e11 (Entered 2000 to 2009, foreign-born, not a US citizen); B05005e12 (Entered 1990 to 1999); B05005e13 (Entered 1990 to 1999, native); B05005e14 (Entered 1990 to 1999, foreign-born); B05005e15 (Entered 1990 to 1999, foreign-born, naturalized US citizen); B05005e16 (Entered 1990 to 1999, foreign-born, not a US citizen); B05005e17 (Entered before 1990); B05005e18 (Entered before 1990, native); B05005e19 (Entered before 1990, foreign-born); B05005e20 (Entered before 1990, foreign-born, naturalized US citizen); B05005e21 (Entered before 1990, foreign-born, not a US citizen).

* __S15:__ B05006e1 (Foreign born population, excluding population born at sea); B05006e2 (Europe); B05006e3 (Northern Europe); B05006e13 (Western Europe); B05006e21 (Southern Europe); B05006e28 (Eastern Europe); B05006e47 (Asia); B05006e48 (Eastern Asia); B05006e56 (South Central Asia); B05006e78 (Western Asia); B05006e91 (Africa); B05006e92 (Eastern Africa); B05006e98 (Middle Africa); B05006e101 (Northern Africa); B05006e106 (Southern Africa); B05006e109 (Western Africa); B05006e117 (Oceania); B05006e118 (Oceania, ANZAC subregion); B05006e121 (Oceania, Fiji); B05006e123 (Americas); B05006e124 (Latin America and Caribbean); B05006e125 (Caribbean); B05006e138 (Central America); B05006e148 (South America); B05006e160 (Northern America).

* __S16:__ C16002e1 (Total households); C16002e2 (English only households); C16002e3 (Spanish households); C16002e6 (Other Indo-European languages households); C16002e9 (Asian and Pacific Island languages households); C16002e12 (Other languages households).

* __S17:__ B16004e1 (Population 5 years and over); B16004e2 (5 to 17 years); B16004e3 (5 to 17 years, speak only English); B16004e4 (5 to 17 years, speak Spanish); B16004e5 (5 to 17 years, speak Spanish, speak English 'very well'); B16004e6 (5 to 17 years, speak Spanish, speak English 'well'); B16004e7 (5 to 17 years, speak Spanish, speak English 'not well'); B16004e8 (5 to 17 years, speak Spanish, speak English 'not at all'); B16004e9 (5 to 17 years, speak other Indo-European languages); B16004e10 (5 to 17 years, speak other Indo-European languages, speak English 'very well'); B16004e11 (5 to 17 years, speak other Indo-European languages, speak English 'well'); B16004e12 (5 to 17 years, speak other Indo-European languages, speak English 'not well'); B16004e13 (5 to 17 years, speak other Indo-European languages, speak English 'not at all'); B16004e14 (5 to 17 years, speak Asian and Pacific Island languages); B16004e15 (5 to 17 years, speak Asian and Pacific Island languages, speak English 'very well'); B16004e16 (5 to 17 years, speak Asian and Pacific Island languages, speak English 'well'); B16004e17 (5 to 17 years, speak Asian and Pacific Island languages, speak English 'not well'); B16004e18 (5 to 17 years, speak Asian and Pacific Island languages, speak English 'not at all'); B16004e19 (5 to 17 years, speak other languages); B16004e20 (5 to 17 years, speak other languages, speak English 'very well'); B16004e21 (5 to 17 years, speak other languages, speak English 'well'); B16004e22 (5 to 17 years, speak other languages, speak English 'not well'); B16004e23 (5 to 17 years, speak other languages, speak English 'not at all'); B16004e24 (18 to 64 years); B16004e25 (18 to 64 years, speak only English); B16004e26 (18 to 64 years, speak Spanish); B16004e27 (18 to 64 years, speak Spanish, speak English 'very well'); B16004e28 (18 to 64 years, speak Spanish, speak English 'well'); B16004e29 (18 to 64 years, speak Spanish, speak English 'not well'); B16004e30 (18 to 64 years, speak Spanish, speak English 'not at all'); B16004e31 (18 to 64 years, speak other Indo-European languages); B16004e32 (18 to 64 years, speak other Indo-European languages, speak English 'very well'); B16004e33 (18 to 64 years, speak other Indo-European languages, speak English 'well'); B16004e34 (18 to 64 years, speak other Indo-European languages, speak English 'not well'); B16004e35 (18 to 64 years, speak other Indo-European languages, speak English 'not at all'); B16004e36 (18 to 64 years, speak Asian and Pacific Island languages); B16004e37 (18 to 64 years, speak Asian and Pacific Island languages, speak English 'very well'); B16004e38 (18 to 64 years, speak Asian and Pacific Island languages, speak English 'well'); B16004e39 (18 to 64 years, speak Asian and Pacific Island languages, speak English 'not well'); B16004e40 (18 to 64 years, speak Asian and Pacific Island languages, speak English 'not at all'); B16004e41 (18 to 64 years, speak other languages); B16004e42 (18 to 64 years, speak other languages, speak English 'very well'); B16004e43 (18 to 64 years, speak other languages, speak English 'well'); B16004e44 (18 to 64 years, speak other languages, speak English 'not well'); B16004e45 (18 to 64 years, speak other languages, speak English 'not at all'); B16004e46 (65 years and over); B16004e47 (65 years and over, speak only English); B16004e48 (65 years and over, speak Spanish); B16004e49 (65 years and over, speak Spanish, speak English 'very well'); B16004e50 (65 years and over, speak Spanish, speak English 'well'); B16004e51 (65 years and over, speak Spanish, speak English 'not well'); B16004e52 (65 years and over, speak Spanish, speak English 'not at all'); B16004e53 (65 years and over, speak other Indo-European languages); B16004e54 (65 years and over, speak other Indo-European languages, speak English 'very well'); B16004e55 (65 years and over, speak other Indo-European languages, speak English 'well'); B16004e56 (65 years and over, speak other Indo-European languages, speak English 'not well'); B16004e57 (65 years and over, speak other Indo-European languages, speak English 'not at all'); B16004e58 (65 years and over, speak Asian and Pacific Island languages); B16004e59 (65 years and over, speak Asian and Pacific Island languages, speak English 'very well'); B16004e60 (65 years and over, speak Asian and Pacific Island languages, speak English 'well'); B16004e61 (65 years and over, speak Asian and Pacific Island languages, speak English 'not well'); B16004e62 (65 years and over, speak Asian and Pacific Island languages, speak English 'not at all'); B16004e63 (65 years and over, speak other languages); B16004e64 (65 years and over, speak other languages, speak English 'very well'); B16004e65 (65 years and over, speak other languages, speak English 'well'); B16004e66 (65 years and over, speak other languages, speak English 'not well'); B16004e67 (65 years and over, speak other languages, speak English 'not at all').

* __S18:__ B04007e1 (Total population); B04007e2 (Population with ancestry specified); B04007e3 (Population with single ancestry specified); B04007e4 (Population with multiple ancestry specified); B04007e5 (Population with ancestry not specified); B04006e1 (Total population); B04006e2 (Afghan); B04006e3 (Albanian); B04006e4 (Alsatian); B04006e5 (American); B04006e6 (Arab); B04006e7 (Egyptian Arab); B04006e8 (Iraqi Arab); B04006e9 (Jordanian Arab); B04006e10 (Lebanese Arab); B04006e11 (Moroccan Arab); B04006e12 (Palestinian Arab); B04006e13 (Syrian Arab); B04006e14 (Nondefined Arab); B04006e15 (Other Arab); B04006e16 (Armenian); B04006e17 (Assyrian/Chaldean/Syriac); B04006e18 (Australian); B04006e19 (Austrian); B04006e20 (Basque); B04006e21 (Belgian); B04006e22 (Brazilian); B04006e23 (British); B04006e24 (Bulgarian); B04006e25 (Cajun); B04006e26 (Canadian); B04006e27 (Carpatho Rusyn); B04006e28 (Celtic); B04006e29 (Croatian); B04006e30 (Cypriot); B04006e31 (Czech); B04006e32 (Czechoslovakian); B04006e33 (Danish); B04006e34 (Dutch); B04006e35 (Eastern European); B04006e36 (English); B04006e37 (Estonian); B04006e38 (European); B04006e39 (Fubbusg); B04006e40 (French (except Basque)); B04006e41 (French Canadian); B04006e42 (German); B04006e43 (German Russian); B04006e44 (Greek); B04006e45 (Guyanese); B04006e46 (Hungarian); B04006e47 (Icelander); B04006e48 (Iranian); B04006e49 (Irish); B04006e50 (Israeli); B04006e51 (Italian); B04006e52 (Latvian); B04006e53 (Lithuanian); B04006e54 (Luxemburger); B04006e55 (Macedonian); B04006e56 (Maltese); B04006e57 (New Zealander); B04006e58 (Northern European); B04006e59 (Norwegian); B04006e60 (Pennsylvania German); B04006e61 (Polish); B04006e62 (Portugese); B04006e63 (Romanian); B04006e64 (Russian); B04006e65 (Scandinavian); B04006e66 (Scotch-Irish); B04006e67 (Scotish); B04006e68 (Serbian); B04006e69 (Slavic); B04006e70 (Slovak); B04006e71 (Slovene); B04006e72 (Soviet Union); B04006e73 (Subsaharan African); B04006e74 (Cape Verdean); B04006e75 (Ethiopian); B04006e76 (Ghanaian); B04006e77 (Kenyan); B04006e78 (Liberian); B04006e79 (Nigerian); B04006e80 (Senegalese); B04006e81 (Sierra Leonean); B04006e82 (Somali); B04006e83 (South African); B04006e84 (Sudanese); B04006e85 (Ugandan); B04006e86 (Zimbabwean); B04006e87 (African, general); B04006e88 (Other Subsaharan African); B04006e89 (Swedish); B04006e90 (Swiss); B04006e91 (Turkish); B04006e92 (Ukranian); B04006e93 (Welsh); B04006e94 (West Indian (except Hispanic groups)); B04006e95 (Bahamian); B04006e96 (Barbadian); B04006e97 (Belizean); B04006e98 (Bermudan); B04006e99 (British West Indian); B04006e100 (Dutch West Indian); B04006e101 (Haitian); B04006e102 (Jamaican); B04006e103 (Trinidadian and Tobagonian); B04006e104 (US Virgin Islander); B04006e105 (West Indian, general); B04006e106 (Other West Indian); B04006e107 (Yugoslavian); B04006e108 (Other groups); B04006e109 (Unclassified or not reported).

* __S19:__ B28008e1 (Population in households); B28008e2 (Has a computer); B28008e4 (With a broadband subscription); B28008e9 (Without internet subscription); B28008e10 (No computer); B28010e1 (Total households); B28010e3 (Households with desktop or laptop); B28010e4 (Households with smartphone, tablet, or other portable wireless computer); B28010e5 (Households without a computer); B28011e2 (Households with an internet subscription); B28011e4 (Households with a broadband connection (cable, fiber optic, DSL)); B28011e5 (Households with satellite internet service); B28011e6 (Households without internet access).

<br><br>


#### E: Economic Characteristics (19 groups, 397 fields)

The economic characteristics selected for spatial representation can be found in ACS data tables X8, X17, X19-20, X23-24, and X27. They are divided in 19 subgroups: employment and work status, commuting and travel time to work, vehicles available for workers, means of transportation (age and race), occupation, industry, worker's class, household income and earnings, individual and family income and earnings, health insurance coverage, ratio of income to poverty level, poverty in population, households and families, and poverty income deficit in families estimates.

Code|Name|Universe|Table|Fields|Count
---|---|---|---|---|---:
E01|Employment status|population 16 years and over|X23|B23025|7
E02|Work status by age of worker|population 16 years and over|X23|B23027|36
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

The following fields are included for each of the economic groups:

* __E01:__ B23025e1 (Population 16 years and over); B23025e2 (In labor force); B23025e3 (Civilian labor force); B23025e4 (Civilian labor force, employed); B23025e5 (Civilian labor force, unemployed); B23025e6 (Armed forces); B23025e7 (Not in labor force). 

* __E02:__ B23027e1 (Total population, 16 years and over); B23027e2 (16 to 19 years); B23027e3 (16 to 19 years, worked in the past 12 months); B23027e4 (16 to 19 years, worked full-time, year-round for the past 12 months); B23027e5 (16 to 19 years, worked less than full time, year-round for the past 12 months); B23027e6 (16 to 19 years, did not work for the past 12 months); B23027e7 (20 to 24 years); B23027e8 (20 to 24 years, worked in the past 12 months); B23027e9 (20 to 24 years, worked full-time, year-round for the past 12 months); B23027e10 (20 to 24 years, worked less than full time, year-round for the past 12 months); B23027e11 (20 to 24 years, did not work for the past 12 months); B23027e12 (25 to 44 years); B23027e13 (25 to 44 years, worked in the past 12 months); B23027e14 (25 to 44 years, worked full-time, year-round for the past 12 months); B23027e16 (25 tp 44 years, worked less than full time, year-round for the past 12 months); B23027e16 (25 to 44 years, did not work for the past 12 months); B23027e17 (45 to 54 years); B23027e18 (45 to 54 years, worked in the past 12 months); B23027e19 (45 to 54 years, worked full-time, year-round for the past 12 months); B23027e20 (45 to 54 years, worked less than full time, year-round for the past 12 months); B23027e21 (45 to 54 years, did not work for the past 12 months); B23027e22 (55 to 64 years); B23027e23 (55 to 64 years, worked in the past 12 months); B23027e24 (55 to 64 years, worked full-time, year-round for the past 12 months); B23027e25 (55 to 64 years, worked less than full time, year-round for the past 12 months); B23027e26 (55 to 64 years, did not work for the past 12 months); B23027e27 (65 to 69 years); B23027e28 (65 to 69 years, worked in the past 12 months); B23027e29 (65 to 69 years, worked full-time, year-round for the past 12 months); B23027e30 (65 to 69 years, worked less than full time, year-round for the past 12 months); B23027e31 (65 to 69 years, did not work for the past 12 months); B23027e32 (70 years and over); B23027e33 (70 years and over, worked in the past 12 months); B23027e34 (70 years and over, worked full-time, year-round for the past 12 months); B23027e35 (70 years and over, worked less than full time, year-round for the past 12 months); B23027e36 (70 years and over, did not work for the past 12 months).

* __E03:__ B08301e1 (Workers 16 years and over); B08301e3 (Car, truck, or van - drove alone); B08301e4 (Car, truck, or van - carpooled); B08301e10 (Public transportation (excluding taxicab)); B08301e19 (Walked); B08301e20 (Other means); B08301e21 (Worked at home); B08135e1 (Aggregate travel time to work (minutes)).

* __E04:__ B08012e1 (Total workers 16 years and over who did not work at home); B08012e2 (Less than 5 minutes); B08012e3 (5 to 9 minutes); B08012e4 (10 to 14 minutes); B08012e5 (15 to 19 minutes); B08012e6 (20 to 24 minutes); B08012e7 (25 to 29 minutes); B08012e8 (30 to 34 minutes); B08012e9 (35 to 39 minutes); B08012e10 (40 to 44 minutes); B08012e11 (45 to 59 minutes); B08012e12 (60 to 89 minutes); B08012e13 (90 or more minutes); B08013e1 (Aggregate time to work (in minutes)).

* __E05:__ B08014e1 (Workers 16 years and over in households); B08014e2 (No vehicle available); B08014e3 (1 vehicle available); B08014e4 (2 vehicles available); B08014e5 (3 vehicles available); B08014e6 (4 vehicles available); B08014e7 (5 or more vehicles available); B08015e1 (Aggregate number of vehicles (car, truck or van) used in commuting).

* __E06:__ B08103e1 (Median age, total workers 16 years and over); B08103e2 (Median age, using car, truck or van - drove alone); B08103e3 (Median age, using car, truck or van - carpooled); B08103e4 (Median age, using public transportation); B08103e5 (Median age, walked); B08103e6 (Median age, using taxicab, motorcycle, bicycle, or other means); B08103e7 (Median age, worked at home).

* __E07:__ B08301e1 (Workers, 16 years and over); B08105Ae1 (White alone); B08105Ae2 (White alone, car, truck, or van - drove alone); B08105Ae3 (White alone, car, truck, or van - carpooled); B08105Ae4 (White alone, public transportation); B08105Ae5 (White alone, walked); B08105Ae6 (White alone, taxicab, motorcycle, bicycle, or other means); B08105Ae7 (White alone, worked at home); B08105Be1 (Black or African American alone); B08105Be2 (Black or African American alone, car, truck, or van - drove alone); B08105Be3 (Black or African American alone, car, truck, or van - carpooled); B08105Be4 (Black or African American alone, public transportation); B08105Be5 (Black or African American alone, walked); B08105Be6 (Black or African American alone, taxicab, motorcycle, bicycle, or other means); B08105Be7 (Black or African American alone, worked at home); B08105Ce1 (American Indian and Alaska Native alone); B08105Ce2 (American Indian and Alaska Native alone, car, truck, or van - drove alone); B08105Ce3 (American Indian and Alaska Native alone, car, truck, or van - carpooled); B08105Ce4 (American Indian and Alaska Native alone, public transportation); B08105Ce5 (American Indian and Alaska Native alone, walked); B08105Ce6 (American Indian and Alaska Native alone, taxicab, motorcycle, bicycle, or other means); B08105Ce7 (American Indian and Alaska Native alone, worked at home); B08105De1 (Asian alone); B08105De2 (Asian alone, car, truck, or van - drove alone); B08105De3 (Asian alone, car, truck, or van - carpooled); B08105De4 (Asian alone, public transportation); B08105De5 (Asian alone, walked); B08105De6 (Asian alone, taxicab, motorcycle, bicycle, or other means); B08105De7 (Asian alone, worked at home); B08105Ee1 (Native Hawaiian and Other Pacific Islander alone); B08105Ee2 (Native Hawaiian and Other Pacific Islander alone, car, truck, or van - drove alone); B08105Ee3 (Native Hawaiian and Other Pacific Islander alone, car, truck, or van - carpooled); B08105Ee4 (Native Hawaiian and Other Pacific Islander alone, public transportation); B08105Ee5 (Native Hawaiian and Other Pacific Islander alone, walked); B08105Ee6 (Native Hawaiian and Other Pacific Islander alone, taxicab, motorcycle, bicycle, or other means); B08105Ee7 (Native Hawaiian and Other Pacific Islander alone, worked at home); B08105Fe1 (Some other race alone); B08105Fe2 (Some other race alone, car, truck, or van - drove alone); B08105Fe3 (Some other race alone, car, truck, or van - carpooled); B08105Fe4 (Some other race alone, public transportation); B08105Fe5 (Some other race alone, walked); B08105Fe6 (Some other race alone, taxicab, motorcycle, bicycle, or other means); B08105Fe7 (Some other race alone, worked at home); B08105Ge1 (Two or more races); B08105Ge2 (Two or more races, car, truck, or van - drove alone); B08105Ge3 (Two or more races, car, truck, or van - carpooled); B08105Ge4 (Two or more races, public transportation); B08105Ge5 (Two or more races, walked); B08105Ge6 (Two or more races, taxicab, motorcycle, bicycle, or other means); B08105Ge7 (Two or more races, worked at home); B08105He1 (White alone, not Hispanic or Latino); B08105He2 (White alone, not Hispanic or Latino, car, truck, or van - drove alone); B08105He3 (White alone, not Hispanic or Latino, car, truck, or van - carpooled); B08105He4 (White alone, not Hispanic or Latino, public transportation); B08105He5 (White alone, not Hispanic or Latino, walked); B08105He6 (White alone, not Hispanic or Latino, taxicab, motorcycle, bicycle, or other means); B08105He7 (White alone, not Hispanic or Latino, worked at home); B08105Ie1 (Hispanic or Latino); B08105Ie2 (Hispanic or Latino, car, truck, or van - drove alone); B08105Ie3 (Hispanic or Latino, car, truck, or van - carpooled); B08105Ie4 (Hispanic or Latino, public transportation); B08105Ie5 (Hispanic or Latino, walked); B08105Ie6 (Hispanic or Latino, taxicab, motorcycle, bicycle, or other means); B08105Ie7 (Hispanic or Latino, worked at home).

* __E08:__ C24010e1 (Civilian employed population 16 years and over); C24010e2 (Male); C24010e5 (Male, management occupations); C24010e6 (Male, business and financial operations occupations); C24010e8 (Male, computer and mathematical occupations); C24010e9 (Male, architecture and engineering occupations); C24010e10 (Male, life, physical, and social science occupations); C24010e12 (Male, community and social service occupations); C24010e13 (Male, legal occupations); C24010e14 (Male, education, training, and library occupations); C24010e15 (Male, arts, design, entertainment, sports, and media occupations); C24010e17 (Male, health diagnosing and treating practitioners and other technical occupations); C24010e18 (Male, health technologists and technicians occupations); C24010e20 (Male, healthcare support occupations); C24010e22 (Male, fire fighting and prevention, and other protective service occupations); C24010e23 (Male, law enforcement occupations); C24010e24 (Male, food preparation and serving related occupations); C24010e25 (Male, building and grounds cleaning and meintanence occupations); C24010e26 (Male, personal care and service occupations); C24010e28 (Male, sales and related occupations); C24010e29 (Male, office and administrative support occupations); C24010e31 (Male, farming, fishing, and forestry occupations); C24010e32 (Male, construction and extraction occupations); C24010e33 (Male, installation, maintenance and repair occupations); C24010e35 (Male, production occupations); C24010e36 (Male, transportation occupations); C24010e37 (Male, material moving occupations); C24010e38 (Female); C24010e41 (Female, management occupations); C24010e42 (Female, business and financial operations occupations); C24010e44 (Female, computer and mathematical occupations); C24010e45 (Female, architecture and engineering occupations); C24010e46 (Female, life, physical, and social science occupations); C24010e48 (Female, community and social service occupations); C24010e49 (Female, legal occupations); C24010e50 (Female, education, training, and library occupations); C24010e51 (Female, arts, design, entertainment, sports, and media occupations); C24010e53 (Female, health diagnosing and treating practitioners and other technical occupations); C24010e54 (Female, health technologists and technicians occupations); C24010e56 (Female, healthcare support occupations); C24010e58 (Female, fire fighting and prevention, and other protective service occupations); C24010e59 (Female, law enforcement occupations); C24010e60 (Female, food preparation and serving related occupations); C24010e61 (Female, building and grounds cleaning and meintanence occupations); C24010e62 (Female, personal care and service occupations); C24010e64 (Female, sales and related occupations); C24010e65 (Female, office and administrative support occupations); C24010e67 (Female, farming, fishing, and forestry occupations); C24010e68 (Female, construction and extraction occupations); C24010e69 (Female, installation, maintenance and repair occupations); C24010e71 (Female, production occupations); C24010e72 (Female, transportation occupations); C24010e73 (Female, material moving occupations).

* __E09:__ C24030e1 (Civilian employed population 16 years and over); C24030e2 (Male); C24030e4 (Male, agriculture, forestry, fishing and hunting); C24030e5 (Male, mining, quarrying, and oil and gas extraction); C24030e6 (Male, construction); C24030e7 (Male, manufacturing); C24030e8 (Male, wholesale trade); C24030e9 (Male, retail trade); C24030e11 (Male, transportation and warehousing); C24030e12 (Male, utilities); C24030e13 (Male, information); C24030e15 (Male, finance and insurance); C24030e16 (Male, real estate and rental and leasing); C24030e18 (Male, professional, scientific and technical services); C24030e19 (Male, management of companies and enterprises); C24030e20 (Male, administrative and support and waste management services); C24030e22 (Male, educational services); C24030e23 (Male, health care and social assistance); C24030e25 (Male, arts, entertainment, and recreation); C24030e26 (Male, accommodation and food services); C24030e27 (Male, other services, except public administration); C24030e28 (Male, public administration); C24030e29 (Female); C24030e31 (Female, agriculture, forestry, fishing and hunting); C24030e32 (Female, mining, quarrying, and oil and gas extraction); C24030e33 (Female, construction); C24030e34 (Female, manufacturing); C24030e35 (Female, wholesale trade); C24030e36 (Female, retail trade); C24030e38 (Female, transportation and warehousing); C24030e39 (Female, utilities); C24030e40 (Female, information); C24030e42 (Female, finance and insurance); C24030e43 (Female, real estate and rental and leasing); C24030e45 (Female, professional, scientific and technical services); C24030e46 (Female, management of companies and enterprises); C24030e47 (Female, administrative and support and waste management services); C24030e49 (Female, educational services); C24030e50 (Female, health care and social assistance); C24030e52 (Female, arts, entertainment, and recreation); C24030e53 (Female, accommodation and food services); C24030e54 (Female, other services, except public administration); C24030e55 (Female, public administration).

* __E10:__ B24080e1 (Civilian employed population 16 years and over); B24080e2 (Male); B24080e4 (Male, employee of private company workers); B24080e5 (Male, self-employed in own incorporated business workers); B24080e6 (Male, private not-for-profit wage and salary workers); B24080e7 (Male, local government workers); B24080e8 (Male, state government workers); B24080e9 (Male, federal government workers); B24080e10 (Male, self-employed in own not incorporated business workers); B24080e11 (Male, unpaid family workers); B24080e12 (Female); B24080e14 (Female, employee of private company workers); B24080e15 (Female, self-employed in own incorporated business workers); B24080e16 (Female, private not-for-profit wage and salary workers); B24080e17 (Female, local government workers); B24080e18 (Female, state government workers); B24080e19 (Female, federal government workers); B24080e20 (Female, self-employed in own not incorporated business workers); B24080e21 (Female, unpaid family workers).

* __E11:__ B19001e1 (Total households); B19001e2 (Households, less than $10,000); B19001e3 (Households, $10,000 to $14,999); B19001e4 (Households, $15,000 to $19,999); B19001e5 (Households, $20,000 to $24,999); B19001e6 (Households, $25,000 to $29,999); B19001e7 (Households, $30,000 to $34,999); B19001e8 (Households, $35,000 to $39,999); B19001e9 (Households, $40,000 to $44,999); B19001e10 (Households, $45,000 to $49,999); B19001e11 (Households, $50,000 to $59,999); B19001e12 (Households, $60,000 to $74,999); B19001e13 (Households, $75,000 to $99,999); B19001e14 (Households, $100,000 to $124,999); B19001e15 (Households, $125,000 to $149,999); B19001e16 (Households, $150,000 to $199,999); B19001e17 (Households, $200,000 or more); B19013e1 (Median household income (dollars)); B19025e1 (Aggregate household income (dollars)); B19081e1 (Mean household income of lowest quintile); B19081e2 (Mean household income of second quntile); B19081e3 (Mean household income of third quintile); B19081e4 (Mean household income of fourth quintile); B19081e5 (Mean household income of highest quintile); B19081e6 (Mean household income of top 5 percent); B19083e1 (Gini index of income inequality); B19051e2 (Househols with earnings); B19051e3 (Households without earnings); B19052e2 (Households with wage or salary income); B19053e2 (Households with self-employment income); B19054e2 (Households with interest, dividents, or net rental income); B19055e2 (Households with social security income); B19056e2 (Households with supplemental security income); B19057e2 (Households with public assistance income); B19059e2 (Households with retirement income); B19060e2 (Households with other types of income); B22010e2 (Households received food stamps/SNAP income).

* __E12:__ B19061e1 (Aggregate earnings in households); B19062e1 (Aggregate wage or salary income in households); B19063e1 (Aggregate self-employment income in households); B19064e1 (Aggregate interest, dividents, or net rental income in households); B19065e1 (Aggregate social security income in households); B19066e1 (Aggregate supplemental security income in households); B19067e1 (Aggregate public assistance income in households); B19069e1 (Aggregate retirement income in households); B19069e1 (Aggregate other types of income in household); B19113e1 (Median family income); B19202e1 (Median nonfamily household income); B19214e1 (Aggregate nonfamily household income); B19301e1 (Per capita income (total population)); B19301Ae1 (Per capita income, White alone); B19301Be1 (Per capita income, Black or African American alone); B19301Ce1 (Per capita income, American Indian and Alaska Native alone); B19301De1 (Per capita income, Asian alone); B19301Ee1 (Per capita income, Native Hawaiian and Other Pacific Islander alone); B19301Fe1 (Per capita income, some other race alone); B19301Ge1 (Per capita income, two or more races); B19301He1 (Per capita income, White alone, not Hispanic or Latino); B19301Ie1 (Per capita income, Hispanic or Latino); B19313e1 (Aggregate income (total population)); B20002e1 (Median earnings (total population)); B20002e2 (Median earnings, male population); B20002e3 (Median earnings, female population); B20003e1 (Aggregate earnings (total population)); B20003e2 (Aggregate earnings, male population); B20003e3 (Aggregate earnings, male, worked full-time); B20003e5 (Aggregate earnings, female population); B20003e6 (Aggregate earnings, female, worked full-time).

* __E13:__ B19101e1 (Total families); B19101e2 (Families, less than $10,000); B19101e3 (Families, $10,000 to $14,999); B19101e4 (Families, $15,000 to $19,999); B19101e5 (Families, $20,000 to $24,999); B19101e6 (Families, $25,000 to $29,999); B19101e7 (Families, $30,000 to $34,999); B19101e8 (Families, $35,000 to $39,999); B19101e9 (Families, $40,000 to $44,999); B19101e10 (Families, $45,000 to $49,999); B19101e11 (Families, $50,000 to $59,999); B19101e12 (Families, $60,000 to $74,999); B19101e13 (Families, $75,000 to $99,999); B19101e14 (Families, $100,000 to $124,999); B19101e15 (Families, $125,000 to $149,999); B19101e16 (Families, $150,000 to $199,999); B19101e17 (Families, $200,000 or more).

* __E14:__ B27010e1 (Civilian non-institutionalized population); B27010e2 (Under 19 years); B27010e3 (Under 19 years, with one type of health insurance coverage); B27010e10 (Under 19 years, with two or more types of health insurance coverage); B27010e17 (Under 19 years, without health insurance coverage); B27010e18 (19 to 34 years); B27010e19 (19 to 34 years, with one type of health insurance coverage); B27010e26 (19 to 34 years, with two or more types of health insurance coverage); B27010e33 (19 to 34 years, without health insurance coverage); B27010e34 (35 to 64 years); B27010e35 (35 to 64 years, with one type of health insurance coverage); B27010e42 (35 to 64 years, with two or more types of health insurance coverage); B27010e50 (35 to 64 years, without health insurance coverage); B27010e51 (65 years and over); B27010e52 (65 years and over, with one type of health insurance coverage); B27010e58 (65 years and over, with two or more types of health insurance coverage); B27010e66 (65 years and over, without health insurance coverage).

* __E15:__ C17002e1 (Total population (for whom poverty status id determined)); C17002e2 (Under 0.50); C17002e3 (0.50 to 0.99); C17002e4 (1.00 to 1.24); C17002e5 (1.25 to 1.49); C17002e6 (1.50 to 1.84); C17002e7 (1.84 to 1.99); C17002e8 (2.00 and over).

* __E16:__ B17021e1 (Total population (for whom poverty status is determined)); B17021e2 (Population below poverty level); B17021e3 (Population in family households below poverty level); B17021e4 (Population in married couple family households below poverty level); B17021e8 (Population in male householder, no wife present households below poverty level); B17021e11 (Population in female householder, no husband present households below poverty level); B17021e14 (Population in nonfamily households below poverty level).

* __E17:__ B17017e1 (Total households); B17017e2 (All households below poverty level); B17017e3 (Family households below poverty level); B17017e4 (Married couple family households below poverty level); B17017e10 (Male householder, no wife present households below poverty level); B17017e15 (Female householder, no husband present households below poverty level); B17017e20 (Nonfamily households below poverty level); B17017e21 (Nonfamily households, male householder below poverty level); B17017e26 (Nonfamily households, female householder below poverty level).

* __E18:__ B17010e1 (All families); B17010e2 (All families below poverty level); B17010e3 (Married couple families below poverty level); B17010e4 (Married couple families with related children under 18 years below poverty level); B17010e10 (Male householder, no wife present families below poverty level); B17010e11 (Male householder, no wife present families with related children under 18 years below poverty level); B17010e16 (Female householder, no husband present families below poverty level); B17010e17 (Female householder, no husband present families with related children under 18 years below poverty level).

* __E19:__ B17011e1 (Families below poverty: aggregate income deficit (past 12 months)); B17011e2 (Married couple families below poverty: aggregate income deficit); B17011e4 (Male householder, no wife present below poverty: aggregrate income deficit); B17011e5 (Female householder, no husband present below poverty: aggregate income deficit).

<br><br>

#### H: Housing Characteristics (23 groups, 406 fields)

The housing characteristics selected for spatial representation can by found in ACS data table X25. They are divided into 23 subgroups: housing occupancy, units in struture, housing tenure for population, year built, rooms, bedrooms, tenure by race, tenure by occupancy, vacancy status, occupancy by householder race, other selected housing characteristics, occupants per room, housing value, price asked for housing unit, mortgage status, monthly owner costs (in dollars and as % of income), contract rent and rent asked, gross rent costs (in dollaras and as % of income) estimates.

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

<br>

The following fields are included for each of the housing groups:



* __H01:__ B25002e1 (Total housing units); B25002e2 (Occupied housing units); B25002e3 (Vacant housing units).

* __H02:__ B25024e1 (Total housing units); B25024e2 (1-unit, detatched); B25024e3 (1-unit, attached); B25024e4 (2-units); B25024e5 (3 or 4 units); B25024e6 (5 to 9 units); B25024e7 (10 to 19 units); B25024e8 (20 to 49 units); B25024e9 (50 or more units); B25024e10 (Mobile home); B25024e11 (Boat, RV, van, etc).

* __H03:__ B25033e1 (Total population in occupied housing units); B25033e2 (Population in owner-occupied housing units); B25033e3 (Population in owner-occupied 1 detached or attached housing units); B25033e4 (Population in owner-occupied 2 to 4 housing units); B25033e5 (Population in owner-occupied 5 or more housing units); B25033e6 (Population in owner-occupied mobile home); B25033e7 (Population in owner-occupied boat, RV, van, etc); B25033e8 (Population in renter-occupied housing units); B25033e9 (Population in renter-occupied 1 detached or attached housing units); B25033e10 (Population in renter-occupied 2 to 4 housing units); B25033e11 (Population in renter-occupied 5 or more housing units); B25033e12 (Population in renter-occupied mobile home); B25033e13 (Population in renter-occupied boat, RV, van, etc).

* __H04:__ B25034e1 (Total housing units); B25034e2 (Built 2014 or later); B25034e3 (Built 2010 to 2013); B25034e4 (Built 2000 to 2009); B25034e5 (Built 1990 to 1999); B25034e6 (Built 1980 to 1989); B25034e7 (Built 1970 to 1979); B25034e8 (Built 1960 to 1969); B25034e9 (Built 1950 to 1959); B25034e10 (Built 1940 to 1949); B25034e11 (Built 1939 or earlier); B25035e1 (Median year structure built); B25037e1 (Median year structure built, occupied housing units); B25037e2 (Median year structure built, owner-occupied housing units); B25037e3 (Median year structure built, renter-occupied housing units).

* __H05:__ B25017e1 (Total housing units); B25017e2 (1 room); B25017e3 (2 rooms); B25017e4 (3 rooms); B25017e5 (4 rooms); B25017e6 (5 rooms); B25017e7 (6 rooms); B25017e8 (7 rooms); B25017e9 (8 rooms); B25017e10 (9 rooms or more); B25018e1 (Median number of rooms); B25019e1 (Aggregate number of rooms); B25021e1 (Median number of rooms in occupied housing units); B25021e2 (Median number of rooms in owner-occupied housing units); B25021e3 (Median number of rooms in renter-occupied housing units); B25022e1 (Aggregate number of rooms in occupied housing units); B25022e2 (Aggregate number of rooms in owner-occupied housing units); B25022e3 (Aggregate number of rooms in renter-occupied housing units).

* __H06:__ B25041e1 (Total housing units); B25041e2 (No bedroom); B25041e3 (1 bedroom); B25041e4 (2 bedrooms); B25041e5 (3 bedrooms); B25041e6 (4 bedrooms); B25041e7 (5 or more bedrooms); B25042e (Owner-occupied housing units); B25042e3 (Owner-occupied, no bedroom); B25042e4 (Onwer-occupied, 1 bedroom); B25042e5 (Owner-occupied, 2 bedrooms); B25042e6 (Owner-occupied, 3 bedrooms); B25042e7 (Owner-occupied, 4 bedrooms); B25042e8 (Owner-occupied, 5 or more bedrooms); B25042e9 (Renter-occupied housing units); B25042e10 (Renter-occupied, no bedroom); B25042e11 (Onwer-occupied, 1 bedroom); B25042e12 (Renter-occupied, 2 bedrooms); B25042e13 (Renter-occupied, 3 bedrooms); B25042e14 (Renter-occupied, 4 bedrooms); B25042e15 (Renter-occupied, 5 or more bedrooms).

* __H07:__ B25003e1 (Occupied houging units); B25003e2 (Owner-occupied); B25003e3 (Renter-occuped); B25003Ae1 (Occupied housing units with a householder who is White alone); B25003Ae2 (Owner-occupied housing units with a householder who is White alone); B25003Ae3 (Renter-occupied housing units with a householder who is White alone); B25003Be1 (Occupied housing units with a householder who is Black or African American alone); B25003Be2 (Owner-occupied housing units with a householder who is Black or African American alone); B25003Be3 (Renter-occupied housing units with a householder who is Black or African American alone); B25003Ce1 (Occupied housing units with a householder who is American Indian and Alaska Native alone); B25003Ce2 (Owner-occupied housing units with a householder who is American Indian and Alaska Native alone); B25003Ce3 (Renter-occupied housing units with a householder who is American Indian and Alaska Native alone); B25003De1 (Occupied housing units with a householder who is Asian alone); B25003De2 (Owner-occupied housing units with a householder who is Asian alone); B25003De3 (Renter-occupied housing units with a householder who is Asian alone); B25003Ee1 (Occupied housing units with a householder who is Native Hawaiian and Other Pacific Islander alone); B25003Ee2 (Owner-occupied housing units with a householder who is Native Hawaiian and Other Pacific Islander alone); B25003Ee3 (Renter-occupied housing units with a householder who is Native Hawaiian and Other Pacific Islander alone); B25003Fe1 (Occupied housing units with a householder who is other race alone); B25003Fe2 (Owner-occupied housing units with a householder who is other race alone); B25003Fe3 (Renter-occupied housing units with a householder who is other race alone); B25003Ge1 (Occupied housing units with a householder who is two or more races); B25003Ge2 (Owner-occupied housing units with a householder who is two or more races); B25003Ge3 (Renter-occupied housing units with a householder who is two or more races); B25003He1 (Occupied housing units with a householder who is White alone, not Hispanic or Latino); B25003He2 (Owner-occupied housing units with a householder who is White alone, not Hispanic or Latino); B25003He3 (Renter-occupied housing units with a householder who is White alone, not Hispanic or Latino); B25003Ie1 (Occupied housing units with a householder who is Hispanic or Latino); B25003Ie2 (Owner-occupied housing units with a householder who is Hispanic or Latino); B25003Ie3 (Renter-occupied housing units with a householder who is Hispanic or Latino); B25007e3 (Owner-occupied, householder 15 to 24 years); B25007e4 (Owner-occupied, householder 25 to 34 years); B25007e5 (Owner-occupied, householder 35 to 44 years); B25007e6 (Owner-occupied, householder 45 to 54 years); B25007e7 (Owner-occupied, householder 55 to 59 years); B25007e8 (Owner-occupied, householder 60 to 64 years); B25007e9 (Owner-occupied, householder 65 to 74 years); B25007e10 (Owner-occupied, householder 75 to 84 years); B25007e11 (Owner-occupied, householder 85 years and over); B25007e13 (Renter-occupied, householder 15 to 24 years); B25007e14 (Renter-occupied, householder 25 to 34 years); B25007e15 (Renter-occupied, householder 35 to 44 years); B25007e16 (Renter-occupied, householder 45 to 54 years); B25007e17 (Renter-occupied, householder 55 to 59 years); B25007e18 (Renter-occupied, householder 60 to 64 years); B25007e19 (Renter-occupied, householder 65 to 74 years); B25007e20 (Renter-occupied, householder 75 to 84 years); B25007e21 (Renter-occupied, householder 85 years and over); B25010e1 (Average household size of occupied housing units); B25010e2 (Average household size of owner-occupied housing units); B25010e3 (Average household size of renter-occupied houding units).

* __H08:__ B25008e1 (Total population in occupied housing units); B25008e2 (Population in owner-occupied housing units); B25008e3 (Population in renter-occupied housing units).

* __H09:__ B25004e1 (Total vacant housing units); B25004e2 (For rent); B25004e3 (Rented, not occupied); B25004e4 (For sale only); B25004e5 (Sold, not occupied); B25004e6 (For seasonal, recreational, or occassional use); B25004e7 (For migrant workers); B25004e8 (Other vacant units).

* __H10:__ B25006e1 (Occupied housing units); B25006e2 (Units with White alone householder); B25006e3 (Units with Black or Afican American alone householder); B25006e4 (Units with American Indian and Alaska Native alone householder); B25006e5 (Units with Asian alone householder); B25006e6 (Units with Native Hawaiian and Other Pacific Islander alone householder); B25006e7 (Units with some other race alone householder); B25006e8 (Units with two or more races householder).

* __H11:__ B25038e1 (Occupied housing units); B25038e2 (Owner-occupied housing units); B25038e3 (Owner-occupied, moved in 2015 or later); B25038e4 (Owner-occupied, moved in 2010 to 2014); B25038e5 (Owner-occupied, moved in 2000 to 2009); B25038e6 (Owner-occupied, moved in 1990 to 1999); B25038e7 (Owner-occupied, moved in 1980 to 1989); B25038e8 (Owner-occupied, moved in 1979 or earlier); B25038e9 (Renter-occupied housing units); B25038e10 (Renter-occupied, moved in 2015 or later); B25038e11 (Renter-occupied, moved in 2010 to 2014); B25038e12 (Renter-occupied, moved in 2000 to 2009); B25038e13 (Renter-occupied, moved in 1990 to 1999); B25038e14 (Renter-occupied, moved in 1980 to 1989); B25038e15 (Renter-occupied, moved in 1979 or earlier); B25039e1 (Median year householder moved into occupied housing unit); B25039e2 (Median year householder moved into owner-occupied unit); B25039e3 (Median year householder moved into renter-occupied unit).

* __H12:__ B25044e1 (Occupied housing units); B25044e2 (Owner-occupied housing units); B25044e3 (Owner-occupied, no vehicles available); B25044e4 (Owner-occupied, 1 vehicle available); B25044e5 (Owner-occupied, 2 vehicles available); B25044e6 (Owner-occupied, 3 vehicles available); B25044e7 (Owner-occupied, 4 vehicles available); B25044e8 (Owner-occupied, 5 or more vehicles available); B25044e9 (Renter-occupied housing units); B25044e10 (Renter-occupied, no vehicles available); B25044e11 (Renter-occupied, 1 vehicle available); B25044e12 (Renter-occupied, 2 vehicles available); B25044e13 (Renter-occupied, 3 vehicles available); B25044e14 (Renter-occupied, 4 vehicles available); B25044e15 (Renter-occupied, 5 or more vehicles available); B25046e1 (Aggregate number of vehicles available in occupied housing units); B25046e2 (Aggregate number of vehicles available in owner-occupied housing units); B25046e3 (Aggregate number of vehicles available in renter-occupied housing units).

* __H13:__ B25040e1 (Occupied housing units); B25040e2 (Utility gas); B25040e3 (Bottled, tank, or LP gas); B25040e4 (Electricity); B25040e5 (Fuel oil, kerosene, etc); B25040e6 (Coal or coke); B25040e7 (Wood); B25040e8 (Solar energy); B25040e9 (Other fuel); B25040e10 (No fuel used).

* __H14:__ B25016e1 (Occupied housing units); B25016e2 (Onwer-occupied housing units); B25016e11 (Renter-occupied housing units); B25016e7 (Onwer-occupied, lacking complete plumbing facilities); B25016e16 (Renter-occupied, lacking complete plumbing facilities); B25043e7 (Owner-occupied, no telephone service available); B25043e16 (Renter-occupied, no telephone service available); B25053e4 (Owner-occupied, lacking complete kitchen facilities); B25053e7 (Renter-occupied, lacking complete kitchen facilities).

* __H15:__ B25014e1 (Occupied housing units); B25014e2 (Owner-occupied housing units); B25014e3 (Owner-occupied housing units, 0.5 or less occupants per room); B25014e4 (Owner-occupied housing units, 0.51 to 1.00 occupants per room); B25014e5 (Owner-occupied housing units, 1.01 to 1.50 occupants per room); B25014e6 (Owner-occupied housing units, 1.51 to 2.00 occupants per room); B25014e7 (Owner-occupied housing units, 2.01 or more occupants per room); B25014e8 (Renter-occupied housing units); B25014e9 (Renter-occupied housing units, 0.5 or less occupants per room); B25014e10 (Renter-occupied housing units, 0.51 to 1.00 occupants per room); B25014e11 (Renter-occupied housing units, 1.01 to 1.50 occupants per room); B25014e12 (Renter-occupied housing units, 1.51 to 2.00 occupants per room); B25014e13 (Renter-occupied housing units, 2.01 or more occupants per room).

* __H16:__ B25075e1 (Owner-occupied units); B25075e2 (Less than $10,000); B25075e3 ($10,000 to $14,999); B25075e4 ($15,000 to $19,999); B25075e5 ($20,000 to $24,999); B25075e6 ($25,000 to $29,999); B25075e7 ($30,000 to $34,999); B25075e8 ($35,000 to $39,999); B25075e9 ($40,000 to $49,999); B25075e10 ($50,000 to $59,999); B25075e11 ($60,000 to $69,999); B25075e12 ($70,000 to $79,999); B25075e13 ($80,000 to $89,999); B25075e14 ($90,000 to $99,999); B25075e15 ($100,000 to $124,999); B25075e16 ($125,000 to $149,999); B25075e17 ($150,000 to $174,999); B25075e18 ($175,000 to $199,999); B25075e19 ($200,000 to $249,999); B25075e20 ($250,000 to $299,999); B25075e21 ($300,000 to $399,999); B25075e22 ($400,000 to $499,999); B25075e23 ($500,000 to $749,999); B25075e24 ($750,000 to $999,999); B25075e25 ($1,000,000 to $1,499,999); B25075e26 ($1,500,000 to $1,999,999); B25075e27 ($2,000,000 or more); B25076e1 (Lower value quartile (dollars)); B25077e1 (Median value (dollars)); B25078e1 (Upper value quartile (dollars)); B25079e1 (Aggregate value (dollars)); B25083e1 (Median value (dollars) for mobile homes).

* __H17:__ B25085e1 (Total vacant for-sale only and sold, not occupied housing units); B25085e2 (Less than $10,000); B25085e3 ($10,000 to $14,999); B25085e4 ($15,000 to $19,999); B25085e5 ($20,000 to $24,999); B25085e6 ($25,000 to $29,999); B25085e7 ($30,000 to $34,999); B25085e8 ($35,000 to $39,999); B25085e9 ($40,000 to $49,999); B25085e10 ($50,000 to $59,999); B25085e11 ($60,000 to $69,999); B25085e12 ($70,000 to $79,999); B25085e13 ($80,000 to $89,999); B25085e14 ($90,000 to $99,999); B25085e15 ($100,000 to $124,999); B25085e16 ($125,000 to $149,999); B25085e17 ($150,000 to $174,999); B25085e18 ($175,000 to $199,999); B25085e19 ($200,000 to $249,999); B25085e20 ($250,000 to $299,999); B25085e21 ($300,000 to $399,999); B25085e22 ($400,000 to $499,999); B25085e23 ($500,000 to $749,999); B25085e24 ($750,000 to $999,999); B25085e25 ($1,000,000 to $1,499,999); B25085e26 ($1,500,000 to $1,999,999); B25085e27 ($2,000,000 or more); B25086e1 (Aggregate price asked (dollars)).

* __H18:__ B25081e1 (Owner-occupied units); B25081e2 (Housing units with a mortgage); B25081e7 (Housing units with a mortgage only); B25081e4 (Housing units with a mortgage and a second mortgage); B25081e5 (Housing units with a mortgage and a home equity loan); B25081e6 (Housing units with a mortgage and both a second mortgage and a home equity loan); B25081e8 (Housing units without a mortgage); B25082e1 (Aggregate value (dollars) of owner-occupied units); B25082e2 (Aggregate value (dollars) of housing units with a mortgage); B25082e3 (Aggregate value (dollars) of housing units without a mortgage).

* __H19:__ B25087e1 (Total owner-occupied housing units); B25087e2 (Housing units with a mortgage); B25087e3 (With mortgage, less than $200); B25087e4 (With mortgage, $200 to $299); B25087e5 (With mortgage, $300 to $399); B25087e6 (With mortgage, $400 to $499); B25087e7 (With mortgage, $500 to $599); B25087e8 (With mortgage, $600 to $699); B25087e9 (With mortgage, $700 to $799); B25087e10 (With mortgage, $800 to $899); B25087e11 (With mortgage, $900 to $999); B25087e12 (With mortgage, $1,000 to $1,249); B25087e13 (With mortgage, $1,250 to $1,499); B25087e14 (With mortgage, $1,500 to $1,999); B25087e15 (With mortgage, $2,000 to $2,499); B25087e16 (With mortgage, $2,500 to $2,999); B25087e17 (With mortgage, $3,000 to $3,499); B25087e18 (With mortgage, $3,500 to $3,999); B25087e19 (With mortgage, $4,000 or more); B25087e20 (Housing units without a mortgage); B25087e21 (Without mortgage, less than $100); B25087e22 (Without mortgage, $100 to $149); B25087e23 (Without mortgage, $150 to $199); B25087e24 (Without mortgage, $200 to $249); B25087e25 (Without mortgage, $250 to $299); B25087e26 (Without mortgage, $300 to $349); B25087e27 (Without mortgage, $350 to $399); B25087e28 (Without mortgage, $400 to $499); B25087e29 (Without mortgage, $500 to $599); B25087e30 (Without mortgage, $600 to $699); B25087e31 (Without mortgage, $700 to $799); B25087e32 (Without mortgage, $800 to $899); B25087e33 (Without mortgage, $900 to $999); B25087e34 (Without mortgage, $1,000 to $1,099); B25087e35 (Without mortgage, $1,100 to $1,199); B25087e36 (Without mortgage, $1,200 to $1,299); B25087e37 (Without mortgage, $1,300 to $1,399); B25087e38 (Without mortgage, $1,400 to $1,499); B25087e39 (Without morrgage, $1,500 or more); B25088e1 (Median selected monthly owner costs (dollars) for all owner-occupied housing units); B25088e2 (Median selected monthly owner costs (dollars) for units with a mortgage); B25088e3 (Median selected monthly owner costs (dollars) for units without a mortgage); B25089e1 (Aggregate selected monthly owner costs (dollars) for all owner-occupied housing units); B25089e2 (Aggregate selected monthly owner costs (dollars) for units with a mortgage); B25089e3 (Aggregate selected monthly owner costs (dollars) for units without a mortgage).

* __H20:__ B25091e1 (Owner-occupied housing units); B25091e2 (Housing units with a mortgage); B25091e3 (With mortgage, less than 10.0 percent); B25091e4 (With mortgage, 10.0 to 14.9 percent); B25091e5 (With mortgage, 15.0 to 19.9 percent); B25091e6 (With mortgage, 20.0 to 24.9 percent); B25091e7 (With mortgage, 25.0 to 29.9 percent); B25091e8 (With mortgage, 30.0 to 34.9 percent); B25091e9 (With mortgage, 35.0 to 39.9 percent); B25091e10 (With mortgage, 40.0 to 49.9 percent); B25091e11 (With mortgage, 50.0 percent or more); B25091e12 (With mortgage, not computed); B25091e13 (Housing units without a mortgage); B25091e14 (Without mortgage, less than 10.0 percent); B25091e15 (Without mortgage, 10.0 to 14.9 percent); B25091e16 (Without mortgage, 15.0 to 19.9 percent); B25091e17 (Without mortgage, 20.0 to 24.9 percent); B25091e18 (Without mortgage, 25.0 to 29.9 percent); B25091e19 (Without mortgage, 30.0 to 34.9 percent); B25091e20 (Without mortgage, 35.0 to 39.9 percent); B25091e21 (Without mortgage, 40.0 to 49.9 percent); B25091e22 (Without mortgage, 50.0 percent or more); B25091e23 (Without mortgage, not computed); B25092e1 (Median selected monthly owner costs (dollars) as percentage of household income for all units); B25092e2 (Median selected monthly owner costs (dollars) as percentage of household income for units with a mortgage); B25092e3 (Median selected monthly owner costs (dollars) as percentage of household income for units without a mortgage).

* __H21:__ B25056e2 (Renter-occupied housing units paying cash rent); B25057e1 (Lower contract rent quartile); B25058e1 (Median contract rent); B25059e1 (Upper contract rent quartile); B25060e1 (Aggregate contract rent); B25061e1 (Vacant for rent and rented, not occupied housing units); B25062e1 (Aggregate rent asked).

* __H22:__ B25063e2 (Occupied units paying rent); B25063e3 (Less than $500); B25063e4 ($100 to $149); B25063e5 ($150 to $199); B25063e6 ($200 to $249); B25063e7 ($250 to $299); B25063e8 ($300 to $349); B25063e9 ($350 to $399); B25063e10 ($400 to $449); B25063e11 ($450 to $499); B25063e12 ($500 to $549); B25063e13 ($550 to $599); B25063e14 ($600 to #649); B25063e15 ($650 to $699); B25063e16 ($700 to $749); B25063e17 ($750 to $799); B25063e18 ($800 to $899); B25063e19 ($900 to $999); B25063e20 ($1,000 to $1,249); B25063e21 ($1,250 to $1,499); B25063e22 ($1,500 to $1,999); B25063e23 ($2,000 to $2,499); B25063e24 ($2,500 to $2,999); B25063e25 ($3,000 to $3,499); B25063e26 ($3,500 or more); B25063e27 (No cash rent); B25064e1 (Median gross rent (dollars)); B25065e1 (Aggregate gross rent (dollars)).

* __H23:__ B25070e1 (Occupied units paying rent); B25070e2 (Less than 10.0 percent); B25070e3 (10.0 to 14.9 percent); B25070e4 (15.0 to 19.9 percent); B25070e5 (20.0 to 24.9 percent); B25070e6 (25.0 to 29.9 percent); B25070e7 (30.0 to 34.9 percent); B25070e8 (35.0 to 39.9 percent); B25070e9 (40.0 to 49.9 percent); B25070e10 (50.0 percent or more); B25070e11 (Not computed).

<br><br>

### Geodatabase Feature Class Metadata Description
<br>

Tabulation of level abbreviations by geography and ACS category characteristics. The 3-letter abbreviation consists of: 
* First and Second letter: Geography level (14-levels)
* Third letter: ACS category characteristics (4-levels)

Total abbreviations: 14 georaphies x 4 characteristics = 56 feature class levels (four in each geodatabase).


Geography|Demographic (D)|Social (S)|Economic (E)|Housing (H)
---|:---:|:---:|:---:|:---:
County (CO)|COD|COS|COE|COH
County Subdivision (CS)|CSD|CSS|CSE|CSH
Cities/Places (PL)|PLD|PLS|PLE|PLH
ZIP Code Tabulation Areas (ZC)|ZCD|ZCS|ZCE|ZCH
Congressional Districts (CD)|CDD|CDS|CDE|CDH
State Assembly Legislative Districts (LL)|LLD|LLS|LLE|LLH
State Senate Legislative Districts (UL)|ULD|ULS|ULE|ULH
Elementary School Districts (ED)|EDD|EDS|EDE|EDH
Secondary School Districts (SD)|SDD|SDS|SDE|SDH
Unified School Districts (UD)|UDD|UDS|UDE|UDH
Urban Areas (UA)|UAD|UAS|UAE|UAH
Public Use Microdata Areas (PU)|PUD|PUS|PUE|PUH
Block Groups (BG)|BGD|BGS|BGE|BGH
Census Tracts (TR)|TRD|TRS|TRE|TRH

<br>

<h4 id="CO">Orange County</h4>

<h5>COD: County Demographic Characteristics</h5>

Name|Orange County ACS 2017 (5-year estimates): County Level Demographic Characteristics (ACS2017COD)
:---|:---
Tags|geodemographics; Orange County; California; US Census; ACS; American Community Survey; demographics; age and sex; median age; race; Hispanic or Latino; voting age
Summary|Key demographic characteristics of the 2017 American Community Survey (ACS), 5-year estimates for Orange County, California. The purpose of the dataset is to assist spatial visualization and analysis of basic demographic statistical information in the county. Universe: Total population.
Description | US Census American Community Survey (ACS) 2017, 5-year estimates of the key demographic characteristics for Orange County, California. The layer contains demographic data for tables X01, X02, X03 and X05 of the ACS 2017 (5-year) dataset for Orange County. The US Census geodemographic data are based on the 2017 TigerLines across multiple census geographies. The spatial geographies were merged with ACS demographic data tables. The selected fields contain six table groups: D01 - Sex and age (universe: total population, 49 fields, table X01); D02 - Median age by sex and race (universe: total population, 12 fields, table X1); D03 - Race (universe: total population, 8 fields, table X2); D04 - Race alone or in combination with one or more other races (universe: total population, 7 fields, table X2); D05 - Hispanic or Latino and race (universe: total population, 21 fields, X3); D06 - Citizen voting age population (universe: citizen, 18 years and over population, 8 fields, table X5).
Terms of Use | Original datasets from US Census [TigerLine Geography](https://www.census.gov/geo/maps-data/data/tiger-line.html), and [American FactFinder](https://factfinder.census.gov) for the selected tables of the American Community Survey (ACS, 2017). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey/Geospatial Services, Dr. Kostas Alexandridis, GISP, on December 2019.

<br>
<h5>COS: County Social Characteristics</h5>

Name|Orange County ACS 2017 (5-year estimates): County Level Social Characteristics (ACS2017COD)
:---|:---
Tags|geodemographics; Orange County; California; US Census; ACS; American Community Survey; social characteristics; households; 
Summary|Key demographic characteristics of the 2017 American Community Survey (ACS), 5-year estimates for Orange County, California. The purpose of the dataset is to assist spatial visualization and analysis of basic demographic statistical information in the county. Universe: Total population.
Description | US Census American Community Survey (ACS) 2017, 5-year estimates of the key demographic characteristics for Orange County, California. The layer contains demographic data for tables X01, X02, X03 and X05 of the ACS 2017 (5-year) dataset for Orange County. The US Census geodemographic data are based on the 2017 TigerLines across multiple census geographies. The spatial geographies were merged with ACS demographic data tables. The selected fields contain six table groups: D01 - Sex and age (universe: total population, 49 fields, table X01); D02 - Median age by sex and race (universe: total population, 12 fields, table X1); D03 - Race (universe: total population, 8 fields, table X2); D04 - Race alone or in combination with one or more other races (universe: total population, 7 fields, table X2); D05 - Hispanic or Latino and race (universe: total population, 21 fields, X3); D06 - Citizen voting age population (universe: citizen, 18 years and over population, 8 fields, table X5).
Terms of Use | Original datasets from US Census [TigerLine Geography](https://www.census.gov/geo/maps-data/data/tiger-line.html), and [American FactFinder](https://factfinder.census.gov) for the selected tables of the American Community Survey (ACS, 2017). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey/Geospatial Services, Dr. Kostas Alexandridis, GISP, on December 2019.

<br>
<h5>COE: County Economic Characteristics</h5>


<br>
<h5>COH: County Housing Characteristics</h5>

<br>
<h4 id="CS">County Subdivisions</h4>

<h5>CSD: County Subdivisions Demographic Characteristics</h5>

<br>
<h5>CSS: County Subdivisions Social Characteristics</h5>

<br>
<h5>CSE: County Subdivisions Economic Characteristics</h5>

<br>
<h5>CSH: County Subdivisions Housing Characteristics</h5>


<br>
<h4 id="PL">Cities/Places</h4>

<h5>PLD: Cities/Places Demographic Characteristics</h5>

<br>
<h5>PLS: Cities/Places Social Characteristics</h5>

<br>
<h5>PLE: Cities/Places Economic Characteristics</h5>

<br>
<h5>PLH: Cities/Places Housing Characteristics</h5>


<br>
<h4 id="ZC">ZIP Code Tabulation Areas</h4>

<h5>ZCD: ZIP Code Tabulation Areas Demographic Characteristics</h5>

<br>
<h5>ZCS: ZIP Code Tabulation Areas Social Characteristics</h5>

<br>
<h5>ZCE: ZIP Code Tabulation Areas Economic Characteristics</h5>

<br>
<h5>ZCH: ZIP Code Tabulation Areas Housing Characteristics</h5>


<br>
<h4 id="CD">Congressional Districts</h4>

<h5>CDD: Congressional Districts Demographic Characteristics</h5>

<br>
<h5>CDS: Congressional Districts Social Characteristics</h5>

<br>
<h5>CDE: Congressional Districts Economic Characteristics</h5>

<br>
<h5>CDH: Congressional Districts Housing Characteristics</h5>


<br>
<h4 id="SA">State Assembly Legislative Districts</h4>

<h5>SAD: State Assembly Legislative Districts Demographic Characteristics</h5>

<br>
<h5>SAS: State Assembly Legislative Districts Social Characteristics</h5>

<br>
<h5>SAE: State Assembly Legislative Districts Economic Characteristics</h5>

<br>
<h5>SAH: State Assembly Legislative Districts Housing Characteristics</h5>


<br>
<h4 id="SS">State Senate Legislative Districts</h4>

<h5>SSD: State Senate Legislative Districts Demographic Characteristics</h5>

<br>
<h5>SSS: State Senate Legislative Districts Social Characteristics</h5>

<br>
<h5>SSE: State Senate Legislative Districts Economic Characteristics</h5>

<br>
<h5>SSH: State Senate Legislative Districts Housing Characteristics</h5>


<br>
<h4 id="EE">Elementary School Districts</h4>

<h5>EED: Elementary School Districts Demographic Characteristics</h5>

<br>
<h5>EES: Elementary School Districts Social Characteristics</h5>

<br>
<h5>EEE: Elementary School Districts Economic Characteristics</h5>

<br>
<h5>EEH: Elementary School Districts Housing Characteristics</h5>
