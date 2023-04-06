import pandas as pd
import numpy as np


chat_id = 706100023 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
     speeds = x
     error_dist = lambda x: -49 + np.random.exponential(1)
     measurements = speeds + np.array([error_dist(x) for x in range(len(speeds))])
     variances = np.array([1/np.exp(1)**2, 1/np.exp(2)**2, 1/np.exp(3)**2])
     weights = 1/variances
     theta_hat = np.sum(weights * measurements) / np.sum(weights)
     return theta_hat 
