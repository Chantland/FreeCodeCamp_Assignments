# Input

# def add_time(start, duration, StartDay = False):
start = "11:43 PM"
duration = "24:20"
StartingDay = "TueSday"

TempNumb = start.split()

DayCount = 0
StartTime = TempNumb[0]
StartAMorPM = TempNumb[1]
if StartAMorPM == "AM":
    AMorPM_Digit = 0
elif StartAMorPM == "PM":
    AMorPM_Digit = 12
else:
    print("Error, must be an AM or PM input")
    quit()

# set up the start time integers
StartTime = StartTime.split(":")
StartMinute = int(StartTime[1])
StartHour = int(StartTime[0])
if StartHour == 12:
    if StartAMorPM == "AM":
        StartHour = StartHour - 12
    elif StartAMorPM == "PM":
        StartHour = StartHour    # put in just as a reminder that the 12 does not change
else:
    StartHour += AMorPM_Digit


# set up the Duration integers
DurationTime = duration.split(":")
DurationHour = int(DurationTime[0])
DurationMinute = int(DurationTime[1])

# Minute addition for new number
NewMinute = (StartMinute + DurationMinute)/100 # use decimals since it makes creating a string easier
if NewMinute > .59:
    AddNewMinute = 1
    NewMinute = NewMinute - .6
else:
    AddNewMinute = 0
NewMinute = "{:.2f}".format(NewMinute)[2:4]# format to accept 2 decimal places then choose those last 2



# hour addition for new numbers
NewHour = StartHour + AddNewMinute + DurationHour
while NewHour >= 24:
    NewHour = NewHour - 24
    DayCount += 1

# Set AM or PM then convert new hour to a string for output
if NewHour > 12:
    NewAMorPM = "PM"
    NewHour = str(NewHour - 12)
elif NewHour == 12:
    NewAMorPM = "PM"
    NewHour = str(NewHour)
elif 0 < NewHour < 12:
    NewAMorPM = "AM"
    NewHour = str(NewHour)
elif NewHour == 0:
    NewAMorPM = "AM"
    NewHour = "12"

# list how many days it has been
if DayCount == 1:
    DayText = " (next day)"
elif DayCount > 1:
    DayText = " (" + str(DayCount) + " days later)"
else:
    DayText = ""

if StartingDay != None:
    StartingDay = StartingDay.lower()
    DayDict = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}

    try:
        DayCount = DayDict[StartingDay] + DayCount
    except:
        New_time = 'Error: Did not supply a legible date'
        # return New_time
        quit()

    while DayCount > 6:
        DayCount = DayCount - 7

    DayDict_Rev = {'0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday', '4': 'Friday', '5': 'Saturday', '6': 'Sunday' }
    NewDay = ', ' + DayDict_Rev[str(DayCount)]
else:
    NewDay = ""

# produce completed text
new_time = NewHour + ":" + NewMinute + ' ' + NewAMorPM + NewDay + DayText
print(new_time)






# day: 0 - 6, Hour 12-24