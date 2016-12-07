import math

class Angle():
    #Angle class for handling an angle representing degrees and minutes.
    
    def __init__(self):
        #set as default constructor

        self.degrees = 0.0
        self.minutes = 0.0
        self.originalDegree = 0

    def setDegrees(self, degrees=0.0):
        #Sets degrees and minutes using received float value which set by user
        try:
            self.minutes, self.degrees = math.modf(float(degrees))
        except Exception as e:
            try:
                self.degrees, self.minutes = int(degrees), 0
            except Exception as e:
                raise ValueError("Angle.setDegrees:  You Enter Invalid degrees value.")

        temporary = float((self.degrees % 360) + self.minutes) % 360
        self.minutes, self.degrees = math.modf(temporary)
        return temporary
        
    # setDegreesAndMinutes method receives angleString of type string.
    # It splits string with separator "d" and sets degrees and minutes.
    def setDegreesAndMinutes(self, angle_String1):
        """Sets degrees and minutes using received string value"""
        
        before_D = None
        after_D = None
        self.originalDegree = 0
        self.isMinus = False
        
        # the below code check received string is blank or not
        if angle_String1 == "":
            raise ValueError("Angle.setDegreesAndMinutes:  Please enter value of angle_String1 is blank.")

        # check separator exists or not
        elif "d" not in angle_String1:
            raise ValueError("Angle.setDegreesAndMinutes: Please enter value of Separator 'd' value not found.")

        # spit string with separator
        degreesAndMinutes = angle_String1.split("d")
        #check for degrees and minutes length
        if len(degreesAndMinutes) != 2:
            raise ValueError("Angle.setDegreesAndMinutes: You entered Invalid angle_String1.")

        elif "." in degreesAndMinutes[0]:
            raise ValueError("Angle.setDegreesAndMinutes:  You entered Invalid Degrees in angle_String1.")

        # if string is valid then
        else:
            #need to set variables by string parts
            before_D = degreesAndMinutes[0]
            after_D = degreesAndMinutes[1]

        # need to Validate beforeD part.
        try:
            # convert variable to integer
            before_D = int(before_D)
        except Exception as e:
            raise ValueError("Angle.setDegreesAndMinutes:  Not valid Degree part.")

        # Validate afterD part.
        try:
            # convert variable to float
            after_D = float(after_D)
        except Exception as e:
            raise ValueError("Angle.setDegreesAndMinutes:  Not valid Minute part.")

        if after_D < 0:
            raise ValueError("Angle.setDegreesAndMinutes: You Entered Negative Minute part.")

        if len(str(after_D).split(".")[1]) > 1:
            raise ValueError("Angle.setDegreesAndMinutes:  Not valid Minutes part.")
        #start from here to update
        self.originalDegree = before_D
        if before_D < 0:
            before_D = 360 - before_D - (int(after_D % 60) if after_D > 60 else 0)

        self.degrees = (before_D + (int(after_D % 60) if after_D > 60 else 0)) % 360
        self.minutes = (after_D % 60) / 60

        temp_add = float(self.degrees + self.minutes)
        if self.originalDegree < 0:
            return (360 - temp_add)
        else:
            return temp_add


    def addition(self, angle=None):
        #Addition degrees and minutes to current object from received object
        
        if not isinstance(angle, Angle):
            raise ValueError("Angle.addition:  received angle is not valid please enter valid angle.")

        if angle.originalDegree < 0:
            data = (float(self.degrees + self.minutes) - float(angle.degrees + angle.minutes)) % 360
        else:
            data = (float(self.degrees + self.minutes) + float(angle.degrees + angle.minutes)) % 360

        self.minutes, self.degrees = math.modf(data)
        return float(data)

    def subtraction(self, angle=None):
        #Subtraction degrees and minutes from current object from received object
        
        if not isinstance (angle, Angle):
            raise ValueError("Angle.subtraction:  received angle is invalid please enter valid angle.")

        if angle.originalDegree < 0:
            data = (float(self.degrees + self.minutes) + float(angle.degrees + angle.minutes)) % 360
        else:
            data = (float(self.degrees + self.minutes) - float(angle.degrees + angle.minutes)) % 360

        self.minutes, self.degrees = math.modf(data)
        return data

    # compare method compares received angle object with another.
    def comparition(self, angle=None):
        #comparition current object with received object
        
        if not isinstance (angle, Angle):
            raise ValueError("Angle.compare:  received angle is invalid please enter a valid angle.")

        if self.getDegrees() > angle.get_Degrees():
            return 1
        elif self.getDegrees() < angle.get_Degrees():
            return -1
        else:
            return 0
            
    def get_String(self):
        #Returns string representation of this object
        
        self.degrees = int(self.degrees)
        return str(self.degrees) + "d" + str(round(self.minutes * 60, 1))

    def get_Degrees(self):
        #Returns degrees as a floating point number
        
        degreesAndMinutes = (float(self.degrees + round(self.minutes * 60.0, 1) / 60.0)) % 360
        
        return ((360 - degreesAndMinutes) if self.originalDegree < 0 else degreesAndMinutes)
        