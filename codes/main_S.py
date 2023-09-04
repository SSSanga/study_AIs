## conda install -c conda-forge fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# app.post('/api_v1/mlmodel')

import pickle

# app.post('/api_v1/mlmodelwithregression with dict params')
# method : post 
@app.post("/api_v1/mlmodelwithregression")
# with Machine Learning model(pkl로 만든 파일을 이용해서 진행)
def mlmodelwithregression(data:dict) : # ← {'texture_mean' :'16.34','perimeter_mean':87.21}
    print('data with dict{}'.format(data))
    # data dict to 변수 할당
    # texture_mean = float(input('texture_mean : ')) console에서 받을때 이렇게 이고 
    # perimeter_mean = float(input('perimeter_mean : '))
    
    texture_mean = data['texture_mean'] 
    perimeter_mean = data['perimeter_mean']
    #pkl 파일 존재 확인 코드 필요함
    # 소스 참고

    result_predict = 0;
    # 학습모델 불러와서 예측
    with open('datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file:
        loaded_model = pickle.load(regression_file)
        input_labels = [[texture_mean, perimeter_mean]] # 학습했던 설명변수 형식 맞게 적용
        result_predict = loaded_model.predict(input_labels)
        print('Predict radius_mean Result : {}'.format(result_predict))
        pass

    # 예측값 return
    result = {'radious_mean':result_predict[0]}

    return result

