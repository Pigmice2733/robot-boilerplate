#!/usr/bin/env python3

import wpilib
from ctre.cantalon import CANTalon
from magicbot import MagicRobot
import ctre

from components.drivetrain import Drivetrain
from components.intake import Intake, Action as IntakeAction


class Robot(MagicRobot):

    intake = Intake
    drivetrain = Drivetrain

    def createObjects(self):
        self.robot_drive = wpilib.RobotDrive(
            0, 1, 2, 3, motorController=CANTalon)

        self.l_intake_motor = CANTalon(4)
        self.r_intake_motor = CANTalon(5)

        self.drive_joystick = wpilib.Joystick(0)
        self.operator_joystick = wpilib.Joystick(1)

    def teleopPeriodic(self):
        self.drivetrain.turn_at(
            self.drive_joystick.getRawAxis(0), squaredInputs=True)
        self.drivetrain.forward_at(self.drive_joystick.getRawAxis(1))

        action = IntakeAction.Stop

        if self.drive_joystick.getRawButton(1):
            action = IntakeAction.Outtake

        if self.drive_joystick.getRawButton(2):
            action = IntakeAction.Intake

        self.intake.cur_action = action


if __name__ == '__main__':
    wpilib.run(Robot)
