import arcade
arcade.open_window(600,600,"Lab_2_project")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

"""Start Render"""
arcade.start_render()

#grass
arcade.draw_lrtb_rectangle_filled(0,600,200,0,arcade.csscolor.DARK_GREEN)

#house
arcade.draw_xywh_rectangle_filled(450,120,100,120,arcade.color.RED_BROWN)

# x axis grid lines
arcade.draw_line(50,0,50,600,arcade.color.BLACK)
arcade.draw_line(100,0,100,600,arcade.color.BLACK)
arcade.draw_line(150,0,150,600,arcade.color.BLACK)
arcade.draw_line(200,0,200,600,arcade.color.BLACK)
arcade.draw_line(250,0,250,600,arcade.color.BLACK)
arcade.draw_line(300,0,300,600,arcade.color.BLACK)
arcade.draw_line(350,0,350,600,arcade.color.BLACK)
arcade.draw_line(400,0,400,600,arcade.color.BLACK)
arcade.draw_line(450,0,450,600,arcade.color.BLACK)
arcade.draw_line(500,0,500,600,arcade.color.BLACK)
arcade.draw_line(550,0,550,600,arcade.color.BLACK)

# y axis grid lines



"""Finish Render"""
arcade.finish_render()

arcade.run()