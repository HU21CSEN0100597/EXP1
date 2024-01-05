def main():
    static_values()

def static_values():
    t = 35.0
    h = 60.0
    w = 70.0

    process_input(t, h, w)

def process_input(t, h, w):
    W = 0.5 * t**2 - 0.2 * h - 0.1 * w - 15
    print(W)

    if W > 300:
        print("Sunny")
    elif 200 < W <= 300:
        print("Cloudy")
    elif 100 < W <= 200:
        print("Rainy")
    else:
        print("Stormy")

if __name__ == "__main__":
    main()
