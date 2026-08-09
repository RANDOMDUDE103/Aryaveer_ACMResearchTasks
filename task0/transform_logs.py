from datetime import datetime
import re
pat1=r"\d{2}/\d{2}/\d{4}"
pat2=r"\w@[a-z]mail.com|\w@mail.com"
pat3=r"error"
pat4=r"\d{2}:\d{2}"
pat5=r"\d{10}"
pat6=r"\d{3}.\d{3}.\d{1}.\d{1}"
pat7=r"<\w+>"

def modify_log(str):
    s=""
    str=re.sub(r"\s{2,}"," ",str)
    a = str.rsplit(" ")

    for i in range(len(a)):
        if re.search(pat2,a[i]):
            a[i] = a[i].rstrip(".,!?")
            a[i]="[HIDDEN]"
        elif re.search(pat1,a[i]):
            a[i] = a[i].rstrip(".,!?")
            dt=datetime.strptime(a[i],"%d/%m/%Y")
            a[i]=dt.strftime("%d %B %Y")
        elif re.search(pat3,a[i],re.IGNORECASE):
            a[i]=a[i].rstrip(".,!?:")
            a[i]="--->"
        elif re.search(pat4,a[i]):
            a[i] = a[i].rstrip(".,!?")
            dt = datetime.strptime(a[i], "%H:%M")
            a[i]=dt.strftime("%I:%M %p")
        elif re.search(pat5,a[i]):
            a[i] = "[PHONE NO.]"
        elif re.search(pat6, a[i]):
            a[i] = "[IP]"
        elif re.search(pat7, a[i]):
            a[i] = "*"*(len(a[i])-2)
        s=s+a[i]
        s=s+" "
    s=s.strip()
    return s





print(modify_log("    User    john@mail.com 9543457780 <password> logged in at 30/09/2025 18:05 from 192.168.1.1.  error session timeout "))

