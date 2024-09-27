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

4. **Model Analysis**: Implemented multiple machine learning models, starting with simple linear regression and increasing complexity in subsequent models.

## Results
The performance of various models was evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score. 

## Conclusion
This project illustrates the potential of machine learning in accurately predicting housing prices, highlighting the importance of data preprocessing and model selection for improved prediction accuracy.

## Technologies Used
- Python
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

