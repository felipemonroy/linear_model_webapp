"""
App
"""

import numpy as np

from src.metrics import LinearModelMetrics
from src.models import LinearRegressionExpanded
from src.statistics import ShapiroWilkTest

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])

y = np.random.rand(4)

reg = LinearRegressionExpanded()
reg.fit(X, y)

metrics = LinearModelMetrics(reg, X, y)

swt = ShapiroWilkTest(reg.resid(X, y))

print(metrics.r_2)

print(swt.p_value)
