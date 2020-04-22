"""
Use this file to hold parameters that are in the SOW or elsewhere that
influence the design of the entire plant. This provides an easy mechanism
for all of us to share the same assumptions.

"""

import aguaclara as ac
from aguaclara.core.units import unit_registry as u

"""Constants or assumptions from the SOW"""

# Length and Width of project site (pending)
project_w = 1 * u.m
project_l = 1 * u.m
project_a = project_w * project_l

# Plant flow variability

# from Table VI-2 of SOW
q_max = (720 * u.ft**3/u.s).to(u.kL/u.s)
# from page 16 of SOW
q_ave = (320 * u.ft**3/u.s).to(u.kL/u.s)
# q_min = need to find this value

# Turbidity assumptions

# from Table VIII_1 of SOW
# were derived from the 99th percentile maximum 10‐year
turbidity_c_in_design = 23 * u.NTU
# from page 16 of SOW
turbidity_c_in_ave = 14 * u.NTU

# from Table VIII_1 of SOW
turbidity_c_out_design = 3 * u.NTU


# Coagulant assumptions
# This is the FeCl3 concentration
Fe_c_ave = 13.14 * u.mg/u.L

# Arsenic
As_c_in_ave = 25 * u.ug/u.L

# from Table VIII_1 of SOW
As_c_in_design = 55 * u.ug/u.L
As_c_out_design = 10 * u.ug/u.L

As_m = (q_ave * As_c_in_ave).to(u.kg/u.day)

# organic carbon
# from Table VIII_1 of SOW
C_c_in_design = 4 * u.mg/u.L
C_c_out_design = 3 * u.mg/u.L

# energy use
# from Table XV-1 of SOW
electricity_power = (9377471 * u.kW*u.hr/u.year).to(u.kW)

"""Regulations that influence the design"""

# waiting for some of these!

"""
Assumptions that we are making that influence the entire design.
This will include the number of treatment trains
and more as our design progresses.

The following parameter values are currently randomly assigned by Monroe. 
The dimensions are for ONE of the units with n units total
"""
#random by Monroe
n_rm_hyd = 4
#random by Monroe
L_rm_hyd = 3 * u.m
#random by Monroe
W_rm_hyd = 3 * u.m

#random by Monroe
n_rm_mech = 4
#random by Monroe
L_rm_mech = 3 * u.m
#random by Monroe
W_rm_mech = 3 * u.m

#random by Monroe
n_floc_hyd = 4
#random by Monroe
L_floc_hyd = 10 * u.m
#random by Monroe
W_floc_hyd = 10 * u.m

#random by Monroe
n_floc_mech = 4
#random by Monroe
L_floc_mech = 10 * u.m
#random by Monroe
W_floc_mech = 10 * u.m

#random by Monroe
n_sed_hyd = 16
#random by Monroe
L_sed_hyd = 10 * u.m
#random by Monroe
W_sed_hyd = 40 * u.m

#random by Monroe
n_sed_mech = 16
#random by Monroe
L_sed_mech = 10 * u.m
#random by Monroe
W_sed_mech = 40 * u.m
