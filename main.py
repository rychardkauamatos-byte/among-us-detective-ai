
from datetime import datetime

class AmongUsDetective:

    def __init__(self):
        self.players = {}

    def register_player(self, color):
        self.players[color] = {
            "suspicion": 0,
            "evidence": []
        }

    def add_evidence(self, color, evidence, points):
        if color not in self.players:
            self.register_player(color)

        self.players[color]["suspicion"] += points
        self.players[color]["evidence"].append(evidence)

    def report(self):
        print("\n=== AMONG US DETECTIVE AI ===")
        print("Data:", datetime.now())

        for color, data in sorted(
            self.players.items(),
            key=lambda item: item[1]["suspicion"],
            reverse=True
        ):
            print(f"\nJogador: {color}")
            print(f"Suspeita: {data['suspicion']} pontos")

            for evidence in data["evidence"]:
                print("-", evidence)


detective = AmongUsDetective()

detective.add_evidence(
    "Vermelho", "Seguiu outro jogador", 15
)

detective.add_evidence(
    "Azul", "Permaneceu parado", 5
)

detective.report()
