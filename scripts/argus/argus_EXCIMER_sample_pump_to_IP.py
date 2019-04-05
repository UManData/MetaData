#===============================================================================
# EXTRACTION SCRIPT argus_EXCIMER_sample_pump_to_IP.py
#===============================================================================
"""
"""

def main():
    info('Excimer sample')
    
    # prepare for analysis
    close(description='Prep IG')
    sleep(10)
    close('D') # Ion Pump
    open('B') # CO2 inlet In this configuration gas is cleaned by hot getter in CO2 line
    sleep(2)
    
    if analysis_type=='blank':
        info('is blank. not heating')
        sleep(196)
    else:
        info('Starting long delay for user to manually fire laser')
        sleep(76) # change this number to be equivalent to ablation time
            
    close(description='MS IG')
    sleep(cleanup)
#===============================================================================
# POST EQUILIBRATION SCRIPT argus_pump_sample_to_IP.py
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
    open(name="B", description="CO2 Inlet")
    open(name="A", description="Excimer Inlet")
    open(name="D", description="Ion Pump")
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
