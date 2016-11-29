data.zip:
	wget "https://s3-us-west-2.amazonaws.com/ml-is-fun/data.zip"

full_dataset.pkl:
	unzip data.zip

BirdClassifier.py:
	jupyter nbconvert --to python BirdClassifier.ipynb

.PHONY: clean
clean:
	rm -rf bird-classifier.tfl*
