# Detect  Leaks  in  the  Urbana  and  Champaign  Sewage  Collection  System

Organization  Name:  Urbana  &  Champaign  Sanitary  District  

# Local  Sponsor:  
Jackie  Christensen,  Director  of  Operations,  Urbana  &  Champaign  Sanitary  District 

# Overview:
The  mission  of  the  Urbana  &  Champaign  Sanitary  District  (UCSD)  is  to  protect  public  health  and  safety,  preserve  the  public  trust,  and  protect  the  natural  environment.  UCSD  is  a  municipal  body  which  provides  wastewater  treatment  for  properties  in  the  Cities  of  Urbana  and  Champaign,  the  Villages  of  Bondville  and  Savoy,  the  University  of  Illinois  and  the  surrounding  adjacent  developed  areas.  

UCSD  operates  two  wastewater  treatment  plants.  The  Northeast  plant  is  located  in  Urbana  immediately  north  of  Ambucs  Park.  The  Southwest  plant  is  located  in  Champaign  at  the  intersection  of  Windsor  and  Rising  Roads.  UCSD  also  operates  large  diameter  sanitary  interceptor  sewers  and  28  pumping  stations  that  transport  wastewater  to  the  treatment  plants.  Champaign,  Urbana,  Savoy  and  the  University  of  Illinois  operate  their  respective  collector  sewers  to  which  homes  and  businesses  are  connected.

# Problem  Statement:
Inflow  and  infiltration  (referred  to  as  I&I)  is  when  groundwater  and  stormwater  enter  the  sanitary  sewer  through  leaks  in  the  piping  and  connections.      When  groundwater  and  stormwater  enter  the  sewage  collection  system  as  I&I,  it  must  be  sent  to  the  wastewater  treatment  plant  along  with  the  actual  wastewater  generated  within  the  community.    Due  to  I&I,  wastewater  treatment  plants  end  up  treating  much  higher  volumes  of  wastewater  than  they  otherwise  would,  leading  to  higher  energy  consumption  and  costs.    During  a  particularly  large  storm,  the  increased  flow  reaching  a  treatment  plant  due  to  I&I  may  even  exceed  the  treatment  plant’s  capacity.  Under  such  circumstances,  untreated  wastewater  may  be  discharged  into  the  environment.  

By  detecting  and  fixing  leaks  in  the  sewage  collection  system,  one  can  eliminate  the  energy  consumed  in  pumping  and  treating  groundwater  and  stormwater  that  enters  the  sewage  collection  system,  and  that  otherwise  would  not  require  treatment.      Furthermore,  if  I&I  were  significantly  reduced,  wastewater  treatment  plants  could  plan  to  use  more  of  their  treatment  capacity  for  treating  wastewater,  rather  than  a  combination  of  wastewater  and  I&I,  and  thus  service  greater  populations  with  existing  treatment  infrastructure.    However,  identification  of  leaks  in  underground  piping  is  difficult  and  costly  using  currently  available  technologies.    

For  this  problem  we  encourage  teams  to  develop  innovative  ways  to  identify  areas  of  potential  I&I  in  the  UCSD  sewage  collection  system,  using  historical  plant  flow  data,  lift  station  flow  data,  and  precipitation  data.    For  this  challenge  we  will  focus  on  the  UCSD  NE  plant,  and  assume  that  similar  techniques  would  work  for  the  UCSD  SW  plant  (where  similar  data  is  available).  In  addition  to  historical  flow  data,  we  have  provided  basin  maps  to  understand  the  flow  of  lift  stations  into  other  lift  stations,  and  ultimately  into  the  NE  plant.    The  goal  of  this  challenge  will be  to  identify  the  specific  lift  stations  where  the  most  I&I  is  entering  during  a  rainstorm  event.    The  results  of  this  challenge  which  will  help  guide  where  money  should  be  spent  for  collection  system  repair.   

# North East  Plant  LIFT  Stations: 
Lift  stations  are  located  throughout  the  sewage  collection  system,  and  represent  points  in  the  collection  system  where  water  is  pumped  and  moved  towards  the  treatment  plant.    Data  is  collected  at  lift  stations,  including  pump  status,  liquid  level,  and  daily  flow  rates.    Given  that  data  is  available  at  lift  stations,  but  not  at  other  points  in  the  collection  system,  this  problem  focuses  on  identifying  lift  stations  where  the  most  I&I  is  entering.    By  identifying  these  lift  stations,  we  can  focus  our  leak  detection  /  remediation  efforts  on  the  subsections  of  the  collections  system  that  feed  into  these  lift  stations.    Below  is  a  list  of  the  lift  stations  within  the  NE  Plant  basin.    Sewage  from  certain  lift  stations  will  flow  through  another  lift  station  prior  to  entering  the  NE  Plant,  which  is  also  indicated  in  the  list  below.     

