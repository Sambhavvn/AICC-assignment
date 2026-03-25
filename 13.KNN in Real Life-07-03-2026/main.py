import numpy as np
from sklearn.neighbors import KNeighborsRegressor

X = np.array([
    [5, 3],
    [4, 2],
    [1, 5]
])

y = np.array([2, 1, 4])

model = KNeighborsRegressor(n_neighbors=2)
model.fit(X, y)

new_user = np.array([[5, 2]])

pred = model.predict(new_user)

print("Predicted Drama Rating:", pred[0])