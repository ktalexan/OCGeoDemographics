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
X07 | Migration | Migration, geographical mobility, residence and emigration information tables.
X08 | Commuting | Commutting patterns from/to work and other relevant characteristics of participants.
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
X21 | Veteran Status | Veteran status by type of veteran, age and other demographic characteristics.
X22 | Food Stamps |
X23 | Employment Status | Employment and unemployment status and characteristics for the sampled population.
X24 | Industry and Occupation | Participant industry and occupational codes (NAICS codes)
X25 | Housing Characteristics |
X26 | Group Quarters |
X27 | Health Insurance |
X28 | Computer and Internet Use | Use of computers and internet use for the sampled population. Most data does not exist for the sample. Excluded from analysis.
X98 | Unweighted Housing Unit Sample | Housing unit sample unweighted. Excluded from analysis.
X99 | Imputation | Imputation flags for statistical tables. Excluded from analysis.


<br><br>

### Fields and Execution Times

Table|BG|CD115|COUNTY|COUSUB|PLACE|PUMA|SDE|SDS|SDU|SLDL|SLDU|TRACT|UA|ZCTA
:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:
COUNTS|4|4|4|4|4|4|4|4|4|4|4|4|4|4
X01|160|718|718|718|718|718|718|718||||||
X02|68|420|420|420|420|420|420|420||||||
X03|48|110|110|110|110|110|110|110||||||
X04|_|664|664|664|664|664|664|664||||||
X05|_|1,692|1,692|1,692|1,692|1,692|1,540|1,540||||||
X06|_|1,220|1,220|1,220|1,220|1,220|610|610||||||
X07|150|1,782|3,082|2,432|3,082|1,782|886|886||||||
X08|580|2,540|4,454|4,454|4,454|2,540|2,540|2,540||||||
X09|230|312|312|312|312|312|312|312||||||
X10|628|372|372|372|372|372|372|372||||||
X11|_|744|744|744|744|744|744|744||||||
X12|38|758|758|758|758|758|758|758||||||
X13|_|402|402|402|402|402|402|402||||||
X14|536|778|778|778|778|778|778|778||||||
X15|346|710|710|710|710|710|710|710||||||
X16|162|870|870|870|870|870|870|870||||||
X17|296|3,940|3,940|3,940|3,940|3,940|3,940|3,940||||||
X18|_|892|892|892|892|892|892|892||||||
X19|400|2,968|2,968|2,968|2,968|2,968|2,968|2,968||||||
X20|116|2,152|2,152|2,152|2,152|2,152|2,152|2,152|||||
X21|172|564|564|564|564|564|564|564||||||
X22|14|242|242|242|242|242|242|242||||||
X23|662|1,624|1,624|1,624|1,624|1,624|1,624|1,624||||||
X24|678|2,106|2,106|2,106|2,106|2,106|2,106|2,106||||||
X25|1,738|4,410|4,410|4,410|4,410|4,410|4,410|4,410||||||
X26|_|2|2|2|2|2|2|||||||
X27|132|1,502|1,502|1,502|1,502|1,502|1,502|||||||
X28|_|_|_|_|_|_|_|||||||
X98|_|_|24|_|4|_|_|||||||
X99|532|718|746|746|746|718|704|||||||
TOTAL|7,690|35,216|38,482|37,808|38,462|35,216|33,544|||||||
ExecTime|1:48:43|18:50:30|23:21:07|22:35:30|23:10:17|18:42:47|17:47:56|||||||




### Description


List of variables


Group Characteristics||Fields
---|---|---:
|**Demographics**||**105**
||D01: Sex and Age|49



<table>
    <thead>
            <th colspan = "2">Group Characteristic</th>
            <th>Number of fields</th>
    </thead>
    <tbody>
        <tr>
            <td colspan = "2"><b>Demographic (D)</b></th>
            <td><b>105</b></td>
        </tr><tr>
            <td></td>
            <td>D01: Sex and Age</td>
            <td>49</td>
    </tbody>
</table>


### 1. Demographic Characteristics (D)

<table>
    <th>
        <thead>
            <th>Code</th>
            <th>Name</th>
            <th>Universe</th>
            <th>Table</th>
            <th>Vars</th>
            <th>No</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>D01</td>
            <td>Sex and age</td>
            <td>total population</td>
            <td>X01</td>
            <td>B01001</td>
            <td>49</td>
        </tr><tr>
            <td>D02</td>
            <td>Race</td>
            <td>total population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>D03</td>
            <td>Race alone, or in combination with one or more other races</td>
            <td>total population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>D04</td>
            <td>Hispanic or Latino and race</td>
            <td>total population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>D05</td>
            <td>Citizen voting age population</td>
            <td>citizen, 18 and over population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>


