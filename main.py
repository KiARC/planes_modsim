from modsim import State, TimeSeries
from random import randint

# Constants (Start, Dest, volume, time)
planes = State(Miami=0, Dulles=0, Design=0)

planes_miami = TimeSeries()
planes_dulles = TimeSeries()
planes_design = TimeSeries()

in_air = []

"""
Does the thing that makes the simulation simulate stuff

p1: probability 1
p2: probability 2
num_steps: number of steps
"""


def run_simulation(steps):
    planes_miami[0] = 12
    planes_dulles[0] = 15
    planes_design[0] = 25
    for i in range(1, steps):
        step()
        planes_miami[i] = planes.Miami
        planes_dulles[i] = planes.Dulles
        planes_design[i] = planes.Design


def takeoff(origin, dest, count, time):
    global in_air
    planes[origin] -= count
    for _ in range(count):
        in_air.append([dest, time])
    return in_air

"""
A single step in the simulation

p1: probability 1
p2: probability 2
"""

def step():
    global in_air
    randomInts = [randint(1, 12) for i in range(12)]

    takeoff("Miami", "Dulles", randomInts[0], randomInts[1])
    takeoff("Miami", "Design", randomInts[2], randomInts[3])
    takeoff("Dulles", "Miami", randomInts[4], randomInts[5])
    takeoff("Dulles", "Design", randomInts[6], randomInts[7])
    takeoff("Design", "Miami", randomInts[8], randomInts[9])
    takeoff("Design", "Dulles", randomInts[10], randomInts[11])
    temp = in_air
    count = 0
    for i in range(len(in_air)):
        if in_air[1] == 1:
            del temp[i]
            dest, _ = i
            planes[dest] += 1
            continue
        temp[i][1] -= 1
        count += 1
    in_air = temp


run_simulation(100)

""" Graphy stuff
results_wheaton.plot(label="Wheaton")
results_silver_spring.plot(label="Silver Spring")
decorate(title='Wheaton-SilverSpring Bikeshare',
         xlabel='Time step (min)', 
         ylabel='Number of bikes per location')
plt.show()
"""
print(
    f"Miami:\n{planes_miami}\nDulles:\n{planes_dulles}\nDesign:\n{planes_design}")