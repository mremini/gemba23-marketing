# gemba23-marketing
GEMBA 23 Marketing Python Solutions

## Basic level

<details>

### 5 - Creating your own function
![function_exc1_2](images/function-exc1-2.png)
![function_exc4](images/function-exc4.png)
![function_exc5](images/function-exc5.png)
![function_exc6](images/function-exc6.png)



### 6 - Lists

![lists_exc1](images/lists-exc1.png)

![lists_exc2](images/lists-exc2.png)

![lists_exc3](images/lists-exc3.png)

### 7 - Loops
[loops-exercise1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/loops-exercise1.py)

```
def length_of_longest_word(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

```

[loops-exercise2.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/loops-exercise2.py)

```
def sum_leq(num):
	somme=0
	for in in range(1,num+1)
		somme=somme+in
	return somme

s= sum_leq(100)
s

```


### 8 - FunctionsII Advanced Topics

### 9 - Boolean Logic


[bool-exercise1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/bool-exercise1.py)

![bool-exercise1.py](images/bool-exc1.png)

```
def get_loyalty_program(customer_spending_usd):
    status = "no status"
    if customer_spending_usd > 20000 and customer_spending_usd < 50000:
        status="gold"
    elif customer_spending_usd > 50000:
        status="platinum"
    else:
        status = "no status"
    return status
```

[bool-exercise2.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/bool-exercise2.py)

![bool-exercise2.py](images/bool-exc2.png)

```
def should_get_hired(interview_one_score, interview_two_score):
    if interview_one_score > 4 and interview_two_score > 4:
        action = 'hire'
    elif interview_one_score > 4 or interview_two_score > 4:
        action = 'interview again'
    else:
        action = 'nope'
        return action
```

</details>

## Intermediate level

<details>

### 1 - Loading Data into Python


![loaddata-exc1](images/loaddata-exc1.png)

[loaddata-exercise2.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/loaddata-exercise2.py)

![loaddata-exc2](images/loaddata-exc2.png)

```
sales_q2=df.get('Sales Q2 2019 (USD)')
sales_q2

```

[loaddata-exercise3.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/loaddata-exercise3.py)

![loaddata-exc3](images/loaddata-exc3.png)
```
df['sales_q1_in_thousands'] = df["Sales Q1 2019 (USD)"] / 1000
df.head()

```


### 2 - Matlolib
![Visualizingdata-exec1](images/Visualizingdata-exec1.png)
[visualisedata-exercise1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/visualisedata-exercise1.py)

```
annual_income_usd = [100000, 130000, 40000, 50000, 120000, 48000, 50000,78000, 150000]
age_yrs = [60, 24, 32, 36, 28, 36, 32, 60, 68]
plt.scatter(age_yrs, annual_income_usd, marker="p", c="g")
plt.xlabel("Age (yrs)")
plt.ylabel("Annual Income (USD)")
plt.title("Annual Income vs. Age")

```

[visualisedata-exercise2.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/visualisedata-exercise2.py)

```
churn_df = pd.read_csv("data/employee-churn.csv")
plt.scatter(churn_df['gpa'], churn_df['aptitude.score'], marker="*")
plt.show()
```

### 3 - The numpy Module
![numpy-exc1.png](images/numpy-exc1.png)
[numpy-exercise1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/numpy-exercise1.py)

```
def count_zeros(my_array):
    nbr_zero=0
    for row in my_array:
        for cell in row:
            if cell==0:
               nbr_zero=nbr_zero+1
    return nbr_zero
```

![numpy-exc2.png](images/numpy-exc2.png)
[numpy-exercise2.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/numpy-exercise2.py)

```
def shaped_range(start, end, n_rows, n_cols):
        range_arr = np.arange(start, end, 1)
        reshaped_arr = range_arr.reshape(n_rows, n_cols)
        return reshaped_arr
```

### 4 - Principal Component Analysis
![pca-exc1.png](images/pca-exc1.png)
[pca-exec1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/pca-exec1.py)

