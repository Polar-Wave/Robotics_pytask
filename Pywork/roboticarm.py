def valid_angle_check(angle):
    return 0 <= angle <= 180

def convert(angle):
    return angle*10

input = [30,-15,45,200,60,90]

valid_angles = filter(valid_angle_check, input)
valid_angles_list = list(valid_angles)

servo_commands = map(convert, valid_angles_list)
servo_commands_list = list(servo_commands)

print(f"Valid angles: {valid_angles_list}")
print(f"Servo commands: {servo_commands_list}")