class Set:
    def __init__(self, setA:set, setB:set):
        self.setA = setA
        self.setB = setB

    def perform_interection(self):
        self.intersection_set = self.setA.intersection(self.setB)

    def perform_union(self):
        self.union_set = self.setA.union(self.setB)

    def perform_difference(self):
        self.diff_set = self.setA.difference(self.setB)
