results = open('result.txt','r')

map_list = []

actual_category = open('actual_cat.txt','r')

for result in results:
    categ_set = result
    act_cat = actual_category.readline().split('\n')[0]
    act_cat = act_cat.split(',')
    predictions =  categ_set.split(',')
    predictions[len(predictions)-1] = predictions[len(predictions)-1].split('\n')[0]
    count = 0
    map_val = 0.0
    number_of_relevant = 0
    #print predictions, act_cat
    if "other" in act_cat:
        continue
    for prediction in predictions:
        #if number_of_relevant>=len(act_cat):
        #    break
        if number_of_relevant>=1:
            break
        if prediction in act_cat:
            number_of_relevant+=1
            count+=1
            map_val += float(number_of_relevant)/float(count)
        #elif prediction=="other":
        #    number_of_relevant+=1
        #    count+=1
        #    map_val += float(number_of_relevant)/float(count)
        #elif "other" in act_cat:
        #    number_of_relevant+=1
        #    count+=1
        #    map_val += float(number_of_relevant)/float(count)
        else:
            count+=1
    try:
        map_list.append(map_val/number_of_relevant)
    except:
        map_list.append(0.0)


#print map_list


count_docs = 0
total_map  = 0.0
count_finite=0

for values in map_list:
    if values>0.0:
        count_finite+=1
    count_docs+=1
    total_map+=values



map_score = total_map/count_docs

print "Map_Score= " + str(map_score)
print "Count_docs= " + str(count_docs)
print "Count_finite= " + str(count_finite)
