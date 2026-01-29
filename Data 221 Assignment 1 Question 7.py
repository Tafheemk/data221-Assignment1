# Tafheem Khan 30219735
# Data 221 Assignment_1 Question 7 "Time Conversion Function"
# Need to write a function that converts a input of seconds since midnight into hours, minutes, seconds and whether it is PM or AM
def timeConversion(SecondSinceMidnight):
    # Validate the input, make sure it is integers and not 24 hours being 86400 seconds or zero seconds
    if not isinstance(SecondSinceMidnight, int):
        return "Input must be an integer."
    if SecondSinceMidnight < 0 or SecondSinceMidnight >= 86400:
        return "Input must be between 0 and 86399 seconds."

    # Calculate hours, minutes, seconds 3600 secs in an hour so floor division gives us hours, use the remainder from that and divide by 60 to get minutes and finally the remainder of that gives us seconds
    hours = SecondSinceMidnight // 3600
    minutes = (SecondSinceMidnight % 3600) // 60
    seconds = SecondSinceMidnight % 60

    # Determine whether AM or PM
    if hours >= 12:
        period = "PM"
    else:
        period = "AM"

    # Convert to 12-hour format 
    DisplayHour = hours % 12
    if DisplayHour == 0:
        DisplayHour = 12
# Return the sentence 
    return f"{DisplayHour} {minutes} {seconds} {period}"

