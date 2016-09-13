class Angle:
    'default constructor'
    def __init__(self,degrees=None,minutes=None):
        if degrees is None:
            self.degrees=0
        else:
            self.degrees=degrees
        if minutes is None:
            self.minutes=0
        else:
            self.minutes=minutes
        pass
    'instance methods for setDegrees'
    def setDegrees(self=None,degrees=None):
        if degrees is  None:
            raise ValueError("Angle.setDegrees:Degreess is not None")
        elif(degrees is ""):
            raise ValueError("Angle.setDegrees:illegal not allowed null")
        elif(degrees is ''):
            raise ValueError("Angle.setDegrees:illegal not allowed null")
        else:
            self.degrees=degrees
            return self.degrees
    pass
    'instance methods for setDegreesAndMinutes'
    def setDegreesAndMinutes(self=None,degreesAndMinutes=None): 
        if degreesAndMinutes is None:
            raise ValueError("Angle.setDegreesAndMinutes:Degrees and Minutes not be None Please re enter data")
        elif(degreesAndMinutes is ""):
            raise ValueError("Angle.setDegreesAndMinutes:illegal not allowed null")
        elif(degreesAndMinutes is ''):
            raise ValueError("Angle.setDegreesAndMinutes:illegal not allowed null")
        else:
            temp=degreesAndMinutes.split('d')
            degrees=int(temp[0])
            minutes=float(temp[1])
            if(degrees is ''):
                raise ValueError("Angle.setDegreesAndMinutes:Missing degrees")
            elif(minutes is ''):
                raise ValueError("Angle.setDegreesAndMinutes:Missing minutes")
            elif((degrees is '') and (minutes is '')):
                raise ValueError("Angle.setDegreesAndMinutes:Both Missing degrees and Minutes")
            else:
                'raise ValueError("All is well")'
        'check weather degrees in integer or not'    
        if(not(isinstance(degrees,int))):
                raise ValueError("Angle.setDegreesAndMinutes:degrees must have integer value")
        else:
                degrees=int(temp[0]);
        
        'check weather minutes in float or not'    
        if(not(isinstance(minutes,float))):
            raise ValueError("Angle.setDegreesAndMinutes:Minutes must have float value")
        else:
                minutes=float(temp[1])
        'condition to know whether single decimal point in degree or not ?'
        minutes_check=temp[1].split('.')
        minutes_check_decimal=minutes_check[1]
        if((len(minutes_check_decimal))>=2):
                raise ValueError("Angle.setDegreesAndMinutes:Minutes must have Only One decimal")    
        minutes=float(temp[1])
        'condition for checking modulo 360 and negative'
        if(degrees>360):
            degrees=degrees%360
        else:
            degrees=degrees
        if(minutes>60):
            temp_minutes=(minutes%60)  
            degrees=degrees+(minutes/60)
            degrees=int(degrees) 
            minutes=temp_minutes
        else:
            minutes=float(minutes)
        'check for negativee'    
        if(degrees<0):
            degrees=degrees*-1
            degrees=degrees%360
            degrees=360-(degrees)
        else:
            degrees=degrees
        if(minutes>60):
            temp_minutes=(minutes%60)  
            degrees=degrees+(minutes/60)
            degrees=int(degrees) 
            minutes=temp_minutes
        else:
            minutes=float(minutes)
            
        self.degrees=degrees
        self.minutes=minutes        
        
        return ((self.degrees,self.minutes))
    pass
    'getString'
    def getString(self=None):
        print "in side get string"
        if self is None:
            raise ValueError("Angle.getString:")
        else:
            return str(str(self.degrees)+str("d")+str(self.minutes))
    pass
    'Add two Objects'
    def add(self=None,other=None):
        if(not(isinstance(self,Angle))):
            raise ValueError("Angle.Add:Not and Angle Object")
        elif(not(isinstance(other,Angle))):
            raise ValueError("Angle.Add:Not and Angle Object")
        else:
            'condition for checking modulo 360 and negative'
            total_minutes=self.minutes+other.minutes
            total_degrees=self.degrees+other.degrees
            if(total_degrees>360):
                total_degrees=total_degrees%360
            else:
                total_degrees=total_degrees
            if(total_minutes>60):
                temp_minutes=(total_minutes%60)  
                total_minutes=total_degrees+(total_minutes/60)
                total_degrees=int(total_degrees) 
                total_minutes=temp_minutes
            else:
                total_minutes=float(total_minutes)
                return (total_degrees,total_minutes)
    pass
        
    'Subtract two Objects'
    def subtract(self=None,other=None):
        if self is None:
            total_minutes=0
            total_degrees=0
        elif other is None:
            total_minutes=0
            total_degrees=0
        elif(not(isinstance(self,Angle))):
            raise ValueError("Angle.Subtract:Not and Angle Object")
        elif(not(isinstance(other,Angle))):
            raise ValueError("Angle.Subtract:Not and Angle Object")
        else:
            total_minutes=self.minutes-other.minutes
            total_degrees=self.degrees-other.degrees
            if(total_degrees>360):
                total_degrees=total_degrees%360
            else:
                total_degrees=total_degrees
            if(total_minutes>60):
                temp_minutes=(total_minutes%60)  
                total_minutes=total_degrees+(total_minutes/60)
                total_degrees=int(total_degrees) 
                total_minutes=temp_minutes
            else:
                total_minutes=float(total_minutes)
            return (total_degrees,total_minutes)
    pass

        
    'compare two objects'
    def compare(self=None,other=None):
        if self is None:
            raise ValueError("Angle.Compare:Object 1 Degree value is Missing")
        elif other is None:
            raise ValueError("Angle.Compare:Object 2 Degree value is Missing")
        elif(not(isinstance(self,Angle))):
            raise ValueError("Angle.Compare:Degree1 Not and Angle Object")
        elif(not(isinstance(other,Angle))):
            raise ValueError("Angle.Compare:Degree 2 Not and Angle Object")
        else:
            if(self.degrees<other.degrees):
                return -1
            elif(self.degrees==other.degrees):
                return 0
            else:
                return 1
    pass
            
            
            