#  real number - precision in program
import sys 
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49

print(f"ideal temp {ideal_temp}")
print(f"current temp {current_temp}")
print(f"diff temp. {ideal_temp-current_temp}")
print(sys.float_info)
