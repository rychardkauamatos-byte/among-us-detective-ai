
import cv2
import numpy as np

class PlayerDetector:

    def __init__(self):
        self.colors = {
            "Vermelho": [
                ((0, 100, 80), (10, 255, 255)),
                ((170, 100, 80), (180, 255, 255))
            ],
            "Azul": [
                ((90, 100, 80), (130, 255, 255))
            ],
            "Verde": [
                ((35, 80, 70), (85, 255, 255))
            ],
            "Amarelo": [
                ((20, 100, 100), (35, 255, 255))
            ]
        }

    def detect(self, image):
        hsv = cv2.cvtColor(
            image, cv2.COLOR_BGR2HSV
        )

        results = []

        for color, ranges in self.colors.items():
            mask = np.zeros(
                hsv.shape[:2], dtype=np.uint8
            )

            for lower, upper in ranges:
                part = cv2.inRange(
                    hsv,
                    np.array(lower),
                    np.array(upper)
                )
                mask = cv2.bitwise_or(mask, part)

            contours, _ = cv2.findContours(
                mask,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )

            for contour in contours:
                area = cv2.contourArea(contour)

                if area < 100:
                    continue

                x, y, w, h = cv2.boundingRect(contour)

                results.append({
                    "color": color,
                    "position": (x + w // 2, y + h // 2),
                    "area": area
                })

        return results
          
