def movementer(sensor_list):
    if sensor_list == [0, 0, 1, 1, 0, 0]:
        return "Move forward"
    elif sensor_list == [0, 1, 1, 0, 0, 0] or sensor_list == [0, 1, 1, 1, 0, 0] or sensor_list == [1, 1, 0, 0, 0, 0] or sensor_list == [1, 1, 1, 1, 0, 0] or sensor_list == [1, 1, 1, 0, 0, 0] or sensor_list == [1, 0, 0, 0, 0, 0]or sensor_list == [0, 1, 0, 0, 0, 0] or sensor_list == [0, 0, 1, 0, 0, 0]:
        return "Turn left"
    elif sensor_list == [0, 0, 0, 1, 1, 0] or sensor_list == [0, 0, 1, 1, 1, 0] or sensor_list == [0, 0, 0, 0, 1, 1] or sensor_list == [0, 0, 1, 1, 1, 1] or sensor_list == [0, 0, 0, 1, 1, 1] or sensor_list == [0, 0, 0, 0, 0, 1] or sensor_list == [0, 0, 0, 0, 1, 0] or sensor_list == [0, 0, 0, 1, 0, 0]:
        return "Turn right"
    elif sensor_list == [1, 1, 1, 1, 1, 1]:
        return "Junction detected"
    else:
        return "No line detected! Stop robot"
