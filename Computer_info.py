import psutil
import pandas as pd


# Function that converts the number of seconds into minutes and hours
def sec2hours(sec):
    mm, ss = divmod(sec, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


# System CPU times
CPU_times = psutil.cpu_times()

# The current system-wide CPU utilization as a %. When interval is > 0.0 compares system CPU times elapsed before and
# after the interval (blocking)
CPU_percent = psutil.cpu_percent(interval=1)

# If we want to display this percentage for each CPU we use the following command:
# psutil.cpu_percent(interval=1, percpu=True)

# Number of logica cores:
logic_CPU = psutil.cpu_count()

# Number of physical cores:
physical_CPU = psutil.cpu_count(logical=False)

# Various CPU statistics
# psutil.cpu_stats()

"""
All these information about the CPU will be displayed in a data frame
"""

data_CPU = {

    "user": CPU_times[0],
    "system": CPU_times[1],
    "interrupt": CPU_times[3],
    "dpc": CPU_times[4],
    "CPU percent": [CPU_percent],
    "No. of logic CPUs": [logic_CPU],
    "No. of physical CPUs": [physical_CPU]
}

# Creating the data frame from the CPU information
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
CPU_dataframe = pd.DataFrame(data_CPU)
print("\nInformation about computer's CPU: \n", CPU_dataframe)


# Information about the computer's memory
memory_info = psutil.virtual_memory()

list_memoryInfo = []
for element in memory_info:
    list_memoryInfo.append(element)

# Converting memory Information from bytes to GB using list comprehension
print("\nInformation about computer's memory")
GB_value = [value/10**9 for value in list_memoryInfo]
GB_value[2] = memory_info[2]
print("- Total memory = %.2f GB \n- Available = %.2f GB \n- Percent = %d \n- Used = %.2f GB \n- Free = %.2f GB" % (GB_value[0], GB_value[1], GB_value[2], GB_value[3], GB_value[4]))


# Displaying the battery percentage and time remaining till discharge
print("\nComputer's battery: ")
battery = psutil.sensors_battery()
time_to_charge = sec2hours(battery.secsleft)
if time_to_charge[0] == "-":
    print(f"Charge = {battery.percent}%, Time left = Is charging")
else:
    print("Charge = %s%%, Time left = %s" % (battery.percent, sec2hours(battery.secsleft)))
