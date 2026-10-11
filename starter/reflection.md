
# Project Reflection: Customer Support AI Agent

## 1. Design Decision

For this project, I followed Udacity's starter architecture and implemented the required components using Amazon Bedrock AgentCore, Strands Agents, and AWS services.
One important implementation decision was to strengthen the agent's system prompt with explicit accuracy rules. For example, I instructed the agent to retrieve policies from the Knowledge Base rather than invent information, distinguish estimated from confirmed delivery dates.

I also implemented long-term memory through hooks that retrieve relevant customer information before processing requests and save interactions afterward. This allows the agent to provide more personalized support across sessions.

## 2. Technical Challenge

One of the most challenging issues occurred when testing the Browser tool after deployment. Although the integration was configured, the agent could not access websites.
To resolve this, I investigated Amazon CloudWatch logs and identified a file permission error involving the Playwright executable. I corrected the permissions within the deployment ZIP, uploaded the modified package to Amazon S3, and updated the existing AgentCore runtime using the AWS SDK. After redeployment, the Browser tool successfully retrieved the Udacity website title.

Another challenge involved ensuring the accuracy of loyalty discount calculations. The agent's responses needed to correctly reflect redeemed points, tier discounts, total savings, and the final order amount.
To address this, I updated the loyalty calculation tool's output to provide clearer, more consistent results and refined the system prompt to ensure the agent used those values rather than recalculating them independently.

## 3. Production Considerations
For production use, I would focus on security, reliability, and cost management.
Refund processing should include customer authentication, authorization checks, and safeguards against duplicate transactions. I would also improve error handling, implement automated tests, and configure CloudWatch monitoring and alerts.
Additionally, I would establish AWS budget alerts and review the cost of resources such as OpenSearch Serverless. Finally, I would use a CI/CD pipeline to automate deployment packaging and ensure consistent executable permissions across environments.