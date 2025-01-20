import random


weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]


weaponRoll = random.randint(1,6)
print(f"You rolled a {weaponRoll}. You will use the weapon: {weapons[weaponRoll - 1]}")


combatStrength = int(input("Enter your combat Strength: "))
weaponStrength = weaponRoll

totalCombatStrength = combatStrength + weaponStrength
print(f"Your total combat strength with the {weapons[weaponRoll - 1]} is: {totalCombatStrength}")

print(f"Your weapon is: {weapons[weaponRoll - 1]}")

if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if weapons[weaponRoll - 1] != "Fist":
    print(f"Thank goodness you didn't roll the Fist...")

try:
    combatStrength = int(input("Enter your combat Strength: "))
    if combatStrength < 0:
        raise ValueError("Combat strength cannot be negative!")
except ValueError as e:
    print(f"Error: {e}")
    exit()
