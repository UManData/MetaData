#===============================================================================
# EXTRACTION SCRIPT argus_Air_(no_split)_pump_to_IP.py
#===============================================================================
"""
modifier: 01
"""
DEBUG = False

def main():
    info('Air (no split) pump to IP')
# Evacuating Ar pipette    
    open('D')
    open('H')
    
    if DEBUG:
        sleep(10)
    else:
        sleep(120)
    
# Filling Ar pipette
    close('H')
    sleep (2)
    open('D')
    if analysis_type=='blank':
        info('analysis is a blank. not filling pipette')
    else:
        open('I')
        
    if DEBUG:
        sleep(10)
    else:
        sleep(120)
# Expand Ar pipette volume into manifold volume
    close(description='Prep IG')
    sleep(10)
    close('I')
    close('A')
    close('B')
    close('D')
    sleep (2)
    open('H')

    if DEBUG:
        sleep(10)
    else:
        sleep(120)
    
# Expand manifold volume into MS
    close('H')
    
    if DEBUG:
        sleep(10)
    else:
        sleep(60)
    
    close(description='MS IG')
    sleep(10)
    #close('E')
    #sleep(2)
    #open('C')
#===============================================================================
# POST EQUILIBRATION SCRIPT argus_pump_air_to_IP.py
#===============================================================================
"""
"""

# '---Equilibrate gas into mass spectrometer
# '---First, if overlapping runs, make sure spectrometer
# '---has been pumped down for the minimum time specified
# IF OverlapRuns
#     BeginInterval RemainingSpecPumpdown
#         Message "Waiting for minimum spectrometer pumpdown--"
#     CompleteInterval
# END if
# '---Now equilibrate gas from extraction line into MS
# Close "MS IG"
# BeginInterval 10
# CompleteInterval
# Close MSIonPump    '---Close Spec/Ion Pump valve
# Delay 3
# Open ExtrToMS    '---Open spec/extr. line valve
# Message "Allowing equilibration--"
# Equil    '---Doing gas equilibration subroutine
# '---End of equilibration, set valves for analysis
# Close ExtrToMS             '---Close spec/Getter valve
# Delay 2
# Open "Inlet 1"
# Open "Inlet 2"
# Open "Prep IG"
# '---Valves set for analysis, measure the gas
# MeasureGas
# Delay 2
# Open MSIonPump
# Open "MS IG"


def main():
    info('pump sample')    
    open('D') # Ion pump extraction line
    open('B') # CO2 Inlet
    open('A') # Excimer Inlet

#===============================================================================
# POST MEASUREMENT SCRIPT argus_pump_ms.py
#===============================================================================
"""
"""

# Open "MS IG"


def main():
    info('pump ms')
    open(description='MSIonPump')
    close(description='MS IG')
