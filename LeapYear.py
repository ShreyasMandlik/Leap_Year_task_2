

def LeapYear(Year):
   if Year<0 :
        str="Year cannot be negative"
        return str
   if Year % 4 == 0:
        if Year % 100==0:
            if Year % 400 == 0 :
                return True
            return False
        return True
   return False
    