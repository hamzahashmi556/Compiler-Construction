from prettytable import PrettyTable


def initialize():
    global name, A, M, C, Z, minPriority, maxPriority, simulation, precision, arrSimulation, arrZ, arrR, arrRand, arrPriority

    # name  = "LCG"
    # A = 55
    # M = 1994
    # C = 9
    # Z = 10112166
    # minPriority = 1
    # maxPriority = 3
    # simulation = 10
    # precision = 5

    name = input("Enter name: ")
    A = int(input("Enter A: "))
    M = int(input("Enter M: "))
    C = int(input("Enter C: "))
    Z = 10112166
    minPriority = 1
    maxPriority = int(input("Enter priority 1 to "))
    simulation = int(input("Enter number of simulations: "))
    precision = int(input("Enter decimal precision: "))

    arrSimulation = []
    arrZ = []
    arrR = []
    arrRand = []
    arrPriority = []


def push(no, Z, R, Rand, Priority):
    arrSimulation.append(no)
    arrZ.append(Z)
    arrR.append(R)
    arrRand.append(Rand)
    arrPriority.append(Priority)


if __name__ == "__main__":
    # Q -> Generate Probability And Pseudo Random Numbers Using LCG
    initialize()
    for i in range(simulation):
        no = i + 1
        R = (A * Z + C) % M
        Rand = round(R / M, precision)
        Priority = int(round((maxPriority - minPriority) * Rand + minPriority, 0))
        push(no, Z, R, Rand, Priority)
        Z = R

    table = PrettyTable()
    table.title = name
    table.field_names = ["Simulation", "Z", "R (LCG)", "Random Number (X)", "Priority (Y)"]

    # Add rows to the table
    for i in range(len(arrSimulation)):
        table.add_row([arrSimulation[i], arrZ[i], arrR[i], arrRand[i], arrPriority[i]])

    print(table)