1.  Bradley-McKinley 
2.  Staley 
3.  Freshville
4.  I-74 -> LELS  
5.  Timber  Hills ->  Broadway
6.  O.L.  Johnson ->  LELS 
7.  Perkins ->  LELS  
8.  Locust  Street  
9.  Broadway 
10.  Carle  Park
11.  Vine 
12.  Amvets 
13.  East  Main 
14.  Mumford 
15.  Myra  
16.  Race  Street -> Half  to  Myra  &  half  to  Amvets  
17.  South  Ridge ->  Myra
18.  LELS

# Evaluation  criteria:
1. Appropriateness  of  analytics  techniques  used  to  solve  the  problem.
2. Were  lift  stations  where  the  most  I&I  is  entering  during  a  rainstorm  identified?    With  what  level  of  confidence?
3. How  robust  is  the  solution  in  the  presence  of  imperfect  data  (does  it  work  well  even  if  data  is  missing  /  data      has  uncertainty  /  is  at  the  day-level  rather  than  more  granular)?
4. Were  results  explained  in  a  way  that  is  helpful  to  UCSD  /  City officials?

# Datasets: 
Please find the datasets uploaded as xlsx/csv files in the repository. Below is a list of the datasets and columns in each datasets.

# 1. NE  Plant  Flow  Data: 

A. Filename: NEPinfluent_dailyflow.xlsx
*  Month 
*  Day  
*  Year 
*  Total  Influent  Flow  [MGD  =  Million  Gallons  Per  Day] 
*  Note:  The  flow  shown  in  this  dataset  is  the  actual  total  daily  wastewater  (i.e.,  influent)  flow  entering  the  NE     
   Plant. 

B. Filename: NEPinfluent_instantflow.csv
*  Date 
*  Time 
*  Total  Influent  Flow  [MGD  =  Million  Gallons  Per  Day]  
*  Note  1:  The  flow  shown  in  this  dataset  is  the  instantaneous  wastewater  (i.e.,  influent)  flow  entering  the  NE  Plant,    which  is  defined  at  the  wastewater  flow  entering  the  NE  Plant  at  that  specific  point  in  time.   
*  Note  2:  For  those  who  are  wondering,  the  units  for  daily  influent  flow  and  instantaneous  flow  are  the  same.     
   Daily  flow  is  the  actual  volume  of  influent  received  on  a  particular  day  at  the  NE  Plant,  instantaneous  flow  is  a    measure  of  what  the  volume  received  would  have  been  if  the  instantaneous  flow  rate  were  sustained  over  a  24-hour      period.  

# 2. LIFT  Station  Data:  

A. Filename: NEPlift_dailyflow.xlsx
*  Date
*  Each  following  column  represents  the  daily  wastewater  flow  at  that  lift  station  [gallons/day]  
*  Note:  Daily  wastewater  flow  values  of  zero  are  errors  and  should  be  considered  as  not  available. 

B. Filename: NEPlift_data.csv 
*  Date    
*  Time   
*  Millitm 
*  Each  following  column  represents  pump  status  or  liquid  level  for  the  following  lift  stations:  Broadway,  Myra,  I-74,   
   Locust  Street  and  Race  Street  
    *  Pump  Status  for  Each  Pump  at  a  Lift  Station  [1  =  ON  &  0  =  OFF] 
    *  Liquid  Level  [the  wastewater  liquid  level  in  each  lift  station  measured  in  feet] 
*  Note  1:  To  determine  the  pump  flow  rate  at  a  given  lift  station,  one  must  look  at  how  many  pumps  are  running  at    each  lift  station  and  match  with  the  pump  capacity  chart  shown  in NEPlift_pumpcapacity.xlsx excel  spreadsheet.  
*  Note  2:  Only  give  NE  Plant  lift  stations  have  pump  status  and  level  data,  whereas,  almost  all  NE  Plant  lift   
   stations  have  daily  wastewater  flow  data.    

