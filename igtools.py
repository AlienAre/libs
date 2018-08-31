
import datetime, sys
from datetime import date
from dateutil import relativedelta
import pandas as pd

def getCycleStartDate(pdate):
	if int(pdate.strftime("%d")) > 15:
		return pdate.replace(day=1)
	else: 
		return (pdate.replace(day=1) - datetime.timedelta(days=1)).replace(day=16)

def getCycleEndDate(pdate):
	if int(pdate.strftime("%d")) > 15:
		return pdate.replace(day=15)
	else: 
		return pdate.replace(day=1) - datetime.timedelta(days=1)

def get24CycleStartDate(pdate):
	if int(pdate.strftime("%d")) > 15: #for cycle 16-31
		lastyrnextmonth = pdate.replace(year=(pdate.year-1), day=1) + datetime.timedelta(days=32) #set date to 1st of last year, then add 32 days to the following month 
		lastyrnextmonth = lastyrnextmonth.replace(day=1)
		return lastyrnextmonth - datetime.timedelta(days=1)
	else: #for cycle 1-15
		return pdate.replace(year=(pdate.year-1))	
		
def get24CycleEndDate(pdate):
	if int(pdate.strftime("%d")) > 15: #for cycle 16-31
		return pdate.replace(day=15)
	else: #for cycle 1-15
		return pdate.replace(day=1) - datetime.timedelta(days=1)		
		
def getLastMonthEndDate(pdate):
		return pdate.replace(day=1) - datetime.timedelta(days=1)
		
def getLast2MonthEndDate(pdate):
		return (pdate.replace(day=1) - datetime.timedelta(days=1)).replace(day=1) - datetime.timedelta(days=1) 		
		
def getQuarter(pdate):
		return (int(pdate.strftime("%m")) - 1)//3 + 1

def getLastQuarterEndDate(pdate):
    if pdate.month < 4:
        return datetime.date(pdate.year - 1, 12, 31)
    elif pdate.month < 7:
        return datetime.date(pdate.year, 3, 31)
    elif pdate.month < 10:
        return datetime.date(pdate.year, 6, 30)
    return datetime.date(pdate.year, 9, 30)
	
#------------ get cycle start date ----------------
def getCStartDate(pcycleenddate):
	if int(pcycleenddate.strftime("%d")) > 15:
		return pcycleenddate.replace(day=16)
	else: 
		return pcycleenddate.replace(day=1)
#--------------------------------------------------	
	
def getTenure(pdate1, pdate2):
	#date1 = datetime.datetime.strptime(str(pdate1), '%Y-%m-%d')
	#date2 = datetime.datetime.strptime(str(pdate2), '%Y-%m-%d')
	r = relativedelta.relativedelta(pdate1, pdate2)
	#print "{0.years} years and {0.months} months".format(r)
	return abs(r.years)

def addZero(str, length):
	strlength = len(str)
	if strlength < length:
		targetstr = (length - strlength) * '0' + str
		return targetstr
	elif strlength > length:	
		print 'The string you entered is longer than your target length'
		return str
	else:
		return str
		
def fix_negative(pstr):
	str = ""
	try:
		str = float(pstr)
	except ValueError:
		str = float(pstr.replace("-", "")) *-1
	
	return str

def str2float(pstr):
	
	output = 0.00
	#strip blanks and end '\n', '\r'
	str = pstr.lstrip(' ').rstrip(' ').rstrip('\n').rstrip('\r')
	str = str.replace(',', '')

	#------- hand () as negative sign -------
	if (str[0] == '(') & (str[-1] ==')'):
			str = '-' + str[1:-1]

	#------- hand - as negative sign, showed at the end of string -------			
	if str[-1] == '-':
			str = '-' + str[:-1]
	
	try: 
		float(str)
	except:
		print str + ' is not numeric, please check'
		sys.exit()
	else:
		output = float(str)
		
	return output

if __name__=="__main__":	
	#today = datetime.datetime.strptime('01/26/2017', '%m/%d/%Y') #date.today()	
	today = date.today()	
	startday = getCycleStartDate(today)
	endday = getCycleEndDate(today)
	
	#print(getQuarter(today))
	#print(today.year)
	#print(getLastQuarterEndDate(today))
	#print startday
	#print endday
	#
	#date1 = datetime.datetime.strptime(str('2017-10-31'), '%Y-%m-%d')
	#date2 = datetime.datetime.strptime(str('2010-12-25'), '%Y-%m-%d')
	#r = relativedelta.relativedelta(date2, date1)
	#print "{0.years} years and {0.months} months".format(r)
	#print abs(r.years)

	#for d in df[0]:
	#	print 'The cycle end date is ' + str(d)
	#	print 'The 24 cycle start day is ' + str(get24CycleStartDate(d))
	#	print 'The 24 cycle end day is ' + str(get24CycleEndDate(d))
	#for d in df[1]:
	#	print 'The cycle end date is ' + str(d)
	#	#print 'The 24 cycle start day is ' + str(get24CycleStartDate(d))
	#	print 'The 24 cycle end day is ' + str(get24CycleEndDate(d))
	#df[2] = df[1].replace(year=(df[1].year-1),day=1) + datetime.timedelta(months=1)	
	#print df
