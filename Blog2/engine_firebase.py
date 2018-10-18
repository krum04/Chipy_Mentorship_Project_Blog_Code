import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import obd
import time

cred = credentials.Certificate("link to firebase credentials")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'url for firebase datbase'})

ref = db.reference('/')

connection = obd.OBD('\\.\\COM3')
#Create a list of all possible PIDs
pidSens = ['ENGINE_LOAD',
        'COOLANT_TEMP',
        'SHORT_FUEL_TRIM_1',
        'LONG_FUEL_TRIM_1',
        'SHORT_FUEL_TRIM_2',
        'LONG_FUEL_TRIM_2',
        'FUEL_PRESSURE',
        'INTAKE_PRESSURE',
        'RPM',
        'SPEED',
        'TIMING_ADVANCE',
        'INTAKE_TEMP',
        'MAF',
        'THROTTLE_POS',
        'RUN_TIME',
        'DISTANCE_W_MIL',
        'FUEL_RAIL_PRESSURE_VAC',
        'FUEL_RAIL_PRESSURE_DIRECT',
        'FUEL_LEVEL',
        'WARMUPS_SINCE_DTC_CLEAR',
        'DISTANCE_SINCE_DTC_CLEAR',
        'EVAP_VAPOR_PRESSURE',
        'BAROMETRIC_PRESSURE',
        'O2_S1_WR_CURRENT',
        'O2_S2_WR_CURRENT',
        'O2_S3_WR_CURRENT',
        'O2_S4_WR_CURRENT',
        'O2_S5_WR_CURRENT',
        'O2_S6_WR_CURRENT',
        'O2_S7_WR_CURRENT',
        'O2_S8_WR_CURRENT',
        'CATALYST_TEMP_B1S1',
        'CATALYST_TEMP_B2S1',
        'CATALYST_TEMP_B1S2',
        'CATALYST_TEMP_B2S2',
        'CONTROL_MODULE_VOLTAGE',
        'ABSOLUTE_LOAD',
        'COMMANDED_EQUIV_RATIO',
        'RELATIVE_THROTTLE_POS',
        'AMBIANT_AIR_TEMP',
        'THROTTLE_POS_B',
        'THROTTLE_POS_C',
        'ACCELERATOR_POS_D',
        'ACCELERATOR_POS_E',
        'ACCELERATOR_POS_F',
        'THROTTLE_ACTUATOR',
        'RUN_TIME_MIL',
        'TIME_SINCE_DTC_CLEARED',
        'MAX_MAF',
        'FUEL_TYPE',
        'ETHANOL_PERCENT',
        'EVAP_VAPOR_PRESSURE_ABS',
        'EVAP_VAPOR_PRESSURE_ALT',
        'SHORT_O2_TRIM_B1',
        'LONG_O2_TRIM_B1',
        'SHORT_O2_TRIM_B2',
        'LONG_O2_TRIM_B2',
        'FUEL_RAIL_PRESSURE_ABS',
        'RELATIVE_ACCEL_POS',
        'HYBRID_BATTERY_REMAINING',
        'OIL_TEMP',
        'FUEL_INJECT_TIMING',
        'FUEL_RATE']
#Empty dictionary to hold supported PIDs & Values
supPids = {}
#Take full list of PIDs and pass them to the car's ECU, if a "None" response is received, they will not be added to supPids
def obdPidTest(pids):
    for pid in pids:
        cmd = obd.commands[pid]
        response = connection.query(cmd)
        if str(response) != 'None':
            supPids[pid]=response
#Take supPids dictionary and update the values
def obdRequest(dict):
    for key in dict:
        cmd = obd.commands[key]
        response = connection.query(cmd)
        dict[key] = str(response)
#Pass pidSens list to generate supPids dictionary
obdPidTest(pidSens)
#While statement to loop and print updates
while True:
    #Update supported PIDs and print the PID and Value
    obdRequest(supPids)
    #for key, val in supPids.items():
    ref.set({
            ('object'):
            supPids
            })
