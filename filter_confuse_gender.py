f = open('../imei_combine_filtered_gender_prune.uniq')
imei_gender_dict = {}
for line in f:
    cur_line = line.strip().split('\t')
    try:
        gender = imei_gender_dict[cur_line[0]]
    except Exception,e:
        imei_gender_dict[cur_line[0]] = cur_line[1]
    else:
        if gender != cur_line[1]:
            del imei_gender_dict[cur_line[0]]
fw = open('imei_gender_combine_no_confuse','w')
for (k,v) in imei_gender_dict.items():
    fw.write(k+'\t'+v+'\n')
f.close()
fw.close()
