from pybricks.tools import StopWatch

class PDControl:
    def __init__(self, kp=0, kd=0, min_output=None, max_output=None):
        self.kp = kp
        self.kd = kd

        self.min_output = min_output
        self.max_output = max_output

        self.last_error = 0
        self.timer = StopWatch()

    def reset(self):
        self.last_error = 0
        self.timer.reset()

    def compute(self, error):
        p = self.kp * error

        dt = self.timer.time() / 1000
        derivative = (error - self.last_error) / dt if dt > 0 else 0
        d = derivative * self.kd

        output = p + d
        
        self.timer.reset()
        self.last_error = error

        # Apply min output properly (with sign)
        if self.min_output is not None and abs(output) > 0:
            if abs(output) < self.min_output:
                output = self.min_output * (1 if output > 0 else -1)

        # Apply max output
        if self.max_output is not None:
            if abs(output) > self.max_output:
                output = self.max_output * (1 if output > 0 else -1)

        return output