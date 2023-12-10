isRobotWork = True
robotState = '0'
moveDirection = '1'
translationState = ''
rotationState = ''

# Stany robota
chooseRobotState = {
    '0': "idle",
    '4': "walk",
    '5': "rotate_left",
    '6': "rotate_right",
    '7': "body_manipulation",
    '8': "torque_enable",
    '9': "torque_disable",
}

movementDirection = {
    '1': 1,
    '2': -1,
}

moveBindings = {
    'w': (10, 0, 0),
    's': (-10, 0, 0),
    'd': (0, 10, 0),
    'a': (0, -10, 0),
    'q': (0, 0, 10),
    'e': (0, 0, -10),
}

rotationBindings = {
    'u': (2, 0, 0),
    'i': (-2, 0, 0),
    'j': (0, 2, 0),
    'k': (0, -2, 0),
    'm': (0, 0, 2),
    ',': (0, 0, -2),
}