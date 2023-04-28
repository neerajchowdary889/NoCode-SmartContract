import re

string = '''Sure, here's an updated version of the Solidity code that allows the user to input two numbers into the `add` function:

pragma solidity ^0.8.0;

contract AddNumbers {
    
    function add(uint256 a, uint256 b) public pure returns (uint256) {
        return a + b;
    }
    
    function userInputAdd() public pure returns (uint256) {
        uint256 num1;
        uint256 num2;
        // Prompt user to input values for num1 and num2
        // For example, using the "read" function from the "ethers" library:
        // num1 = ethers.utils.parseEther(read("Enter the first number: "));
        // num2 = ethers.utils.parseEther(read("Enter the second number: "));
        // Or simply hardcode some values for testing:
        num1 = 5;
        num2 = 7;
        return add(num1, num2);
    }
    
}'''

# Define the regex pattern to match Solidity code
pattern = r"(?s)pragma solidity.*\}"
matches = re.findall(pattern, string)
solidity_code = ''.join(matches)
# print(solidity_code)

index = solidity_code.index('contract')
print(index)
Bracket_index = solidity_code.index('{')

word = solidity_code[index+8:Bracket_index].strip()
print(word)


### Creating migration files and saving it
fileName1 = "1_initial_migration.js"
data1 = """const Migrations = artifacts.require("Migrations");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
};"""
f = open(fileName1, "w")
f.write(data1)
f.close()

fileName2 = "2_deploy_contracts.js"
data2 = """var FLIRContract = artifacts.require("%s");

module.exports = function(deployer) {
	deployer.deploy(FLIRContract);
};"""%(word)
ff = open(fileName2, "w")
ff.write(data2)
ff.close()
print(data2)

txtfile = open("FileHistory.txt", "w")
txtfile.write(fileName1+"\n")
txtfile.write(fileName2)
txtfile.close()


with open("FileHistory.txt") as f:
    f.readline()
    second_line = f.readline().rstrip()
    print(second_line)

with open("FileHistory.txt") as f:
    first_line = f.readline().rstrip()
    print(first_line)