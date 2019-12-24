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


**SOCIAL CHARACTERISTICS**
1. Households by Type (*total households*)
2. Relationship (*population in households*)
3. Marital Status (*males or femalse 15 years and over*)
4. Fertility (*number of women 15 to 50 years old who had a birth in the past 12 months*)
5. Grandparents (*number of grandparents living or responsible for own grandchildren under 18 years*)
6. School Enrollment (*population 3 years and over enrolled in school*)
7. Educational Attainment (*population 25 years and over*)
8. Veteran Status (*civilian population 18 years and over*)
9. Disability Status (*total civilian non-institutionalized populations*)
10. Residence 1 Year Ago (*population 1 year and over*)
11. Place of Birth (*total population*)
12. US Citizenship Status (*foreign-born population*)
13. Year of Entry (*popultion born outside the United States*)
14. Wirkd Region of Birth of Foreign Born Population (*foreign-born population, excluding population born at sea*)
15. Language Spoken at Home (*Population 5 years and over*)
16. Ancestry (*Total population*)
17. Computers and Internet Use (*total households*)


**ECONOMIC CHARACTERISTICS**
1. Employment Status (*total households*)
2. Commuting to Work (*workers 16 years and over*)


**1. SOCIAL CHARACTERISTICS**

**1.1. Households by Type**
* Universe: total households

Variable|Name
---|---
B11001e1|Total households
B11001e2|Family households (families)
B11003e1|Family households with own children of the householder under 18 years
B11001e3|Married-couple family households
B11003e3|Married-couple family households with own children of the householder under 18 years
B11001e5|Male householder, no wife present, family households
B11003e10|Male householder, no wife present, family households with own children of the householder under 18 years
B11001e6|Female householder, no husband present, family households
B11003e16|Female householder, no husband present, family households with own children of the householder under 18 years
B11001e7|Nonfamily households
B11001e8|Nonfamily households, householder living alone
B|Nonfamily households, householder living alone, 65 years and over
B11005e2|Households with one or more people under 18 years
B11007e2|Households with one or more people 65 years and over
B|Average household size
B|Average family size


