#!/usr/bin/env python3

import wpilib
from ctre.cantalon import CANTalon
from magicbot import MagicRobot

from components.drivetrain import Drivetrain


class Robot(MagicRobot):

    drivetrain = Drivetrain

    def createObjects(self):
        self.robot_drive = wpilib.RobotDrive(
            0, 1, 2, 3, motorController=CANTalon)

        self.drive_joystick = wpilib.Joystick(0)
        self.operator_joystick = wpilib.Joystick(1)

    def teleopPeriodic(self):
        self.drivetrain.turn_at(
            self.drive_joystick.getRawAxis(0), squaredInputs=True)
        self.drivetrain.forward_at(self.drive_joystick.getRawAxis(1))


if __name__ == '__main__':
    wpilib.run(Robot)
