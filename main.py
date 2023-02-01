def on_button_pressed_a():
    Kitronik_Robotics_Board.stepper_motor_turn_angle(Kitronik_Robotics_Board.StepperMotors.STEPPER1,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        180)
    basic.show_string("a")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Kitronik_Robotics_Board.stepper_motor_turn_angle(Kitronik_Robotics_Board.StepperMotors.STEPPER1,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        180)
    basic.show_string("b")
input.on_button_pressed(Button.B, on_button_pressed_b)

Kitronik_Robotics_Board.set_stepper_motor_steps(Kitronik_Robotics_Board.StepperMotors.STEPPER1, 2038)

def on_forever():
    pass
basic.forever(on_forever)
