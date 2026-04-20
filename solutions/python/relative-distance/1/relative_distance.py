from collections import deque, defaultdict

class RelativeDistance:
    def __init__(self, family_tree):
        self.graph = defaultdict(set)
        self.people = set()

        for parent, children in family_tree.items():
            self.people.add(parent)

            # Add parent-child connections
            for child in children:
                self.people.add(child)
                self.graph[parent].add(child)
                self.graph[child].add(parent)

            # 🔑 Add sibling connections
            for i in range(len(children)):
                for j in range(i + 1, len(children)):
                    c1, c2 = children[i], children[j]
                    self.graph[c1].add(c2)
                    self.graph[c2].add(c1)

    def degree_of_separation(self, person_a, person_b):
        if person_a not in self.people:
            raise ValueError("Person A not in family tree.")
        if person_b not in self.people:
            raise ValueError("Person B not in family tree.")

        if person_a == person_b:
            return 0

        visited = set([person_a])
        queue = deque([(person_a, 0)])

        while queue:
            current, distance = queue.popleft()

            if current == person_b:
                return distance

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        raise ValueError("No connection between person A and person B.")