from plyer import notification
from datetime import datetime
import time
def notify(title1, message1):
    notification.notify(title=title1, message=message1, app_icon="icon.ico", timeout=10)

while True:
    title=""
    message=""       
    mon=["No class now", "DMDW", "No class now", "No class now", "DAA","No class now","BD"]
    tue=["No class now", "DAA", "No class now", "SE", "BD","No class now","No class now"]
    wed=["No class now", "DMDW", "CN", "CN LAB", "CN LAB","SE","No class now"]
    thurs=["CN", "SE", "No class now", "DMDW", "No class now","DAA","DAA LAB"]
    fri=["No class now", "No class now", "BD", "CN", "SE","No class now","No class now"]

    t=datetime.today()
    daylist=[mon, tue, wed, thurs, fri, "Sat", "Sun"]
    day=daylist[t.weekday()]
    i=-1
    
    if t.weekday() in range(0,5):
        i=0
        if(t.hour==9):
            title=day[0]
            message="9:00 - 10:00"
            i=1
            
        
        if(t.hour==10):
            title=day[1]
            message="10:00 - 11:00"
            i=1

        if(t.hour==11):
            title=day[2]
            message="11:00 - 12:00"
            i=1
            
        if(t.hour==12):
            title=day[3]
            message="12:00 - 13:00"
            i=1
        
        if(t.hour==13):
            title=day[4]
            message="13:00 - 14:00"
            i=1

        if(t.hour==15):
            title=day[5]
            message="15:00 - 16:00"
            i=1
        
        if(t.hour==16):
            title=day[6]
            message="16:00 - 17:00"
            i=1
        
    if(i==1):
        notify(title, message)
            
    elif(i==-1):
        notify("Enjoy!!", "Today is weekend")
        
    else:
        notify("Enjoy!!", "Classes are over")
    time.sleep(60*30)




