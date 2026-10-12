import math
from solar_physics import Star, Planet, recalculate_space_objects_positions

def run_kepler_test():
    sun = Star()
    sun.m = 2.0E30  
    sun.x = 0.0
    sun.y = 0.0
    sun.Vx = 0.0
    sun.Vy = 0.0

    planet = Planet()
    planet.m = 3.0E24  
    planet.x = 1.5E11  
    planet.y = 0.0
    planet.Vx = 0.0
    planet.Vy = 29780.0  

    space_objects = [sun, planet]
    
    dt = 3600  
    steps = 24 * 365  
    
    sector_speeds = []

    for _ in range(steps):
        recalculate_space_objects_positions(space_objects, dt)

        r_squared = planet.x**2 + planet.y**2
 
        sector_speed = 0.5 * abs(planet.x * planet.Vy - planet.y * planet.Vx)
        sector_speeds.append(sector_speed)

    mean_speed = sum(sector_speeds) / len(sector_speeds)
    max_deviation = max(abs(s - mean_speed) for s in sector_speeds)
    relative_error = (max_deviation / mean_speed) * 100

    print(f"Средняя секторная скорость: {mean_speed:.4e}")
    print(f"Максимальное отклонение: {max_deviation:.4e}")
    print(f"Относительная погрешность выполнения закона Кеплера: {relative_error:.4f}%")

if __name__ == "__main__":
    run_kepler_test()