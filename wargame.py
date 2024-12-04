# With a correction already implemented: dont forget to initialize an instance of Class "War"


from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
great_war = War()

#Create 5 Vikings
for i in range(0, 5):
    if i:  # Ensure the loop starts after the first iteration
        name = soldier_names[random.randint(0, 9)]  # Randomly select a name
        health = 100  # Fixed health for Vikings
        strength = random.randint(0, 100)  # Random strength between 0 and 100
        great_war.addViking(Viking(name, health, strength))  # Add Viking to the Viking army

#Create 5 Saxons
for i in range(0, 5):
    if i:  # Ensure the loop starts after the first iteration
        health = 100  # Fixed health for Saxons
        strength = random.randint(0, 100)  # Random strength between 0 and 100
        great_war.addSaxon(Saxon(health, strength))  # Add Saxon to the Saxon army
# Simulate the war
round = 0  # Track the number of rounds
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    # Perform attacks
    great_war.vikingAttack()  # Vikings attack first
    great_war.saxonAttack()  # Saxons retaliate

    # Print the current status of the war
    print(f"Round: {round} // Viking army: {len(great_war.vikingArmy)} warriors, Saxon army: {len(great_war.saxonArmy)} warriors")
    print(great_war.showStatus())  # Print the current status
    round += 1  # Increment the round counter