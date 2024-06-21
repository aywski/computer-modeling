import matplotlib.pyplot as plt
import math

radars_data = [
    {
        'point': (1, 6),
        'angle': 42
    },
    {
        'point': (-5, -9),
        'angle': 163
    },
    {
        'point': (16, 5),
        'angle': 158,
    },
    {
        'point': (-14, -21),
        'angle': 360
    },
]


def find_angles(ship_location, radars_data):
    possible_angles = []

    for angle1 in range(360):
        for angle2 in range(360):
            if angle1 == angle2:
                continue

            intersection = find_intersection(
                ship_location,
                angle1,
                ship_location,
                angle2
            )

            if intersection is not None:
                possible_angles.append((angle1, angle2))

    return possible_angles

ship_location = (3, 3)

possible_angles = find_angles(ship_location, radars_data)

print('Standard deviation: ', standard_deviation)
print('Average point: ', average_possible_location)
print('Real ship location: ', real_ship_location)
print('Distance between real ship location and average point: ', calculate_distance_between_points(real_ship_location, average_possible_location))

possible_location_circle = plt.Circle(average_possible_location,
                                   standard_deviation,
                                   fill = False)

figure, axes = plt.subplots()

axes.add_artist(possible_location_circle)


for point in possible_ship_points:
    plt.plot(point[0], point[1], 'ro')


plt.plot(average_possible_location[0], average_possible_location[1], 'ro')

plt.plot(real_ship_location[0], real_ship_location[1], 'b*')

for radar in radars_data:
    plot_point(radar['point'], radar['angle'], 20)

plt.show()