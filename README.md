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
def should_get_hired(interview_one_score, interview_two_score):
    if interview_one_score > 4 and interview_two_score > 4:
        action = 'hire'
    elif interview_one_score > 4 or interview_two_score > 4:
        action = 'interview again'
    else:
        action = 'nope'
        return action
```

[loaddata-exercise3.py](https://github.com/mremini/gemba23-marketing/blob/main/Python/loaddata-exercise2.py)

![loaddata-exc3](images/loaddata-exc3.png)


### 2 - Matlolib

### 3 - The numpy Module

### 4 - Principal Component Analysis

### 5 - Multi Dimension SCaling

### 6 - CLuster abalysis

### 7 - Linear Regression

### 8 - Logistic Regression

### 9 - Metrics: EValuating Model Accuracy

</details>


## Advanced level

<details>

### 1 - Neural Netwroks

### 2 - Building and Training Neural Networks

### 3 - Training Neural Networks

### 4 - Overfitting

### 5 - Applying Neural Networks to Business Problems

### 6 - Transfer Learning - Standing on the shoulders of Giants

</details>