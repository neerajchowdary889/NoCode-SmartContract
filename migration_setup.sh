echo "Setting up the migration files..."
first_line=$(head -n 1 MigrationFileHistory.txt)
second_line=$(head -n 2 MigrationFileHistory.txt | tail -n 1)

file=$(head -n 1 created_dir.txt)
sudo mv $first_line $file/migrations
sudo mv $second_line $file/migrations