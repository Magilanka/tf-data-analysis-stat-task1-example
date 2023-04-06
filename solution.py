import pandas as pd
import numpy as np


chat_id = 706100023 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
     from scipy.stats import norm
     error_dist = lambda n: -49 + np.exp(1)
     v_true = np.random.uniform(0, 50, n) # истинные значения скоростей
     v_error = error_dist(n) # случайная ошибка измерения скорости
     v_observed = v_true + v_error # наблюдаемые значения скоростей
     v_mean = np.mean(v_observed) # Вычисляем среднюю скорость
     a_hat = (v_mean) / 10 # Вычисляем оценку коэффициента ускорения
#      n = len(x)
#      a = v / t
#     t_value = t.ppf(0.975, n-1)
#     error = -49 + np.exp(1)
#     ci_lower = a - t_value * error / np.sqrt(n)
#     ci_upper = a + t_value * error / np.sqrt(n)
    # Измените код этой функции sss
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
# np.sqrt(n) - корень
# var(x) - дисперсия
    return a_hat # Ваш ответ
