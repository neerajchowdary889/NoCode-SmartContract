def create_migrationFile(word):
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
    txtfile.write(fileName1)
    txtfile.write("\n")
    txtfile.write(fileName2)
    txtfile.close()

    return