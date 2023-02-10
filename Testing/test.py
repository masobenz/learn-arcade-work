import arcade
arcade.open_window(600,600,"Drawing Example")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0,600,300,0, arcade.csscolor.GREEN)

# tree with circle top
arcade.draw_rectangle_filled(100,320,20,60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100,350,30, arcade.csscolor.DARK_GREEN)

# arcade.draw_rectangle_outline(300,300,350,200, arcade.csscolor.BLACK, 3)
# arcade.draw_ellipse_outline(300,300,350,200, arcade.csscolor.RED, 3)

# tree with ellipse top
arcade.draw_rectangle_filled(200,320,20,60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200,370,60,80, arcade.csscolor.DARK_GREEN)

#tree with arc top
arcade.draw_rectangle_filled(300,320,20,60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300,340,60,100, arcade.csscolor.DARK_GREEN, 0,180)

# tree with triangle top
arcade.draw_rectangle_filled(400,320,20,60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400,400,370,320,430,320, arcade.csscolor.DARK_GREEN)

# tree with polygon top
arcade.draw_rectangle_filled(500,320,20,60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500,400),(480,360),(470,320),(530,320),(520,360)), arcade.csscolor.DARK_GREEN)

arcade.finish_render()

arcade.run()