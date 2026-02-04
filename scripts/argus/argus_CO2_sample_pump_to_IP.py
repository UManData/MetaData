#===============================================================================
# EXTRACTION SCRIPT argus_CO2_sample_pump_to_IP.py
#===============================================================================
"""
"""

def main():
    info('CO2 sample')
    
    # prepare for analysis
    open('B')
    close(description='Prep IG')
    sleep(30)
    
    if analysis_type=='blank':
        info('is blank. not heating')
        close('A') # excimer inlet
        sleep(2)
        close('D') # Ion Pump
        sleep(2)
        sleep(240) # Getter time (180s) + ramp (20s) and heating (40s) CO2 time
        #sleep(300) # Getter time (240) + ramp (20s) and heating (40s) CO2 time (TF mica)
        #sleep(100) # ramp (20s) and heating (80s) CO2 time (TF Sanidine, Olduvai)
        #sleep(80) # ramp (20s) + heating (60s) CO2 time (SH)
        open('B') # CO2 inlet
        
    else:
        info('move to position {}'.format(position))
        move_to_position(position)
        
        # prepare for extraction
        close('A') # excimer inlet
        sleep(2)
        close('D') # Ion Pump
        sleep(2)
        enable()
        fire_laser()
        if ramp_duration>0:
            '''
            style 1.
            '''
            begin_interval(duration)
            info('ramping to {}. ramp_duration={}'.format(extract_value, ramp_duration))
            ramp(setpoint=extract_value, duration=ramp_duration)
            complete_interval()
            
        else:
            extract()
            sleep(duration)
    open('B')
            
    end_extract()
    disable()
    
    close(description='MS IG')
    #sleep(10)
    #close('B')
    sleep(cleanup)
#===============================================================================
# POST EQUILIBRATION SCRIPT argus_pump_sample_to_turbo.py
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
    open('B')
    #open(description='Excimer Inlet')
    close('D')
    open('A')
    close(description='Prep IG')

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
