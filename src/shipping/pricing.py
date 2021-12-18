import datetime
def get_ocean_shipment_price():
    return 30

def get_truck_regular_price():
    return 25

def get_truck_urgent_price():
    return 45

#weight, volume

def calculate_air_shipment_cost(weight, volume):
    weight = weight * 10
    volume = volume * 20
    if weight > volume:
        return weight
    return volume

#weight, volume (cubic meters)
def identify_conveyance_type(weight, volume, urgent=True):
    if weight >= 10 or volume >= 125:
        return "truck", "boat"
    if urgent:
        return "plane",
    return "truck", "boat", "plane"


def is_urgent(request_delivery_date, start_date):
    x = request_delivery_date.split("/")
    y = start_date.split("/")
    #TODO: NEED TO REWORK FOR BUSINESS DAYS
    difference = (datetime.datetime(int(y[2]), int(y[0]), int(y[1])) - datetime.datetime(int(x[2]), int(x[0]), int(x[1]))).days
    if difference <= 3:
        return True
    return False


def is_dangerous(dangerous):
    if dangerous in "yY":
        return True
    return False


def get_input():
    pass


def is_customer_name_valid(test):
    if len(test) > 6:
        return True
    return False


def validate_input(data):
    is_customer_name_valid()


    #request_delivery_date = datetime.datetime(request_delivery_date)
    #datetime.datetime
    #if request_delivery_date - start_date >= 3:
    #    return True
    #return False