```
stock_pca = PCA()
stock_pca.fit(stock_df)
stock_n_important_components = 3
stock_important_components = stock_pca.components_[0:stock_n_important_components,:]
stock_final_components = varimax_rotation(stock_important_components)
stock_final_components_df = pd.DataFrame(stock_final_components, columns=stock_df.columns)
stock_final_components_df
```

### 5 - Multi Dimension SCaling
![mds-exc1.png](images/mds-exc1.png)
[MDS-exec1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/MDS-exec1.py)

```
cookies_models = [
    'Prince',
    'Oreo',
    'Choco Bueno',
    'Petit Ecolier',
    'Mikado',
    'Granola',
    'Kinder',
    'Sables'
]
my_dissimilarity_matrix = np.array([
    [0, 5, 8, 4, 5, 3, 8, 5],
    [5, 0, 1, 5, 4, 7, 8, 3],
    [8, 1, 0, 4, 4, 3, 3, 4],
    [4, 5, 4, 0, 2, 5, 9, 8],
    [5, 4, 4, 2, 0, 5, 3, 7],
    [3, 7, 3, 5, 5, 0, 1, 9],
    [8, 8, 3, 9, 3, 1, 0, 8],
    [5, 3, 4, 8, 7, 9, 8, 0]
])
mds = MDS(dissimilarity="precomputed",random_state=63)
my_perceptual_map = mds.fit_transform(my_dissimilarity_matrix)
x = my_perceptual_map[:,0]
y = my_perceptual_map[:,1]
plt.scatter(x, y)
for i in range(0, len(cookies_models)):
    txt = cookies_models[i]
    plt.annotate(txt, [x[i], y[i]])
plt.show()
```

### 6 - Cluster analysis
![clusteranalysis-exc1.png](images/clusteranalysis-exc1.png)
[clusteranalysis-exec1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/clusteranalysis-exec1.py)

```
import numpy as np
inertia_values = []
all_k = np.arange(1,7)
for k in all_k:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(points_scaled)
    inertia_values.append(kmeans.inertia_)
plt.plot(all_k, inertia_values)
plt.show()
optimal_k = 4
```

![clusteranalysis-exc2.png](images/clusteranalysis-exc2.png)
[clusteranalysis-exec2.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/clusteranalysis-exec2.py)

```
optimal_clusters = KMeans(n_clusters=4, random_state=0)
labels = optimal_clusters.fit_predict(points_scaled)
plot_clusters(points_scaled, labels, optimal_clusters.cluster_centers_)
```

### 7 - Linear Regression
![linearregression-exc1.png](images/linearregression-exc1.png)
[linearregression-exec1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/linearregression-exec1.py)

```
my_linear_model = None
my_linear_model = linear_model.LinearRegression()
my_linear_model.fit(customer_annual_income_usd, avg_monthly_spending_usd)
predicted_values = my_linear_model.predict(customer_annual_income_usd)
plt.scatter(customer_annual_income_usd, avg_monthly_spending_usd, color="b")
plt.plot(customer_annual_income_usd, predicted_values, color="r")
plt.show()
r_squared = my_linear_model.score(customer_annual_income_usd, avg_monthly_spending_usd)
```

### 8 - Logistic Regression

![logisticregression-exc1.png](images/logisticregression-exc1.png)
[logisticregression-exec1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/logisticregression-exec1.py)

```
df = pd.read_csv("data/credit_card_exercise.csv")
logistic = LogisticRegression(solver='liblinear', random_state=0)
x = np.array(df['Months in Good Standing'])
newx = x[:,np.newaxis]
y = np.array(df['Defaulted? (0/1 = no/yes)'])
logistic.fit(newx, y)
predicted_probs = logistic.predict_proba(months_in_good_standing.reshape(-1,1))
plt.scatter(months_in_good_standing, probabilities_by_months, label="actual")
plt.scatter(months_in_good_standing, predicted_probs[:,1], label="predicted")
plt.legend()
plt.show()
```

