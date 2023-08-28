import pickle
# 설명변수: 'texture_worst','smoothness_worst','concavity_worst'
texture = float(input('texture_worst: '))
smoothness = float(input('smoothness_worst: '))
concavity = float(input('concavity_worst: '))

with open ('datasets/BreastCancerWisconsin_Logistic_quest.pkl', 'rb') as logistic :
    loaded_model = pickle.load(logistic)
    input_features = [[texture, smoothness, concavity]]
    result_predict = loaded_model.predict(input_features)
    print ('Predicted diagnosis : {}'.format(result_predict))
    pass