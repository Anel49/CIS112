# assumes that 1.6 kilometers == 1 mile.
def dist_to_empty_km(gallons_remaining, miles_per_gallon):
    
    mi_to_go = gallons_remaining * miles_per_gallon              
    km_to_go = mi_to_go * 1.6
    return km_to_go

# assume the minutes parameter is an non-negative integer.
# how many fortnights, days, hours, and minutes are included in that period?
def timing(minutes):

    num_fortnight = int(minutes / 20160)
    minutes -= num_fortnight * 20160
    num_days = int(minutes / 1440)
    minutes -= num_days * 1440
    num_hours = int(minutes / 60)
    minutes -= num_hours * 60
    num_minutes = int(minutes)

    return (num_fortnight, num_days, num_hours, num_minutes)

# how many scruples are in a pool with our given dimensions?
# call int() on your answer to make it a nice, whole number.
def scruples(depth_feet, length_feet, width_feet):

    volume = float(depth_feet * length_feet * width_feet)
    acres = (volume / 43560.0)
    acres_in_gals = (acres * 325851.0)   
    acres_in_scruples = (acres_in_gals * 3072.0)

    return int(acres_in_scruples)