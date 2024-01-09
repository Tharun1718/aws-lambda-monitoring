# AWS Serverless Data Pipeline

## Overview

This repository contains three AWS Lambda functions designed to create a serverless data pipeline:

1. A step function is triggered every 1 minute.
2. **`invoke_lambda_function`**: Triggered by the step function every minute, it invokes another lambda function every 15 seconds.
3. **`main_lambda_function`**: Fetches data from an API and stores it in an Amazon RDS database.
4. An alarm is triggered when the instance goes down.
5. **`notify_lambda_function`**: Triggered by the alarm, sends a notification to a Slack channel.

