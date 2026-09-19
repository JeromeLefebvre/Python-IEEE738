import cigre601
import conductor
import ieee738

# Weather data - 5 minute values from Openeweather
ambient_temperature = 50.0
wind_speed = 0 

# Monthly averages from BOM
solar_irradiation = 1000

# Calculation
angle_of_attack = 90

# design
conductor_temperature = 85.0
# Have to figure this out?
horizontal_angle = 0
# not part of the data set
elevation = 0.0

cigre = cigre601.thermal_rating(
    ambient_temperature,
    wind_speed,
    angle_of_attack,
    solar_irradiation,
    conductor.venus_constants,
    conductor_temperature,
    horizontal_angle,
    elevation=elevation,
)
print(f"cigre601: {cigre}")

ieee = ieee738.thermal_rating(
    ambient_temperature,
    wind_speed,
    angle_of_attack,
    solar_irradiation,
    conductor.venus_constants,
    conductor_temperature,
    horizontal_angle,
    elevation=elevation,
)
print(f"ieee738: {ieee}")



