import turtle as t

scr = t.Screen()
scr.setup(width=600, height=600)
scr.title("Snake")
scr.bgcolor("black")

turts = []
for i in range(3):
    turt = t.Turtle()
    turt.penup()
    turt.shape("square")
    turt.color("white")
    turt.setposition(i*10, 0)
    turts.append(turt)

scroll_direction = "d"
is_game_on = True
user_interaction_started = False


def start_game():
    while is_game_on:
        for st in turts:
            current_pos = st.position()
            if scroll_direction == "d":
                new_x_pos = current_pos[0] + 10
                if new_x_pos > 300:
                    st.hideturtle()
                    st.speed("fastest")
                    new_x_pos = -300
                st.goto(new_x_pos, current_pos[1])
            elif scroll_direction == "a":
                new_x_pos = current_pos[0] - 10
                if new_x_pos < -300:
                    st.hideturtle()
                    st.speed("fastest")
                    new_x_pos = 300
                st.goto(new_x_pos, current_pos[1])
            elif scroll_direction == "w":
                new_y_pos = current_pos[1] + 10
                if new_y_pos > 300:
                    st.hideturtle()
                    st.speed("fastest")
                    new_y_pos = -300
                st.goto(current_pos[0], new_y_pos)
            elif scroll_direction == "s":
                new_y_pos = current_pos[1] - 10
                if new_y_pos < -300:
                    st.hideturtle()
                    st.speed("fastest")
                    new_y_pos = 300
                st.goto(current_pos[0], new_y_pos)
            st.speed("normal")
            st.showturtle()


def set_direction(d):
    global scroll_direction
    if (scroll_direction == "d" and (d == "d" or d == "a")) \
            or (scroll_direction == "a" and (d == "d" or d == "a")) \
            or (scroll_direction == "w" and (d == "w" or d == "s")) \
            or (scroll_direction == "s" and (d == "w" or d == "s")):
        pass
    else:
        scroll_direction = d


def up():
    set_direction("w")


def down():
    set_direction("s")


def left():
    set_direction("a")


def right():
    set_direction("d")


scr.listen()

scr.onkey(start_game, "g")
scr.onkey(up, "w")
scr.onkey(left, "a")
scr.onkey(down, "s")
scr.onkey(left, "d")

scr.exitonclick()