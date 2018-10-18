#import our obd library
import obd
#OBD() will search for a serial connection
connection = obd.OBD()
#We will pass in our argument "RPM" and query the ECU for a response
pid = 'RPM'
cmd = obd.commands[pid]
response = connection.query(cmd)
#print said response
print(response)
