# 케라스 기본 사용법

1. 모델 객체 생성
2. 층 추가(입력, 은닉, 출력)
3. activation함수 추가
4. 모델 compile
5. 모델 학습(fit)
6. 점수 확인(evaluate)

```python
from keras.models import Sequential

model = Sequential() #시퀀스 모델 객체 생성
model.add(Dense(512, input_shape=(2, ))) # 입력층 추가
model.add(Activation('relu')) # 활성화 함수로 relu 사용
model.add(Dropout(0.1)) # dropout 추가
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax')) # 출력층 활성화 함수로 relu 사용
model.compile(loss="categorical_crossentropy",
              optimizer="rmsprop",
              metrics=['accuracy'])
hist = model.fit(
    X_train,
    Y_train,
    batch_size=100,
    epochs=20,
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1)
score = model.evaluate(X_test, Y_test)
print("loss=", score[0])
print("accuracy=", score[1])

'''
Train on 13500 samples, validate on 1500 samples
Epoch 1/20
13500/13500 [==============================] - 1s 79us/step - loss: 0.5228 - accuracy: 0.7881 - val_loss: 0.2854 - val_accuracy: 0.9093
Epoch 2/20
13500/13500 [==============================] - 1s 57us/step - loss: 0.2552 - accuracy: 0.8993 - val_loss: 0.1913 - val_accuracy: 0.9260
Epoch 3/20
13500/13500 [==============================] - 1s 58us/step - loss: 0.1948 - accuracy: 0.9164 - val_loss: 0.1436 - val_accuracy: 0.9407
Epoch 4/20
13500/13500 [==============================] - 1s 57us/step - loss: 0.1724 - accuracy: 0.9262 - val_loss: 0.1307 - val_accuracy: 0.9387
Epoch 5/20
13500/13500 [==============================] - 1s 58us/step - loss: 0.1513 - accuracy: 0.9360 - val_loss: 0.1020 - val_accuracy: 0.9627
Epoch 6/20
13500/13500 [==============================] - 1s 59us/step - loss: 0.1455 - accuracy: 0.9329 - val_loss: 0.1133 - val_accuracy: 0.9513
Epoch 7/20
13500/13500 [==============================] - 1s 58us/step - loss: 0.1395 - accuracy: 0.9390 - val_loss: 0.0789 - val_accuracy: 0.9733
Epoch 8/20
13500/13500 [==============================] - 1s 59us/step - loss: 0.1324 - accuracy: 0.9443 - val_loss: 0.0835 - val_accuracy: 0.9627
Epoch 9/20
13500/13500 [==============================] - 1s 58us/step - loss: 0.1281 - accuracy: 0.9417 - val_loss: 0.0635 - val_accuracy: 0.9893
Epoch 10/20
13500/13500 [==============================] - 1s 60us/step - loss: 0.1215 - accuracy: 0.9508 - val_loss: 0.0912 - val_accuracy: 0.9553
Epoch 11/20
13500/13500 [==============================] - 1s 58us/step - loss: 0.1141 - accuracy: 0.9533 - val_loss: 0.0964 - val_accuracy: 0.9493
4999/4999 [==============================] - 0s 31us/step
loss= 0.10233065565840486
accuracy= 0.947189450263977
'''
```

---

입력 데이터

```python
import

df = pd.read_csv(goal_path/'bmi.csv')
df["height"] /= 200
df["weight"] /= 100
X = df[["weight", "height"]].as_matrix()
bclass = {"thin": [1, 0, 0] , "normal":[0, 1, 0], "fat": [0, 0, 1]}
Y = np.empty((20000, 3))
for i, v in enumerate(df["label"]):
    Y[i] = bclass[v]
X_train, Y_train = X[1:15001], Y[1:15001]
X_test, Y_test = X[15001:20001], Y[15001:20001]
```

