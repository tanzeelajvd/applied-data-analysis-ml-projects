# Used Car Market in India

<p style="font-size: 15px; color: black; font-family: TimesNewRoman">
The Indian market for used cars is experiencing significant demand, surpassing that of new cars. As new car sales have slowed down, the pre-owned car market has continued to grow, reaching a larger scale than the new car market. In this scenario, Cars4U, a promising tech start-up, aims to capitalize on opportunities within the used car market.
In the 2018-19 period, while new car sales amounted to 3.6 million units, approximately 4 million second-hand cars were bought and sold. The decline in new car sales suggests a shifting demand towards the pre-owned market. In fact, some car owners are now replacing their old cars with pre-owned ones rather than purchasing brand new vehicles. Unlike new cars, which have relatively predictable pricing and supply managed by Original Equipment Manufacturers (OEMs), used cars present a different challenge with considerable uncertainty in both pricing and supply. Therefore, establishing an effective pricing scheme for used cars becomes crucial for market growth. The aim is to develop a pricing model that accurately predicts the prices of used cars and enables the business to devise profitable strategies through differential pricing.</p>

# Dataset Description

This data set contains information about used cars for sale in India. The data set includes the following features:

- `Name` : The brand and model of the car.
- `Location` : The location in which the car is being sold or is available for purchase.
- `Year`: The year or edition of the model.
- `Kilometers_Driven` : The total kilometers driven in the car by the previous owner(s) in KM.
- `Fuel_Type` : The type of fuel used by the car.
- `Transmission` : The type of transmission used by the car.
- `Owner_Type` : Whether the ownership is Firsthand, Second hand or other.
- `Mileage` : The standard mileage offered by the car company in kmpl or km/kg.
- `Engine` : The displacement volume of the engine in cc.
- `Power` : The maximum power of the engine in bhp.
- `Seats` : The number of seats in the car.
- `New_Price` : Price of new model.

**Predicting Attribute**
- `Price` : The price of the used car in INR Lakhs.

$$Lakh = \frac{Million}{10}$$

$$Crore (Cr) = 100 * Lakh$$ 

or

$$Crore (Cr) = 10 * Million$$ 


This data set can be used to analyze the pricing trends of used cars in India based on various factors such as location, year, kilometers driven, and other features. Additionally, this data set can be used to build predictive models to estimate the price of used cars based on their characteristics.


**For more details check:** https://www.kaggle.com/datasets/sukhmanibedi/cars4u

## Description of the Problem

During this analysis task, we aim to gain valuable insights into the dataset of used cars in the Indian market by addressing the following questions. Consider the following potential inquiries:

1. Which are the top 10 features that have the highest impact on the price of used cars in India?
2. How does the engine size (Engine) affect the price of used cars in India?
3. What is the importance of mileage (Mileage) in determining the price of used cars in India?
4. Does the type of transmission (Transmission_Manual, Transmission_Automatic) significantly influence the price of used cars in India?
5. How does the power of the car (Power) contribute to its price in the used car market in India?
6. Is the number of kilometers driven (Kilometers_Driven) a significant factor in determining the price of used cars in India?
7. What is the impact of the fuel type (Fuel_Type_Petrol) on the price of used cars in India?
8. Does the age of the car (Car_Age) affect its price in the used car market in India?
9. How does the brand (Brand_Maruti) influence the price of used cars in India?
10. Are there any other specific features that significantly contribute to the price of used cars in India, according to the feature importance analysis?

These questions will help us gain insights into the factors affecting the prices of used cars in India and understand the relative importance of different features in the regression model.

---
## Analysis Workflow

The notebook follows a structured exploratory workflow:

1. **Data Loading**
   - Reading the used car dataset
   - Initial inspection of columns and data types

2. **Data Cleaning**
   - Handling missing values
   - Removing or correcting inconsistent entries
   - Formatting numerical and categorical variables

3. **Exploratory Data Analysis (EDA)**
   - Distribution analysis of price, mileage, and age
   - Feature-wise comparison using visualizations
   - Correlation analysis between numerical features

4. **Insights and Observations**
   - Key factors affecting car prices
   - Patterns related to depreciation and usage
   - Summary of actionable insights

---


## Repository Structure

```

03_used_car_dataset_analysis/
│
├── dataset/                     # Dataset directory (ignored in Git)
│   └── .gitkeep
├── Used_Car_Dataset_Analysis.ipynb
├── requirements.txt
└── README.md

````

---

## How to Run

1. Clone the main repository:
   ```bash
   git clone git@github.com:tanzeelajvd/applied-data-analysis-ml-projects.git
   ````

2. Navigate to this project:

   ```bash
   cd applied-data-analysis-ml-projects/03_used_car_dataset_analysis
   ```

3. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Launch the notebook:

   ```bash
   jupyter notebook Used_Car_Dataset_Analysis.ipynb
   ```

---

## Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Jupyter Notebook

---

## Key Takeaways

* Vehicle price is influenced by a combination of age, mileage, and specifications
* Exploratory analysis provides valuable insights before model building
* Clean EDA is essential for reliable downstream machine learning tasks

---

## Author

**Tanzeela Javid**
Applied Machine Learning · Data Analysis · AI Systems

