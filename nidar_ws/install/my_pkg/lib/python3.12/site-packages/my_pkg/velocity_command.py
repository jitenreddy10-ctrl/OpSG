import rclpy
from rclpy.node import Node
from px4_msgs.msg import TrajectorySetpoint
from rclpy.qos import qos_profile_sensor_data
import math

class VelocityControl(Node):
    def __init__(self):
        super().__init__("celocity_control")

        self.pub = self.create_publisher(
            TrajectorySetpoint
            ,
            "/fmu/in/trajectory_setpoint",
            qos_profile_sensor_data
        )

        self.timer = self.create_timer(1.0,self.publish_velocity)

    def publish_velocity(self):
        msg = TrajectorySetpoint()
        msg.velocity = [1.0,0.0,0.0]
        msg.position = [math.nan,math.nan,math.nan]
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = VelocityControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()