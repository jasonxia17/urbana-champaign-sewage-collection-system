# Urbana-Champaign-Sewage-Collection-System
Organization  Name:  Urbana  &amp;  Champaign  Sanitary  District 

# Overview:
The  mission  of  the  Urbana  &  Champaign  Sanitary  District  (UCSD)  is  to  protect  public  health  and  safety,  preserve  the  public  trust,  and  protect  the  natural  environment.  UCSD  is  a  municipal  body  which  provides  wastewater  treatment  for  properties  in  the  Cities  of  Urbana  and  Champaign,  the  Villages  of  Bondville  and  Savoy,  the  University  of  Illinois  and  the  surrounding  adjacent  developed  areas.    UCSD  operates  two  wastewater  treatment  plants.  The  Northeast  plant  is  located  in  Urbana  immediately  north  of  Ambucs  Park.  The  Southwest  plant  is  located  in  Champaign  at  the  intersection  of  Windsor  and  Rising  Roads.  UCSD  also  operates  large  diameter  sanitary  interceptor  sewers  and  28  pumping  stations  that  transport  wastewater  to  the  treatment  plants.  Champaign,  Urbana,  Savoy  and  the  University  of  Illinois  operate  their  respective  collector  sewers  to  which  homes  and  businesses  are  connected.

# Problem  Statement:
Inflow  and  infiltration  (referred  to  as  I&I)  is  when  groundwater  and  stormwater  enter  the  sanitary  sewer  through  leaks  in  the  piping  and  connections.      When  groundwater  and  stormwater  enter  the  sewage  collection  system  as  I&I,  it  must  be  sent  to  the  wastewater  treatment  plant  along  with  the  actual  wastewater  generated  within  the  community.    Due  to  I&I,  wastewater  treatment  plants  end  up  treating  much  higher  volumes  of  wastewater  than  they  otherwise  would,  leading  to  higher  energy  consumption  and  costs.    During  a  particularly  large  storm,  the  increased  flow  reaching  a  treatment  plant  due  to  I&I  may  even  exceed  the  treatment  plant’s  capacity.  Under  such  circumstances,  untreated  wastewater  may  be  discharged  into  the  environment.      By  detecting  and  fixing  leaks  in  the  sewage  collection  system,  one  can  eliminate  the  energy  consumed  in  pumping  and  treating  groundwater  and  stormwater  that  enters  the  sewage  collection  system,  and  that  otherwise  do  not  require  treatment.      Furthermore,  if  I&I  were  significantly  reduced,  wastewater  treatment  plants  could  plan  to  use  more  of  their  treatment  capacity  for  treating  wastewater,  rather  than  a  combination  of  wastewater  and  I&I,  and  thus  service  greater  populations  with  existing  treatment  infrastructure.    However,  identification  of  leaks  in  underground  piping  is  difficult  and  costly  using  currently  available  technologies.      For  this  problem  we  encourage  teams  to  develop  innovative  ways  to  identify  areas  of  potential  I&I  in  the  UCSD  sewage  collection  system,  using  historical  plant  flow  data,  lift  station  flow  data,  and  precipitation  data.For  this  challenge  we  will  focus  on  the  UCSD  NE  plant,  and  assume  that  similar  techniques  would  work  for  the  UCSD  SW  plant  (where  similar  data  is  available).  In  addition  to  historical  flow  data,  we  have  provided  basin  maps  to  understand  the  flow  of  lift  stations  into  other  lift  stations,  and  ultimately  into  the  NE  plant.    The  goal  of  this  challenge  will  be  to  identify  the  specific  lift  stations  where  the  most  I&I  is  entering  during  a  rainstorm  event.    The  results  of  this  challenge  which  will  help  guide    where    money  should  be  spent  for  collection  system  repair. 

# NE  Plant  LIFT  Stations: 
Lift  stations  are  located  throughout  the  sewage  collection  system,  and  represent  points  in  the  collection  system  where  water  is  pumped  and  moved  towards  the  treatment  plant.    Data  is  collected  at  lift  stations,  including  pump  status,  liquid  level,  and  daily  flow  rates.    Given  that  data  is  available  at  lift  stations,  but  not  at  other  points  in  the  collection  system,  this  problem  focuses  on  identifying  lift  stations  where  the  most  I&I  is  entering.    By  identifying  these  lift  stations,  the  geographic  area  where  the  most  significant  leaks  are  will  also  be  known,  since  the  pipes  that  connect  to  each  lift  station  are  known.    Below  is  a  list  of  the  lift  stations  within  the  NE  Plant  basin.    Sewage  from  certain  lift  stations  will  flow  through  another  lift  station  prior  to  entering  the  NE  Plant,  which  is  also  indicated  in  the  list  below.    A  basin  map  with  this  information  is  provided. 

1.  Bradley-McKinley 
2.  Staley 
3.  Freshville
4.  I-74  To  LELS  
5.  Timber  Hills    To  Broadway
6.  O.L.  Johnson    To  LELS 
7.  Perkins    To  LELS  
8.  Locust  Street  
9.  Broadway 
10.  Carle  Park
11.  Vine 
12.  Amvets 
13.  East  Main 
14.  Mumford 
15.  Myra  
16.  Race  Street    Half  to  Myra  &  half  to  Amvets  
17.  South  Ridge    To  Myra
18.  LELS

# Evaluation  criteria:
-Appropriateness  of  analytics  techniques  used  to  solve  the  problem.
-Were  lift  stations  where  the  most  I&I  is  entering  during  a  rainstorm  identified?    With  what  level  of  confidence?
-How  robust  is  the  solution  in  the  presence  of  imperfect  data  (does  it  work  well  even  if  data  is  missing  /  data  has  uncertainty  /  is  at  the  day-level  rather  than  more  granular)?
-Were  results  explained  in  a  way  that  is  helpful  to  UCSD  /  City officials?

# Datasets:
The  following  historical  datasets  are  available: 
1.  NE  Plant  Flow  Data
2.  NE  Plant  LIFT  Station  Flow  Data
3.  NOAA  Precipitation  Data  

# USGS  Rain  Gage  DataFile  descriptions:  
Below  are  file  descriptions  for  each  type  of  dataset.

NE  Plant  Flow  Data:    
Filename: NEPinfluent_dailyflow.xlsx
  Month 
  Day 
  Year 
  Total  Influent  Flow  [MGD]  

LIFT  Station  Data:
Filename: NEPlift_dailyflow.xlsx 
  Date
  Daily  flow  at  each  lift  station  [gallons/day] 
  Note:  Daily  flow  values  of  zero  are  errors  and  should  be  considered  as  not  available.  

NOAA  Weather  Data:  
Filename:  NOAA.csv
  Station  ID
  Name  
  Latitude  
  Longitude  
  Elevation  
  Date  
  PCRP  [daily  precipitation  in  inches]  
  Note:  Data  for  the  7  NOAA  weather  stations  in  the  NE  Plant  basin  are  provided.  

USGS  Rain  Gage  Data:  
USGS  operates  two  rain  gages  in  the  NE  Plant  basin:  urls  for  RDB  output  have  been  provided.  
  Agency  
  Site  Number  
  Datetime  
  Time  zone  
  Total  Precipitation  [inches]  

Boneyard  Creek:  https://nwis.waterservices.usgs.gov/nwis/iv/?format=rdb&sites=03337000&startDT=2012-01-01T00:00-0400&parameterCd=00045&siteStatus=all  

South  Side  Elementary  School:  https://nwis.waterservices.usgs.gov/nwis/iv/?format=rdb&sites=400620088151801&startDT=2012-01-01T00:00-0400&parame
