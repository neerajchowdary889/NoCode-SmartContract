var FLIRContract = artifacts.require("Voting");

    module.exports = function(deployer) {
        deployer.deploy(FLIRContract);
    };