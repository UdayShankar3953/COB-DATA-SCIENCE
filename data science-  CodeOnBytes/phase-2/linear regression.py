import pandas as pd

# Load the training dataset
train_data_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRTK2NvcndgPX41Czu6Ft2Ho_nE-z50BgTqdzwFW0rsJ2nvyNLe2DoIg1COzUbgw80oaRBjfy5-WtFk/pub?output=csv'
train_data = pd.read_csv(train_data_url)

# Display the first few rows of the training data
print(train_data.head())

# Check for NaN values in the 'y' column of the training data
nan_values = train_data['y'].isnull().sum()
print("Number of NaN values in 'y' column:", nan_values)

train_data = train_data.dropna(subset=['y'])

train_data['y'].fillna(train_data['y'].mean(), inplace=True)

from sklearn.linear_model import LinearRegression

# Create the linear regression model
model = LinearRegression()

# Fit the model using the training data
X_train = train_data[['x']]  # Features
y_train = train_data['y']    # Target variable
model.fit(X_train, y_train)

# Load the test dataset
test_data_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRyvZ7lknwiSghK9aen1SaTEYoN3JS40rrGLpcyrsVZy1tB2T4gn6Y3-cdzPUFCPMmmqREWefW3kl4_/pub?output=csv'
test_data = pd.read_csv(test_data_url)

# Display the first few rows of the test data
print(test_data.head())

# Perform predictions using the trained model
X_test = test_data[['x']]  # Features
predictions = model.predict(X_test)

# Display the predictions
print(predictions)
