"""Data Logging and Plotting"""

import random, time
import matplotlib.pyplot as plt

temps = []
for t in range(10):
    temp = 25 + random.randint(-1, 1)
    temps.append(temp)
    with open("temps.csv", "a") as f:
        f.write(f"{temp}\n")
    time.sleep(0.5)

plt.plot(temps)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Log")
plt.show()

"""# Task
Modify the existing code to generate and log both temperature and humidity data. The new data should be saved to `temp_humidity.csv` and `temp_humidity.txt` files, with error handling for file operations. Finally, update the plotting to visualize both temperature and humidity data separately.

## Modify Logging to Include Humidity

### Subtask:
Modify the code to generate random humidity values along with temperature. Store both in a suitable data structure (e.g., a list of dictionaries or separate lists).

**Reasoning**:
The user wants to modify the existing code to include humidity data generation, store it in a new list, and remove the file writing and sleep operations. I will provide a code block that reflects these changes.
"""

import random, time
import matplotlib.pyplot as plt

temps = []
humidity_data = [] # Initialize a new list for humidity data
for t in range(10):
    temp = 25 + random.randint(-1, 1)
    temps.append(temp)
    humidity = random.randint(40, 60) # Generate random humidity
    humidity_data.append(humidity) # Store humidity
    # Removed file writing and time.sleep as per instructions

plt.plot(temps)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Log")
plt.show()

"""## Implement CSV Logging with Error Handling

### Subtask:
Add functionality to save the temperature and humidity data to a new CSV file (`temp_humidity.csv`). This step will include writing a header row and each data point, wrapped in a `try-except` block to handle potential file writing errors.

**Reasoning**:
The subtask requires implementing CSV logging with error handling for temperature and humidity data. The provided instructions detail how to achieve this using a `try-except` block and iterating through the generated data.
"""

import random, time
import matplotlib.pyplot as plt

temps = []
humidity_data = [] # Initialize a new list for humidity data
for t in range(10):
    temp = 25 + random.randint(-1, 1)
    temps.append(temp)
    humidity = random.randint(40, 60) # Generate random humidity
    humidity_data.append(humidity) # Store humidity
    # Removed file writing and time.sleep as per instructions

# --- Start of new functionality for CSV logging ---
file_name_csv = "temp_humidity.csv"

try:
    with open(file_name_csv, "w") as f:
        f.write("Time,Temperature,Humidity\n") # Write header
        for i in range(len(temps)):
            f.write(f"{i},{temps[i]},{humidity_data[i]}\n") # Write data row
    print(f"Successfully wrote data to {file_name_csv}")
except IOError as e:
    print(f"Error writing to {file_name_csv}: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# --- End of new functionality for CSV logging ---

plt.plot(temps)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Log")
plt.show()

"""## Implement TXT Logging with Error Handling

### Subtask:
Add functionality to save the temperature and humidity data to a new TXT file (`temp_humidity.txt`). This step will include writing each data point, wrapped in a `try-except` block to handle potential file writing errors.

#### Instructions
1. Open a new file named `temp_humidity.txt` in write mode. Use a `try-except` block to handle `IOError` or any other exceptions that might occur during file operations. If an error occurs, print an informative error message.
2. Iterate through the `temps` and `humidity_data` lists. For each iteration, write the temperature and humidity, perhaps separated by a space or tab, to the TXT file. A header is optional for a simple TXT log, but consistent formatting is key.
3. Ensure the file is properly closed after writing, which can be done automatically using a `with open(...)` statement.

**Reasoning**:
The previous markdown block outlined the subtask of implementing TXT logging with error handling. This code block will implement that functionality, saving the temperature and humidity data to a new TXT file, including error handling.
"""

import random, time
import matplotlib.pyplot as plt

temps = []
humidity_data = [] # Initialize a new list for humidity data
for t in range(10):
    temp = 25 + random.randint(-1, 1)
    temps.append(temp)
    humidity = random.randint(40, 60) # Generate random humidity
    humidity_data.append(humidity) # Store humidity
    # Removed file writing and time.sleep as per instructions

# --- Start of new functionality for CSV logging ---
file_name_csv = "temp_humidity.csv"

try:
    with open(file_name_csv, "w") as f:
        f.write("Time,Temperature,Humidity\n") # Write header
        for i in range(len(temps)):
            f.write(f"{i},{temps[i]},{humidity_data[i]}\n") # Write data row
    print(f"Successfully wrote data to {file_name_csv}")
except IOError as e:
    print(f"Error writing to {file_name_csv}: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# --- End of new functionality for CSV logging ---

# --- Start of new functionality for TXT logging ---
file_name_txt = "temp_humidity.txt"

try:
    with open(file_name_txt, "w") as f:
        for i in range(len(temps)):
            f.write(f"Time: {i}, Temperature: {temps[i]}°C, Humidity: {humidity_data[i]}%\n") # Write data row to TXT
    print(f"Successfully wrote data to {file_name_txt}")
except IOError as e:
    print(f"Error writing to {file_name_txt}: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# --- End of new functionality for TXT logging ---

plt.plot(temps)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Log")
plt.show()



import random, time
import matplotlib.pyplot as plt

temps = []
humidity_data = [] # Initialize a new list for humidity data
for t in range(10):
    temp = 25 + random.randint(-1, 1)
    temps.append(temp)
    humidity = random.randint(40, 60) # Generate random humidity
    humidity_data.append(humidity) # Store humidity
    # Removed file writing and time.sleep as per instructions

# --- Start of new functionality for CSV logging ---
file_name_csv = "temp_humidity.csv"

try:
    with open(file_name_csv, "w") as f:
        f.write("Time,Temperature,Humidity\n") # Write header
        for i in range(len(temps)):
            f.write(f"{i},{temps[i]},{humidity_data[i]}\n") # Write data row
    print(f"Successfully wrote data to {file_name_csv}")
except IOError as e:
    print(f"Error writing to {file_name_csv}: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# --- End of new functionality for CSV logging ---

# --- Start of new functionality for TXT logging ---
file_name_txt = "temp_humidity.txt"

try:
    with open(file_name_txt, "w") as f:
        for i in range(len(temps)):
            f.write(f"Time: {i}, Temperature: {temps[i]}°C, Humidity: {humidity_data[i]}%\n") # Write data row to TXT
    print(f"Successfully wrote data to {file_name_txt}")
except IOError as e:
    print(f"Error writing to {file_name_txt}: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# --- End of new functionality for TXT logging ---

# --- Start of new functionality for plotting both temperature and humidity ---
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1) # 1 row, 2 columns, first plot
plt.plot(temps, color='red')
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Log")

plt.subplot(1, 2, 2) # 1 row, 2 columns, second plot
plt.plot(humidity_data, color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Humidity (%)")
plt.title("Humidity Log")

plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
plt.show()
# --- End of new functionality for plotting both temperature and humidity ---

