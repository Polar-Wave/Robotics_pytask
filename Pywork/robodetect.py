detections = [
{"object": "box", "confidence": 78, "mode": "infrared", "distance": 2.5},
{"object": "human", "confidence": 95, "mode": "camera", "distance": 1.2},
{"object": "ball", "confidence": 82, "mode": "ultrasonic", "distance": 3.0},
{"object": "human", "confidence": 88, "mode": "camera", "distance": 0.8},
{"object": "chair", "confidence": 70, "mode": "infrared", "distance": 2.8}
]

human_detect= list(filter(lambda x: x["object"]=="human" and x["mode"]=="camera" and x["confidence"]>85,detections))

human_distance= list(map(lambda x: x["distance"], human_detect))

def proximity(distances):
    for distance in distances:
        if distance < 1.0:
            print(f"Distance {distance}m: ALERT: Human very close!")
        else:
            print(f"Distance {distance}m: Human detected at safe distance.")

print(f"\nHuman detections: {human_detect}")
print(f"\nHuman distances: {human_distance}\n")
proximity(human_distance)