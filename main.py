from typing import Counter


class itemPairs:
  """ base class for itemPairs """
  counterDict = {}
  manhattanDistance = []
  level = 0

  def __init__(self) -> None:
    self.level = 1
    pass
  
  def count_disk(self, path):
    pass

  def generate_next_level_pairs(self):
    pass

  def generate_manhattan_distance_matrix(self):
    pass

  def reduce_dimension(self):
    pass

  def prune_non_frequent(self):
    pass

