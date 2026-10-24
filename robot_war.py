# This is day 60 (project day) of daily practice from cgpt

enemies = {
    "Scout": {
        "health": 30,
        "damage": 10,
        "reward": 10
    },
    "Tank": {
        "health": 60,
        "damage": 20,
        "reward": 25
    },
    "Boss": {
        "health": 100,
        "damage": 30,
        "reward": 50
    }
}

# Task 1
def battle_turn(robot_health, energy, enemy_health, action):
  if action == "attack" and energy >= 10:
    energy -= 10
    enemy_health -= 20
  elif action == "heavy_attack" and energy >= 20:
    energy -= 20
    enemy_health -= 35
  elif action == "recharge":
    energy = min(50, energy + 20)
  return (robot_health, energy, enemy_health)

# Task 2
def enemy_attack(robot_health, enemy_name, enemies):
  robot_health -= enemies[enemy_name]["damage"]
  return robot_health

# Task 3
def defeat_enemy(enemy_name, enemies, score, defeated):
  if enemy_name not in defeated:
    defeated.add(enemy_name)
    score += enemies[enemy_name]["reward"]
  return (f"Score: {score}\nDefeated: {defeated}")
