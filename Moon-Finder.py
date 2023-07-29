import pylunar

mi = pylunar.MoonInfo((12, 52, 11.6), (80, 7, 54.3))
mi.update((2023, 8,1, 18,27, 29))
print("Moon Age:", mi.age())
print("Moon Fractional Phase: ",mi.fractional_phase())
print("Moon Phase Name", mi.phase_name())
print("Moon Altitude",mi.altitude())
print("Moon Azimuth",mi.azimuth())
print("Next Full Moon", mi.time_to_full_moon())


