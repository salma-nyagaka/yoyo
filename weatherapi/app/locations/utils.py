import statistics


def perform_computations(data):
    """Function to get get the minimum, maximum, average and median temperature for a
    given city and period of time."""

    temp_in_celsius = []
    temp_in_fahrenheit = []

    for d in data["forecast"]["forecastday"]:
        temp_in_celsius.append(d["day"]["avgtemp_c"])
        temp_in_fahrenheit.append(d["day"]["avgtemp_f"])

    # get average of temperature in both celcius degrees
    # and fahrenheit
    average = {
        "average_temp_in_celcius": sum(temp_in_celsius) / len(temp_in_celsius),
        "average_temp_in_fahrenheit": sum(temp_in_fahrenheit) / len(temp_in_fahrenheit),
    }

    # get maximum of temperature in both celcius degrees
    # and fahrenheit
    maximum = {
        "max_temp_in_celcius": max(temp_in_celsius),
        "max_temp_in_fahrenheit": max(temp_in_fahrenheit),
    }

    # get minimum of temperature in both celcius degrees
    # and fahrenheit
    minimum = {
        "min_temp_in_celcius": min(temp_in_celsius),
        "min_temp_in_fahrenheit": min(temp_in_fahrenheit),
    }

    # get median of temperature in both celcius degrees
    # and fahrenheit
    median = {
        "median_temp_in_celcius": statistics.median(temp_in_celsius),
        "median_temp_in_fahrenheit": statistics.median(temp_in_fahrenheit),
    }

    data = {
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
        "median": median,
    }

    return data
