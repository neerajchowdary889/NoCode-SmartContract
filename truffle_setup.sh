echo "Creating Truffle project..."
file=$(python3 Filecreation.py)
mkdir $file
cd $file
truffle init
echo "Truffle project created successfully!"
npm install --save truffle-hdwallet-provider
cd ..
sol_file=$(python3 SolFileName.py)
echo $sol_file
sudo mv $sol_file $file/contractsextras/testing.py