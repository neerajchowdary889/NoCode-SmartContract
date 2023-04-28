echo "Setting up the migration files..."
second_line=$(head -n 1 MigrationFileHistory.txt)


file=$(head -n 1 created_dir.txt)
sudo mv $second_line $file/migrations
cd $file
truffle develop <<EOF
migrate
EOF