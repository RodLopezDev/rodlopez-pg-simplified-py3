# Build image

python setup.py sdist bdist_wheel

# Upload to pip

twine upload dist/*



## Option 2

# Install 

pip install build setuptools