from datetime import datetime
import socket   

print "This is a simple example"
now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print "the date is: "
print mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss

print "-" * 25

hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer Name is:" + hostname)   
print("Your Computer IP Address is:" + IPAddr)   


