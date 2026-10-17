
import math
import time

class PlayerTracker:

    def __init__(self):
        self.players = {}

    def update(self, detections):
        current_time = time.time()

        for player in detections:
            color = player["color"]
            x, y = player["position"]

            if color not in self.players:
                self.players[color] = {
                    "position": (x, y),
                    "last_seen": current_time,
                    "distance": 0
                }
                continue

            old_x, old_y = self.players[color]["position"]

            distance = math.sqrt(
                (x - old_x) ** 2 +
                (y - old_y) ** 2
            )

            self.players[color]["distance"] += distance
            self.players[color]["position"] = (x, y)
            self.players[color]["last_seen"] = current_time

    def get_report(self):
        for color, data in self.players.items():
            print(
                color,
                "Posição:", data["position"],
                "Distância percorrida:",
                round(data["distance"], 2)
            )
          
