
class SuspicionAnalyzer:

    def __init__(self):
        self.players = {}

    def register(self, color):
        if color not in self.players:
            self.players[color] = {
                "score": 0,
                "evidence": []
            }

    def add_evidence(self, color, description, points):
        self.register(color)

        points = max(0, min(points, 100))

        player = self.players[color]
        player["score"] = min(
            100, player["score"] + points
        )

        player["evidence"].append(description)

    def get_ranking(self):
        return sorted(
            self.players.items(),
            key=lambda item: item[1]["score"],
            reverse=True
        )

    def report(self):
        print("\n=== DETECTIVE AI: INVESTIGAÇÃO ===")

        for color, data in self.get_ranking():
            print(f"\n{color}: {data['score']}/100")

            for evidence in data["evidence"]:
                print("-", evidence)
          
