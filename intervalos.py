import math

def intervalos(s, f):
    x = []
    i = 0
    s.insert(0, 0)
    f.insert(0, -math.inf)
    for k in range(1, len(s)):
        if(s[k]>f[i]):
            x.append(k)
            i=k
    return x

def main():
    s = [4, 6, 13, 4, 2, 6, 7,  9,  1, 3,  9]
    f = [8, 7, 14, 5, 4, 9, 10, 11, 6, 13, 12]
    print(f"s {s}")
    print(f"f {f}")
    print(intervalos(s, f))

if __name__ == "__main__":
    main()
        