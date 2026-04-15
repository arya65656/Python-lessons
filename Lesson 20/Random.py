import random
import time
def get_random_date(startdate, enddate):
    print("Printing random dates between", startdate, "and", enddate)
    random_generator=random.random()
    date_format='%m/%d/%Y'
    starttime=time.mktime(time.strptime(startdate, date_format))
    endtime=time.mktime(time.strptime(enddate, date_format))
    randomtime=starttime+random_generator*(endtime-starttime)
    randomdate=time.strftime(date_format, time.localtime(randomtime))
    return randomdate
print("Random date is=", get_random_date("1/1/2016","12/12/2018"))
