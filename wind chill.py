#wind chill
import math
v = float(input('wind speed in kilometers/hour: '))
t = float(input('temperature in degree celsius: '))
wci = 13.12 + 0.6215*t - 11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
print ('the wind chill index is', int(round(wci, 0)))
