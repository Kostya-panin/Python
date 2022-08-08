#Самая далекая планета
#S=pab
from difflib import Match
import math


list_of_orbits= [(1,3),(2.5,10),(7,2),(6,6),(3,3),(9,9)]

def find_farthest_orbits(list_of_orbits):
    j=0
    p=math.pi
    farthest_orbits = [i for i in list_of_orbits if (not(i[j]==i[j+1]))]
    max=0
    j=0
    for i in farthest_orbits:
            max=i[j]*i[j+1]*p
            farthest_orbits=i
    return farthest_orbits
print(find_farthest_orbits(list_of_orbits))





