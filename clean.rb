# This is a file to keep track of variables that will clean the enviroment
# clean pytest cache and pyachche
puts("Removing all pychache....")
system("find . | grep -E \"(__pycache__|\.pyc$)\" | xargs rm -rf")
puts("Done!")

puts("Removing pytest_cache...")
system("rm -r .pytest_cache/")
puts("Done!")