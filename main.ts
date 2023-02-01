input.onButtonPressed(Button.A, function () {
    Kitronik_Robotics_Board.stepperMotorTurnAngle(Kitronik_Robotics_Board.StepperMotors.Stepper1, Kitronik_Robotics_Board.MotorDirection.Reverse, 180)
    basic.showString("a")
})
input.onButtonPressed(Button.B, function () {
    Kitronik_Robotics_Board.stepperMotorTurnAngle(Kitronik_Robotics_Board.StepperMotors.Stepper1, Kitronik_Robotics_Board.MotorDirection.Reverse, 180)
    basic.showString("b")
})
Kitronik_Robotics_Board.setStepperMotorSteps(Kitronik_Robotics_Board.StepperMotors.Stepper1, 2038)
basic.forever(function () {
	
})
