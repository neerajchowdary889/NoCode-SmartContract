def create_migrationFile(word):
    fileName2 = "2_deploy_contracts.js"
    data2 = """var FLIRContract = artifacts.require("%s");

    module.exports = function(deployer) {
        deployer.deploy(FLIRContract);
    };"""%(word)
    ff = open(fileName2, "w")
    ff.write(data2)
    ff.close()

    txtfile = open("MigrationFileHistory.txt", "w")
    txtfile.write(fileName2)
    txtfile.close()

    return