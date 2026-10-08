\# Machine Learning Analysis and Forecasting of Electric Vehicle Adoption Trends



\## Overview



This project analyzes electric vehicle (EV) adoption trends using machine learning and forecasting techniques.



The analysis was developed as part of the \*\*Business Data Analysis (ADA) Master's Program\*\* at the \*\*University of Bucharest, Faculty of Business and Administration\*\*, during the 2025–2026 academic year.



The project combines exploratory data analysis, machine learning classification, feature importance analysis, and time-series forecasting to investigate patterns in electric vehicle adoption.



\## Dataset



The analysis uses the \*\*Electric Vehicle Population Data\*\* dataset provided through the Washington State Open Data API.



The dataset contains information including:



\* Model Year

\* Make

\* Electric Vehicle Type

\* Clean Alternative Fuel Vehicle (CAFV) Eligibility

\* Electric Range

\* County



The original analysis retrieves the dataset directly from the Washington State data API.



The dataset is not stored directly in this repository; the analysis can retrieve it from the source API.



\## Data Preparation



The data preparation process included:



\* selecting the relevant variables

\* removing missing values

\* removing duplicate records

\* encoding categorical variables using `LabelEncoder`

\* separating the predictors from the target variable

\* splitting the data into training and testing sets



The target variable used for classification was \*\*Electric Vehicle Type\*\*.



The dataset was divided into training and testing subsets using an 80/20 split with a fixed random state of 42.



\## Machine Learning Models



Three classification models were evaluated:



\* Random Forest

\* Logistic Regression

\* Decision Tree



Model performance was evaluated using accuracy, classification reports, and a confusion matrix.



\### Results



The reported classification accuracies were:



| Model               | Accuracy |

| ------------------- | -------: |

| Random Forest       |   0.9995 |

| Logistic Regression |    0.998 |

| Decision Tree       |    0.997 |



Random Forest achieved the highest reported accuracy among the three models.



\## Exploratory Analysis



The project also examines several aspects of the EV dataset, including:



\* EV distribution by model year

\* electric range distribution

\* the most represented EV brands

\* distribution of electric vehicle types

\* relationships between numerical variables

\* feature importance from the Random Forest model



The analysis found strong growth in the number of vehicles represented in newer model years and examined differences in electric range and representation across manufacturers.



\## Feature Importance



Feature importance was extracted from the Random Forest classifier to identify which variables contributed most to the model's predictions.



The resulting feature importance analysis is visualized in the project figures.



\## Forecasting



To examine future EV growth, the number of vehicles was aggregated by model year and analyzed using \*\*Prophet\*\*.



The forecasting model was used to project the trend forward by five future periods.



The project includes both the forecast results and visualizations comparing the observed trend with the forecasted trend.



\## Limitations



Several limitations were identified in the original analysis:



\* The dataset represents \*\*Washington State\*\*, rather than the entire United States.

\* Model year does not necessarily correspond exactly to the year of vehicle registration.

\* Longer-term forecasts are subject to greater uncertainty.

\* External factors such as economic conditions, government policies, incentives, and charging infrastructure were not incorporated into the forecasting model.



\## Technologies Used



\* Python

\* pandas

\* scikit-learn

\* matplotlib

\* seaborn

\* Prophet

\* Jupyter Notebook



\## Project Structure



```text

ev-adoption-ml-forecasting/

│

├── data/

├── notebooks/

├── src/

│   ├── data\_preprocessing.py

│   ├── classification.py

│   └── forecasting.py

├── figures/

├── results/

├── README.md

├── requirements.txt

└── .gitignore

```



\## Academic Context



\*\*University of Bucharest\*\*

Faculty of Business and Administration

Master's Program: Business Data Analysis (ADA)

Academic Year: 2025–2026



