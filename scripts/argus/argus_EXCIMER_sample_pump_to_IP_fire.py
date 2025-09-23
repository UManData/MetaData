#===============================================================================
# EXTRACTION SCRIPT argus_EXCIMER_sample_pump_to_IP_fire.py
#===============================================================================
"""
"""

def main():
    info('Excimer sample')
    
    # prepare for analysis
    close(description='Prep IG')
    close(name="B", description="CO2 Inlet")
    sleep(2)
       
    if analysis_type=='blank':
        info('is blank. not heating')
        close(name="B", description="CO2 Inlet")
        sleep(62) # Ablation time (s) + 2 sleep after closing valve 30 s warmup not taken into account
    else:
        # info('Starting long delay for user to manually fire laser')
        # sleep(54) # change this number to be equivalent to ablation time
        info('Starting uv scans')

        for i, pi in enumerate(position):
            # position should be a scan number
            if pi.startswith('s'):
                info('move to scan position {}'.format(pi))
                
                #move to the start of the scan. wait until reached destination
                move_to_position(pi)
                
                sleep(1)
                if not i:
                    warmup()
                    sleep(2)
                    close('D') # Ion Pump
                    close('B') # CO2 Inlet
                    # close to pumps
                    close('O')
                    #sleep(60)
                
                # run the active scan. wait until completed
                extract()
                info('scan {} complete'.format(pi))
                
        
            
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
