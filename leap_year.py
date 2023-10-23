
def leap_year(year):
    if(year %4 ==0 and year % 100==0) or(year%400==0):   
        print( "this is a leap year")
    else:
        print("the given year is not a leap year")
leap_year(1900) # TRUE
leap_year(2003) # FALSE

#THIS IS THE CODE TO FIN OUT HE GIVEN YEAR IS LEAP YEAR OT NOT
