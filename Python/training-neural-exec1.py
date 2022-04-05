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