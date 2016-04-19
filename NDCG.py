from math import log


actual = open('actual_cat.txt','r')

predictions = open('result_doc2vec.txt','r')

NDCG_array = []

for prediction in predictions:
    pred_array = prediction.split(',')
    num_prediction = len(pred_array)
    pred_array[num_prediction - 1] = pred_array[num_prediction-1].split('\n')[0]

    act_array = actual.readline().split(',')
    num_act = len(act_array)
    act_array[num_act-1] = act_array[num_act-1].split('\n')[0]

    count = 0
    DCG  = 0.0
    for pred in pred_array:
        count+=1
        if pred in act_array:
            gain = 1.0
        else:
            gain  = 0.0
        if count==1:
            DCG += gain
        else:
            DCG += gain/(log(count)/log(2))
    
    count2 = 0
    IDCG = 0.0
    for act_cat in act_array:
        count2+=1
        if count2==1:
            IDCG += 1.0
        else:
            IDCG += 1.0/(log(count)/log(2))

    NDCG = DCG/IDCG
    NDCG_array.append(NDCG)

cumulative = 0.0
for NDCG in NDCG_array:
    cumulative+= NDCG

net_NDCG = cumulative/len(NDCG_array)

print net_NDCG




