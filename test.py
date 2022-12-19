# Sample Run:

# Welcome to the Electricity Usage Calculator

# This program is to help you determine the electricity usage and energy costs of
# your electrical devices, taking the wattage of your devices and the number of
# hours they were used, and doing a number of calculations.
# Once you have entered all of your devices, the total amount of
# power consumed (in Watt Hours), and the estimated cost, will be displayed.

# Enter the price per kWh of your electricity (typically found on your utility
# company's website), in cents: ¢8.5

# Enter name of device: LED Light Strip
# Do you know the wattage of the device? (y/n): n
# Enter voltage of device: 12.2
# Enter amperage of device: 2
# Enter number of hours used: 3.5

# Your LED Light Strip uses 24.40 Watts.
# Running for 3.50 hours, your LED Light Strip will consume 85.40 Watt Hours
# of energy and cost $0.0073 at the given price for electricity.

# Would you like to enter another device? (y/n): y

# Enter name of device: Fan
# Do you know the wattage of the device? (y/n): y
# Enter wattage of device: 5.5
# Enter number of hours used: 15.25

# Your Fan uses 5.5 Watts.
# Running for 15.25 hours, your Fan will consume 83.88 Watt Hours of energy
# and cost $0.0071 at the given price for electricity.

# Would you like to enter another device? (y/n): n

# Device Name         Wattage        Hours Used     Energy Consumed   Cost ($)
# _______________     __________     __________     __________        __________
# LED Light Strip     24.40 W        3.50           85.40 Wh          $0.0073
# Fan                 5.50 W         15.25          83.88 Wh          $0.0071
# _______________
# Total:              29.90 W        18.75          169.27            $0.0144

# In total, all of your devices, running for 18.75 hours, will consume 169.27
# Watt Hours of energy, costing $0.0144 at the energy price of $0.0850 per kWh.

#******************************************************************************
import energyusage

device_1 = energyusage.Device('LED Light', amps=12.2, volts=3, hours_used=5.5)