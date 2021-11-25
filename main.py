from typing import Counter


class itemPairs:
  """ base class for itemPairs """
  counterDict = {}
  manhattanDistance = []
  level = 0

  def __init__(self, level, path) -> None:
    self.level = level
    pass
  
  def count_disk(self, path):
    baskets = []
    with open('T10I4D100K.dat') as f:
      for line in f:
        items = line.split(' ')
        items.remove('\n')
        baskets.append(frozenset(items))
    return baskets


  def generate_next_level_pairs(self):
    pass

  def reduce_dimension(self):
    pass

  def prune_non_frequent(self):
    pass

  def manhattan_distance(self, seta, setb):
    return len(seta|setb)-len(seta&setb)

  def generate_manhattan_distance_matrix(self, seta, setb):
    return len(seta|setb)-len(seta&setb)


if __name__ == "__main__":
  f = frozenset([1,2])
  s = set([1,2,3,4])
  print(f.issubset(s))
  