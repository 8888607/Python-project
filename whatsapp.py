import pywhatkit as kit 
import time
numbers=[
   # "+919209125801",
    #"+917397829851",
  #  "+917559275240",
   # "+919561962047",
   # "+919022172582",
    "+919960669455",
   # "+917248977661",
   # "+919309567429",
   # "+919503467675"
]
message="Hey,What's up?How are you?"
#start_time=datetime.now()+timedelta(minutes=2)

#for i,phone in enumerate(numbers):
 #   send_time=start_time + timedelta(minutes=i*2)

for phone in numbers:
    kit.sendwhatmsg_instantly(phone,message)
    time.sleep(15)
               