import numpy as np
import matplotlib.pyplot as plt
import time
import random

try:
    R = 1000
    C = 1e-6
    V = 5

    t = np.linspace(0, 0.01, 1000)
    Vc = V * (1 - np.exp(-t / (R*C)))

    plt.plot(t, Vc)
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.title("RC Charging Curve")
    plt.show()

    csv_file = open("data.csv", "w")
    txt_file = open("log.txt", "w")

    csv_file.write("Timestamp,Temperature,Humidity\n")
    txt_file.write("Log Data\n")
    txt_file.write("--------------------\n")

    temp_list = []
    hum_list = []
    time_list = []

    for i in range(10):
        t = time.strftime("%H:%M:%S")
        temp = 25 + random.uniform(-1, 1)
        hum = 50 + random.uniform(-5, 5)

        temp_list.append(temp)
        hum_list.append(hum)
        time_list.append(i)

        csv_line = str(t) + "," + str(temp) + "," + str(hum) + "\n"
        csv_file.write(csv_line)

        txt_line = "Time: " + str(t) + " | Temp: " + str(temp) + " | Hum: " + str(hum) + "\n"
        txt_file.write(txt_line)

        time.sleep(1)

    csv_file.close()
    txt_file.close()

except Exception as e:
    print("A problem occurred:", e)
