#!Measurement
'''
baseline:
  after: true
  before: false
  counts: 10
  detector: H1
  mass: 39.5
  settling_time: 10.0
default_fits: nominal
equilibration:
  eqtime: 15.0
  inlet: C
  inlet_delay: 3
  outlet: E
  use_extraction_eqtime: false
multicollect:
  counts: 150
  detector: H1
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H1
  isotope: Ar40
peakhop:
  hops_name: hop_ic
  use_peak_hop: true
'''

ACTIVE_DETECTORS=('H1','AX','L1','L2', 'CDD')

def main():
    #this is a comment
    '''
        this is a multiline
        comment aka docstring
    '''
    #display information with info(msg)
    info('unknown measurement script')

    #set the spectrometer parameters
    #provide a value
    #set_source_parameters(YSymmetry=10)

    #or leave blank and values are loaded from a config file (setupfiles/spectrometer/config.cfg)
    #set_source_optics()

    #set the cdd operating voltage
    #set_cdd_operating_voltage(100)

    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)

    #open a plot panel for this detectors
    activate_detectors(*ACTIVE_DETECTORS)

    if mx.baseline.before:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector)

    #position mass spectrometer
    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)

    #gas is staged behind inlet

    #post equilibration script triggered after eqtime elapsed
    #equilibrate is non blocking
    #so use either a sniff of sleep as a placeholder until eq finished
    if mx.equilibration.use_extraction_eqtime:
        e = ex.eqtime
    else:
        e = mx.equilibration.eqtime

    equilibrate(eqtime=e, inlet=mx.equilibration.inlet, 
    delay=mx.equilibration.inlet_delay,
    outlet=mx.equilibration.outlet)

    #equilibrate returns immediately after the inlet opens
    set_time_zero()

    sniff(e)
    #set default regression
    set_fits()
    set_baseline_fits()

    #multicollect on active detectors
    multicollect(ncounts=mx.multicollect.counts, integration_time=1)

    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector,
                  settling_time=mx.baseline.settling_time)

    if mx.peakcenter.after:
        activate_detectors(*mx.peakcenter.detectors, **{'peak_center':True})
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope, 
                    integration_time=mx.peakcenter.integration_time)
    info('finished measure script')

#========================EOF==============================================================
