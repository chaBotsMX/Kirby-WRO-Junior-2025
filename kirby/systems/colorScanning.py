from pybricks.tools import wait

class ColorScanSystem:
    def __init__(self, color_sensor):
        self.colorSensor = color_sensor

    def scanCurrentColor(self, iterations):
        h_total = 0
        s_total = 0
        v_total = 0

        for i in range(iterations):
            h = self.colorSensor.hsv().h
            s = self.colorSensor.hsv().s
            v = self.colorSensor.hsv().v

            h_total += h
            s_total += s
            v_total += v
            wait(1)

        h_avg = h_total / iterations
        s_avg = s_total / iterations
        v_avg = v_total / iterations

        if (h_avg >= 330 or h_avg <= 30) and s_avg > 20:
            return("red")

        elif 40 <= h_avg <= 70 and s_avg > 30:
            return("yellow")

        elif 100 <= h_avg <= 170 and s_avg > 30:
            return("green")

        elif v_avg < 2:
            return("blank")

        else:
            return("white")