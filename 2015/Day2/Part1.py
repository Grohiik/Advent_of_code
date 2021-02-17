from Day2.input import input



packets = input.split("\n")


for packet in packets:
    sizes = packet.split("x")

    l = sizes[0]
    w = sizes[1]
    h = sizes[2]

    side1 = l*w
    side2 = w*h
    side3 = h*l

    