# pickle 이용하여 서비스 이용해보기
import pickle

fat_density= float(input('fat_density : '))
MFandES = float(input('MFandES : '))
disc_curvature = float(input ('disc_curvature : '))

with open('datasets/RecurrenceOfSurgery_regression_quest.pkl', 'rb') as ROS_pkl:
    loaded_model = pickle.load(ROS_pkl)
    input_labels = [[fat_density,MFandES,disc_curvature]]
    result_predict = loaded_model.predict(input_labels)
    print('Predicted Age: {}'.format(result_predict))
    pass
    