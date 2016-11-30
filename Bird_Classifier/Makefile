data.zip:
	wget "https://s3-us-west-2.amazonaws.com/ml-is-fun/data.zip"

full_dataset.pkl: data.zip
	unzip -o data.zip

BirdClassifier.py: BirdClassifier.ipynb
	jupyter nbconvert --to python BirdClassifier.ipynb

bird-classifier.tfl: BirdClassifier.py
	python3 BirdClassifier.py

PickleToHDF.py: PickleToHDF.ipynb
	jupyter nbconvert --to python BirdClassifier.ipynb

full_dataset.hdf5: full_dataset.pkl PickleToHDF.py
	python3 PickleToHDF.py

merged_dataset.hdf5:


.PHONY: clean
clean:
	rm -rf bird-classifier.tfl*
