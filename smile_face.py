# Displays a white window with a blue circle in the middle
import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to Arcade"
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
x = 40; y = 40; radius = 40
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)
x = 55; y = 50; radius = 4
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)
x = 25; y = 50; radius = 4
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)
x = 40; y = 30; width = 35; height = 25
start_angle = 190; end_angle = 350; line_width = 6
arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle,end_angle,line_width)
arcade.finish_render()
arcade.run() 