from input import input


packets = input.split("\n")

sum = 0
ribonsum = 0


for packet in packets:
    sizes = packet.split("x")

    l = int(sizes[0])
    w = int(sizes[1])
    h = int(sizes[2])

    side1 = l * w
    side2 = w * h
    side3 = h * l

    perimiters = [l * 2 + w * 2, w * 2 + h * 2, h * 2 + l * 2]
    perimiters.sort()

    sides = [side1, side2, side3]
    sides.sort()

    ribonsum += perimiters[0] + l * w * h
    sum += sides[0] * 3 + sides[1] * 2 + sides[2] * 2

print(sum, ribonsum)