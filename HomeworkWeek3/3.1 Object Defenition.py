class University():
  """описание университета"""
  def __init__(self, name, year_of_foundation):
    """свойства университета"""
    self.name = name
    self.year_of_foundation = year_of_foundation
    self.direction="General"
    self.rector="None"
  def dr_of_un(self,direction):
    """изменение направленности вуза"""
    self.direction=direction
  def rect_of_un(self,rector):
    """изменение ректора вуза"""
    self.rector=rector
    
