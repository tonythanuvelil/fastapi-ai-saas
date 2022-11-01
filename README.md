# fastapi-ai-saas

AI saas app

Stack:
- FastAPI
- openai
- awscli
- Node
- AWS CDK
- AWS CloudFormation
- AWS Lambda
- AWS API Gateway

Prerequisities for aws cdk:
- Install nodejs: `sudo apt install nodejs` or check how to install nodejs on your OS.
- Install npm
- Install aws-cdk: `sudo npm install -g aws-cdk`
- Install aws-cli in your python venv: `pip install awscli`
- Install aws-cdk-lib: `npm install aws-cdk-lib`
- Install docker on your machine.

- This can be done using python alone, but the native language of aws-cdk is typescript, so it's better using typescript, + the fun!

Run the following to make sure you have everything setup correctly:
- `node -v` -> you should see something like v16.18.0
- `npm -v` -> 8.19.2 or similar
- `aws --version` -> aws-cli/1.26.5 Python/3.10.6 Linux/5.15.0-52-generic botocore/1.28.5 or similar
- `cdk --version` -> 2.49.1 (build be5fcf4) or similar

Setting up infrastructure (by infra-as-code):
- Run `mkdir copykitt-infra && cd copykitt-infra` or a name of your choice.
- Run `cdk init --language typescript`.
- Make changes in `copykitt-infra-stack.ts` or `<your-dir-name>-stack.ts`
- Configure aws using `aws configure` if not done already.
- Run `cdk bootstrap aws://your-account-id/your-region`.
- Once success, run `cdk deploy`.

Now your AWS CloudFormation stack should be ready and you should see your newly created AWS Lambda.

#### Further steps needs to be confirmed, will update soon.

Original tutorial by [pixegami](https://www.youtube.com/watch?v=yxyyYMWu1ZA&list=PLZJBfja3V3RuH2VRbRh9F0mB9hfdzkUKk&index=11).