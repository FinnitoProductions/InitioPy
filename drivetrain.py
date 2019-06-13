import gpiozero


class Drivetrain:
   def __init__(self, leftMotors, rightMotors):
      self.leftMotors = leftMotors
      self.rightMotors = rightMotors

   def setBothOutputs(self, leftOutput, rightOutput):
      for leftMotor in self.leftMotors:
         if leftOutput > 0:
            leftMotor.forward(leftOutput)
         else:
            leftMotor.backward(-leftOutput)

      for rightMotor in self.rightMotors:
         if rightOutput > 0:
            rightMotor.forward(rightOutput)
         else:
            rightMotor.backward(-rightOutput)
