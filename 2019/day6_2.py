# Advent of Code 2019 Day 6 Part 2

from collections import defaultdict, deque

def main():
    orbits_list = parse_input_to_tuple_list("2019/input_6_demo.txt")
    orbit_graph = build_orbit_graph(orbits_list)
    print(orbit_graph)

    orbit_path = orbit_graph.find_path("YOU", "SAN")
    print(orbit_path)
    print("num_hops =", len(orbit_path))

def build_orbit_graph(orbits_list):
    orbit_graph = OrbitGraph(orbits_list)

    return orbit_graph

def parse_input_to_tuple_list(input_file):
    tuple_list = []
    with open(input_file) as file:
        for line in file:
            nodes_tuple = line.strip().split(')')
            tuple_list.append(nodes_tuple)
    
    return tuple_list

class OrbitGraph:
    def __init__(self, orbits):
        self.orbit_graph = defaultdict(list)
        self.orbited_by = defaultdict(list)
        self.body_set = set()
        self.add_orbits(orbits)

    def add_orbits(self, orbit_list):
        for orbiting_body, body_orbited_by in orbit_list:
            if (orbiting_body not in self.body_set):
                self.body_set.add(orbiting_body)
            if (body_orbited_by not in self.body_set):
                self.body_set.add(body_orbited_by)

            self.orbited_by[orbiting_body].append(body_orbited_by)
            self.orbit_graph[orbiting_body].append(body_orbited_by)
            self.orbit_graph[body_orbited_by].append(orbiting_body)

    def find_path(self, begin, end):
        path = []
        # visited = set()
        orbiters = self.orbit_graph[begin]
        print("orbiters:", orbiters)
        to_visit = orbiters
        while (len(to_visit) != 0):
            cur_node = to_visit.pop()
            if (cur_node not in path):
                cur_node_orbiters = self.orbited_by[cur_node]
                if (cur_node != begin):
                    path.append(cur_node)
                if (end in cur_node_orbiters):
                    return path

                # visited.add(cur_node)
                cur_node_connections = self.orbit_graph[cur_node]
                to_visit += cur_node_connections

        return path
            
        

    def find_total_orbits(self):
        if (len(self.orbit_graph) == 0):
            return 0
        
        visited_bodies = set()
        to_visit = []
        total_orbits = 0        
        
        body_specific_orbits = {}

        body_list = list(self.body_set)

        # Now for each body in our list figure out total # orbits
        # Do a DFS starting at each body
        for body in body_list:
            to_visit = list(self.orbit_graph[body])
            total_orbits += len(to_visit)
            visited = set()

            while(len(to_visit) > 0):
                cur_body = to_visit.pop()
                if (cur_body not in visited):
                    visited.add(cur_body)
                    direct_orbits = list(self.orbit_graph[cur_body])
                    to_visit.extend(direct_orbits)
                    total_orbits += len(direct_orbits)

        return total_orbits

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.orbit_graph))

if __name__ == "__main__":
    main()