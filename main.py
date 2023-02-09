from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

class SnakePart(Widget):
  pass
class GameScreen(Widget):
  step_size = 40
  movement_x = 0
  movement_y = 40
  snake_parts = []
  def new_game(self):
    self.snake_parts = []
    head = SnakePart()
    head.pos = (0,0)
  self.snake_parts.append(head)
  self.add_widget(head)
  def next_frame(self, *args):
    #move the snake
    #check for snake colliding with food
    #check for snake colliding with snake
    #check for snake colliding with wall
    pass
  class MainApp(App):
    MainApp().run()
    pass
    def on_start(self):
      self.root.new_game()
      clock.schedule_interval(self.root.next_frame, .5)
      
    
  
  

  
