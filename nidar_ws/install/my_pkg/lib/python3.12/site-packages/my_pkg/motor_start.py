import rclpy
from rclpy.node import Node
from px4_msgs.msg import VehicleCommand
from rclpy.qos import qos_profile_sensor_data


class MotorStart(Node):

    def __init__(self):
        super().__init__("motor_start")

        self.pub = self.create_publisher(
            VehicleCommand,
            "/fmu/in/vehicle_command",
            qos_profile_sensor_data
        )

        self.timer = self.create_timer(5.0, self.arm)

    def arm(self):
        cmd = VehicleCommand()

        cmd.command = VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM
        cmd.param1 = 1.0

        cmd.target_system = 1
        cmd.target_component = 1
        cmd.source_system = 1
        cmd.source_component = 1
        cmd.from_external = True

        self.pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = MotorStart()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()