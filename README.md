```markdown
# 🏠 Housing Price Prediction (Linear Model)

This project demonstrates a simple linear regression model to predict housing prices based on the size of the house. The predictions are visualized using Matplotlib.

## 📈 Overview

We use the basic linear formula:
```

f(x) = w \* x + b

````
Where:
- `x` = size of the house (in 1000 sqft)
- `w` = weight (slope)
- `b` = bias (intercept)

Example:
```python
w = 100
b = 200
x = 1  # 1000 sqft
f(x) = 100 * 1 + 200 = 300 (i.e., $300,000)
````

## 🔧 Features

* Predicts house prices for given input sizes
* Plots model predictions vs actual values
* Calculates price of custom house sizes (e.g., 1200 sqft)

## 📊 Visualization

The model plots:

* **Blue line**: Model prediction
* **Red crosses**: Actual data points

![Example Plot](https://via.placeholder.com/600x300.png?text=Model+Prediction+Plot)

## 📦 Requirements

* Python 3.x
* NumPy
* Matplotlib
* pandas (optional, included in imports)

Install dependencies using:

```bash
pip install numpy matplotlib pandas
```

## 🧪 Example Output

```python
x_i = 1.5
w = 200
b = 100
cost = w * x_i + b
```

Output:

```
$400 thousand dollars
```

## 📁 Files

* `predict_and_plot.py` – Main script with prediction logic and plotting
* `README.md` – Project overview (this file)

## ✅ To Run

```bash
python predict_and_plot.py
```

## 📌 License

This project is licensed under the MIT License.

---
