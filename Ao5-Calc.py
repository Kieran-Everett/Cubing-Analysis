while True:
    solves = []
    for i in range(1, 6):
        solves.append(float(input(f"Solve {i}: ")))
    

    ao5 = (sum(solves)-max(solves)-min(solves))/3
    print(f"Average of 5: {ao5}")