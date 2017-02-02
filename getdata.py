import urllib
import csv, sqlite3
import zipfile
import os
import MySQLdb
from datetime import datetime

headers = ['SOS_VOTERID','COUNTY_NUMBER','COUNTY_ID','LAST_NAME','FIRST_NAME','MIDDLE_NAME','SUFFIX','DATE_OF_BIRTH','REGISTRATION_DATE','VOTER_STATUS','PARTY_AFFILIATION','RESIDENTIAL_ADDRESS1','RESIDENTIAL_SECONDARY_ADDR','RESIDENTIAL_CITY','RESIDENTIAL_STATE','RESIDENTIAL_ZIP','RESIDENTIAL_ZIP_PLUS4','RESIDENTIAL_COUNTRY','RESIDENTIAL_POSTALCODE','MAILING_ADDRESS1','MAILING_SECONDARY_ADDRESS','MAILING_CITY','MAILING_STATE','MAILING_ZIP','MAILING_ZIP_PLUS4','MAILING_COUNTRY','MAILING_POSTAL_CODE','CAREER_CENTER','CITY','CITY_SCHOOL_DISTRICT','COUNTY_COURT_DISTRICT','CONGRESSIONAL_DISTRICT','COURT_OF_APPEALS','EDU_SERVICE_CENTER_DISTRICT','EXEMPTED_VILL_SCHOOL_DISTRICT','LIBRARY','LOCAL_SCHOOL_DISTRICT','MUNICIPAL_COURT_DISTRICT','PRECINCT_NAME','PRECINCT_CODE','STATE_BOARD_OF_EDUCATION','STATE_REPRESENTATIVE_DISTRICT','STATE_SENATE_DISTRICT','TOWNSHIP','VILLAGE','WARD','PRIMARY-03/07/2000','GENERAL-11/07/2000','SPECIAL-05/08/2001','GENERAL-11/06/2001','PRIMARY-05/07/2002','GENERAL-11/05/2002','SPECIAL-05/06/2003','GENERAL-11/04/2003','PRIMARY-03/02/2004','GENERAL-11/02/2004','SPECIAL-02/08/2005','PRIMARY-05/03/2005','PRIMARY-09/13/2005','GENERAL-11/08/2005','SPECIAL-02/07/2006','PRIMARY-05/02/2006','GENERAL-11/07/2006','PRIMARY-05/08/2007','PRIMARY-09/11/2007','GENERAL-11/06/2007','PRIMARY-11/06/2007','GENERAL-12/11/2007','PRIMARY-03/04/2008','PRIMARY-10/14/2008','GENERAL-11/04/2008','GENERAL-11/18/2008','PRIMARY-05/05/2009','PRIMARY-09/08/2009','PRIMARY-09/15/2009','PRIMARY-09/29/2009','GENERAL-11/03/2009','PRIMARY-05/04/2010','PRIMARY-07/13/2010','PRIMARY-09/07/2010','GENERAL-11/02/2010','PRIMARY-05/03/2011','PRIMARY-09/13/2011','GENERAL-11/08/2011','PRIMARY-03/06/2012','GENERAL-11/06/2012','PRIMARY-05/07/2013','PRIMARY-09/10/2013','PRIMARY-10/01/2013','GENERAL-11/05/2013','PRIMARY-05/06/2014','GENERAL-11/04/2014','PRIMARY-05/05/2015','PRIMARY-09/15/2015','GENERAL-11/03/2015','PRIMARY-03/15/2016','GENERAL-06/07/2016','PRIMARY-09/13/2016','GENERAL-11/08/2016']
e_tables=[]
tables = ['person','location','address']

for column in headers[46:98]:
	c_split = column.split("-")
	c_date = str(c_split[1])
	c_type = str(c_split[0])
	date = datetime.strftime(datetime.strptime(c_date, '%m/%d/%Y'), '%m_%d_%Y')
	print(date)
	c_name = c_type.lower()+"_"+date
	e_tables.append(c_name)
	#print(e_tables)

#for i in e_tables:
#	tables.append(i)

print(tables)

def getfile(file):
	server = "ftp://sosftp.sos.state.oh.us/free/Voter/"+file
	urllib.urlretrieve(server, file)

def unzip(file):
	zip = zipfile.ZipFile(file)
	zip.extractall()

def cleanup(file):
	os.remove(file)

def createtables():
	cnx = mysql.connector.connect(user='root', database='voter_dev')
	cursor = cnx.cursor()
	for table in e_tables: 
		t_create = "CREATE TABLE "+table+" (sos_voterid VARCHAR(50), vote VARCHAR(1));"

createtables()	
#def buildsql(file):
#	with open(file, 'wb') as csvfile:
#	linereader = csv.reader(csvfile, delimiter=',')
#	for row in linereader:
	#Code here to write to scratch table

#def t_name():
#def t_district():
#def t_addr():
#def t_contact():
#def t_touch():
#def t_rating():
#def t_status():
#def t_purged():
#def t_inout():

#def splittable():
	#Code to check for updates and split data into different tables
	#if record does not exist
		#Write new record and record date
	#elif record exists
		#case address changed
			#update address
			#case address into/out of franklin
				#add to change list
		#case vote record changed
			#update vote record
		#check for previous purge flag and remove
		#mark update date

#def purgesearch():
	#if update date is older than most recent update and purge flag is not set:
		#add to purge list

county = "NOBLE"
countyfile = county+".zip"
getfile(countyfile)
unzip(countyfile)
cleanup(countyfile)
