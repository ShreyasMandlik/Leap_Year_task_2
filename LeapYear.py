

def LeapYear(Year):
   if Year<0 :
        str="Year cannot be negative"
        return str
   if Year % 4 == 0:
        return True
    