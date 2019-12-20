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
X01|160|718|718|718|718|||||||||
X02|68|420|420|420|420|||||||||
X03|48|110|110|110|110|||||||||
X04|_|664|664|664|664|||||||||
X05|_|1,692|1,692|1,692|1,692|||||||||
X06|_|1,220|1,220|1,220|1,220|||||||||
X07|150|1,782|3,082|2,432|3,082|||||||||
X08|580|2,540|4,454|4,454|4,454|||||||||
X09|230|312|312|312||||||||||
X10|628|372|372|372||||||||||
X11|_|744|744|744||||||||||
X12|38|758|758|758||||||||||
X13|_|402|402|402||||||||||
X14|536|778|778|778||||||||||
X15|346|710|710|710||||||||||
X16|162|870|870|870||||||||||
X17|296|3,940|3,940|3,940||||||||||
X18|_|892|892|892||||||||||
X19|400|2,968|2,968|2,968||||||||||
X20|116|2,152|2,152|2152|||||||||
X21|172|564|564|564||||||||||
X22|14|242|242|242||||||||||
X23|662|1,624|1,624|1,624||||||||||
X24|678|2,106|2,106|2,106||||||||||
X25|1,738|4,410|4,410|4,410||||||||||
X26|_|2|2|2||||||||||
X27|132|1,502|1,502|1,502||||||||||
X28|_|_|_|_||||||||||
X98|_|_|24|_||||||||||
X99|532|718|746|746||||||||||
TOTAL|7,690|35,216|38,482|37,808||||||||||
ExecTime|1:48:43|18:50:30|23:21:07|22:35:30||||||||||

### Description

**SOCIAL CHARACTERISTICS**

A. HOUSEHOLDS BY TYPE
  1. Total households
     i. Family households (families)
       a. with own children of the householder under 18 years
         2. 
     ii. Married-couple family