import matplotlib.pyplot as plt
import math

radars_data = [
  {
    'point': (8, 6),
    'angle': 42
  },
  {
    'point': (-4, 5),
    'angle': 158
  },
  {
    'point': (1, -3),
    'angle': 248,
  }
]

real_ship_location = (3, 3)

def get_normal_ray_angle(y, angle):
    if y < 0:
        return angle
    else:
        return 180 + angle


def plot_point(point, angle, length):
     x, y = point

     angle = get_normal_ray_angle(y, angle)

     endy = y + length * math.sin(math.radians(angle))
     endx = x + length * math.cos(math.radians(angle))

     ax = plt.subplot(111)
     ax.set_ylim([-length, length])   # set the bounds to be 10, 10
     ax.set_xlim([-length, length])
     ax.plot([x, endx], [y, endy])

     ax.plot(x, y, 'o')

def is_point_on_ray(point, ray_start, normal_ray_angle):
    x, y = point
    x1, y1 = ray_start

    x2 = x1 + 100 * math.cos(math.radians(normal_ray_angle))
    y2 = y1 + 100 * math.sin(math.radians(normal_ray_angle))

    # Перевірка на відмінність x1 і x2, щоб уникнути ділення на нуль
    if x2 == x1:
      return x == x1 and min(y1, y2) <= y <= max(y1, y2)

    # Обчислення параметра t
    t = (x - x1) / (x2 - x1)

    # Перевірка, чи t знаходиться в інтервалі [0, 1]
    return 0 <= t <= 1


def find_intersection(ray1_start, ray1_angle, ray2_start, ray2_angle):
    x1, y1 = ray1_start
    x2, y2 = ray2_start
    
    ray1_normal_angle = get_normal_ray_angle(y1, ray1_angle)
    ray2_normal_angle = get_normal_ray_angle(y2, ray2_angle)

    # Обчислюємо коефіцієнти прямих
    m1 = math.tan(math.radians(ray1_normal_angle))
    m2 = math.tan(math.radians(ray2_normal_angle))

    if m1 == m2:
        return None

    # Знаходимо точку перетину прямих
    x_intersect = (m1 * x1 - m2 * x2 + y2 - y1) / (m1 - m2)
    y_intersect = m1 * (x_intersect - x1) + y1

    # Перевірка, чи точка перетину лежить на обох променях
    if (
      is_point_on_ray((x_intersect, y_intersect), ray1_start, ray1_normal_angle) and
      is_point_on_ray((x_intersect, y_intersect), ray2_start, ray2_normal_angle)
    ):
        return x_intersect, y_intersect
    else:
        return None

def calculate_distance_between_points(point1, point2):
  x1, y1 = point1
  x2, y2 = point2

  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_average_point(points):
  x_sum = 0
  y_sum = 0

  for point in points:
    x, y = point

    x_sum += x
    y_sum += y

  return (x_sum / len(points), y_sum / len(points))

def calculate_standard_deviation(points):
  average_point = get_average_point(points)

  return math.sqrt(sum([calculate_distance_between_points(average_point, point) ** 2 for point in points]) / (len(points) - 1))

def distance_to_ray(ray_origin, ray_angle, point):
    ray_x, ray_y = ray_origin
    point_x, point_y = point

    ray_angle = math.radians(get_normal_ray_angle(ray_y, ray_angle))

    distance = abs((point_x - ray_x) * math.sin(ray_angle) - (point_y - ray_y) * math.cos(ray_angle)) / math.sqrt(math.sin(ray_angle)**2 + math.cos(ray_angle)**2)

    return min(distance, calculate_distance_between_points(ray_origin, point))

def angle_between_points(point1, point2):
    # Розпаковуємо координати точок
    x1, y1 = point1
    x2, y2 = point2

    # Обчислюємо різницю координат
    delta_x = x2 - x1
    delta_y = y2 - y1

    # Використовуємо atan2 для обчислення кута між відрізком і віссю x
    angle_rad = math.atan2(delta_y, delta_x)

    # Переводимо радіани в градуси
    angle_deg = math.degrees(angle_rad)

    if y1 >= 0:
        angle_deg = angle_deg - 180

    return angle_deg

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


possible_ship_points = []

for radar1_data in radars_data:
  for radar2_data in radars_data:
    if radar1_data == radar2_data:
      continue

    intersection = find_intersection(
      radar1_data['point'],
      radar1_data['angle'],
      radar2_data['point'],
      radar2_data['angle']
    )

    if intersection is None:
      continue

    possible_ship_points.append(intersection)


standard_deviation = calculate_standard_deviation(possible_ship_points)
average_possible_location = get_average_point(possible_ship_points)

print('Standard deviation: ', standard_deviation)
print('Average point: ', average_possible_location)
print('Real ship location: ', real_ship_location)
print('Distance between real ship location and average point: ', calculate_distance_between_points(real_ship_location, average_possible_location))
print('Find angels: ', find_angles(real_ship_location, radars_data))

possible_location_circle = plt.Circle(average_possible_location,
                                      standard_deviation,
                                      fill = False )

figure, axes = plt.subplots()

axes.add_artist(possible_location_circle)


for point in possible_ship_points:
  plt.plot(point[0], point[1], 'ro')


plt.plot(average_possible_location[0], average_possible_location[1], 'ro')

plt.plot(real_ship_location[0], real_ship_location[1], 'b*')

plt.plot(find_angles(real_ship_location, radars_data), 'k', linewidth=2)

for radar in radars_data:
    plot_point(radar['point'], radar['angle'], 20)

plt.show()
