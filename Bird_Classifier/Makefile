.PHONY: all
all:
	@echo "'make all' not supported"

.PHONY: clean
clean:
	rm -rf bird-classifier.tfl* *.hdf5 *.py Images/

data.zip:
	wget "https://s3-us-west-2.amazonaws.com/ml-is-fun/data.zip"

full_dataset.pkl: data.zip
	unzip -o data.zip

01\ -\ PickleToHDF.py: 01\ -\ PickleToHDF.ipynb
	jupyter nbconvert --to python "$<"

02\ -\ Merge\ Data.py: 02\ -\ Merge\ Data.ipynb
	jupyter nbconvert --to python "$<"

04\ -\ ExtractImages.py: 04\ -\ ExtractImages.ipynb
	jupyter nbconvert --to python "$<"

05\ -\ Import Images.py: 05\ -\ Import\ Images.ipynb
	jupyter nbconvert --to python "$<"

full_dataset.hdf5: 01\ -\ PickleToHDF.py
	python3 "$<"

merged_dataset.hdf5: 02\ -\ Merge\ Data.py full_dataset.hdf5
	python3 "$<"

Images: 04\ -\ ExtractImages.py merged_dataset.hdf5
	python3 "$<"

imported_dataset.hdf5: 05\ -\ Import\ Images.py Images
	python3 "$<"
