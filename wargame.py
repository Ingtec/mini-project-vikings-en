# With a correction already implemented: don't forget to initialize an instance of Class "War"

from vikingsClasses import Soldier, Viking, Saxon, War  # Import classes
import random  # For random values

# List of potential soldier names for Vikings
soldier_names = ["albert", "andres", "archie", "dani", "david", "gerard", "german", "graham", "imanol", "laura"]

# Initialize the War instance
great_war = War()

# Create 5 Vikings
for i in range(5):
    # Randomly select a name and assign random strength
    name = soldier_names[random.randint(0, len(soldier_names) - 1)]
    health = 100  # Fixed health for all Vikings
    strength = random.randint(50, 100)  # Random strength between 50 and 100
    great_war.addViking(Viking(name, health, strength))  # Add Viking to the army

# Create 5 Saxons
for i in range(5):
    health = 100  # Fixed health for all Saxons
    strength = random.randint(30, 70)  # Random strength between 30 and 70
    great_war.addSaxon(Saxon(health, strength))  # Add Saxon to the army

# Simulate the war
round = 0  # Track the number of rounds
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    # Alternate attacks
    great_war.vikingAttack()
    great_war.saxonAttack()

    # Print the current status of the war
    print(f"Round {round}:")
    print(f"  Viking Army: {len(great_war.vikingArmy)} warriors")
    print(f"  Saxon Army: {len(great_war.saxonArmy)} warriors")
    print(f"  Status: {great_war.showStatus()}")
    print("-" * 40)  # Separator for readability

    # Increment the round counter
    round += 1

# Print the final outcome
print("\nThe war is over!")
print(great_war.showStatus())
