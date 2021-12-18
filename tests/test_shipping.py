import shipping.pricing

def test_ocean_shipment():
    assert shipping.pricing.get_ocean_shipment_price() == 30

def test_truck_shipment_regular():
    assert shipping.pricing.get_truck_regular_price() == 25

def test_truck_shipment_urgent():
    assert shipping.pricing.get_truck_urgent_price() == 45

def test_air_shipment_cost_weight():
    #weight, volume
    assert shipping.pricing.calculate_air_shipment_cost(11, 5) == 110

def test_air_shipment_cost_volume():
    #weight, volume
    assert shipping.pricing.calculate_air_shipment_cost(4, 5) == 100

#name fucntion with verb noun verb_noun (good for readability)

def test_identify_conveyance_type():
    #weight, volume (cubic meters) 
    assert shipping.pricing.identify_conveyance_type(9, 126) == ("truck", "boat")
    assert shipping.pricing.identify_conveyance_type(9, 120, False) == ("truck", "boat", "plane")
    assert shipping.pricing.identify_conveyance_type(9, 120, True) == ("plane",) #fuction return same data type

def test_is_urgent():
    assert shipping.pricing.is_urgent("12/16/2021", "12/18/2021") is True
    assert shipping.pricing.is_urgent("12/16/2021", "12/20/2021") is False

def test_is_dangerous():
    assert shipping.pricing.is_dangerous("y") is True
    assert shipping.pricing.is_dangerous("n") is False


def test_validate_input():
    scenarios = []
    scenarios.append({
        "customer_name": "John Hunter Battle",
        "package_description": "HPZ210",
        "dangerous": "Y",
        "weight": "11",
        "volume": "10",
        "delivery_date": "12/25/2021",
        "international_destination": "No",
    })
    scenarios.append({
        "customer_name": "White house",
        "package_description": "12",
        "dangerous": "354",
        "weight": "yes",
        "volume": "test",
        "delivery_date": "tomorrow",
        "international_destination": "no",
    })
    for senario in scenarios:
        senario_validated = shipping.pricing.validate_input(senario)



#def test_get_input():
#    assert shipping.pricing.get_input()