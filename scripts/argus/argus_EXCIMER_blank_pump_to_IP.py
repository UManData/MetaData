#===============================================================================
# EXTRACTION SCRIPT argus_EXCIMER_blank_pump_to_IP.py
#===============================================================================
"""
"""

def main():
    info('EXCIMER sample')
    
    # prepare for analysis
    close(description='Prep IG')
    
    if analysis_type=='blank':
        info('is blank. not heating')
        close('B') # close CO2 inlet
        sleep(2)
        close('D') # Ion Pump
        sleep(2)
        sleep(100) # Ablation time (s) + sleep time (2s): 5 s warmup not taken into account
        #if ramp_duration>0:
        #    '''
        #    #style 1.
        #    '''
        #    begin_interval(duration)
        #   info('ramping to {}. ramp_duration={}'.format(extract_value, ramp_duration))
        #    ramp(setpoint=extract_value, duration=ramp_duration)
        #    complete_interval()
    else:
        info('move to position {}'.format(position))
        move_to_position(position)
        
        # prepare for extraction
        close('B') # close CO2 inlet
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
            
    end_extract()
    disable()
    
    close(description='MS IG')
    sleep(cleanup)
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
