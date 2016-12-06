.PHONY: all
all:
	@echo "'make all' not supported"

data.zip:
	wget "https://s3-us-west-2.amazonaws.com/ml-is-fun/data.zip"

full_dataset.pkl: data.zip
	unzip -o data.zip

01\ -\ PickleToHDF.py: 01\ -\ PickleToHDF.ipynb
	jupyter nbconvert --to python "01 - PickleToHDF.ipynb"

full_dataset.hdf5: full_dataset.pkl 01\ -\ PickleToHDF.py
	python3 PickleToHDF.py

merged_dataset.hdf5:


.PHONY: clean
clean:
	rm -rf bird-classifier.tfl* *.hdf5 *.py
