def turn_left():
    pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def at_goal():
    return False

def right_is_clear():
    return False

def front_is_clear():
    return False

def move():
    pass

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()