import math

def intervalos(s, f):
    x = []
    i = 0
    s.insert(0, 0)
    f.insert(0, -math.inf)
    for k in range(1, len(s)):
        if(s[k]>f[i]):
            x.append(1)
            i=k
        else:
            x.append(0)
    return x

def main():
    s = [4, 6, 13, 4, 2, 6, 7,  9,  1, 3,  9]
    f = [8, 7, 14, 5, 4, 9, 10, 11, 6, 13, 12]
    sf = list(zip(s, f))
    sf.sort(key= lambda x: x[1])
    s = [x for x, y in sf]
    f = [y for x, y in sf]
    print(f"s {s}")
    print(f"f {f}")
    print(f"x {intervalos(s, f)}")

if __name__ == "__main__":
    main()
        