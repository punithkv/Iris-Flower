# 🌸 Iris Flower Prediction (Machine Learning + Streamlit)

This project predicts the **species of an Iris flower** based on its **sepal** and **petal** measurements using a **Machine Learning model**. It includes an interactive **Streamlit web app** to make predictions in real-time.

---

## 📌 Features
- Train a model on the Iris dataset using **scikit-learn**.
- Save and load the trained model with **joblib**.
- Simple and interactive **Streamlit UI** for predictions.
- Real-time prediction based on user inputs.

---

## 📂 Project Structure
.
├── app.py # Streamlit web app
├── iris_model.pkl # Trained model (generated after training)
├── train_model.py # Script to train and save the model
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/iris-flower-prediction.git
cd iris-flower-prediction
2️⃣ Install dependencies
Make sure you have Python 3.8+ installed.
pip install -r requirements.txt
3️⃣ Train the model (only if iris_model.pkl is missing)
python train_model.py
4️⃣ Run the Streamlit app
streamlit run app.py
📊 Example Prediction
Input:

Sepal Length: 5.1

Sepal Width: 3.5

Petal Length: 1.4

Petal Width: 0.2

Output: Iris-setosa

🛠️ Technologies Used
Python 3

scikit-learn

joblib

Streamlit

pandas, numpy

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
UCI Machine Learning Repository for the Iris dataset.

Streamlit for the web framework.




https://punithkv-iris-flower.streamlit.app

