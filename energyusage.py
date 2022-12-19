#******************************************************************************
#                       Electricity Usage Calculator
# Author:      Brendan Krueger
# Vesion:      1.0.0 - 12/18/2022
# Description: This program prompts for local electricity costs,
#              the voltage and amperage of a device,
#              and the number of hours it was running, and calculates the total
#              Watt Hours consumed. The user can calculate this for multiple
#              devices. Once finished, data for all devices is displayed.
#
# Input:       energy cost (float), device name (str),
#              device wattage known prompt (str), device watts (float),
#              device volts (float), device amps (float), hours device
#              used (float), additional device prompt (string)
#
# Output:      Watts, and watt hours consumed by each device in the given
#              amount of time.
#              Cost of using device for specified amount of time
#              Table with usage and cost calculations for all devices
#              Hours used and watt hours consumed by all devices
#              Electricity cost per device and in total
#******************************************************************************
import valid
from electricity import calc_watts, calc_avg_usage, calc_energy_cost
from electricity import convert_cents_to_dollars
# import pickle

# Device Object

class Device():
    """
    Electrical Device Object
    """
    name = ""
    __watts = 0.0
    __amps = None
    __volts = None
    __hours_used = 0.0
    __energy_cost = None

    def __init__(self, name, watts=None, amps=None, volts=None, hours_used=0.0):
        """
        Sets fields, and calcs and sets watt hours from given watt and hours.
        :param name: str, name of device
        :param watts: float, wattage of device,
                      optional if amps and volts given
        :param amps: float, amperage, used to calc watts
        :param volts: float, voltage, used to calc watts
        :param hours_used: float, hours device was/is to be used
        """
        self.set_name(name)
        self.set_watts(watts, amps, volts)
        self.set_hours_used(hours_used)
        self.calc_watt_hours()

    def __str__(self):
        """
        Prints device attributes/fields
        :return: None
        """
        return ("Device(Name: {}, Wattage: {:}, Amps: {}, Volts: {}, Hours Used: {:}, "
        "Watt Hours: {:}, Energy Cost: {})").format(
            self.name, self.__watts, self.__amps, self.__volts,  self.__hours_used,
            self.__watt_hours, self.__energy_cost)

    def get_name(self):
        return self.name

    def get_watts(self):
        return self.__watts

    def get_amps(self):
        return self.__amps

    def get_volts(self):
        return self.__volts

    def get_hours_used(self):
        return self.__hours_used

    def get_watt_hours(self):
        return self.__watt_hours

    def get_energy_cost(self):
        return self.__energy_cost

    def set_name(self, name):
        self.name = name

    def set_watts(self, watts=None, amps=None, volts=None):
        """
        Sets device watts. If volt and amp args present, sets by volts * amps
        Either wattage, or amps and volts, must be passed to the function
        If all three are present, amps and volts will take precedent.
        :param watts: float, wattage of device
        :param amps: amps, amperage of device
        :param volts: volts, voltage of device
        :return: float, wattage of device
        """
        self.__amps = amps
        self.__volts = volts
        watts = (amps * volts) if (amps and volts) else watts
        self.__watts = watts
        return watts

    def set_amps(self, amps):
        self.__amps = amps

    def set_volts(self, volts):
        self.__volts = volts

    def set_hours_used(self, hours_used):
        self.__hours_used = hours_used

    def calc_watt_hours(self):
        """
        Calculates, sets and returns device watt hours used.
        :return: float, device's energy consumption in watt hours
        """
        watt_hours = 0.0
        watt_hours = self.__watts * self.__hours_used
        self.__watt_hours = watt_hours
        return watt_hours

    def set_energy_cost(self, energy_price):
        """
        Sets the energy cost field of this device, using given energy price
        :param energy_price: Price of energy in cents
        :return: Energy cost of device
        """
        self.__energy_cost = calc_energy_cost(self.__watt_hours, energy_price)

        return self.__energy_cost


