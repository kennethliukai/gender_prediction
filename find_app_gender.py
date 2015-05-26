"""Find the app gender"""
import sys
f = open(sys.argv[1])
app_gender_dict = {}
i = 0
for line in f:
    cur_line = line.strip().split('\t')
    gender = cur_line[1]
    app_id = cur_line[2]
    app_name = cur_line[3]
    if i%10000 ==0:
        print i/10000
    i += 1
    try:
        app_gender_dict[app_id]
    except Exception,e:
        if gender == '0':
            app_gender_dict[app_id] = [app_name,1,0]
        else:
            app_gender_dict[app_id] = [app_name,0,1]
    else:
        if gender == '0':
            app_gender_dict[app_id][1] += 1
        else:
            app_gender_dict[app_id][2] += 1
fwm = open('male_app_count','w')
fwf = open('female_app_count','w')
male_list = []
female_list = []
for (k,v) in app_gender_dict.items():
    male_count = v[1]
    female_count = v[2]
    fract = float(male_count)/(male_count+female_count)
    if male_count > 100 and female_count > 100:
        if fract >0.8:
            male_list.append([k,v[0],v[1],v[2],str('%.4f'%fract),'0'])
        elif fract <0.25:
            female_list.append([k,v[0],v[1],v[2],str('%.4f'%(1-fract)),'1'])
male_list.sort(key = lambda x:x[4],reverse = True)
female_list.sort(key = lambda x:x[4],reverse = True)
for line in male_list:
    fwm.write(line[0]+'\t'+line[1]+'\t'+str(line[2])+'\t'+str(line[3])+'\t'+line[4]+'\t'+line[5]+'\n')
for line in female_list:
    fwf.write(line[0]+'\t'+line[1]+'\t'+str(line[2])+'\t'+str(line[3])+'\t'+line[4]+'\t'+line[5]+'\n')
f.close()
fwm.close()
fwf.close()

