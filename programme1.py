"""exercice calculer un integrale"""
from math import*
def sommek():
    ss = int(input("Donner un nombre ss: "))
    terme = 0  # Initialize the sum
    n = 1  # Start from the first term

    while True:
        terme1 = terme  # Store the previous sum
        terme += 1 / n**ss  # Add the current term to the sum
        
        # Check if the difference is less than or equal to 10^(-6)
        if abs(terme - terme1) <= 10**(-6):
            break
            
        n += 1  # Move to the next term

    print(f"La somme est: {terme}")

# Call the function
sommek()
   
            