import aguaclara as ac
from aguaclara.core.units import unit_registry as u

LAAWFP_Q = 480 * u.Mgal/u.day
LAAWFP_As_C = 25 * u.ug/u.L
LAAWFP_As_M = (LAAWFP_Q * LAAWFP_As_C).to(u.kg/u.day)