C. Filename: NEPlift_pumpcapacity.xlsx 
*  Lift  Station  Name  
*  Pump  Capacity  [GPM  =  Gallons  Per  Minute] 
*  Note:  Pump  capacity  at  a  lift  station  changes  depending  on  whether  1,  2,  or  3  pumps  are  running,  as  shown  in  the    excel  sheet.Where  there  are  blanks  in  the  third  pump  column,  it  means  there  is  not  third  pump  at  that  lift    
   station.

# 3. NOAA  Weather  Data:

A. Filename:  NOAA.csv 
*  Station  ID
*  Station  Name  
*  Latitude  
*  Longitude  
*  Elevation  
*  Date  
*  PCRP  [daily  precipitation  in  inches]  
*  Note:  Data  for  the  7  NOAA  weather  stations  in  the  NE  Plant  basin  are  provided. 

# 4. USGS  Rain  Gage  Data: 

A. Boneyard  Creek  Rain  Gage  (a  link  to  the  tsv  file  has  been  provided below)

Dataset link: 

https://waterdata.usgs.gov/nwis/dv?cb_00045=on&cb_00060=on&cb_00065=on&format=rdb&site_no=03337000&referred_module=sw&period=&begin_date=2012-01-01&end_date=2018-09-20

*  Agency  
*  Site  Number  
*  Datetime 
*  Time  zone  
*  Discharge  in  Boneyard  Creek  [cubic  feet  per  second]  /  Approval  Status 
   Note: The discharge is the flow of water in the Boneyard Creek where the raingage is located.
*  Gage  Height  [feet]  /  Approval  Status  
*  Total  Precipitation  [inches]  /  Approval  Status  Approval  Status:  A  =  approved,  P  =  provisional,  e  =  value  is     
   estimated  South  Side  Elementary  School  Rain  Gage  (a  link  to  the  tsv  file  has  been  provided)  
*  Agency 
*  Site  Number  
*  Datetime  
*  Time  zone 
*  Total  Precipitation  [inches]  /  Approval  Status  
   Approval  Status:  A  =  approved,  P  =  provisional,  e  =  value  is  estimated  

B. South  Side  Elementary  School  Rain  Gage (a  link  to  the  tsv  file  has  been  provided below)

Dataset link:

https://nwis.waterdata.usgs.gov/il/nwis/uv/?begin_date=2012-01-01&cb_00045=on&end_date=2018-09-24&format=rdb&period=&site_no=400620088151801

*  Agency 
*  Site  Number 
*  Datetime 
*  Time  zone 
*  Total  Precipitation  [inches]  /  Approval  Status
   Approval  Status:  A  =  approved,  P  =  provisional,  e  =  value  is  estimated

# 5. MAPS:
Please find the pdf map files in the repository. 

A. Filename: LIFT  Station Map_Marked.pdf

This  basin  map  shows  the  locations  of  all  the  lift  stations  in  the  UCSD  service  area.    The  NE  Plant  lift  stations  are  highlighted  in  purple  and  yellow.    Lift  stations  highlighted  in  purple  send  their  flow  directly  to  the  NE  Plant,  the  ones  highlighted  in  yellow  send  flow  to  another  lift  station  first  (as  indicated  in  red),  and  from  that  lift  station  the  flow  ultimately  reaches  the  NE  Plant.

B. Filename:  LIFT  Station  and  Interceptor Map.pdf

This  is  a  detailed  basin  map  showing  the  locations  of  all  lift  stations  and  lift  stations  in  the  UCSD  service  area.

C. Filename:  NOAA  Weather Station Map.pdf 

This  is  a  map  showing  the  locations  of  the  NOAA  weather  stations  in  the  UCSD  service  area.    The  weather  stations  marked  in  green  are  in  the  NE  Plant  service  area.

# Final  Note:

The  day-level  datasets  provided  here  are  more  complete  than  the  more  granular  data.    Both  are  provided  to  give  teams  flexibility  to  explore  innovative  solutions.    Teams  can  decide  which  of  the  datasets  they  want  to  use  in  their  analysis,  it  is  not  necessary  to  use  all  that  we  have  provided.    As  is  the  case  when  working  on  real-world  problems,  neither  dataset  is  perfect,  but  we  believe  useful  insight  to  the  I&I  problem  can  be  obtained  from  the  data  available.
                  
