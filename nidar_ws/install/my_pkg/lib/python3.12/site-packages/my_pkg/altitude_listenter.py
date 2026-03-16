import rclpy
from rclpy.node import Node
from px4_msgs.msg import VehicleLocalPosition
from rclpy.qos import qos_profile_sensor_data


class AltSub(Node):
    def __init__(self):
        super().__init__("altitude_listener")

        self.sub = self.create_subscription(
            VehicleLocalPosition,
            "/fmu/out/vehicle_local_position_v1",
            self.altitude_callback,
            qos_profile_sensor_data
        )

        self.get_logger().info("Altitude listener started")

    def altitude_callback(self, msg):
        altitude = -msg.z
        self.get_logger().info(f"Altitude: {altitude}")


def main(args=None):
    rclpy.init(args=args)
    node = AltSub()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()