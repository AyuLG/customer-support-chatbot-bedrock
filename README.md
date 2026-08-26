# 🤖 Customer Support Chatbot with Amazon Bedrock

[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bedrock](https://img.shields.io/badge/Amazon_Bedrock-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/bedrock/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An AI-powered customer support chatbot built with **Amazon Bedrock AgentCore** that handles bug reports, FAQ questions, and redirects other requests.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Results](#-results)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
- [Testing & Evaluation](#-testing--evaluation)
- [Screenshots](#-screenshots)
- [Cleanup](#-cleanup)
- [License](#-license)

---

## 🎯 Overview

This project implements a **customer support chatbot** using Amazon Bedrock's AgentCore managed harness. The chatbot automatically:

1. **Classifies** incoming customer messages
2. **Routes** them to the appropriate handler
3. **Takes action** based on the request type

The chatbot is designed for a fictional online shop and handles three types of requests:

| Request Type | Action |
|--------------|--------|
| 🐛 **Bug Reports** | Collects details → Creates ticket in DynamoDB |
| ❓ **Platform Questions** | Answers from embedded FAQ |
| 📞 **Other Requests** | Redirects to human support |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Single System Prompt** | All routing and behavior controlled by one text file |
| **Multi-Turn Conversations** | Maintains context across multiple messages |
| **Tool Integration** | Lambda function creates tickets via AgentCore Gateway |
| **Database Storage** | Bug reports stored in Amazon DynamoDB |
| **Automated Evaluation** | LLM-as-a-judge testing with perfect score |
| **Perfect Score** | 1.00/1.00 correctness on all test cases |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Amazon Bedrock** | AI model hosting and orchestration |
| **Amazon Nova Pro** | Large Language Model (LLM) |
| **AWS Lambda** | Serverless compute for bug report tool |
| **Amazon DynamoDB** | Bug ticket storage |
| **AWS CloudFormation** | Infrastructure as Code |
| **Python 3.10+** | Application logic |
| **AgentCore Gateway** | Tool execution and session management |

---

## 🏆 Results

| Metric | Score |
|--------|-------|
| **Evaluation Score** | **1.00/1.00** ✅ |
| **Test Cases Passed** | 3/3 (100%) |
| **Bug Report** | ✅ All 3 fields collected |
| **FAQ Handling** | ✅ Accurate answers |
| **Other Requests** | ✅ Proper redirects |

---

## 🏗️ Architecture
