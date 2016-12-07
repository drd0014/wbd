import datetime
import time
import os
from xml.etree import ElementTree
import Angle as Angle
from math import *
class Fix():
    """Fix class to perform different calculation based on sightings, aries and stars."""
    
    def __init__(self, logFile="log.txt"):
        """Constructor"""
        
        self.errors = 0
        self.approximate_Latitude = 0.0
        self.approximate_Longitude = 0.0
        self.assumedLat = None
        self.assumedLon = None
        self.hemi = ""
        
        if not isinstance(logFile, str) or len(logFile) < 1:
            self.raiseException("Fix.__init__: file name not valid the parameter specification.")

        try:
            txtFile = open(logFile, "a")
            time_stamp = time.time()
            tmp_1 = datetime.datetime.utcfromtimestamp(time_stamp)
            tmp_2 = tmp_1.replace(tzinfo=time.timezone.utc)
            tmp_3 = tmp_2.astimezone()
            local_time = tmp_3.replace(microsecond=0)

            self.txtFile = txtFile
            self.txtFile.write("LOG: " + str(local_time) + " Log file:\t" + os.path.realpath(logFile) + "\n")
        except:
            self.raiseException("Fix.__init__: Log file can not be created or appended for whatever reasons.")

    def raiseException(self, msg):
        #generate a value error with received message
        print msg
        raise ValueError(str(msg))

    def set_AriesFile(self, ariesFile=""):
        #Sets the aries file

        if len(ariesFile.split(".")[0]) < 1:
            self.raiseException("Fix.setAriesFile:  Received Filename is Not valid")

        if ariesFile.split(".")[1] != "txt":
            self.raiseException("Fix.setAriesFile:  Received Filename is Not valid")

        time_stamp = time.time()
        tmp_1 = datetime.datetime.utcfromtimestamp(time_stamp)
        tmp_2 = tmp_1.replace(tzinfo=time.timezone.utc)
        tmp_3 = tmp_2.astimezone()
        local_time = tmp_3.replace(microsecond=0)

        self.ariesFile = ariesFile

        try:
            f = open(self.ariesFile, "r")
            f.close()
        except Exception as e:
            self.raiseException("Fix.setAriesFile:  Aries file could not be opened")

        self.txtFile.write("LOG: " + str(local_time) + " Aries file:\t" + os.path.realpath(self.ariesFile) + " \n")

        return os.path.realpath(self.ariesFile)

    def set_StarFile(self, starFile=""):
        """Sets the star file"""

        if len(starFile.split(".")[0]) < 1:
            self.raiseException("Fix.setStarFile:  Received Filename is not valid")

        if (starFile.split(".")[1]) != "txt":
            self.raiseException("Fix.setStarFile:  Received Filename is not valid")

        time_stamp = time.time()
        tmp_1 = datetime.datetime.utcfromtimestamp(time_stamp)
        tmp_2 = tmp_1.replace(tzinfo=time.timezone.utc)
        tmp_3 = tmp_2.astimezone()
        local_time = tmp_3.replace(microsecond=0)

        self.starFile = starFile
        self.txtFile.write("LOG: " + str(local_time) + " Star file:\t" + os.path.realpath(self.starFile) + " \n")

        try:
            f = open(self.starFile, "r")
            f.close()
        except Exception as e:
            self.raiseException("Fix.setStarFile:  Star file not opened")

        return os.path.realpath(self.starFile)

    def get_Sightings(self,assumed_Latitude="0d0.0", assumed_Longitude="0d0.0"):
        #Performs all the calculations for each sighting record
        
        if not self.sightingFile or not self.ariesFile or not self.starFile:
            self.raiseException("Fix.getSightings:  sighting File and/or aries File and/or star File not set.")

        if not isinstance(assumed_Latitude, str):
            self.raiseException("Fix.getSightings:  Not valid assumed Latitude.")

        for char in assumed_Latitude:
            if char == "N":
                self.hemi = char
                assumed_Latitude = assumed_Latitude.replace(char, "")

            elif char == "S":
                self.hemi = char
                assumed_Latitude = assumed_Latitude.replace(char, "")

        degreesAndMinutes = assumed_Latitude.split("d")
        degree = int(degreesAndMinutes[0])
        if degree < 0 or degree >= 90:
            self.raiseException("Fix.getSightings:  Not valid degrees of assumed_Latitude.")
            
        minutes = float(degreesAndMinutes[1])
        if minutes < 0 or minutes >= 60:
            self.raiseException("Fix.getSightings:  Not valid minutes of assumed_Latitude.")

        self.assumed_Latitude = assumed_Latitude
        self.assumed_Longitude = assumed_Longitude

        degreesAndMinutes = assumed_Longitude.split("d")

        degree = int(degreesAndMinutes[0])
        if degree < 0 or degree >= 90:
            self.raiseException("Fix.getSightings:  Not valid degrees of assumed_Longitude.")

        minutes = float(degreesAndMinutes[1])
        if minutes < 0 or minutes >= 60:
            self.raiseException("Fix.getSightings:  Not valid minutes of assumed_Longitude.")

        try:
            tree = ElementTree.parse(self.sightingFile)  # VALUE ERROR 1 OPENING FILE
        except :
            self.raiseException("Fix.getSightings:  No sighting file has been set.")

        sightings = tree.findall("sighting")
        self.errorString = ""
        try:
            self.calculate(sightings)
            self.txtFile.close()
            return (self.approximateLat, self.approximateLon)
        except:
            self.raiseException("Fix.getSightings:  Some values are Missing.")

    
    def calculate(self,sightings):
        #Performs all the calculations for received sighting
        
        try:
            dataList = []

            for element in sightings:
                dataDict = {}
                try:
                    dataDict["body"] = element[0].text
                except:
                    self.errors += 1
                    self.errorString += "Body not found"
                    continue

                try:
                    dataDict["dt"] = element[1].text
                except:
                    self.errors += 1
                    self.errorString += "Date not found"
                    continue
                try:
                    dataDict["time"] = element[2].text
                except:
                    self.errors += 1
                    self.errorString += "Time not found"
                    continue
                try:
                    dataDict["observation"] = element[3].text
                except:
                    self.errors += 1
                    self.errorString += "Observation not found"
                    continue

                try:
                    dataDict["height"] = element[4].text

                except:
                    dataDict["height"] = "0"

                try:
                    dataDict["temperature"] = float(element[5].text)
                except :
                    dataDict["temperature"] = 72

                try:
                    dataDict["pressure"] = element[6].text

                except :
                    dataDict["pressure"] = "1010"

                try:
                    dataDict["horizon"] = element[7].text
                except :
                    dataDict["horizon"] = "Natural"

                newAngle = Angle.Angle()
                newAngle.setDegreesAndMinutes(dataDict["observation"])

                dip = 0.0
                if  dataDict["horizon"].strip() == "natural":
                    dip = (-0.97 * sqrt(float( dataDict["height"].strip()))) / 60.0

                celcius = ( dataDict["temperature"] - 32) * 5.0 / 9.0
                newAngle.setDegreesAndMinutes( dataDict["observation"].strip())
                altitude = newAngle.get_Degrees()

                refraction = -0.00452 * float(dataDict["pressure"].strip()) / float(273 + celcius) / tan(radians(altitude))
                adjusted_Altitude = altitude + dip + refraction
                newAngle.setDegrees(adjusted_Altitude)
                adjusted_Altitude = newAngle.get_Degrees()

                hours = dataDict["time"].split(":")[0]
                minutes = dataDict["time"].split(":")[1]
                seconds = dataDict["time"].split(":")[2]

                s = (int(minutes) * 60) + int(seconds)
                formatedDate = datetime.datetime.strptime(dataDict["dt"], '%Y-%m-%d').strftime('%m/%d/%y')

                SHAstarObj = Angle.Angle()
                flag = False
                with open(self.starFile, 'r+') as starFile:
                    for line in starFile:
                        name = line.split("\t")[0]
                        tempDt = line.split("\t")[1]
                        if name == dataDict["body"] and tempDt <= formatedDate:
                            tempStarLine = line
                            flag = True

                    if(not flag):
                        self.errors += 1
                        self.errorString += "Name or date not Found please enter proper data"
                        continue


                self.SHAstar = SHAstarObj.setDegreesAndMinutes(tempStarLine.split("\t")[2])
                self.latitude = (tempStarLine.split("\t")[3]).strip()

                angleObj1 = Angle.Angle()
                angleObj2 = Angle.Angle()

                tempAriesLine1 = ""
                tempAriesLine2 = ""
                with open(self.ariesFile, 'r+') as ariesFile:
                    for line in ariesFile:
                        tempDate = line.split("\t")[0]
                        tempHour = line.split("\t")[1]

                        hours = int(hours)
                        tempHour = int(tempHour)
                        if tempDate == formatedDate and tempHour == hours:
                            tempAriesLine1 = line
                            tempAriesLine2 = next(ariesFile).split("\t")[2]
                            break

                self.GHAaries1 = angleObj1.setDegreesAndMinutes(tempAriesLine1.split("\t")[2])
                self.GHAaries2 = angleObj2.setDegreesAndMinutes(tempAriesLine2)

                self.GHAaries = self.GHAaries1 + abs(self.GHAaries2 - self.GHAaries1) * (s / 3600)

                GHAariesObj = Angle.Angle()
                GHAariesObj.setDegrees(self.GHAaries)

                GHAariesObj.add(SHAstarObj)
                self.GHAobservation = GHAariesObj.getDegrees()

                asLatObj = Angle.Angle()
                asLatObj.setDegreesAndMinutes(self.assumedLatitude)
                asLat = asLatObj.getDegrees()
                if self.hemi == "S":
                    asLat = -asLat

                asLongObj = Angle.Angle()
                asLongObj.setDegreesAndMinutes(self.assumedLongitude)
                asLong = asLongObj.getDegrees()

                LHAObj = Angle.Angle()
                LHAObj.setDegreesAndMinutes(GHAariesObj.getString())
                LHAObj.add(asLongObj)
                LHA = LHAObj.getDegrees()

                latitudeObj = Angle.Angle()
                latitudeObj.setDegreesAndMinutes(self.latitude)

                interDistance = sin(radians(latitudeObj.getDegrees())) * sin(radians(asLat)) + cos(radians(latitudeObj.getDegrees())) * cos(radians(asLat)) * cos(radians(LHA))

                correctedAltitude = degrees(asin(interDistance))

                distanceAdjustment = int(round((correctedAltitude - adjusted_Altitude) * 60, 0))
                dataDict['distanceAdjustment'] = distanceAdjustment

                numerator = sin(radians(latitudeObj.getDegrees())) - sin(radians(asLat)) * interDistance
                denominator = cos(radians(asLat)) * cos(radians(correctedAltitude))

                interAzimuth = numerator / denominator
                azimuthAdjustment = degrees(acos(interAzimuth))

                azimuthAdjustmentObj = Angle.Angle()
                azimuthAdjustmentObj.setDegrees(abs(azimuthAdjustment))
                dataDict['azimuthAdjustmentFloat'] = azimuthAdjustment
                dataDict['azimuthAdjustment'] = ("-" if azimuthAdjustment < 0 else "") + azimuthAdjustmentObj.getString()
                dataDict['assumedLatitude'] = "N" + asLatObj.getString() if asLat > 0 else str("S" + asLatObj.getString())
                dataDict['assumedLongitude'] = asLong
                dataDict['dttim'] = datetime.datetime.strptime(dataDict["dt"] + " " + dataDict["time"], "%Y-%m-%d %H:%M:%S")
                dataDict['degrees'] = newAngle.getString()
                dataDict['latitude'] = self.latitude
                dataDict['longitude'] = GHAariesObj.getString()

                dataList.append(dataDict)

            dataList.sort(key=lambda k: k['body'])
            dataList.sort(key=lambda k: k['dttim'])

            latSum = 0.0
            longSum = 0.0
            for data in dataList:
                time_stamp = time.time()
                tmp_1 = datetime.datetime.utcfromtimestamp(time_stamp)
                tmp_2 = tmp_1.replace(tzinfo=time.timezone.utc)
                tmp_3 = tmp_2.astimezone()
                local_time = tmp_3.replace(microsecond=0)
                self.txtFile.write(
                    "LOG: " + str(local_time) + " " + data["body"] + "\t" + data["dt"] + "\t" + data["time"] + "\t"
                    + data['degrees'] + "\t" + data['latitude'] + "\t" + data['longitude'] + "\t"
                    + dataDict['assumedLatitude'] + "\t"
                    + asLongObj.getString() + "\t" + data['azimuthAdjustment'] + "\t"
                    + str(data['distanceAdjustment']) + "\n")

                latSum += data['distanceAdjustment'] * cos(radians(data['azimuthAdjustmentFloat']))
                longSum += data['distanceAdjustment'] * sin(radians(data['azimuthAdjustmentFloat']))

            approximate_Latitude = asLat + (latSum / 60)
            approximate_Longitude = asLong + (longSum / 60)

            approximateLatitudeObj = Angle.Angle()
            approximateLatitudeObj.setDegrees(abs(approximate_Latitude))
            appLat = approximateLatitudeObj.getString()
            if approximate_Latitude < 0:
                appLat = "S" + appLat
            elif approximate_Latitude > 0:
                appLat = "N" + appLat

            approximateLongitudeObj = Angle.Angle()
            approximateLongitudeObj.setDegrees(approximate_Longitude)
            appLong = approximateLongitudeObj.getString()

            time_stamp = time.time()
            tmp_1 = datetime.datetime.utcfromtimestamp(time_stamp)
            tmp_2 = tmp_1.replace(tzinfo=time.timezone.utc)
            tmp_3 = tmp_2.astimezone()
            local_time = tmp_3.replace(microsecond=0)

            self.txtFile.write("LOG: " + str(local_time) + " Sighting errors:" + "\t" + str(self.errors) + "\n")
            self.txtFile.write("LOG: " + str(local_time) + "\t" + "Approximate latitude:\t" + appLat + "\tApproximate longitude:\t" + appLong + "\n")
            self.txtFile.write("LOG: " + str(local_time) + "\t" + "End of sighting file " + self.sightingFile)

            self.approximateLat = asLat
            self.approximateLon = asLong

        except:
            self.raiseException("Fix.calculate:  Mandatory tag is missing or the information associated with a tag is not valid.")
    def set_SightingFile(self, sightingFile=""):
        #Sets the sighting file
        
        if len(sightingFile.split(".")[0]) < 1:
            self.raiseException("Fix.setSightingFile:  The sighting file name not valid the parameter specification.")

        if (sightingFile.split(".")[1]) != "xml":
            self.raiseException("Fix.setSightingFile:  Not valid sightingFile.")

        time_stamp = time.time()
        tmp_1 = datetime.datetime.utcfromtimestamp(time_stamp)
        tmp_2 = tmp_1.replace(tzinfo=time.timezone.utc)
        tmp_3 = tmp_2.astimezone()
        local_time = tmp_3.replace(microsecond=0)

        try:
            xmlFile = open(sightingFile, "r")
            xmlFile.close()
        except:
            self.raiseException("Fix.setSightingFile:  The sighting file not found or could not be opened.")

        self.sightingFile = sightingFile
        self.txtFile.write("LOG: " + str(local_time) + " Sighting file\t" + os.path.realpath(self.sightingFile) + "\n")

        return os.path.realpath(self.sightingFile)
