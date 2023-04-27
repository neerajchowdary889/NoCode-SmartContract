import openai
import os
from termcolor import colored
from prettytable import PrettyTable

openai.api_key = "---Your OpenAI API_KEY here---" #GptKey



def search(prompt):
    print((colored("Searching for: "+prompt, 'green', attrs=['bold'])))

    response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role":"user",
                "content":prompt}
                ],
        max_tokens=500,                                                                                                                                                           
    )

    Message = response.choices[0].message.content

    history[prompt] = Message
    print(Message)

    return user_satisfaction(Message)




def advanced_search(prompt):
    print((colored("Searching for: "+prompt, 'green', attrs=['bold'])))

    response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role":"assistant", "content":history[list(history)[-1]]},
                    {"role":"user",
                        "content":prompt}
                        ],
            max_tokens=500,
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
    filename = 'SOLFile.sol'
    i = 1

    while os.path.exists(filename):
        filename = f'SOLFile_{i}.sol'
        i += 1

    with open(filename, 'w') as f:
        f.write(history[list(history)[-1]])
        f.close()
        
    print(colored("SOL File Created", 'green', attrs=['bold']))
    return




prompt = input(colored("Enter Prompt you want to search for? >>> ", 'light_magenta', attrs=['bold']))
table = PrettyTable(["Prompt", "Output"])
table.align = "l"
table.max_width = 120
history = {}
search(prompt)


print(colored("\n<-----Searching Done----->\n", 'red', attrs=['bold']))


history_check = input("Do you want to see history? (y/n) >>> ")
if history_check == "y":
    History()
else:
    print(colored("Thankyou...", 'red', attrs=['bold']))


deploy = input(colored("Do you want to deploy this code in a SOL file? (y/n) >>> ", 'yellow', attrs=['bold']))
if deploy == "y":
    create_SOLFile()
else:
    print(colored("Solidity File not created...", 'red', attrs=['bold']))

print(colored("Thankyou for using our service", 'red', attrs=['bold']))