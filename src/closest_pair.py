def pairwise_line(arr):
    pair_wise_x = []
    x = sorted(arr)
    dis = [(x[i+1]-x[i],(x[i+1],x[i]))   for i in range(len(arr)-1)]
    print(dis)
    # sum_x = sum([p[0] for p in points])
    # while sum_x > 0:

def pairwise(points):
    pair_wise_x = []
    x = sorted(points,key=lambda p:p[0])
    dis_x = []
    for i in range(len(x) - 1):
        dis_x.append([(x[i+1][0]-x[i][0],(x[i+1],x[i])) ])
    y = sorted(points,key=lambda p:p[1])
    dis_y = sorted([(y[i+1][1]-y[i][1],(y[i+1],y[i])) for i in range(len(y)-1)])

    print(dis_x)
    print(dis_y)


def closest_pair(points):
    # x = sorted(p[])
    # Your code here!
    pass


points = (
    (2, 2),  # A
    (2, 8),  # B
    (2, 5),  # C
    (6, 3),  # D
    (6, 7),  # E
    (7, 4),  # F
    (7, 9)  # G
)

print(pairwise(points))