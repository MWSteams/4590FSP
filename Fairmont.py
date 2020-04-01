import aguaclara as ac
from aguaclara.core.units import unit_registry as u

Q_max = (480 * u.Mgal/u.day).to(u.kL/u.s)
Q_ave = (320 * u.ft**3/u.s).to(u.kL/u.s)
#Q_min = need to find this value
#N_train = 1

Fe_C_ave = 13.14 * u.mg/u.L

As_Cin_ave = 25 * u.ug/u.L
As_M = (Q_ave * As_Cin_ave).to(u.kg/u.day)

Turbidity_Cin_ave = 14 * u.NTU
Turbidity_Cout_ave = 3 * u.NTU
