X_test_processed = images_to_rgb_and_resized(X_test, (96,96))
evaluation_result = model_combined.evaluate(
    X_test_processed,
    keras.utils.to_categorical(y_test)
)
print(evaluation_result)