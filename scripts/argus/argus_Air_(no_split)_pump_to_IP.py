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
#    sleep(10)
    close('I')
    close('A')
    close('B')
    close('D')
    sleep (2)
    open('H')

    if DEBUG:
        sleep(10)
    else:
        sleep(60)
    
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