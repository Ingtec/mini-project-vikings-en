import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
       # Initialize Soldier with health and strength
        self.health = health
        self.strength = strength
    def attack(self):
        # Return the strength of the soldier
        return self.strength

    def receiveDamage(self, damage):
         # Reduce health by the damage received
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # Initialize Viking with name, health, and strength
        super().__init__(health, strength)
        self.name = name
    def battleCry(self):
        # Return the Viking's battle cry
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # Deduct health and return a message based on remaining health
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # Initialize Saxon with health and strength
        super().__init__(health, strength)

    def receiveDamage(self, damage):
         # Deduct health and return a message based on remaining health
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
         # Initialize War with empty Viking and Saxon armies
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
       # Add a Viking to the Viking army
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # Add a Saxon to the Saxon army
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
         # Perform a Viking attack on a random Saxon
        target_saxon = random.choice(self.saxonArmy)
        attacking_viking = random.choice(self.vikingArmy)
        damage_message = target_saxon.receiveDamage(attacking_viking.strength)
        if target_saxon.health <= 0:
            self.saxonArmy.remove(target_saxon)
        return damage_message
    
    def saxonAttack(self):
        # Perform a Saxon attack on a random Viking
        target_viking = random.choice(self.vikingArmy)
        attacking_saxon = random.choice(self.saxonArmy)
        damage_message = target_viking.receiveDamage(attacking_saxon.strength)
        if target_viking.health <= 0:
            self.vikingArmy.remove(target_viking)
        return damage_message

    def showStatus(self):
    # Return the current status of the war
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
