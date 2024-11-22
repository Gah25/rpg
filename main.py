from random import randint

npcs_list = []

player = {
    "name": input("Digite o nome do personagem: "),
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "damage": 100,
}


def create_npc(level):
    return {
        "name": f"Monster #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level,
    }


def spawn_npcs(n_npcs):
    for x in range(n_npcs):
        npcs_list.append(create_npc(x + 1))


def show_player():
    print(
        f"Name: {player['name']} | Level: {player['level']} | Damage: {player['damage']} | HP: {player['hp']}/{player['hp_max']} | EXP: {player['exp']}/{player['exp_max']}"
    )


def level_up():
    if player["exp"] >= player["exp_max"]:
        player["level"] += 1
        player["exp"] = 0
        player["exp_max"] *= 2
        player["hp_max"] += 20
        player["damage"] += 5
        print(f"Parabéns! {player['name']} subiu para o nível {player['level']}! HP e dano foram aumentados.")


def attack_npc(npc):
    damage = randint(player["damage"] - 5, player["damage"] + 5)
    npc["hp"] = max(npc["hp"] - damage, 0)
    print(f"Você atacou {npc['name']} causando {damage} de dano!")


def attack_player(npc):
    damage = randint(npc["damage"] - 3, npc["damage"] + 3)
    player["hp"] = max(player["hp"] - damage, 0)
    print(f"{npc['name']} atacou você causando {damage} de dano!")


def defense_npc(npc):
    reduced_damage = max(randint(player["damage"] - 5, player["damage"] + 5) - 5, 0)
    npc["hp"] = max(npc["hp"] - reduced_damage, 0)
    print(f"{npc['name']} defendeu e recebeu apenas {reduced_damage} de dano!")


def defense_player(npc):
    reduced_damage = max(randint(npc["damage"] - 3, npc["damage"] + 3) - 5, 0)
    player["hp"] = max(player["hp"] - reduced_damage, 0)
    print(f"Você defendeu e recebeu apenas {reduced_damage} de dano!")


def show_info_battle(npc):
    print(f"{player['name']}: {player['hp']}|{player['hp_max']}")
    print(f"{npc['name']}: {npc['hp']}|{npc['hp_max']}")
    print("-----------------------\n")


def start_battle(npc):
    if npc["hp"] <= 0:
        print(f"{npc['name']} já foi derrotado!")
        return
    
    print(f"Iniciando batalha contra {npc['name']}!")
    while player["hp"] > 0 and npc["hp"] > 0:
        player_action = input("'A' para atacar, 'D' para defender: ").strip().lower()
        npc_action = "a" if randint(0, 1) == 0 else "d"

        if player_action not in ["a", "d"]:
            print("Comando inválido! Tente novamente.")
            continue

        if player_action == "a" and npc_action == "a":
            print("Ambos atacaram!")
            attack_npc(npc)
            if npc["hp"] > 0:
                attack_player(npc)
        elif player_action == "a" and npc_action == "d":
            print(f"{npc['name']} defendeu seu ataque!")
            defense_npc(npc)
        elif player_action == "d" and npc_action == "a":
            print(f"{npc['name']} atacou enquanto você defendia!")
            defense_player(npc)
        elif player_action == "d" and npc_action == "d":
            print("Ambos defenderam. Nada aconteceu!")

        show_info_battle(npc)

    if player["hp"] > 0:
        print(f"{player['name']} venceu e ganhou {npc['exp']} EXP!")
        player["exp"] += npc["exp"]
        level_up()
    else:
        print(f"{npc['name']} venceu a batalha!")
    
    player["hp"] = player["hp_max"]


spawn_npcs(1000)

for npc in npcs_list:
    if player["hp"] > 0:
        start_battle(npc)
    else:
        print("Você foi derrotado! Game Over.")
        break

show_player()
