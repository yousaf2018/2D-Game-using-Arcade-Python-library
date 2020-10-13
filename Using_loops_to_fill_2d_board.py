# Displays a white window with a blue circle in the middle
import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Practice for Project"
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
#arcade.draw_line(80,0,80,1000,arcade.color.BLACK,4)
#smile face code
change_y = 0
for j in range(10,0,-1):
    change_x = 0
    for i in range(j):
        x = 41+change_x; y = 40 + change_y; radius = 35
        arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)
        x = 55+change_x; y = 50 + change_y; radius = 4
        arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)
        x = 25+change_x; y = 50 + change_y; radius = 4
        arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)
        x = 40+change_x; y = 35 + change_y; width = 30; height = 25
        start_angle = 190; end_angle = 350; line_width = 6
        arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle,end_angle,line_width)
        change_x = change_x + 80
    change_y = change_y + 80
#sad face code
change_y = 800
for j in range(9,0,-1):
    change_x = 800
    for i in range(j):
        x = change_x-41; y = change_y - 40; radius = 35
        arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)
        x = change_x - 55; y = change_y - 50; radius = 4
        arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)
        x = change_x - 25; y = change_y - 50; radius = 4
        arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)
        x = change_x - 40; y = change_y - 35; width = 30; height = 25
        start_angle = 10; end_angle = 170; line_width = 6
        arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle,end_angle,line_width)
        change_x = change_x - 80
    change_y = change_y - 80





x = 41+80; y = 40+80; radius = 35
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)
x = 55+80; y = 50+80; radius = 4
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK) 
x = 25+80; y = 50+80; radius = 4
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)
x = 40+80; y = 25+80; width = 30; height = 25
start_angle = 10; end_angle = 170; line_width = 6
arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle,end_angle,line_width)



arcade.draw_line(0,4,800,4,arcade.color.BLACK,4)
arcade.draw_line(0,797,800,797,arcade.color.BLACK,4)
arcade.draw_line(4,0,4,800,arcade.color.BLACK,4)
arcade.draw_line(797,0,797,800,arcade.color.BLACK,4)
for i in range(0,800,80):
    arcade.draw_line(i,0,i,800,arcade.color.BLACK,4)
    arcade.draw_line(0,i,800,i,arcade.color.BLACK,4)
arcade.finish_render()
arcade.run() 