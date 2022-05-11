#UnderGround Railway System.
from collections import defaultdict
class UnderGroundRailway():
    
    def __init__(self):
        self.check_in_data={}
        self.time_taken_data=defaultdict(lambda:[0,0])
    def checkIn(self,Id,startStation,time):
        self.check_in_data[Id]=[startStation,time]
        print("Null")
    def checkOut(self,Id,endStation,time):
        startStation,startTime=self.check_in_data[Id]
        self.time_taken_data[(startStation,endStation)][0]+=(time-startTime)
        self.time_taken_data[(startStation,endStation)][1]=self.time_taken_data[(startStation,endStation)][1]+1
        print("Null")
    def averageTime(self,startStation,endStation):
        timeTaken,totalEntries=self.time_taken_data[(startStation,endStation)]
        print(timeTaken/totalEntries)
if __name__=="__main__":
    command_Array=["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
    data_Array=[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
    obj=UnderGroundRailway()
    for i in range(1,len(command_Array)):
        if(command_Array[i]=="checkIn"):
            obj.checkIn(data_Array[i][0],data_Array[i][1],data_Array[i][2])
        elif(command_Array[i]=="checkOut"):
            obj.checkOut(data_Array[i][0],data_Array[i][1],data_Array[i][2])
        else:
            obj.averageTime(data_Array[i][0],data_Array[i][1])
