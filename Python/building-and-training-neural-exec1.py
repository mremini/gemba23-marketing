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