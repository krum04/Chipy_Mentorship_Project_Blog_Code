#import our obd library
import obd

#OBD() will search for a serial connection
connection = obd.OBD()

#Function to pass list through obd and print respnses
def obdRequest(pidList):
    for pid in pidList:
        cmd = obd.commands[pid]
        response = connection.query(cmd)
        print(response)
        
list = ['SPEED','RPM','RUN_TIME']
obdRequest(list)