### 2. Social Characteristics (S)


<table>
    <th>
        <thead>
            <th>Code</th>
            <th>Name</th>
            <th>Universe</th>
            <th>Table</th>
            <th>Vars</th>
            <th>No</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>S01</td>
            <td>Households by type</td>
            <td>total households</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S02</td>
            <td>Relationship</td>
            <td>population in households</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S03</td>
            <td>Marital status</td>
            <td>males or females 15 years and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S04</td>
            <td>Fertility</td>
            <td>number of women 15 to 50 years old who had a birth in the past 12 months</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S05</td>
            <td>Grandparents</td>
            <td>number of grandparents living or responsible for own grandchildren under 18 years</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S06</td>
            <td>School enrollment</td>
            <td>population 3 years and over enrolled in school</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S07</td>
            <td>Educational attainment</td>
            <td>population 25 years and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S08</td>
            <td>Veteran status</td>
            <td>civilian population 18 years and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S09</td>
            <td>Disability status</td>
            <td>total civilian non-institutionalized population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S10</td>
            <td>Residence 1 year ago</td>
            <td>population 1 year and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S11</td>
            <td>Place of birth</td>
            <td>total population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S12</td>
            <td>US citizenship status</td>
            <td>foreign-born population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S13</td>
            <td>Year of entry</td>
            <td>population born outside the US</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S14</td>
            <td>World region of birth of foreign born population</td>
            <td>foreign-born population, excluding population born at sea</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S15</td>
            <td>Language spoken at home</td>
            <td>population 5 years and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S16</td>
            <td>Ancestry</td>
            <td>total population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>S17</td>
            <td>Computers and internet</td>
            <td>total households</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
    </tbody>
</table>




### 3. Economic Characteristics (E)


<table>
    <th>
        <thead>
            <th>Code</th>
            <th>Name</th>
            <th>Universe</th>
            <th>Table</th>
            <th>Vars</th>
            <th>No</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>E01</td>
            <td>Employment status</td>
            <td>population 16 years and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>E02</td>
            <td>Commuting to work</td>
            <td>workers 16 years and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>E03</td>
            <td>Occupation</td>
            <td>civilian employed population 16 years and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>E04</td>
            <td>Industry</td>
            <td>civilian employed population 16 years and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>E05</td>
            <td>Class of worker</td>
            <td>civilian employed population 17 years and over</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>E06</td>
            <td>Income and benefits</td>
            <td>total households, families, nonfamilies, workers</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>E07</td>
            <td>Health insurance coverage</td>
            <td>civilian non-institutional population, families, total population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>E08</td>
            <td>Percentage of families and people whose income in the past 12 months is below the poverty level</td>
            <td>families, population</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
    </tbody>
</table>




### 4. Housing Characteristics (H)


<table>
    <th>
        <thead>
            <th>Code</th>
            <th>Name</th>
            <th>Universe</th>
            <th>Table</th>
            <th>Vars</th>
            <th>No</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>H01</td>
            <td>Housing occupancy</td>
            <td>total housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H02</td>
            <td>Units in structure</td>
            <td>total housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H03</td>
            <td>Year structure built</td>
            <td>total housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H04</td>
            <td>Rooms</td>
            <td>total housubg units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H05</td>
            <td>Bedrooms</td>
            <td>total housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H06</td>
            <td>Housing tenure</td>
            <td>occupied housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H07</td>
            <td>Year householder moved into unit</td>
            <td>occupied housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H08</td>
            <td>Vehicles available</td>
            <td>occupied housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H09</td>
            <td>House heating fuel</td>
            <td>occupied housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H10</td>
            <td>Selected housing characteristics</td>
            <td>occupied housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H11</td>
            <td>Occupants per room</td>
            <td>occupied housing units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H12</td>
            <td>Housing value</td>
            <td>owner-occupied units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H13</td>
            <td>Mortgage status</td>
            <td>owner-occupied units</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H14</td>
            <td>Selected monthly owner costs (SMOC)</td>
            <td>housing units with or without a mortgage</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H15</td>
            <td>Selected monthly owner costs as a percentage of household income (SMOCAPI)</td>
            <td>housing units with or without a mortgage</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H16</td>
            <td>Gross rent</td>
            <td>occupied units paying rent</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
            <td>H17</td>
            <td>Gross rent as a percentage of household income</td>
            <td>occupied units paying rent</td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr><tr>
    </tbody>
</table>





