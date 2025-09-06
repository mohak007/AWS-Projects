# AWS Password-Based Authentication Project  

This project demonstrates a **simple password-based authentication system** using **AWS services**.  
It includes a frontend hosted on **Amazon S3** and a backend powered by **AWS Lambda + API Gateway + DynamoDB**.  

---

## 🚀 Features
- User registration with **username, email, and password**
- Login system with validation
- Forgot password flow
- Contact Us page (inside dashboard)
- Hosted frontend on **S3 + CloudFront**
- Serverless backend using **AWS Lambda**

---

## 📂 Project Structure

AWS-Projects/
├─ frontend/ # Static frontend (HTML, CSS, JS)
│ ├─ login.html
│ ├─ register.html
│ ├─ dashboard.html
│ ├─ contact.html
│ └─ style.css
│
├─ lambda/ # AWS Lambda backend
│ └─ handler.py
│
├─ assets/ # Images, logos, etc.
│ └─ applogo.jpg
│
├─ README.md # Project documentation
└─ .gitignore # Ignored files

---

## ⚡ AWS Services Used
- **Amazon S3** → Host static frontend  
- **Amazon API Gateway** → Expose REST APIs for frontend communication  
- **AWS Lambda (Python)** → Backend logic (user registration, login)  
- **Amazon DynamoDB** → Store user credentials securely  

---

## 🖥️ Setup Instructions
1. Clone this repo:
 
   git clone https://github.com/mohak007/AWS-Projects.git
   cd AWS-Projects
   
2. Upload frontend/ files to your S3 bucket:
    aws s3 cp frontend/ s3://your-bucket-name/ --recursive
3. Deploy the Lambda function:
    Navigate to lambda/handler.py
    Zip and upload to Lambda:
      zip function.zip handler.py
      aws lambda update-function-code --function-name your-function-name --zip-file fileb://function.zip

4.Connect API Gateway to Lambda.

5.Update the API URL in login.html and register.html.

---
Lambda Function (handler.py)

The Lambda function handles:
1. Register User → Store in DynamoDB
2. Login User → Validate credentials
3. Check if user exists

## Screenshots
Register Page:
![Register Page](Images/register-page.png)

Login Page:
![Register Page](Images/login-page.png)

CloudTech Dashboard:
![Register Page](Images/cloudtech-dashboard.png)

Services:
![Register Page](Images/services.png)

Forgot Password:
![Register Page](Images/forgotPassword.png)

Contact:
![Register Page](Images/contact.png)




## Future Enhancements
- Add OAuth or multi-factor authentication
- Connect with a database to store credentials securely


Mohak Kataria

💼 GitHub: mohak007

🌐 LinkedIn: [https://www.linkedin.com/in/mohak-kataria-39ab78116]
