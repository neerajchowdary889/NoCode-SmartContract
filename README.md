# No-Code SmartContract

This is designed to generate a Smart Contract using OpenAI's ChatGPT and deploy it on the Ethereum chain. The creation of the Smart Contract and its deployment to the blockchain will be done automatically. The user doesnt have to learn Solidity or deal with deployment issues.

## Prerequisites

* Linux
* Node.js (Newer version preferred)
* NPM (Newer version preferred)

## Installation

Install Truffle in your Local Machine.

```bash
npm install -g truffle
truffle version
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required Packages.

```bash
pip install openai
pip install termcolor
pip install prettytable
```

## Getting Started

1. Get OpenAI API key and give it in key.py file in our repository. Make sure you have sufficient funds for API to process your requests.
2. Based on your requirements change the model and max_tokens in main.py file.

   * If you want basic content and you want to save your funds for futher requests use gpt-3.5-turbo. If you want advanced replies choose gpt-4.0 or text-davinci-003. (Refer OpenAI documentation about models and max_tokens.)
3. Run main.py and follow instructions in code for deployment and any editing in the model replies.
4. Code will ask your permission whether to deploy or stop the program so don't panic. (Every further step we take your permission.)
5. If everything runs properly and your code got deployed then press CTRL C at last to stop the process. (we are checking all possibilities to stop it without human input.)
6. You have history of solidity files created in your FileHistory.txt

## Note Points

- Everytime ChatGPT replies are not perfect so due to imperfect replies you may get some issues. Try to solve it by yourself or try rerunning the program again. Sometimes due to some external factors even we might face issues, so try rerunning the program.
- We are not supporting Windows right now. Only Linux Machines are supported.
- Right now we are not returning the contract id, you should see the output from terminal and check for the contract id.
- At Present deploying in Localnet is supported. In future we bring support to deploy your smart contract in ethereum testnet and mainnet.
- Don't forgot to stop the execution of program after deployment of smart contract. ( Press CTRL C )
- Please note this is not perfect yet, we will try to make it better.
