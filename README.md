<!--
title: 'AWS Python Example'
description: 'This project deploys a email validation function running on AWS Lambda using the Serverless Framework.'
framework: v2
platform: AWS
language: python
-->

## Usage

*Commands to run locally:*

- `serverless deploy` (redeploy)

`serverless invoke local --data '{"body": "{\"email\":\"test@example.com\"}"}' --function main`

- https://app.serverless.com/afrida1009/apps/emailvalidapp/aws-email-valid/dev/us-east-1/interact

- everytime handler is changed, deploy

- Test API on terminal run 
  `curl -d '{"email":"testemaile@exam.com"}' https://0rcy9gs1g2.execute-api.us-east-1.amazonaws.com/dev/email/validate`


## Explanation:
Explanation on the above commands.

### Deployment

In order to deploy the project, you need to run the following command:

```
$ serverless deploy
```

After running deploy, you should see output similar to:

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service aws-python.zip file to S3 (711.23 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.................................
Serverless: Stack update finished...
Service Information
service: aws-python
stage: dev
region: us-east-1
stack: aws-python-dev
resources: 6
functions:
  api: aws-python-dev-hello
layers:
  None
```

### Local development

After successful deployment, you can invoke your function locally by using the following command:

```bash
serverless invoke local --function main
```

Which should result in response similar to the following:

```
{
    "statusCode": 200,
    "body": "{'result': "youremail@email.com"}"
}
```

### Bundling dependencies

In case you would like to include third-party dependencies, you will need to use a plugin called `serverless-python-requirements`. You can set it up by running the following command:

```bash
serverless plugin install -n serverless-python-requirements
```
