plant = input("Enter the name of plant: ")
if plant.lower() == 'spathiphyllum':
    if plant.islower():
        print("No, I want a big Spathiphyllum!")
    else:
        print("Yes - Spathiphyllum is the best plant ever!")
else:
    print("Spathiphyllum! Not",plant,"!")