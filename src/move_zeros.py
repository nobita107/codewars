def move_zeros(array):
    zero_count = 0
    ret = []
    for x in array:
        # print(x)
        if isinstance(x,int) or isinstance(x,float):
            if x == 0:
                zero_count +=1
            else:
                ret.append(x)
        else:
            ret.append(x)
    ret.extend([0]*zero_count)
    return ret

print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(isinstance(False,bool))