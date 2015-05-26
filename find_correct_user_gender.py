
def match():
    f = open('/home/kai/rui_zhang/code/weighted_filtered.csv')
    #column 0:user ID, column 1:gender, column 2:APP ID, column 3: APP name, column 4:weight
    user_dict = {}
    for line in f:
        cur_line = line.strip().split(',')
        user_id = cur_line[0]
        gender = cur_line[1]
        weight = float(cur_line[4])
        try:
            user_dict[user_id]
        except Exception,e:
            user_dict[user_id] = [gender,weight]
        else:
            user_dict[user_id][0] = gender
            user_dict[user_id][1] += weight
    fw = open('final_user_gender','w')
    for (k,v) in user_dict.items():
        if (v[0] == '1' and v[1] >1.0) or (v[0] == '0' and v[1] <-1.0):
            fw.write(k+'\t'+v[0]+'\t'+str('%.4f'%v[1])+'\n')

    f.close()
    fw.close()

if __name__ == '__main__':
    match()
