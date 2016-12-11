
def recursion(point, points, classified, index):
    if index not in classified:
        classified[index] = []

    cur_x, cur_y = point
    for x in xrange(cur_x-1,cur_x+2):
        for y in xrange(cur_y-1,cur_y+2):
            # print (x,y)
            is_exist = False
            if (x,y) == point: continue
            for values in classified.itervalues():
                if (x,y) in values: 
                    is_exist = True
                    break

            if not is_exist and (x,y) in points:
                classified[index].append((x,y))
                recursion((x,y), points, classified, index)

def connected_domain(points):
    classified = {}
    index = 0
    for point in points:
        is_exist = False
        for values in classified.itervalues():
            if point in values: 
                is_exist = True
                break
        if is_exist: continue

        # print "index: %d" % index
        # print 
        classified[index] = [point]
        recursion(point, points, classified, index)
        index += 1
    return classified

if __name__ == "__main__":
    points = []
    points.append((4,3))
    points.append((1,0))
    points.append((1,1))
    points.append((1,2))
    points.append((5,6))


    classified = connected_domain(points)
    for i in classified:
        print i, classified[i]
