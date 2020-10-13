import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Snails Game Show"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Background image will be stored in this variable
        self.background = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        # Image from:
        # http://wallpaper-gallery.net/single/free-background-images/free-background-images-22.html
        self.background = arcade.load_texture("Background.jpg")
        self.player_list = None
        self.player = None
        self.player2 = None

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        #Grid lines for 2d board
        arcade.draw_line(0,4,800,4,arcade.color.BLACK,4)
        arcade.draw_line(0,797,800,797,arcade.color.BLACK,4)
        arcade.draw_line(4,0,4,800,arcade.color.BLACK,4)
        arcade.draw_line(797,0,797,800,arcade.color.BLACK,4)
        for i in range(0,800,80):
            arcade.draw_line(i,0,i,800,arcade.color.BLACK,4)
            arcade.draw_line(0,i,800,i,arcade.color.BLACK,4)
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.player = arcade.Sprite("snail.jpg",0.33)
        self.player2 = arcade.Sprite("snail2.jpg",0.09)
        self.player2.width = 72
        self.player2.height = 72
        self.player2.width = 72
        self.player.height = 73
        self.player.center_x = 41
        self.player.center_y = 40
        self.player2.center_x = 759
        self.player2.center_y = 760
        self.player_list.append(self.player)
        self.player_list.append(self.player2)
        self.player.draw()
        self.player2.draw()


        
            


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()