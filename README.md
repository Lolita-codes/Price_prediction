# House Price Prediction Project Report
Analysis of the Boston house price data and building a model that can provide a price estimate based on some home's characteristics. 

## Project Objective
The primary goal of this research project is to gain a comprehensive understanding of the trends and factors contributing to house pricing in Boston. Additionally, the project aims to build a predictive model that can estimate house prices based on various property characteristics. The project focuses on thirteen key characteristics:
1. CRIM: Per capita crime rate by town
2. ZN: Proportion of residential land zoned for large lots
3. INDUS: Proportion of non-retail business acres per town
4. CHAS: Charles River dummy variable (1 if tract bounds river, 0 otherwise)
5. NOX: Nitric oxides concentration (parts per 10 million)
6. RM: Average number of rooms per dwelling
7. AGE: Proportion of owner-occupied units built before 1940
8. DIS: Weighted distances to Boston employment centers
9. RAD: Accessibility to radial highways
10. TAX: Property tax rate
11. PTRATIO: Pupil-teacher ratio by town
12. B: Proportion of Black residents
13. LSTAT: Percentage of lower-income population
14. PRICE: Median value of owner-occupied homes in $1000's

## Methods Used
The analysis encompasses the following methods:
- Preliminary Data Exploration
- Descriptive Statistics
- Data Cleaning
- Data Visualization
- Multivariable Regression
- Model Refinement

## Technologies Utilized
The project relies on several programming and data analysis tools:
- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Plotly
- Scikit-Learn

## Project Description

### Visualizing Features
The project started with an exploration of the features. Data visualization techniques, including Seaborn's displot, Matplotlib's histogram, and Plotly's bar chart, were used to analyze the following:
- PRICE: The average home price is approximately $22,532.8, with most prices below $30,000 and a spike at $50,000.
- RM: The average number of rooms per dwelling is around 6.
- DIS: The average weighted distance to Boston employment centers is approximately 3.8 miles, with a majority of houses within 5 miles.
- RAD: The index of accessibility to highways indicates a lot of houses have better access to roads.
- CHAS: Most homes (471 out of 506) are located near the Charles River.

### Understanding Relationships in the Data
Detailed relationships were explored using Seaborn's jointplot. The analysis revealed insights, including:
- Pollution and Distance from Employment: Pollution levels decrease with greater distances from employment centers. Also, different pollution levels can be observed within 2miles to employment centres and the level of pollution is constant at 9 to 12miles to employment centres.  
- Pollution and Proportion of Non-Retail Industry: Higher industry proportions correspond to higher pollution levels.
- Average Number of Rooms and % of Lower-Income Population: More rooms are associated with lower % of lower-income population.
- Price of Homes and % of Lower-Income Population: Home prices tend to rise as the % of lower-income population decreases. Also, the homes at $50,000 mark lined up at the top of the chart suggesting an imposed maximum value during data collection.  
- Price of Homes and Number of Rooms: Higher prices are observed in homes with more rooms.

### Split Training and Test Dataset
Data was split into training and test datasets (80/20 split) using Scikit-Learn's `train_test_split`. This division helps evaluate the model's performance on unseen data.

### Multivariable Regression
A multivariable regression model was implemented using Scikit-Learn. The model equation is:

\[ PRICE = θ0 + θ1CRIM + θ2ZN + θ3INDUS + θ4CHAS + θ5NOX + θ6RM + θ7AGE + θ8DIS + θ9RAD + θ10TAX + θ11PTRATIO + θ12B + θ13LSTAT \]

The model was evaluated, resulting in an R-squared value of 0.75, indicating a good data fit. The coefficients of the model was then evaluated to understand the strength and direction of the relationship between the features and the target. The estimated values and regression residuals were also analyzed and visualised suggesting a need for model improvement.

### Model Refinement
To enhance model performance, data transformation was applied. The logarithm of house prices (Log prices) was used as the target variable. The model equation becomes:

\[ log(PRI^CE) = θ0 + θ1CRIM + θ2ZN + θ3INDUS + θ4CHAS + θ5NOX + θ6RM + θ7AGE + θ8DIS + θ9RAD + θ10TAX + θ11PTRATIO + θ12B + θ13LSTAT \]

This revised model showed an improved R-squared value of 0.79, indicating a better fit.

### Evaluation and Analysis
The residuals of the model were analyzed. Residuals are the differences between model predictions and true values. Two scatter plots are created:
1. Actual vs. Predicted Prices, revealing the model's predictive accuracy.
2. Residuals vs. Predicted Prices, providing insights into residual distribution.

The mean and skewness of residuals were calculated (mean=0, skewness=0.09).

### Final Model
The preferred model utilizes Log prices. The R-squared values for the Normal and Log test datasets are 0.67 and 0.74, respectively. The final model equation is:

\[ log(PRI^CE) = θ0 + θ1CRIM + θ2ZN + θ3INDUS + θ4CHAS + θ5NOX + θ6RM + θ7AGE + θ8DIS + θ9RAD + θ10TAX + θ11PTRATIO + θ12B + θ13LSTAT \]

In this model, the average property has the mean value for all its characteristics.

## Conclusion
This project has successfully explored the Boston house price dataset, built a regression model to predict house prices, and refined the model using data transformation. The final model provides valuable insights into house pricing based on property characteristics.
