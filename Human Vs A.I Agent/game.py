import arcade
SCREEN_TITLE=" Welcome to Snails Game "
# Importing Images use in the game
Background_image = arcade.load_texture("background.jpg")
Image_welcome_screen = arcade.load_texture("index.jpeg")
Image_End_screen = arcade.load_texture("End_game_screen.jpeg")
Image_win = arcade.load_texture("Win_Screen.png")
Snail = arcade.load_texture("hiclipart.com.png")
Player1 = arcade.load_texture("Player1.png")
Player2 = arcade.load_texture("Player2.png")
Splash1 = arcade.load_texture("Splash1.png")
Splash2 = arcade.load_texture("Splash2.png")

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.board = []
        self.palyer1 = "1"
        self.player2 = "2"
        self.win = "0"
        self.state = "GameMenu"
        self.turn = "Human"
        self.position1 = 0,9
        self.position2 = 9,0
        self.score1 = 0
        self.score2 = 0
        self.initialize_board()
    def initialize_board(self):
        for i in range(0,10):
            new = []
            for j in range(0,10):
                new.append(0)
            self.board.append(new)
        self.board[0][9]=1
        self.board[9][0]=2



    def on_show(self):
        arcade.set_background_color(arcade.color.PERSIAN_INDIGO)

    def on_draw(self):
        arcade.start_render()
        if self.state == "GameMenu":
            arcade.draw_lrwh_rectangle_textured(0,0,1000,600,Image_welcome_screen)
            arcade.draw_lrwh_rectangle_textured(450,20,100,100,Snail)
            arcade.draw_text("Snails Game ", 520, 350, arcade.color.AMBER, font_size=70, anchor_x="center")
            arcade.draw_text("( Press ENTER to Start the Game )", 500, 230, arcade.color.DEEP_CARMINE_PINK, font_size=30, anchor_x="center")
            arcade.draw_text("( Press ENTER to Start the Game )", 501, 230, arcade.color.DEEP_CARMINE_PINK, font_size=30, anchor_x="center")
            arcade.draw_text("( Press ENTER to Start the Game )", 502, 230, arcade.color.DEEP_CARMINE_PINK, font_size=30, anchor_x="center")
            arcade.draw_text("( Press ENTER to Start the Game )", 502, 230, arcade.color.DEEP_CARMINE_PINK, font_size=30, anchor_x="center")

        elif self.state == "GameOn":
            arcade.draw_lrwh_rectangle_textured(0,0,600,600,Background_image)
            arcade.draw_rectangle_filled(800, 450, 180, 80, arcade.color.BRIGHT_LILAC)
            arcade.draw_text(" Turn ", 800, 500, arcade.color.AMBER, font_size=40, anchor_x="center")
            arcade.draw_text(self.turn, 800, 440, arcade.color.BLACK, font_size=25, anchor_x="center")
            arcade.draw_text(self.turn, 801, 440, arcade.color.BLACK, font_size=25, anchor_x="center")
            arcade.draw_rectangle_filled(800, 250, 250, 80, arcade.color.BRIGHT_LILAC)
            arcade.draw_text(" Player2 | A.I Agent ", 800, 300, arcade.color.BRIGHT_GREEN, font_size=20, anchor_x="center")
            arcade.draw_text(" Player2 | A.I Agent ", 801, 300, arcade.color.BRIGHT_GREEN, font_size=20, anchor_x="center")
            arcade.draw_text(" Player2 | A.I Agent ", 801, 300, arcade.color.BRIGHT_GREEN, font_size=20, anchor_x="center")
            arcade.draw_text(str(self.score2), 720, 230, arcade.color.BLACK, font_size=30, anchor_x="center")
            arcade.draw_text(str(self.score1), 845, 230, arcade.color.BLACK, font_size=30, anchor_x="center")

            arcade.draw_line(800,210,800,290,arcade.color.BULGARIAN_ROSE,4)
            arcade.draw_lrwh_rectangle_textured(850,150,60,60,Player1)
            arcade.draw_lrwh_rectangle_textured(680,150,60,60,Player2)

            # Drawing horizontal line
            temp=0
            for i in range(11): 
                arcade.draw_line(0,temp, 600,temp,arcade.color.WHITE,4)
                temp=temp+60
            # Drwing vertical lines
            temp=0
            for i in range(11):
                arcade.draw_line(temp,0, temp,600,arcade.color.WHITE,4)
                temp=temp+60

            # Sinking 2d board with frontend800
            y1 = 540
            x2 = 60
            y2 = 60
            for i in range(10):
                x1 = 0
                for j in range(10):
                    if self.board[i][j] == 1:
                        arcade.draw_lrwh_rectangle_textured(x1,y1,x2,y2,Player1)
                    elif self.board[i][j] == 2:
                        arcade.draw_lrwh_rectangle_textured(x1,y1,x2,y2,Player2)
                    elif self.board[i][j] == 11:
                        arcade.draw_lrwh_rectangle_textured(x1+5,y1+5,x2-10,y2-10,Splash1)
                    elif self.board[i][j] == 22:
                        arcade.draw_lrwh_rectangle_textured(x1+5,y1+5,x2-10,y2-10,Splash2)
                    x1 = x1+60
                y1 = y1-60

        elif self.state == "GameEnd":
            arcade.draw_lrwh_rectangle_textured(0,0,1000,600,Image_End_screen)
            arcade.draw_rectangle_filled(500, 550, 500, 50, arcade.color.CORN)
            arcade.draw_lrwh_rectangle_textured(150,200,800,250,Image_win)
            arcade.draw_text(" CONGRATULATIONS ", 500, 530, arcade.color.BLACK, font_size=30, anchor_x="center")
            arcade.draw_text(" CONGRATULATIONS ", 500, 530, arcade.color.BLACK, font_size=30, anchor_x="center")
            arcade.draw_rectangle_filled(350, 100, 200, 80, arcade.color.CYAN)
            arcade.draw_rectangle_filled(650, 100, 200, 80, arcade.color.ALABAMA_CRIMSON)

            arcade.draw_text(self.win , 450, 320, arcade.color.BLACK, font_size=50, anchor_x="center")
            arcade.draw_text(self.win , 451, 320, arcade.color.BLACK, font_size=50, anchor_x="center")
            arcade.draw_text(self.win , 451, 320, arcade.color.BLACK, font_size=50, anchor_x="center")

            arcade.draw_text(" Play Again ", 350, 90, arcade.color.DARK_BROWN, font_size=20, anchor_x="center")
            arcade.draw_text(" Play Again ", 351, 90, arcade.color.DARK_BROWN, font_size=20, anchor_x="center")
            arcade.draw_text(" EXIT ", 650, 90, arcade.color.WHITE, font_size=20, anchor_x="center")
            arcade.draw_text(" EXIT ", 651, 90, arcade.color.WHITE, font_size=20, anchor_x="center")


    # Function to Calculate position where mouse is clicked
    def calculate_BOX(self,x,y):
        x1=y // 60
        y1=x // 60
        return 9-x1, y1

    # Checking if move is Valid or not
    def move_validation(self,i,j,plr):
        if plr == 1:
            row , col = self.position1[0], self.position1[1]
        else :
            row, col = self.position2[0], self.position2[1]

        if i == row+1 and j == col:
            return 1, "down"
        elif i == row-1 and j == col:
            return 1, "up"
        elif i == row and j == col+1:
            return 1, "right"
        elif i == row and j == col-1:
            return 1, "left"
        else :
            return 0, "invalid"

    # Functions of all slips

    def left_slip(self, plr):
        if plr == 1:
            x, y = self.position1[0], self.position1[1]
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[self.position1[0]][self.position1[1]] = 11
                    self.board[x][y+1] = 1
                    self.position1 = x,y+1
                    self.turn = "Human"
                    break
                elif y == 0 :
                    self.board[self.position1[0]][self.position1[1]] = 11
                    self.board[x][y] = 1
                    self.position1 = x,y
                    self.turn = "Human"
                    break
                else :
                    y = y-1
        else :
            x, y = self.position2[0], self.position2[1]
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[self.position2[0]][self.position2[1]] = 22
                    self.board[x][y+1] = 2
                    self.position2 = x,y+1
                    self.turn = "A.I Agent"
                    break
                elif y == 0 :
                    self.board[self.position2[0]][self.position2[1]] = 22
                    self.board[x][y] = 2
                    self.position2 = x,y
                    self.turn = "A.I Agent"
                    break
                else:
                    y = y-1

    def right_slip(self, plr):
        if plr == 1:
            x, y = self.position1[0], self.position1[1]
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[self.position1[0]][self.position1[1]] = 11
                    self.board[x][y-1] = 1
                    self.position1 = x,y-1
                    self.turn = "Human"
                    break
                elif y == 9 :
                    self.board[self.position1[0]][self.position1[1]] = 11
                    self.board[x][y] = 1
                    self.position1 = x,y
                    self.turn = "Human"
                    break
                else :
                    y = y+1
        else :
            x, y = self.position2[0], self.position2[1]
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[self.position2[0]][self.position2[1]] = 22
                    self.board[x][y-1] = 2
                    self.position2 = x,y-1
                    self.turn = "A.I Agent"
                    break
                elif y == 9 :
                    self.board[self.position2[0]][self.position2[1]] = 22
                    self.board[x][y] = 2
                    self.position2 = x,y
                    self.turn = "A.I Agent"
                    break
                else:
                    y = y+1

    def up_slip(self, plr):
        if plr == 1:
            x, y = self.position1[0], self.position1[1]
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[self.position1[0]][self.position1[1]] = 11
                    self.board[x+1][y] = 1
                    self.position1 = x+1,y
                    self.turn = "Human"
                    break
                elif x == 0:
                    self.board[self.position1[0]][self.position1[1]] = 11
                    self.board[x][y] = 1
                    self.position1 = x,y
                    self.turn = "Human"
                    break
                else :
                    x = x-1
        else :
            x, y = self.position2[0], self.position2[1]
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[self.position2[0]][self.position2[1]] = 22
                    self.board[x+1][y] = 2
                    self.position2 = x+1,y
                    self.turn = "A.I Agent"
                    break
                elif x == 0 :
                    self.board[self.position2[0]][self.position2[1]] = 22
                    self.board[x][y] = 2
                    self.position2 = x,y
                    self.turn = "A.I AgentS"
                    break
                else:
                    x = x-1

    def down_slip(self, plr):
        if plr == 1:
            x, y = self.position1[0], self.position1[1]
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 22 or self.board[x][y] == 2:
                    self.board[self.position1[0]][self.position1[1]] = 11
                    self.board[x-1][y] = 1
                    self.position1 = x-1,y
                    self.turn = "Human"
                    break
                elif x == 9 :
                    self.board[self.position1[0]][self.position1[1]] = 11
                    self.board[x][y] = 1
                    self.position1 = x,y
                    self.turn = "Human"
                    break
                else :
                    x = x+1
        else :
            x, y = self.position2[0], self.position2[1]
            while(True):
                if self.board[x][y] == 0 or self.board[x][y] == 11 or self.board[x][y] == 1:
                    self.board[self.position2[0]][self.position2[1]] = 22
                    self.board[x-1][y] = 2
                    self.position2 = x-1,y
                    self.turn = "A.I Agent"
                    break
                elif x == 9 :
                    self.board[self.position2[0]][self.position2[1]] = 22
                    self.board[x][y] = 2
                    self.position2 = x,y
                    self.turn = "A.I Agent"
                    break
                else:
                    x = x+1


    def on_key_press(self, key, modifiers):
        if self.state == "GameMenu":
            if key == arcade.key.ENTER:
                self.state = "GameOn"


    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn" :
            # Player1 Turn
            if self.turn == "A.I Agent" :
                i , j = self.calculate_BOX(x,y)
                check, slip = self.move_validation(i,j,1)
                if check == 1:
                    if self.board[i][j] == 11:
                        if slip == "left":
                            self.left_slip(1)
                        elif slip == "right":
                            self.right_slip(1)
                        elif slip == "up":
                            self.up_slip(1)
                        elif slip == "down":
                            self.down_slip(1)
                    elif self.board[i][j] == 0:
                        self.board[self.position1[0]][self.position1[1]] = 11
                        self.position1 = i,j
                        self.board[i][j] = 1
                        self.score1 += 1
                        if self.score1 >= 49 :
                            if self.score1 == 49 and self.score2 == 49:
                                self.win = "Match Draw"
                                slef.state = "GameEnd"
                            self.state = "GameEnd"
                            self.win = "A.I Agent Win"
                        self.turn = "Human"
                    else:
                        self.turn = "Human"
                else:
                    self.turn = "Human"
            # Player2 turn
            elif self.turn == "Human" :
                i , j = self.calculate_BOX(x,y)
                check, slip = self.move_validation(i,j,2)
                if check==1:
                    if self.board[i][j] == 22:
                        if slip == "left":
                            self.left_slip(2)
                        elif slip == "right":
                            self.right_slip(2)
                        elif slip == "up":
                            self.up_slip(2)
                        elif slip == "down":
                            self.down_slip(2)
                    elif self.board[i][j] == 0:
                        self.board[self.position2[0]][self.position2[1]]=22
                        self.position2 = i,j
                        self.board[i][j] = 2
                        self.score2 += 1
                        self.turn = "A.I Agent"
                        if self.score2 >= 49 :
                            if self.score1 == 49 and self.score2 == 49:
                                self.win = "Match Draw"
                                self.state = "GameEnd"
                            self.state = "GameEnd"
                            self.win = "Human Win"
                    else :
                        self.turn = "A.I Agent"
                else:
                    self.turn = "A.I Agent"
        # Play again process
        elif self.state == "GameEnd":
            print(x,y)
            if 250 <= x <= 450 and 60 <= y <= 140:
                self.state == "GameMenu"
                self.board.clear()
                reset = Game()
                self.window.show_view(reset)
            elif 550 <= x <= 750 and 60 <= y <= 140:
                exit(0)




if __name__ == "__main__":
    window = arcade.Window(1000, 600, " Welcome to Snails Game ")
    game_view = Game()
    window.show_view(game_view)
    arcade.run()
