age = int(input("Enter Age: "))
maximumHeartRate = 220 - age
print('The maximumHeartRate is :', maximumHeartRate)
target_heartRate = 50 % - 85 % maximumHeartRate
minimum = (0.5 * maximumHeartRate)
maximum = (0.85 * maximumHeartRate)
print('Range of Target heart rate is : ', minimum, ' - ', maximum)