def main():
    device = None
    total_hours_used = 0.00
    total_watt_hours = 0.00
    avg_watt_hours = 0.00
    energy_price_kWh = 0.00
    another = True

    devices = []

    print_welcome()
    energy_price_kWh = prompt_energy_price()

    while (another == True):
        # Inputs
        device = get_device(devices)
        device.set_energy_cost(energy_price_kWh)
        devices.append(device)

        # Outputs
        print_wattage(device.get_name(), device.get_watts())
        print_consumption(device.get_hours_used(), device.get_name(),
                          device.get_watt_hours(), device.get_energy_cost())

        another = prompt_another_device()

    # Post Loop Calculations
    total_hours_used = calc_list_sum([d.get_hours_used() for d in devices])
    total_watt_hours = calc_list_sum([d.get_watt_hours() for d in devices])
    avg_watt_hours = calc_avg_usage(
        total_watt_hours, [d.get_watt_hours() for d in devices])
    total_energy_cost = calc_list_sum([d.get_energy_cost() for d in devices])

    # Final Output
    print_devices(devices)
    print_totals(calc_list_sum([d.get_watts() for d in devices]),
                 total_hours_used, total_watt_hours, total_energy_cost)
    print_total_watt_hours(total_hours_used, total_watt_hours,
                           total_energy_cost,
                           convert_cents_to_dollars(energy_price_kWh))

# Input Functions
def print_welcome():
    """
    Prints a welcome message describing what the program does.
    :return: None
    """
    print("Welcome to the Electricity Usage Calculator\n")
    print("This program will determine the electricity usage and energy costs"
          "of\nyour electrical devices, taking the price of your electricity\n"
          "(typically found on your utility company's website), wattage of \n"
          "your devices and the number of hours they were used, and \n"
          "displaying the estimated usage and cost. \n")
    print("Once you have entered all of your devices, amount of power \n"
          "consumed (in Watt Hours), and the estimated costs, will be \n"
          "displayed in total and for each device individually.")

def prompt_energy_price():
    """
    Prompts for energy price per kilowatt hours
    :return: float, price of energy per kilowatt hours, in cents (¢)
    """
    energy_price = 0.0
    energy_price = valid.get_real_positive(
        "\nEnter the price per kWh of your electricity, in cents: ¢")
    return energy_price

def get_device(devices):
    """
    Prompts for device and usage and returns relevant information
    :param devices: list, list of devices to check name
    :return: Device Object

    """
    device = {}
    device_name = prompt_device_name([d.name for d in devices])
    device_watts = get_watts()
    hours_used = prompt_hours_used()
    device = Device(name=device_name, watts=device_watts,
              hours_used=hours_used)
    return device

def prompt_device_name(device_names):
    """
    Prompts user for name of their electronic device and returns str of name.
    :device_names: list, list of names of devices, to check for duplicates
    :return: str, device_name
    """
    device_name = ""
    device_name = valid.get_string("\nEnter name of device: ", device_names)
    return device_name

def prompt_watts():
    """
    Prompts user for wattage of their device and returns wattage
    :return: float, wattage of device
    """
    wattage = 0.0
    wattage = valid.get_real_positive("Enter wattage of device: ")
    return wattage

def prompt_volts():
    """
    Prompts user for voltage of their device and returns float of voltage.
    :return: float, voltage of device
    """
    voltage = 0.0
    voltage = valid.get_real_positive("Enter voltage of device: ")
    return voltage

def prompt_amps():
    """
    Prompts user for amperage of their device and returns float of amperage.
    :return: float, amperage of device
    """
    amperage = 0.0
    amperage = valid.get_real_positive("Enter amperage of device: ")
    return amperage

def prompt_hours_used():
    """
    Prompts user for the number of hours they used their device and returns it.
    :return: float, number of hours device was used
    """
    hours = 0.0
    hours = valid.get_real_positive("Enter number of hours your device was used: ")
    return hours

def prompt_know_wattage():
    """
    Asks user if they know the wattage of their device.
    Recursively re-runs if given the wrong input.
    :return: bool, whether wattage is known
    """
    watts_known = ""
    watts_known = valid.get_y_or_n("Do you know the wattage of the device? (y/n): ")
    return watts_known

def prompt_another_device():
    """
    Asks user if they want to input another device
    Recursively re-runs if given the wrong input
    :return: bool, True for 'yes' or False for 'no'
    """
    more = ""
    more = valid.get_y_or_n(("\nWould you like to enter another device? (y/n): "))
    return more


def get_watts():
    """
    Gets watts with user prompt functions, then calculates/returns wattage
    :return: float, Wattage of device
    """
    device_watts = 0.0
    watts_known = False
    device_volts = 0.0
    device_amps = 0.0

    watts_known = prompt_know_wattage()
    if watts_known:
        device_watts = prompt_watts()
    else:
        device_volts = prompt_volts()
        device_amps = prompt_amps()
        device_watts = calc_watts(device_volts, device_amps)
    return device_watts

