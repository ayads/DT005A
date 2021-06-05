# Predictive Maintenance in Smart Agriculture Using Machine Learning: A Novel Algorithm for Drift Fault Detection in Hydroponic Sensors

## Abstract
The success of Internet of Things solutions allowed the establishment of new applications such as smart hydroponic agriculture. One typical problem in such an application is the rapid degradation of the deployed sensors. Traditionally, this problem is resolved by frequent manual maintenance which considered to be ineffective and may harm the crops in the long run. The main purpose of this thesis was to propose a machine learning approach for automating the detection of sensor fault drifts. In addition, the solution’s operability was investigated in a cloud computing environment in terms of the response time. This thesis proposes a detection algorithm that utilizes RNN in predicting sensor drifts from time-series data streams. The detection algorithm was later named; Predictive Sliding Detection Window (PSDW) and consisted of forecasting and classification models. Three different RNN algorithms, i.e., LSTM, CNN-LSTM, and GRU, were designed to predict sensor drifts using forecasting and classification techniques. The algorithms were compared against each other in terms of relevant accuracy metrics for forecasting and classification. The operability of the solution was investigated by developing a web server that hosted the PSDW algorithm on an AWS computing instance. The resulting forecasting and classification algorithms were able to make reasonably accurate predictions for this particular scenario. More specifically, the forecasting algorithms acquired relatively low RMSE values as ~0.6, while the classification algorithms obtained an average F1-score and accuracy of ~80% but with a high standard deviation. However, the response time was ~5700% slower during the simulation of the HTTP requests. The obtained results suggest the need for future investigations to improve the accuracy of the models and experiment with other computing paradigms for more reliable deployments.

**Keywords:** : Smart Hydroponic Agriculture, Predictive Maintenance, IoT, Machine Learning, RNN, Forecasting, Classification, LSTM, CNN-LSTM, GRU, Sensor Drift Fault


## Predictive Sliding Detection Window
![Detection Window Flowchart](https://user-images.githubusercontent.com/33630740/120888837-d6bae300-c5fa-11eb-8e13-88bc5caf1731.png)
![Predective Sliding Detection Window in action](https://user-images.githubusercontent.com/33630740/120888930-2d282180-c5fb-11eb-9eb3-710a96a13fea.png)

## Results
### Forecasting
![forecast_lstm_result](https://user-images.githubusercontent.com/33630740/120888976-5cd72980-c5fb-11eb-9877-66a78fa7b68c.png)

![forecast_cnn_lstm_result](https://user-images.githubusercontent.com/33630740/120888965-5052d100-c5fb-11eb-9d31-f1c1162700a5.png)

![forecast_gru_result](https://user-images.githubusercontent.com/33630740/120888969-5779df00-c5fb-11eb-9319-029809dfb7de.png)

### Classification
![classification_result](https://user-images.githubusercontent.com/33630740/120888987-652f6480-c5fb-11eb-843d-09e7bd82a25d.png)

### Response Time
Response time with PSDW
![Response Time With PSDW](https://user-images.githubusercontent.com/33630740/120888993-695b8200-c5fb-11eb-91b2-78f2228bfe35.png)

Response time without PSDW
![Response Time Without PSDW](https://user-images.githubusercontent.com/33630740/120888994-69f41880-c5fb-11eb-8ce2-9eb062975500.png)
