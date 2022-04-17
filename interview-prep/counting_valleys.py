"""
Hike always starts and ends at sea level.

mountain - is a sequence of consecutive steps above sea level,
starting with a step up from sea level and ending with a step down to sea level.

valley - is a sequence of consecutive steps below sea level,
starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike,
find and print the number of valleys walked through.
"""

#import os

class Hike:
    def __init__(self, path: str):
        self._path = path
        self._steps = len(path)
        self._valleys = 0
        self._mountains = 0
        self._alt = 0

    @property
    def path(self):
        return self._path

    @property
    def valleys(self):
        return self._valleys

    @property
    def mountains(self):
        return self._mountains

    @property
    def steps(self):
        return self._steps

    def calc_hike(self):
        """
        psuedocode
        if U
            increase alt by 1
            if now returning to sea level, valley += 1
        if D
            decrease alt by 1
            if now returning to sea level, mountain += 1
        """
        for step in self._path:
            if step.upper() == 'U':
                self._alt += 1
                if self._alt == 0:
                    self._valleys += 1
            elif step.upper() == 'D':
                self._alt -= 1
                if self._alt == 0:
                    self._mountains += 1
            else:
                raise ValueError(f"Error occurred: step: {step}, is NOT U or D")


if __name__ == "__main__":
    # Commented code is stuff hackerrank needs for its submission/testing system

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #steps = int(input().strip())
    #path = input()
    p_input = 'UDDDUDUU'
    hike = Hike(p_input)
    hike.calc_hike()

    print(hike.valleys)
    #fptr.write(str(hike.valleys) + '\n')
    #fptr.close()
