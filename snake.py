import turtle as t

class Snake:
    bones = []

    def __init__(self, size, pos):
        pos_x_offset = 0
        for i in range(size):
            turt = t.Turtle()
            turt.shape("square")
            turt.color("white")
            turt.penup()
            turt.setposition(pos[0] + pos_x_offset, pos[1])
            self.bones.append(turt)
            pos_x_offset += 20

    def init_game(self):


