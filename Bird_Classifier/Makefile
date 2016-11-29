data.zip:
	wget "https://s3-us-west-2.amazonaws.com/ml-is-fun/data.zip"

full_dataset.pkl: data.zip
	unzip data.zip

BirdClassifier.py: BirdClassifier.ipynb
	jupyter nbconvert --to python BirdClassifier.ipynb

bird-classifier.tfl: BirdClassifier.py
	python3 BirdClassifier.py

.PHONY: clean
clean:
	rm -rf bird-classifier.tfl*
