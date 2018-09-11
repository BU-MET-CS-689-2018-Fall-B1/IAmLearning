from datetime import date
from dateutil.relativedelta import relativedelta
import cs689_utils

def gendates(days_back, days_total):
    startDt = date.today() + relativedelta(days=+(-1 * days_back))
    for dateOff in range(days_total):
        dimDate = startDt + relativedelta(days=+dateOff)
        dateYear = dimDate.year
        fiscalPer = str (dimDate.year) + 'm' + str(dimDate.month)
        print (dimDate, dateYear, fiscalPer)