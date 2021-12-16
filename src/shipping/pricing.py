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
