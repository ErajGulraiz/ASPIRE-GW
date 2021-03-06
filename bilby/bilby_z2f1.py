#!/usr/bin/env python
"""
Tutorial to demonstrate running parameter estimation on a reduced parameter
space for an injected signal.

This example estimates the masses using a uniform prior in both component masses
and distance using a uniform in comoving volume prior on luminosity distance
between luminosity distances of 100Mpc and 5Gpc, the cosmology is Planck15.
"""


from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

from bilby import *
from bilby.core.prior import Uniform
from astropy import *
from astropy.cosmology import Planck18
from astropy.cosmology import WMAP9 as cosmo
import numpy as np
import random
import bilby
#from file import *
from rerand import *

# Set the duration and sampling frequency of the data segment that we're
# going to inject the signal into
duration = 4.
sampling_frequency = 2048.

# Specify the output directory and the name of the simulation.
outdir = 'bilby_z2f1'
label = 'bilby_z2f1'
bilby.core.utils.setup_logger(outdir=outdir, label=label)

# Set up a random seed for result reproducibility.  This is optional!
np.random.seed(88170235)

# We are going to inject a binary black hole waveform.  We first establish a
# dictionary of parameters that includes all of the different waveform
# parameters, including masses of the two black holes (mass_1, mass_2),
# spins of both black holes (a, tilt, phi), etc.
z_ = [0.06,0.11]



injection_parameters = dict(
     mass_1= mass2[0], mass_2= 1.64562981, a_1=0.4, a_2=0.3, tilt_1=0.5, tilt_2=1.0,
    phi_12=1.7, phi_jl=0.3, luminosity_distance=np.array (cosmo.luminosity_distance ( np.mean ([z_[0],z_[1]]))), theta_jn=2.33576678, psi=2.659,
    phase=1.3, geocent_time=1126259642.413, ra=0.96971803, dec=-0.4911182)

# Fixed arguments passed into the source model
waveform_arguments = dict(waveform_approximant='IMRPhenomPv2',
                          reference_frequency=50., minimum_frequency=20.)

# Create the waveform_generator using a LAL BinaryBlackHole source function
waveform_generator = bilby.gw.WaveformGenerator(
    duration=duration, sampling_frequency=sampling_frequency,
    frequency_domain_source_model=bilby.gw.source.lal_binary_black_hole,
    parameter_conversion=bilby.gw.conversion.convert_to_lal_binary_black_hole_parameters,
    waveform_arguments=waveform_arguments)

# Set up interferometers.  In this case we'll use two interferometers
# (LIGO-Hanford (H1), LIGO-Livingston (L1). These default to their design
# sensitivity
ifos = bilby.gw.detector.InterferometerList(['H1', 'L1', 'V1', 'K1'])
ifos.set_strain_data_from_power_spectral_densities(
    sampling_frequency=sampling_frequency, duration=duration,
    start_time=injection_parameters['geocent_time'] - 3)
ifos.inject_signal(waveform_generator=waveform_generator,
                   parameters=injection_parameters)

# Set up a PriorDict, which inherits from dict.
# By default we will sample all terms in the signal models.  However, this will
# take a long time for the calculation, so for this example we will set almost
# all of the priors to be equall to their injected values.  This implies the
# prior is a delta function at the true, injected value.  In reality, the
# sampler implementation is smart enough to not sample any parameter that has
# a delta-function prior.
# The above list does *not* include mass_1, mass_2, theta_jn and luminosity
# distance, which means those are the parameters that will be included in the
# sampler.  If we do nothing, then the default priors get used.
priors = bilby.gw.prior.PriorDict()

##########################################
priors['geocent_time'] = bilby.core.prior.Uniform(
    minimum=injection_parameters['geocent_time'] - 1,
    maximum=injection_parameters['geocent_time'] + 1,
    name='geocent_time', latex_label='$t_c$', unit='$s$')
for key in ['a_1', 'a_2', 'tilt_1', 'tilt_2', 'phi_12', 'phi_jl', 'psi', 'ra','dec', 'geocent_time', 'phase']:
	priors[key] = injection_parameters[key]
priors['mass_1'] = bilby.core.prior.Uniform(name='mass_1', minimum=1, maximum=50, unit='$M_{\\odot}$')
priors['mass_2'] = bilby.core.prior.Uniform(name='mass_2', minimum=1, maximum=2, unit='$M_{\\odot}$')

priors['theta_jn'] =Uniform(name = 'theta_jn', minimum=0, maximum=np.pi)
priors['luminosity_distance'] =Uniform(name = 'luminosity_distance', minimum=10, maximum=5000, unit = 'Mpc')

#############################################

#priors['geocent_time'] = bilby.core.prior.Uniform(
  #  minimum=injection_parameters['geocent_time'] - 1,
  #  maximum=injection_parameters['geocent_time'] + 1,
   # name='geocent_time', latex_label='$t_c$', unit='$s$')
    
#for key in ['a_1', 'a_2', 'tilt_1', 'tilt_2', 'phi_12', 'phi_jl', 'psi', 'ra','dec', 'geocent_time', 'phase']:
    #priors[key] = injection_parameters[key]
    
#priors['mass_1'] = bilby.core.prior.Uniform(name='mass_1', minimum=1, maximum=50, unit='$M_{\\odot}$')

#priors['mass_2'] = bilby.core.prior.Uniform(name='mass_2', minimum=1, maximum=2, unit='$M_{\\odot}$')


# Initialise the likelihood by passing in the interferometer data (ifos) and
# the waveform generator
likelihood = bilby.gw.GravitationalWaveTransient(
    interferometers=ifos, waveform_generator=waveform_generator)

# Run sampler.  In this case we're going to use the `dynesty` sampler
result = bilby.run_sampler(
    likelihood=likelihood, priors=priors, sampler='dynesty', npoints=1000,
    injection_parameters=injection_parameters, outdir=outdir, label=label)


result.plot_corner()
