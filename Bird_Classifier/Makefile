.PHONY: all
all:
	@echo "'make all' not supported"

.PHONY: clean
clean:
	rm -rf bird-classifier.tfl* *.hdf5 *.py

data.zip:
	wget "https://s3-us-west-2.amazonaws.com/ml-is-fun/data.zip"

full_dataset.pkl: data.zip
	unzip -o data.zip

01\ -\ PickleToHDF.py: 01\ -\ PickleToHDF.ipynb
	jupyter nbconvert --to python "01 - PickleToHDF.ipynb"

full_dataset.hdf5: full_dataset.pkl 01\ -\ PickleToHDF.py
	python3 "01 - PickleToHDF.py"

02\ -\ Merge\ Data.py: 02\ -\ Merge\ Data.ipynb
	jupyter nbconvert --to python "$<"

merged_dataset.hdf5: full_dataset.hdf5 02\ -\ Merge\ Data.py
	python3 "02 - Merge Data.py"
