# Multi-Tenant Serverless Task Manager

An end-to-end serverless web application built on AWS, featuring secure user isolation and asynchronous task processing.

## 🚀 Features
- **Secure Authentication:** JWT-based login via **AWS Cognito**.
- **Data Isolation:** Owner-based filtering using **DynamoDB** expressions (Users only see their own tasks).
- **Asynchronous Processing:** **Amazon SQS** decouples the API from the database for high performance.
- **Serverless Backend:** Scalable logic handled by **AWS Lambda**.

## 🏗️ Architecture
![Architecture Diagram](./docs/architecture_diagram.png)

## 🛠️ Tech Stack
- **Frontend:** HTML5, JavaScript (Fetch API), S3 Static Hosting.
- **API:** AWS API Gateway (HTTP API).
- **Compute:** AWS Lambda (Python).
- **Database:** Amazon DynamoDB.
- **Messaging:** Amazon SQS.

## 🧠 Lessons Learned
- Handling **CORS Preflight (OPTIONS)** requests at the Lambda level.
- Extracting user identity from the `requestContext['authorizer']['jwt']['claims']` in HTTP APIs.
- Managing asynchronous state updates between Producer and Worker functions.
<img width="1891" height="912" alt="image" src="https://github.com/user-attachments/assets/ae4a7dd5-634a-4fc2-b9e0-3e01eb1b4753" />
<img width="1900" height="372" alt="image" src="https://github.com/user-attachments/assets/c316592c-5847-4f95-87b3-e15a61ffb661" />
