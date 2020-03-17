# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# print(len(action))
# print(set(action))
# from collections import Counter
# l = [1, 1, 2, 3, 3]
# cl = Counter(action)
# for k, v in cl.items():
#     if v > 1:
#         print("{}, 重复{}次".format(k, v))
# action_type=['左转','右转','加速','减速','颠簸开始','颠簸结束','发动机停止','发动机开启','土岭','车撤桥','下坡', '上坡']
def read_data_train():
    new = pd.read_csv('out-19-12-26_000013-utf8.csv',encoding='utf-8',header=None,sep=',')
    new_28 = pd.read_csv('out-19-12-28_000013-utf8.csv',encoding='utf-8',header=None,sep=',')
    #print(len(new),len(new_27),len(new_28))
    feature_0=[]
    feature_1=[]
    feature_2=[]
    feature_3=[]
    feature_4=[]
    feature_5=[]
    feature_6=[]
    feature_7=[]
    feature_8=[]
    feature_9=[]
    feature_10=[]
    feature_11=[]
    feature_12=[]
    feature_13=[]
    feature_14=[]
    feature_15=[]
    action=[]
    for i in new[1]:
        action.append(i)


    for i in new_28[1]:
        action.append(i)

    from collections import Counter
    '''
    cl = Counter(action)
    for k, v in cl.items():
        if v > 0:
            print("{}, {}次".format(k, v))
    '''
    fs= []
    for i in new[4]:
        features = i.split('\n')
        #print(len(features))
        f = [[] for i in range(17)]
        for feature in features:
            if feature=='':
                continue
            feature=feature.split(',')
            for index,sub_f in enumerate(feature):
                f[index].append(np.float(sub_f.split(':')[1]))
        f = np.array(f)
        fs.append(f)
    for i in new_28[4]:
        features = i.split('\n')
        #print(len(features))
        f = [[] for i in range(17)]
        for feature in features:
            if feature=='':
                continue
            feature=feature.split(',')
            for index,sub_f in enumerate(feature):
                f[index].append(np.float(sub_f.split(':')[1]))
        f = np.array(f)
        fs.append(f)

    max_len = max(len(l[0]) for l in fs)
    new_fs_train = []
    for x in fs:
        x = list(x)
        new_f =list(map(lambda l:list(l)+[0]*(max_len-len(l)),x))
        # for l in x:
        #     l+[0]*(max_len-len(l))
        new_f = np.array(new_f)
        new_fs_train .append(new_f)
    for feature in fs:
            feature_0.append(feature[1])
            feature_1.append(feature[2])
            feature_2.append(feature[3])
            feature_3.append(feature[4])
            feature_4.append(feature[5])
            feature_5.append(feature[6])
            feature_6.append(feature[7])
            feature_7.append(feature[8])
            feature_8.append(feature[9])
            feature_9.append(feature[10])
            feature_10.append(feature[11])
            feature_11.append(feature[12])
            feature_12.append(feature[13])
            feature_13.append(feature[14])
            feature_14.append(feature[15])
            feature_15.append(feature[16])

    lengths = []
    for feature in feature_0:
        lengths.append(len(feature))
    data_dict = {'action':action,
                 'f0':feature_0,
                 'f1':feature_1,
                 'f2':feature_2,
                 'f3':feature_3,
                 'f4':feature_4,
                 'f5':feature_5,
                 'f6':feature_6,
                 'f7':feature_7,
                 'f8':feature_8,
                 'f9':feature_9,
                 'f10':feature_10,
                 'f11':feature_11,
                 'f12':feature_12,
                 'f13':feature_13,
                 'f14':feature_14,
                 'f15':feature_15}
    data_df = pd.DataFrame(data_dict)
    #
    # print(data_df)
    # data_df.to_csv('data.csv',index_label='ID')
    return data_df
