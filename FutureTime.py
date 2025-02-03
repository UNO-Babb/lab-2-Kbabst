#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

 

  #TODO:
  #Ask user for hours
  #Ask user for minutes
moreMins = 40
now = datetime.datetime.now()
currentMinute = now.minute

futureMins = (currentMinute + moreMins ) % 60
extraHour = (currentMinute + moreMins ) // 60
print(extraHour)
print(futureMins)

  #Calculate the time after the user-supplied time has passed.


  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"



