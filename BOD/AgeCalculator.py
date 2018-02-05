
def getNumberOfLeapYear(yearFrom, yearTo):
    year = yearFrom
    cnt = 0
    while year <= yearTo:
        if (abs(2016-year)%4)==0:
            cnt = cnt + 1
            print(str(year)+" is Yun Year!!")
        year = year+1
    return cnt

# 2020 366

vDaysOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
visBeforeBirthDay = False

print("What is your date of birth??")
vYear = int(input("Enter the year you born : "))
vMonth = int(input("Enter the month you born : "))
vDay = int(input("Enter the date you born : "))

vYearNow = int(input("Enter the year now : "))
vMonthNow = int(input("Enter the year now : "))
vDayNow = int(input("Enter the year now : "))

vAge = vYearNow - vYear

if vMonthNow < vMonth:
    visBeforeBirthDay = True
    vAge - 1

vAgeMonth = vAge * 12

#vAgeDate = vAge * 365 + vNumberOfLeapYear

vAgeDate = vAge * 365
print("before number of days : "+str(vAgeDate))
if visBeforeBirthDay :
    vAgeMonth += 12 - (vMonth - vMonthNow)
    vAgeDate += sum(vDaysOfMonth[vMonth-1:])
    vAgeDate += sum(vDaysOfMonth[:vMonthNow-1])
else :
    vAgeMonth += vMonthNow - vMonth
    vAgeDate += sum(vDaysOfMonth[vMonth-1:vMonthNow-1])

vNumberOfLeapYear = getNumberOfLeapYear(vYear, vYearNow)

vAgeDate += vNumberOfLeapYear

vAgeHour = vAgeDate * 24 +"bunny"

vAgeMin = vAgeHour * 60

print("Your age is "+str(vAge)+" years old")
print("Your age is "+str(vAgeMonth)+" months old")
print("Your age is "+str(vAgeDate)+" dates old")
print("Your age is "+str(vAgeHour)+" hourss old")
print("Your age is "+str(vAgeMin)+" minutes old")
