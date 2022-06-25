pirate_ships_status = input().split(">")
pirate_ships_status = list(map(int, pirate_ships_status))

warships_status = input().split(">")
warships_status = list(map(int, warships_status))

maximum_health_capacity = int(input())
command = input()

while command != "Retire":
    command = command.split(" ")
    current_command = command[0]

    if current_command == "Fire":
        index = int(command[1])
        damage = int(command[2])

        if 0 <= index < len(warships_status):
            current_section_health = warships_status[index]
            current_section_health -= damage
            if current_section_health <= 0:
                print(f"You won! The enemy ship has sunken.")
                exit()
            else:
                warships_status[index] = current_section_health

    elif current_command == "Defend":
        start_idx = int(command[1])
        end_idx = int(command[2])
        damage = int(command[3])
        if 0 <= start_idx < end_idx < len(pirate_ships_status):
            for ship in range(start_idx, end_idx + 1):
                pirate_ships_status[ship] -= damage
                if pirate_ships_status[ship] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    exit()

    elif current_command == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ships_status):
            if pirate_ships_status[index]+health >= maximum_health_capacity:
                pirate_ships_status[index] = maximum_health_capacity
            else:
                pirate_ships_status[index] += health
    elif current_command == "Status":
        ship_for_repair = list()
        for ship in pirate_ships_status:
            if ship < (maximum_health_capacity * 0.2):
                ship_for_repair.append(ship)
        count_ship_repair = len(ship_for_repair)
        print(f"{count_ship_repair} sections need repair.")

    command = input()

pirate_ships_status_sum = sum(pirate_ships_status)
warships_status_sum = sum(warships_status)
print(f"Pirate ship status: {pirate_ships_status_sum}")
print(f"Warship status: {warships_status_sum}")