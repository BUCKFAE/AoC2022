from __future__ import annotations

import os
import re

import numpy as np
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

class Grid:

    def __init__(self) -> None:
        self.points = {}
        self.distances = {}

        self.max_dist = 0

    def draw_grid(self):
        min_x = min(self.points.keys(), key=lambda p: p.x).x - self.max_dist
        min_y = min(self.points.keys(), key=lambda p: p.y).y - self.max_dist
        max_x = max(self.points.keys(), key=lambda p: p.x).x + self.max_dist
        max_y = max(self.points.keys(), key=lambda p: p.y).y + self.max_dist


        for y in range(9, 11 + 1):

            print(f'{y:3d}: ', end='')
            for x in range(min_x, max_x + 1):
                if Point(x, y) in self.points.keys():
                    print('S', end='')
                elif Point(x, y) in self.points.values():
                    print('B', end='')
                elif any([manhattan_distance(Point(x, y), s) <= self.distances[s] for s in self.points.keys()]):
                    print('#', end='')
                else:
                    print('.', end='')

            print()
        for y in range(9, 11 + 1):

            print(f'{y:3d}: ', end='')
            for x in range(min_x, max_x + 1):
                if Point(x, y) in self.points.keys():
                    print('S', end='')
                elif Point(x, y) in self.points.values():
                    print('B', end='')
                elif any([manhattan_distance(Point(x, y), s) == self.distances[s] for s in self.points.keys()]):
                    print('#', end='')
                else:
                    print('.', end='')

            print()


    def add_sensor_beacon(self, sensor: Point, beacon: Point):

        self.points[sensor] = beacon
        dist = manhattan_distance(sensor, beacon)
        self.distances[sensor] = dist

        self.max_dist = max(self.max_dist, dist)


    def get_covered_points(self, row: int) -> int:

        min_x = min(self.points.keys(), key=lambda p: p.x).x - self.max_dist
        max_x = max(self.points.keys(), key=lambda p: p.x).x + self.max_dist

        sensor_starts: dict[Point, Point] = {}
        sensor_ends: dict[Point, Point] = {}

        occ = [0 for _ in range(min_x, max_x + 1)]
        print(f'Lenght of occ: {len(occ)}')

        for sensor in self.points.keys():

                # Sensor is not in range at all
                if abs(sensor.y - row) > self.distances[sensor]:
                    continue

                # Sensor is on the line
                if sensor.y == row:
                    sensor_starts[sensor] = Point(sensor.x - self.distances[sensor], sensor.y)
                    sensor_ends[sensor] = Point(sensor.x + self.distances[sensor], sensor.y)
                    continue


                c1 = Point(sensor.x - self.distances[sensor], sensor.y)
                c2 = Point(sensor.x, sensor.y + (self.distances[sensor] * (1 if sensor.y < row else -1)))

                slope = (c2.y - c1.y) / (c2.x - c1.x)
                t = c1.y - (slope * c1.x)

                intersect_x = int((row - t) / slope)
                intersect_start = Point(intersect_x, row)

                intersect_x_end = sensor.x + (sensor.x - intersect_start.x)
                intersect_end = Point(intersect_x_end, row)

                assert manhattan_distance(sensor, intersect_start) == manhattan_distance(sensor, intersect_end)

                print(f'{sensor} -> {intersect_start} - {intersect_end}')

                sensor_starts[sensor] = intersect_start
                sensor_ends[sensor] = intersect_end


                for i in range(intersect_start.x, intersect_end.x + 1):
                    occ[i] = 1

                print(occ)

        res = sum(occ)
        print(res)
        res -= sum([1 for p in set(self.points.values()) if p.y == row])
        print(res)

        return res




    def get_covered_points2(self, row: int) -> int:


        min_x = min(self.points.keys(), key=lambda p: p.x).x - self.max_dist
        max_x = max(self.points.keys(), key=lambda p: p.x).x + self.max_dist

        res = 0

        x = min_x
        while x <= max_x:
            p = Point(x, row)
            print(p)

            # Stores for each point the intersection at the given row
            sensor_starts: dict[Point, Point] = {}
            sensor_ends: dict[Point, Point] = {}

            # Jump to the middle of sensor
            for sensor in self.points.keys():

                assert sensor.x != p.x or sensor != p.y, f'Point {p} is a sensor'

                # Sensor is not in range at all
                if abs(sensor.y - p.y) > self.distances[sensor]:
                    continue

                # # Sensor already passed
                #if sensor.x < p.x:
                #     continue

                # Sensor is on the line
                if sensor.y == p.y:
                    sensor_starts[sensor] = Point(sensor.x - self.distances[sensor], sensor.y)
                    sensor_ends[sensor] = Point(sensor.x + self.distances[sensor], sensor.y)
                    continue


                c1 = Point(sensor.x - self.distances[sensor], sensor.y)
                c2 = Point(sensor.x, sensor.y + (self.distances[sensor] * (1 if sensor.y < p.y else -1)))

                #print(f'Sensor: {sensor} - c1: {c1} - c2: {c2} - distance: {self.distances[sensor]}')

                slope = (c2.y - c1.y) / (c2.x - c1.x)
                t = c1.y - (slope * c1.x)

                #print(f'Slope: {slope} - t: {t}')

                intersect_x = int((p.y - t) / slope)
                intersect_start = Point(intersect_x, p.y)

                intersect_x_end = sensor.x + (sensor.x - intersect_start.x)
                intersect_end = Point(intersect_x_end, p.y)

                assert manhattan_distance(sensor, intersect_start) == manhattan_distance(sensor, intersect_end)

                if intersect_end.x <= p.x:
                    continue

                sensor_starts[sensor] = intersect_start
                sensor_ends[sensor] = intersect_end

            if (len(sensor_starts) == 0):
                print(f'No more sensors after {p}')
                break


            print(f'Possible start sensors: {sensor_starts}')
            # Intersection closest to the current point
            start_sensor = min(sensor_starts.keys(), key=lambda s: sensor_starts[s].x - p.x)
            start_intersection = sensor_starts[start_sensor]


            print(f'Start intersection: {start_intersection} - Sensor: {start_sensor}')

            print(f'Res: {res}')
            if start_intersection.x < p.x:
                break

            # All sensors that can be reached from the current point
            possible_end_sensors = []
            for sensor in self.points.keys():

                if not sensor in sensor_starts.keys():
                    continue

                if sensor_starts[sensor].x > p.x:
                    continue

                if sensor_ends[sensor].x < sensor_starts[start_sensor].x:
                    continue

                possible_end_sensors.append(sensor)

            possible_end_sensors.append(start_sensor)
            print(possible_end_sensors)
            print(f'Possible end sensors: {possible_end_sensors}')

            # Jumping to the sensor farthest away
            next_sensor = max(possible_end_sensors, key=lambda s: sensor_ends[s].x)
            end_intersection = sensor_ends[next_sensor]

            if end_intersection.x <= p.x:
                print('No more sensors')
                break


            print(f'End intersection: {end_intersection} - Sensor: {next_sensor}')


            x = end_intersection.x
            res += sum([1 for _ in range(start_intersection.x, end_intersection.x)])
            print(res)



        # Removing counts of beacon / sensor
        #res -= sum([1 for p in self.points.keys() if p.y == row])
        res -= sum([1 for p in self.points.values() if p.y == row])

        return res




def manhattan_distance(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def solve(input_file: str, row: int)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.read().splitlines() if line.strip()]

        g = Grid()

        for line in lines:
            sensor, beacon = line.split(': closest beacon is at')

            # Parsing sensor
            x_sensor = int(re.findall(r"x=(-?\d+)", sensor)[0])
            y_sensor = int(re.findall(r"y=(-?\d+)", sensor)[0])

            # Parsing beacon
            x_beacon = int(re.findall(r"x=(-?\d+)", beacon)[0])
            y_beacon = int(re.findall(r"y=(-?\d+)", beacon)[0])

            print(f'Adding sensor: {x_sensor}, {y_sensor} - beacon: {x_beacon}, {y_beacon}')

            g.add_sensor_beacon(Point(x_sensor, y_sensor), Point(x_beacon, y_beacon))


    print(f'Finished creating grid')
    g.draw_grid()

    res1 = g.get_covered_points(row)
    res2 = 0

    return res1, res2


if __name__ == '__main__':

    # Solving real input
    res1, res2 = solve('day15/input.txt', 2000000)
    print(f'Part 1: {res1} - Part 2: {res2}')
