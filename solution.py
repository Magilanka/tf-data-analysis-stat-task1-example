import pandas as pd
import numpy as np


chat_id = 706100023 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    speeds = x
    num = len(x)
    error_dist = lambda x: -49 + np.random.exponential(1)
    measurements =[]
    for i in range(num):
      measurements = speeds + np.array([error_dist(x) for x in range(num)])
    variances = []
    for i in range(num):
      variances.append(1/np.exp(i)**2)
    weights = 1/np.asarray(variances)
    theta_hat = np.sum(weights * measurements) / np.sum(weights)
    return theta_hat
