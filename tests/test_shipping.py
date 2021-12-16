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


