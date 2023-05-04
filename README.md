# DevOps with GitHub: FastAPI example

[![ci-cd](https://github.com/christosgalano/devops-with-github-example/actions/workflows/ci_cd.yaml/badge.svg?branch=main&event=push)](https://github.com/christosgalano/devops-with-github-example/actions/workflows/ci_cd.yaml)
[![codeql](https://github.com/christosgalano/devops-with-github-example/actions/workflows/codeql.yaml/badge.svg?branch=main&event=push)](https://github.com/christosgalano/devops-with-github-example/actions/workflows/codeql.yaml)
[![deploy-infra](https://github.com/christosgalano/devops-with-github-example/actions/workflows/deploy_infra.yaml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/christosgalano/devops-with-github-example/actions/workflows/deploy_infra.yaml)

## General

The purpose of this repository is to demonstrate how someone can leverage GitHub's numerous DevOps capabilities to streamline both application and infrastructure development and deployment processes.

It consists of a FastAPI application, Bicep infrastructure as code (IaC), and GitHub workflows, collectively showcasing how to leverage different GitHub capabilities to simplify and automate the deployment process of an application to the cloud in a secure and reliable way. The application is deployed to Azure, but the same principles can be applied to any cloud provider or even on-premises infrastructure.

The application is a simple API that returns the message "Hello " followed by each value provided in the path parameters, separated by commas.

For example, if the path parameter is "world", the API will return "Hello world", whereas if the path parameters are "world" and "universe", the API will return "Hello world, universe".

## License

Released under [MIT](/LICENSE) by [@christosgalano](https://github.com/christosgalano).
