# Computer-Info-Program
A short Python script that will help you to discover more infromation about your computer CPU, memory and battery.

## Project's Uses:
The main library used in this mini project is [psutil](https://pypi.org/project/psutil/). 

With the help of the library mentioned above you will see after running the .py file:
* the CPU user
* CPU's system
* CPU interrupt
* CPU percent usage
* Number of logic CPU's
* Number pf physical CPU's

These information will be displayed as a Data Frame, using Python's library Pandas.

After that, you will precisely see the RAM memory and how much is still available. 

## The most important part of the project:
You will be able to see the battery's percentage in the last part of the code. With the help of the function __sec2hours__, you will also find out how many hours, minutes and seconds will take till the battery run out or if your device is charging.
<br></br>

```Python
# Displaying the battery percentage and time remaining till discharge
print("\nComputer's battery: ")
battery = psutil.sensors_battery()
time_to_charge = sec2hours(battery.secsleft)
if time_to_charge[0] == "-":
    print(f"Charge = {battery.percent}%, Time left = Is charging")
else:
    print("Charge = %s%%, Time left = %s" % (battery.percent, sec2hours(battery.secsleft)))

```



