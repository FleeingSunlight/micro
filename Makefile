gitignore:
	rm -rf ./services/.gitignore
	cat ./services/gitignore/*.gitignore > ./services/.gitignore
