
#list[[x, y, type]]


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
def seperate(r_list, max_clusters):
    while len(r_list)>max_clusters:
        min_dis = distance(r_list[0], r_list[1])
        indexs = [0, 1]
        for i in range(len(r_list)):
            for j in range(i + 1, len(r_list)):
                dis = distance(r_list[i], r_list[j])
                if dis < min_dis:
                    indexs = [i, j]

        r_list.remove(r_list[indexs[1]])



def r_to_M(rockets):
    r_sep = []
    for RT in range(4):
        new_r = []
        for i in range(len(rockets)):
            if rockets[i][2] == RT:
                new_r.add([rockets[i][0], rockets[i][1]])

    ret_lst = []
