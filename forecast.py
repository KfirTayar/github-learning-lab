def forecast_population(base, planned, realization=1.0):
    if base < 0 or planned < 0:
        raise ValueError("Population values must be non-negative")
    if not 0 <= realization <= 1:
        raise ValueError("Realization must be between 0 and 1")
    return base + planned * realization
