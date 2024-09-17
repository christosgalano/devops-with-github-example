# DevOps with GitHub: FastAPI example

## Overview

The purpose of this repository is to demonstrate how someone can leverage GitHub's numerous DevOps capabilities to streamline both application and infrastructure development and deployment processes.

It consists of a FastAPI application, Bicep infrastructure as code (IaC), and GitHub workflows, collectively showcasing how to leverage different GitHub capabilities to simplify and automate the deployment process of an application to the cloud securely and reliably. The application is deployed to Azure, but the same principles can be applied to any cloud provider or even on-premises infrastructure.

The simple API application returns the message "Hello " followed by each value provided in the path parameters, separated by commas.

For example, if the path parameter is "world", the API will return "Hello world", whereas if the path parameters are "world" and "universe", the API will return "Hello world, universe".

## License

Released under [MIT](/LICENSE) by [@christosgalano](https://github.com/christosgalano).
