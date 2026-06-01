def fetch_sensor():
    data = input("Enter 6 sensor readings (0 or 1) separated by spaces (for e.g., 0 0 1 1 0 0): ").strip()

    sensor_list = list(map(int, data.split()))

    
    if len(sensor_list) != 6:
        print("Invalid input! Please enter a 6-digit number.")
        return None
    
    return sensor_list

def count_line(sensor_list):
    detected =list(filter(lambda x: x == 1, sensor_list))
    return len(detected)
