import random

def scavenge_event(player, shelter):
    result = random.choice(["success", "radiation", "death"])
    if result == "success":
        shelter.supplies["food"] += 2
        return f"{player.name} found food!"
    elif result == "radiation":
        player.health -= 30
        return f"{player.name} was exposed to radiation!"
    else:
        player.status = "dead"
        return f"{player.name} never returned from scavenging..."

def hatch_event(shelter):
    outcomes = [
        "Trader offers supplies", "Raiders steal supplies",
        "Mutant attacks", "Survivor joins"
    ]
    outcome = random.choice(outcomes)
    if outcome == "Raiders steal supplies":
        shelter.supplies["food"] = max(0, shelter.supplies["food"] - 3)
    return outcome
