def calc_watts(volts, amps):
    """
    Calculates wattage from device's voltage and amperage.
    :param volts: float, voltage of device
    :param amps: float, amperage of device
    :return: float, wattage of device
    """
    return volts * amps

def calc_avg_usage(watt_hours, devices_list):
    """
    Calculates the average watt hours per device
    :param watt_hours: float, the total watt hours
    :param devices_list: list, used to count num of elements/devices to avg
    :return: float, average Watt Hours of all devices
    """
    avg_watt_hours = 0
    avg_watt_hours = watt_hours / len(devices_list)

    return avg_watt_hours

def calc_energy_cost(watt_hours, energy_price):
    """
    Calculates the energy cost by the watt hours given
    :param watt_hours: float, Watt Hours
    :param energy_price: float, price of energy per kW in cents
    :return: float, energy cost in $"""
    energy_price = convert_price_kW_to_W(energy_price)
    energy_price = convert_cents_to_dollars(energy_price)

    energy_cost = 0.00
    energy_cost = watt_hours * energy_price

    return energy_cost

def convert_price_kW_to_W(kW):
    """
    Converts price per kWh to Wh
    :param kW: float, number in kW
    :return: float, price per watt
    """
    W = 0.0
    W = kW / 1000
    return W

def convert_cents_to_dollars(cents):
    """
    Converts cents to dollars
    :param cents: float, cents
    :return: float, converted number in dollars
    """
    dollars = 0
    dollars = cents / 100
    return dollars