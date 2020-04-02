"""
Use this file to hold parameters that are in the SOW or elsewhere that
influence the design of the entire plant. This provides an easy mechanism
for all of us to share the same assumptions.

"""

import aguaclara as ac
from aguaclara.core.units import unit_registry as u

"""Constants or assumptions from the SOW"""

# Plant flow variability
q_max = (480 * u.Mgal/u.day).to(u.kL/u.s)
q_ave = (320 * u.ft**3/u.s).to(u.kL/u.s)
# q_min = need to find this value

# Turbidity assumptions
turbidity_c_in_ave = 14 * u.NTU
turbidity_c_out_ave = 3 * u.NTU

# Coagulant assumptions
# This is the iron concentration, not the FeCl3 concentration
Fe_c_ave = 13.14 * u.mg/u.L

# Arsenic
As_c_in_ave = 25 * u.ug/u.L
As_m = (q_ave * As_c_in_ave).to(u.kg/u.day)

"""Regulations that influence the design"""

# waiting for some of these!

"""
Assumptions that we are making that influence the entire design.
This will include the number of treatment trains
and more as our design progresses.
"""
# n_train = x
