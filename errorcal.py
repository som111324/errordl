import numpy as np

Y_predicted = np.array([1,1,0,0,1])
Y_true = np.array([0.30,0.7,0,0.5])

def mae(Y_true ,Y_predicted):
    total_error = 0 
    for yt ,yp in zip (Y_true ,Y_predicted):
        total_error += ( yt - yp )
        print ("total error :" ,total_error)
        mae = total_error / len(Y_true)
        print("MAE :" , mae)
        return mae 


mae(Y_true ,Y_predicted) 
