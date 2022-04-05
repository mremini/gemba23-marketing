def shaped_range(start, end, n_rows, n_cols):
        range_arr = np.arange(start, end, 1)
        reshaped_arr = range_arr.reshape(n_rows, n_cols)
        return reshaped_arr