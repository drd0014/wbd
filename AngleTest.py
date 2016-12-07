import Navigation.prod.Angle as at
'try to import'
'call angle class'
myAngleTest=at.Angle()
print(myAngleTest)
try:
    a1=at.Angle()
    d1=a1.setDegrees(36.0)
    print d1
    a2=at.Angle()
    d2=a2.setDegrees(51.60)
    print d2
    #result=a1.comparition(a2)
    #print result
except ValueError as e:
    print(e)
    
'a3=at.Angle()'
temp1=a1.get_Degrees()
print temp1
 
'call for setdegreesAndMinutes'
try:
    a3=at.Angle()
    a4=at.Angle()
    
    a5=at.Angle()
    a6=at.Angle()
    a5=a1.setDegreesAndMinutes("21d1.0")
    print(a5)
    a6=a2.setDegreesAndMinutes("31d1.0")
    print(a6)
except ValueError as e:
    print(e)

'call addition '
temp5=a1.addition(a2)
print temp5

'call subtract'
temp2=a1.subtraction(a2)
print temp2
    

