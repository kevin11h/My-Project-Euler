class Point:
    def __init__(self):
        self.neighbors = set([])

def num_routes_to_corner_of_n_by_n_grid(n):
    points_per_row = n + 1
    num_points = points_per_row**2
    points = [Point() for p in range(num_points)]

    for pid in range(num_points):
        point = points[pid]
        south_neighbor = None
        east_neighbor = None

        if pid + points_per_row < num_points:
            south_neighbor = points[pid + points_per_row]

        if pid % points_per_row + 1 < points_per_row:
            east_neighbor = points[pid + 1]

        point.neighbors |= set([east_neighbor, south_neighbor])

    upper_left_corner = points[0]
    lower_right_corner = points[-1]

    def num_paths_to_point(p):
        if p is None:
            return 0
        elif lower_right_corner in p.neighbors:
            return 1
        else:
            return sum(map(num_paths_to_point, p.neighbors))

    return num_paths_to_point(upper_left_corner)

print num_routes_to_corner_of_n_by_n_grid(2)
