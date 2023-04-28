var FLIRContract = artifacts.require("AddNumbers");

module.exports = function(deployer) {
	deployer.deploy(FLIRContract);
};