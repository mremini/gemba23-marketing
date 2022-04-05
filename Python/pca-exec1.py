stock_pca = PCA()
stock_pca.fit(stock_df)
stock_n_important_components = 3
stock_important_components = stock_pca.components_[0:stock_n_important_components,:]
stock_final_components = varimax_rotation(stock_important_components)
stock_final_components_df = pd.DataFrame(stock_final_components, columns=stock_df.columns)
stock_final_components_df