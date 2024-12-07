if __name__ == '__main__':
    with open("day 1/input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
        
    numbers = [int(x) for line in lines for x in line.split('  ')]
    xs = []
    ys = []
    for line in lines:
        x, y = line.split('  ')
        print(x, y)
        xs.append(int(x))
        ys.append(int(y))
    sorted_xs = sorted(xs)
    sorted_ys = sorted(ys)
    similarity = 0
    print(sorted_xs)
    print(sorted_ys)
    for i, x in enumerate(sorted_xs):
        a = sorted_ys.copy()
        if x in a:
            a = [item for item in a if item == x]
        else:
            continue
        appearance_count = len(a)
        similarity = similarity + x*appearance_count
    print(similarity)    
  
