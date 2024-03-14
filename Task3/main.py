import matplotlib.pyplot as plt


def cross_product(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]


def inside_clip(p, q, clip_edge):
    return cross_product(q, clip_edge) <= 0 and cross_product(p, clip_edge) > 0


def intersection_point(p1, p2, clip_edge):
    t = cross_product(p1, clip_edge) / cross_product((p1[0] - p2[0], p1[1] - p2[1]), clip_edge)
    return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))


def cyrus_beck(polygon, clip_window, inside=True):
    output_polygon = []
    n = len(polygon)

    for i in range(n):
        p1, p2 = polygon[i], polygon[(i + 1) % n]
        d = (p2[0] - p1[0], p2[1] - p1[1])

        if inside_clip(p1, p2, clip_window):
            if inside:
                output_polygon.append(p2)
            else:
                output_polygon.append(intersection_point(p1, p2, (-d[1], d[0])))
        elif inside_clip(p2, p1, clip_window):
            if inside:
                output_polygon.append(intersection_point(p1, p2, (-d[1], d[0])))
            else:
                output_polygon.append(p2)

    return output_polygon


# Define the coordinates of the pentagon and clipping window
pentagon = [(3, 2), (6, 4), (5, 7), (3, 6), (1, 4)]
clip_window = [(2, 3), (5, 3), (5, 6), (2, 6)]

# Compute the clipped pentagon
result_polygon = cyrus_beck(pentagon, clip_window, inside=True)

# Extract x and y coordinates for plotting
polygon_x, polygon_y = zip(*pentagon)
clip_x, clip_y = zip(*clip_window)
result_x, result_y = zip(*result_polygon)

# Plot the polygon, clipping window, and clipped polygon
plt.plot(polygon_x + [polygon_x[0]], polygon_y + [polygon_y[0]], label='Pentagon')
plt.plot(clip_x + [clip_x[0]], clip_y + [clip_y[0]], label='Clipping Window', linestyle='--')
plt.plot(result_x + [result_x[0]], result_y + [result_y[0]], label='Clipped Pentagon', linestyle='-', marker='o')

plt.legend()
plt.title('Cyrus-Beck Algorithm for Clipping a Pentagon')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