# Calculation Functions

def calc_list_sum(list):
    """
    Takes a list of numbers and adds them together, returns a sum total
    :param list: list of numbers
    :return: float, sum total of numbers in the list
    """
    sum = 0
    for num in list:
        sum = sum + num
    return sum

# Output Functions

def print_wattage(device_name, wattage):
    """
    Displays wattage of device to user.
    :param device_name: str, name of device
    :param wattage: float, wattage of device
    :return: None
    """
    print("\nYour {0} uses {1:.2f} Watts".format(device_name, wattage))

def print_consumption(hours_used, device_name, watt_hours, cost):
    """
    Displays the energy consumption of user's device, along with hours used.
    :param hours_used: float, number of hours device was used
    :param device_name: str, name of device
    :param watt_hours: float, watt hours device has consumed
    :return: None
    """
    print(
        ("Running for {0:.2f} hours, your {1} will consume {2:.2f} Watt Hours "
         "of energy and cost ${3:.4f} at the given price for electricity.")
        .format(hours_used, device_name, watt_hours, cost, ".2f"))

def print_total_watt_hours(tot_hours_used, tot_watt_hours,
                           tot_energy_cost, energy_price):
    """
    Displays the energy consumption and hour usage total of all devices inputted.
    :param tot_hours_used: float, total number of hours devices were used
    :param tot_watt_hours: float, total watt hours devices consumed
    :param tot_energy_cost: float, total energy cost for all devices
    :param energy_price: float, price of energy in DOLLARS
    :return: None
    """
    print(
        "\nIn total, all of your devices, running for {0:.2f} hours, will"
        " consume {1:.2f} Watt Hours of energy,\n"
        "costing ${2:.4f} at the energy price of ${3:.4f} per kWh."
        .format(tot_hours_used, tot_watt_hours, tot_energy_cost, energy_price))

def print_avg_watt_hours(device_list, avg_watt_hours):
    """
    Displays the average energy consumption between all the devices
    :param device_list: list, used to count # of devices
    :param avg_watt_hours: float, the average number of consumption per device
    :return: None
    """
    print(
        "Your {0} devices will consume on average {1:.2f} "
        "Watt Hours per device.".format(
            len(device_list), avg_watt_hours))

def print_devices(devices):
  """
  Displays devices and their energy consumption in columned list
  Lists should be parallel, every list needs to have same # of items
  :param devices: list, list of Device objects
  :return: None
  """
  print("\n")
  print("{: <20}{: <15}{: <15}{: <18}{: <15}".format("Device Name", "Wattage",
                                       "Hours Used", "Energy Consumed", "Cost ($)"))
  print("{: <20}{: <15}{: <15}{: <18}{: <15}".format(
      "_______________ ", "__________", "__________", "__________", "__________"))

  for device in devices:
    watt_str = '%.2f W' % device.get_watts()
    wh_str = '%.2f Wh' % device.get_watt_hours()
    cost_str = '$%.4f' %  device.get_energy_cost()
    print("{: <20}{: <15}{: <15.2f}{: <18}{: <15}".format(
        device.name, watt_str, device.get_hours_used(), wh_str, cost_str))

def print_totals(watt_total, hours_used_total,
                  watt_hours_total, cost_total):
  """
  Displays devices and their energy consumption in columned list
  Lists should be parallel, every list needs to have same # of items
  :param name_list: list, names of devices
  :param watt_list: list, wattage of devices
  :param hours_used_list: list, hours each device was used
  :param watt_hours_list: list, energy consumption in watt/hours of devices
  :param cost_list: list, cost of energy consumed in watt hours
  :return: None
  """
  #print("{: <20}{: <15}{: <15}{: <18}{: <15}".format("Device Name", "Wattage",
  #                                     "Hours Used", "Energy Consumed", "Cost ($)"))
  print("_______________ ")
  watt_str = '%.2f W' % watt_total
  wh_str = '%.2f Wh' % watt_hours_total
  cost_str = '$%.4f' % cost_total
  print("{: <20}{: <15}{: <15.2f}{: <18}{: <15}".format(
        'Total:', watt_str, hours_used_total, wh_str, cost_str))

main()
