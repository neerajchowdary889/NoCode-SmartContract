import openai
import re
import os
import subprocess
from termcolor import colored
from prettytable import PrettyTable
from key import GptKey
from return_Contract_Name import returnName
from creating_migrationFile import create_migrationFile
openai.api_key = GptKey

Model = 'gpt-3.5-turbo'

def search(prompt):
    print((colored("Searching for: "+prompt, 'green', attrs=['bold'])))

    response=openai.ChatCompletion.create(
        model=Model,
        messages=[{"role":"user",
                "content":prompt}
                ],
        max_tokens=2048,                                                                                                                                                           
    )

    Message = response.choices[0].message.content

    history[prompt] = Message
    print(Message)

    return user_satisfaction(Message)




def advanced_search(prompt):
    print((colored("Searching for: "+prompt, 'green', attrs=['bold'])))

    response = openai.ChatCompletion.create(
            model=Model,
            messages=[{"role":"assistant", "content":history[list(history)[-1]]},
                    {"role":"user",
                        "content":prompt}
                        ],
            max_tokens=2048,
        )

    Message = response.choices[0].message.content

    history[prompt] = Message
    print(Message)

    return user_satisfaction(Message.strip())




def user_satisfaction(message):
    user_choice = input(colored("Satisfy with Output? (y/n) >>> ", 'yellow', attrs=['bold']))
    if user_choice == "y":
        return
    elif user_choice == "n":
        user_prompt = input(colored("Enter Improvisations in Output? >>> ", 'light_magenta', attrs=['bold']))
        return advanced_search(user_prompt)
    else:
        print(colored("Invalid Input, breaking to main...", 'red', attrs=['bold']))
        return 




def History():
    for key, value in history.items():
        table.add_row([key, value], divider=True)
    print(table)
    return




def create_SOLFile():
    pattern = r"(?s)pragma solidity.*\}"
    matches = re.findall(pattern, history[list(history)[-1]])
    solidity_code = ''.join(matches)

    filename = 'SOLFile.sol'
    i = 1

    while os.path.exists(filename):
        filename = f'SOLFile_{i}.sol'
        i += 1

    with open(filename, 'w') as f:
        f.write(solidity_code)
        f.close()
        
    print(colored("SOL File Created", 'green', attrs=['bold']))

    with open('FileHistory.txt','a') as f:
        f.write(filename)
        f.write("\n")
        f.close()

    return solidity_code



prompt = input(colored("Enter Prompt you want to search for? >>> ", 'light_magenta', attrs=['bold']))
table = PrettyTable(["Prompt", "Output"])
table.align = "l"
table.max_width = 120
history = {}
search(prompt)


print(colored("\n<-----Searching Done----->\n", 'red', attrs=['bold']))


history_check = input(colored("Do you want to see history? (y/n) >>> ", 'yellow', attrs=['bold']))
if history_check == "y":
    History()
else:
    print(colored("Thankyou...", 'red', attrs=['bold']))


deploy = input(colored("Do you want to deploy this code in a SOL file? (y/n) >>> ", 'yellow', attrs=['bold']))
if deploy == "y":
    Refactored_code = create_SOLFile()
    TestNet_Deploy = input(colored("Do you want to deploy this code in a TestNet using Truffle? (y/n) >>> ", 'yellow', attrs=['bold']))
    if TestNet_Deploy == "y":
        subprocess.run(["./truffle_setup.sh"], shell=True)
        print(colored("File Moved to contracts", 'green', attrs=['bold']))
        # print(colored("yet to deploy in testnet", 'green', attrs=['bold']))


        print(colored("Trying to do Post Contract creation.....", 'yellow', attrs=['bold']))
        try:
            word = returnName(Refactored_code)      # Getting the CONTRACT NAME
            # print(colored(word, 'red', attrs=['bold']))
        except:
            print(colored("Contract Name not found", 'red', attrs=['bold']))
        
        create_migrationFile(word)
        subprocess.run(["./migration_setup.sh"], shell=True)
    else:
        print(colored("Solidity File not deployed in TestNet...", 'red', attrs=['bold']))

    print(colored("Thankyou for using our service", 'red', attrs=['bold']))
else:
    print(colored("Solidity File not created...", 'red', attrs=['bold']))




