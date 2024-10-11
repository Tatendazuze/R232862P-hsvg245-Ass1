#Calculate_polar
import math
Ys = float(input("enter Ys Y coordinate of S in meters:"))
Xs = float(input("enter Xs X coordinate of S in meters:"))
distance = float(input("enter distance S-T in meters:"))
direction = float(input("enter direction S-T in degrees:"))
Yt = Ys + distance*math.sin((direction/180)*math.pi)
Xt = Xs + distance*math.cos((direction/180)*math.pi)
print(f'Ys Y coordinate: {Ys} meters')
print(f'Xs X coordinate: {Xs} meters')