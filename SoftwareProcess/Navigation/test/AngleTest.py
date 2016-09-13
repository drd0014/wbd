import Navigation.prod.Angle as at

'call angle class'
myAngleTest=at.Angle()
print(myAngleTest)


'call for setdegrees'
'''try:
    setdegrees=at.setDegrees(40)
    print(setdegrees)
except ValueError as e:
    print(e)'''
'Call for Compare method'
try:
    a1=at.Angle()
    d1=a1.setDegrees(36.0)
    print d1
    a2=at.Angle()
    d2=a2.setDegrees(51.60)
    print d2
    result=a1.compare(a2)
    print result
except ValueError as e:
    print(e)
    
'a3=at.Angle()'
temp1=a1.getString()
print temp1
 
'call for setdegreesAndMinutes'
try:
    a3=at.Angle()
    a4=at.Angle()
    
    a5=at.Angle()
    a6=at.Angle()
    a5=a3.setDegreesAndMinutes("21d1.0")
    print(a5)
    a6=a4.setDegreesAndMinutes("31d1.0")
    print(a6)
except ValueError as e:
    print(e)

'call add '    
'''temp5=a5.add(a6)
print temp5

'call subtract'
temp2=a1.subtract(a2)
print temp2
'''
    

