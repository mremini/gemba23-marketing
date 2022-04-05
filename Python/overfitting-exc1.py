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