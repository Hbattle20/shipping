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
    else:
        return volume

#weight, volume (cubic meters)
def identify_conveyance_type(weight, volume, urgent=True):
    if weight >= 10 or volume >= 125:
        return "truck", "boat"
    else:
        if urgent:
            return "plane",
        else:
            return "truck", "boat", "plane"

def is_urgent(request_delivery_date, start_date):
    x = request_delivery_date.split("/")
    y = start_date.split("/")
    w = datetime.datetime(int(x[2]), int(x[0]), int(x[1]))
    b = datetime.datetime(int(y[2]), int(y[0]), int(y[1]))
    c = w - b 
    print(c)
    if c <= 3:
        return True
    return False
is_urgent("12/11/1995", "12/10/1995")



    #request_delivery_date = datetime.datetime(request_delivery_date)
    #datetime.datetime
    #if request_delivery_date - start_date >= 3:
    #    return True
    #return False