### 9 - Metrics: EValuating Model Accuracy
![evaulatingmodelAccuracy-exc1.png](images/evaulatingmodelAccuracy-exc1.png)
[evalmodelAccuracy-exec1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/evalmodelAccuracy-exec1.py)

```
df = pd.read_csv("data/credit_card_exercise.csv")
logistic = LogisticRegression(solver='liblinear', random_state=0)
X = df.values[:, 0].reshape(-1,1)
y = df.values[:, 1]
logistic.fit(X, y)
predicted_probs = logistic.predict_proba(X)
fps, tps, thresh = roc_curve(y, predicted_probs[:,1])
auc = metrics.auc(fps, tps)
print(auc)
plt.plot(fps,tps)
plt.show()
```

</details>


## Advanced level

<details>


### 2 - Building and Training Neural Networks
![building-and-training-neural-exec1.png](images/building-and-training-neural-exec1.png)
[building-and-training-neural-exec1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/building-and-training-neural-exec1.py)

```
my_model = keras.Sequential([
    keras.layers.Dense(
        units=5,
        name="hidden-layer-one",
        activation="tanh",
        input_shape=(2,)
    ),
    keras.layers.Dense(
        units=3,
        name="output-layer-one",
        activation="softmax"
    )
])
```

### 3 - Training Neural Networks
![training-neural-networks.png](images/training-neural-networks.png)
[training-neural-exec1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/training-neural-exec1.py)

```
remove_randomness()
my_model = new_example_model()
my_optimizer = keras.optimizers.Adam(learning_rate=0.02)
my_model.compile(
    optimizer=my_optimizer,
    loss="mean_absolute_error"
)
my_model_tracker = Tracker("my-model")
my_model.fit(x,y, epochs=25, callbacks=[my_model_tracker.get_callback()])
my_model_tracker.visualize_progress(m_true = m, b_true = b)
```

### 4 - Overfitting
![overfitting.png](images/overfitting.png)
[overfitting-exc1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/overfitting-exc1.py)

```
remove_randomness()
my_model = keras.Sequential(
    [
        keras.layers.Dense(
            units=1,
			name="output",
            kernel_initializer=keras.initializers.constant(2)
        )
    ]
)
my_model.compile(
    optimizer=keras.optimizers.Adam(lr=0.01),
    loss="mean_squared_error"
)
my_model.fit(x_demo_train, y_demo_train, epochs=50)
y_pred_my_model = my_model.predict(x_demo_test)
plt.scatter(x_demo_test, y_demo_test)
plt.plot(x_demo_test, y_pred_my_model)
plt.show()
```


### 5 - Applying Neural Networks to Business Problems
![applyingneaural-tobusiness.png](images/applyingneaural-tobusiness.png)
[applyingneural-to-business-exc1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/applyingneural-to-business-exc1.py)

```
remove_randomness()
model_larger = keras.Sequential([
    keras.layers.Dense(
        units=100,
        input_shape=(X_train.shape[1],),
        activation="relu",
        name="hidden"
    ),
    keras.layers.Dense(
        units=2,
        activation="softmax",
        name="output"
    )
])
model_larger.compile(
    loss="categorical_crossentropy",
    optimizer="sgd",
    metrics=["accuracy"]
)
model_larger.fit(
    X_train_scaled,
    keras.utils.to_categorical(y_train),
    epochs=7
)
evaluation_result = model_larger.evaluate(
    X_test_scaled,
    keras.utils.to_categorical(y_test),
)
print(evaluation_result)
```

### 6 - Transfer Learning - Standing on the shoulders of Giants
![standing-shoulder-giant.png](images/standing-shoulder-giant.png)
[standing-on-theshouldersofGiant-exc1.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/standing-on-theshouldersofGiant-exc1.py)

```
X_test_processed = images_to_rgb_and_resized(X_test, (96,96))
evaluation_result = model_combined.evaluate(
    X_test_processed,
    keras.utils.to_categorical(y_test)
)
print(evaluation_result)
```

</details>