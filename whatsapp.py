import pywhatkit as kit 
import time
numbers=[
    "+91XXXXXXXXXX",
    "+91XXXXXXXXXX",
    "+91XXXXXXXXXX",
    "+91XXXXXXXXXX",
    "+91XXXXXXXXXX",
    "+91XXXXXXXXXX",
    "+91XXXXXXXXXX",
    "+91XXXXXXXXXX",
    "+91XXXXXXXXXX"
]
message="Hey,What's up?How are you?"

for phone in numbers:
    kit.sendwhatmsg_instantly(phone,message)
    time.sleep(15)
               
