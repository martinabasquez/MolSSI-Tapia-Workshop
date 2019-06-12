import os
import numpy
import sys

file_location = sys.argv[1]
xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
symbols = xyz_file[:,0]
coordinates = xyz_file[:,1:]
print(symbols)
coordinates = coordinates.astype(numpy.float)
print(coordinates)
num_atoms = len(symbols)
print(num_atoms)
for num1 in range(0,num_atoms):
    for num2 in range(0, num_atoms):
        x_distance = coordinates[num1,0] - coordinates[num2,0]
        y_distance = coordinates[num1,1] - coordinates[num2,1]
        z_distance = coordinates[num1,2] - coordinates[num2,2]
        distance_12 = numpy.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
        print(F'{symbols[num1]} to {symbols[num2]} : {distance_12}')
for num1 in range(0,num_atoms):
    for num2 in range(0, num_atoms):
        if num1>num2:
            x_distance = coordinates[num1,0] - coordinates[num2,0]
            y_distance = coordinates[num1,1] - coordinates[num2,1]
            z_distance = coordinates[num1,2] - coordinates[num2,2]
            distance_12 = numpy.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
            print(F'{symbols[num1]} to {symbols[num2]} : {distance_12}')
def calculate_distance(coords1, coords2):
    """

    This function is something because you didn't make it in time.
    This function has two arguments, the coordinates of two atoms.
    It returns the distance between the atoms.

    """
    x_distance = coordinates[0] - coordinates2[0]
    y_distance = coordinates[1] - coordinates2[1]
    z_distance = coordinates[2] - coordinates2[2]
    distance_12 = numpy.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
    return distance_12
def bond_check(distance,minimum=0,maximum=1.5):
    """

    Checks a distance to see if it's a bond. User specifies minimum and maximum values.

    """
    if distance>minimum and distance_12<maximum:
        return True
    else:
        return False
for num1 in range(0,num_atoms):
    for num2 in range(0, num_atoms):
        if num1>num2:
            distance_12 = calculate_distance(coordinates[num1], coordinates[num2])
            #x_distance = coordinates[num1,0] - coordinates[num2,0]
            #y_distance = coordinates[num1,1] - coordinates[num2,1]
            #z_distance = coordinates[num1,2] - coordinates[num2,2]
            #distance_12 = numpy.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
            if bond_check(distance_12,0,1.5) is True:
                print(F'{symbols[num1]} to {symbols[num2]} : {distance_12:.3f}')
