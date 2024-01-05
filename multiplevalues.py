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

def main():
    n = int(input("Enter n value: "))

    for i in range(n):
        print(f"Data set {i + 1}")
        t = float(input("Enter t value: "))
        h = float(input("Enter h value: "))
        w = float(input("Enter w value: "))

        process_input(t, h, w)

if __name__ == "__main__":
    main()
