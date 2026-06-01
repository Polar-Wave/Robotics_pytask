from line_follower_robot.sensor import fetch_sensor, count_line
from line_follower_robot.movement import movementer

def main():
    sensor_list = fetch_sensor()
    sensor_count = count_line(sensor_list)
    print(f"\nSensor values: {sensor_list}")
    print(f"Active sensors: {sensor_count}")

    roboaction = movementer(sensor_list)
    print(f"Robot action: {roboaction}")

if __name__ == "__main__":
    main()