file_name=$"MVP_to_do.py"
echo Enter the desired command name for the to-do application
read command_name
pathing=$(echo "#!/usr/bin/")
py_version=$(echo $(python3 --version))
py_path=${py_version:0:10}
py_lower=$(echo "$py_path" | tr '[:upper:]' '[:lower:]')
echo $pathing $py_lower | sed 's/ //g' | cat - $file_name > temp && mv temp $file_name
chmod +x $file_name
sudo mv $file_name /usr/local/bin/$command_name
