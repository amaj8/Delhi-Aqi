import notify2
import time

notify2.init('Distraction Alert')

n = notify2.Notification(None)
n.set_urgency(notify2.URGENCY_NORMAL)
# n.set_timeout()

#Distraction Alert
while 1:
    n.update("Whacha doing?","Drink water and get back to work!")
    n.show()
    time.sleep(60*30)

# #Water alert
# while 1:
#     n.update("Stay hydrated!","Time to drink water")
#     n.show()
#     time.sleep(60*60)
