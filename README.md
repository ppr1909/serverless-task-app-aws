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
