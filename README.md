# House Price Prediction Using ANN Model

This project employs machine learning algorithms to develop a housing price prediction model using data from the 1990 California census. The model aims to assist home sellers and real estate agents in making informed decisions by providing accurate home price estimates. The research highlights that linear regression consistently outperforms other models in predicting home prices.

## Introduction
Housing price prediction is vital for stakeholders like real estate investors, buyers, and urban planners. This study aims to develop machine learning models that reliably forecast home prices based on various dataset features.

## Methodology
1. **Data Source**: Utilized the California housing dataset from the 1990 census, available on [Kaggle](https://www.kaggle.com/datasets/camnugent/californiahousing-prices).
2. **Data Acquisition**: The dataset includes various features such as longitude, latitude, and median income.
3. **Data Preprocessing**:
   - **Handling Missing Values**: Filled missing values in "total_bedrooms" with the column mean.
   - **Cleaning Outliers**: Used the Interquartile Range (IQR) method for outlier detection.
   - **Splitting Dataset**: Divided data into 70% training and 30% testing.
   - **Feature Scaling**: Applied MinMaxScaler for normalization.

   Here is the dataset summary and structure after preprocessing:

   ![Dataset Summary](Assets/Images/Dataset%20Summary%20after%20preprocessing.JPG)

4. **Model Analysis**: Implemented multiple machine learning models, starting with simple linear regression and increasing complexity in subsequent models.

   We explored different machine learning techniques and hyperparameters in this study:
   
   - **Model 1**: A simple baseline model. We started simple and planned to increase complexity in subsequent models.
   
   - **Model 2**: Increased complexity to observe performance improvements and experimented with hyperparameter tuning.
   
   - **Model 3**: Continued complexity enhancements and hyperparameter changes.
   
   - **Model 4**: The final, most complex model, optimized for better performance.

## Results
The performance of various models was evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score. Based on these results, **Model 4** proved to be the most effective for predicting house prices, providing the most accurate predictions with the lowest error metrics and the highest R² score.

   ![Model Comparisons](Assets/Images/Models.JPG)

In **Graph 4**, we can see that **Model 4**'s residuals are more centered around zero compared to other models, indicating better predictions.

   ![Model Residuals](Assets/Images/The%20Models%20Reduals.JPG)

## Conclusion
This project illustrates the potential of machine learning in accurately predicting housing prices, highlighting the importance of data preprocessing and model selection for improving prediction accuracy.

## Technologies Used
- Python
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
