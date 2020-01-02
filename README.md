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




<table>
    <tr>
        <th>Group Characteristic</th>
        <th>Table</th>
        <th>Fields</th>
        <th>Count</th>
    </tr>
    <tr>
        <td colspan="3"><b><a href=#d>Demographic (D)</a></b></td>
        <td align="right"><b>105</b></td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#d01>D01: Sex and age</a></td>
        <td>X1</td>
        <td>B01001</td>
        <td align="right">49</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#d02>D02: Median age by sex and race</a></td>
        <td>X1</td>
        <td>B01002</td>
        <td align="right">12</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#d03>D3: Race</a></td>
        <td>X2</td>
        <td>B02001</td>
        <td align="right">8</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#d04>D4: Race alone or in combination with one or more other races</a></td>
        <td>X2</td>
        <td>B02001, B02008, B02009, B02011, B02012, B02013</td>
        <td align="right">7</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#d05>D05: Hispanic or Latino and race</a></td>
        <td>X3</td>
        <td>B03002</td>
        <td align="right">21</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#d06>D06: Citizen voting age population</a></td>
        <td>X5</td>
        <td>B05003</td>
        <td align="right">8</td>
    </tr><tr>
        <td colspan="3"><b><a href=#s>Social (S)</a></b></td>
        <td align="right"><b>500</b></td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s01>S01: Households by type</a></td>
        <td>X11, X25</td>
        <td>B11001, B11003, B11005, B11007, B25010</td>
        <td align="right">17</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s02>S02: Relationship</a></td>
        <td>X9</td>
        <td>B09019</td>
        <td align="right">19</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s03>S03: Marital status</a></td>
        <td>X12</td>
        <td>B12001</td>
        <td align="right">13</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s04>S04: Fertility</a></td>
        <td>X13</td>
        <td>B13002, B13016</td>
        <td align="right">11</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s05>S05: Grandparents</a></td>
        <td>X10</td>
        <td>B10050, B10056, B10057</td>
        <td align="right">18</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s06>S06: School enrollment</a></td>
        <td>X14</td>
        <td>B14007</td>
        <td align="right">17</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s07>S07: Educational attainment</a></td>
        <td>X15</td>
        <td>B15003</td>
        <td align="right">25</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s08>S08: Veteran status</a></td>
        <td>X21</td>
        <td>B21001</td>
        <td align="right">2</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s09>S09: Disability status and type by sex and age</a></td>
        <td>X18</td>
        <td>B18101, B18102, B18103, B18104, B18105, B18106, B18107</td>
        <td align="right">77</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s10>S10: Disability status by age and health insurance coverage</a></td>
        <td>X18</td>
        <td>B18135</td>
        <td align="right">16</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s11>S11: Residence 1 year ago</a></td>10
        <td>X7</td>
        <td>B07001</td>
        <td align="right">6</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s12>S12: Place of birth</a></td>
        <td>X5</td>
        <td>B05002</td>
        <td align="right">27</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s13>S13: Citizenship status by nativity in the US</a></td>
        <td>X5</td>
        <td>B05001</td>
        <td align="right">6</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s14>S14: Year of entry</a></td>
        <td>X5</td>
        <td>B05005</td>
        <td align="right">21</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s15>S15: World region of birth of foreign-born population</a></td>
        <td>X5</td>
        <td>B05006</td>
        <td align="right">25</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s16>S16: Language spoken in households</a></td>
        <td>X16</td>
        <td>C16002</td>
        <td align="right">6</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s17>S17: Language spoken at home</a></td>
        <td>X16</td>
        <td>B16004</td>
        <td align="right">67</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s18>S18: Ancestry</a></td>
        <td>X4</td>
        <td>B04006</td>
        <td align="right">114</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#s19>S19: Computers and internet use</a></td>
        <td>X28</td>
        <td>B28008, B28010, B28011</td>
        <td align="right">13</td>
    </tr><tr>
        <td colspan="3"><b><a href=#e>Economic (E)</a></b></td>
        <td align="right"><b>397</b></td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e01>E01: Employment status</a></td>
        <td>X23</td>
        <td>B23025</td>
        <td align="right">7</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e02>E02: Work status by age of workers</a></td>
        <td>X23</td>
        <td>B23027</td>
        <td align="right">36</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e03>E03: Commuting to work</a></td>
        <td>X8</td>
        <td>B08301, B08135</td>
        <td align="right">8</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e04>E04: Travel time to work</a></td>
        <td>X8</td>
        <td>B08012, B08013</td>
        <td align="right">14</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e05>E05: Number of vehicles available for workers</a></td>
        <td>X8</td>
        <td>B08014, B08015</td>
        <td align="right">8</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e06>E06: Median age by means of transportation to work</a></td>
        <td>X8</td>
        <td>B08103</td>
        <td align="right">7</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e07>E07: Means of transportation to work by race</a></td>
        <td>X8</td>
        <td>B08105</td>
        <td align="right">64</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e08>E08: Occupation</a></td>
        <td>X24</td>
        <td>C24010</td>
        <td align="right">53</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e09>E09: Industry</a></td>
        <td>X24</td>
        <td>C24030</td>
        <td align="right">43</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e10>E10: Class of worker</a></td>
        <td>X24</td>
        <td>B24080</td>
        <td align="right">19</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e11>E11: Household income and earnings in the past 12 months</a></td>
        <td>X19, X22</td>
        <td>B19001, B19013, B19025, B19081, B19083, B19051-60, B22010</td>
        <td align="right">37</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e12>E12: Income and earnings in dollars</a></td>
        <td>X19, X20</td>
        <td>B19061-69, B19113, B19202, B19214, B19301, B19313, B20002</td>
        <td align="right">31</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e13>E13: Family income in dollars</a></td>
        <td>X19</td>
        <td>B19101</td>
        <td align="right">17</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e14>E14: Health insurance coverage</a></td>
        <td>X27</td>
        <td>B27010</td>
        <td align="right">17</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e15>E15: Ratio of income to poverty level</a></td>
        <td>X17</td>
        <td>C17002</td>
        <td align="right">8</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e16>E16: Poverty in population in the past 12 months</a></td>
        <td>X17</td>
        <td>B17021</td>
        <td align="right">7</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e17>E17: Poverty in households in the past 12 months</a></td>
        <td>X17</td>
        <td>B17017</td>
        <td align="right">9</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e18>E18: Percentage of families and people whose income in the past 12 months is below the poverty level</a></td>
        <td>X17</td>
        <td>B17010</td>
        <td align="right">8</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#e19>E19: Poverty and income deficit (dollars) in the past 12 months for families</a></td>
        <td>X17</td>
        <td>B17011</td>
        <td align="right">4</td>
    </tr><tr>
        <td colspan="3"><a href=#h><b>Housing (H)</b></a></td>
        <td align="right"><b>406</b></td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h01>H01: Housing occupancy</a></td>
        <td>X25</td>
        <td>B25002</td>
        <td align="right">3</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h02>H02: Units in structure</a></td>
        <td>X25</td>
        <td>B25024</td>
        <td align="right">11</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h03>H03: Population in occupied housing units by tenure by units in structure</a></td>
        <td>X25</td>
        <td>B25033</td>
        <td align="right">13</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h04>H04: Year structure built</a></td>
        <td>X25</td>
        <td>B25034-35, B25037</td>
        <td align="right">15</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h05>H05: Rooms</a></td>
        <td>X25</td>
        <td>B25017-19, B25021-22</td>
        <td align="right">18</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h06>H06: Bedrooms</a></td>
        <td>X25</td>
        <td>B25041-42</td>
        <td align="right">21</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h07>H07: Housing tenure by race of householder</a></td>
        <td>X25</td>
        <td>B25003, B25007, B25010</td>
        <td align="right">51</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h08>H08: Total population in occupied housing units by tenure</a></td>
        <td>X25</td>
        <td>B25008</td>
        <td align="right">3</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h09>H09: Vacancy status</a></td>
        <td>X25</td>
        <td>B25004</td>
        <td align="right">8</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h10>H10: Occupied housing units by race of householder</a></td>
        <td>X25</td>
        <td>B25006</td>
        <td align="right">8</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h11>H11: Year householder moved into unit</a></td>
        <td>X25</td>
        <td>B25038-39</td>
        <td align="right">18</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h12>H12: Vehicles available</a></td>
        <td>X25</td>
        <td>B25044, B25046</td>
        <td align="right">18</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h13>H13: House heating fuel</a></td>
        <td>X25</td>
        <td>B25040</td>
        <td align="right">10</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h14>H14: Selected characteristics</a></td>
        <td>X25</td>
        <td>B25016, B25043, B25053</td>
        <td align="right">9</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h15>H15: Occupants per room</a></td>
        <td>X25</td>
        <td>B25014</td>
        <td align="right">13</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h16>H16: Housing value</a></td>
        <td>X25</td>
        <td>B25075-79, B25083</td>
        <td align="right">32</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h17>H17: Price asked for vacant for-sale only, and sold, not occupied housing units</a></td>
        <td>X25</td>
        <td>B25085-86</td>
        <td align="right">28</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h18>H18: Mortgage status</a></td>
        <td>X25</td>
        <td>B25081-82</td>
        <td align="right">10</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h19>H19: Selected monthly owner costs (SMOC)</a></td>
        <td>X25</td>
        <td>B25087-89</td>
        <td align="right">45</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h20>H20: Selected monthly owner costs as a percentage of household income (SMOCAPI)</a></td>
        <td>X25</td>
        <td>B25091-92</td>
        <td align="right">26</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h21>H21: Contract rent distribution and rent asked distribution in dollars</a></td>
        <td>X25</td>
        <td>B25056-62</td>
        <td align="right">7</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h22>H22: Gross rent</a></td>
        <td>X25</td>
        <td>B25063-65</td>
        <td align="right">28</td>
    </tr><tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href=#h23>H23: Gross rent as percentage of household income</a></td>
        <td>X25</td>
        <td>B25070</td>
        <td align="right">11</td>
    </tr>
</table>

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


