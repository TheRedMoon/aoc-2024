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
    remains = []
    print(sorted_xs)
    print(sorted_ys)
    for i, x in enumerate(sorted_xs):
        remain = x-sorted_ys[i]
        if(remain<0):
            remain = remain*-1
        remains.append(remain)
    print(sum(remains))
    
  
