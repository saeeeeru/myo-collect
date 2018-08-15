# myo-collect
This is a repository for collecting a time-series sequence using [myo armband](https://jp.myo.com/).

## Usage
### requirements
- Written for Python 3.x
- Please Check required Python library in ./requirements.txt

### Installation
1. Download Myo Connect and SDK from [Myo Developer Page](https://developer.thalmic.com/downloads)

2. Install required Python Library

		pip install -r ./requirements.txt


3. Edit line.49 in a source code of main.py

		myo.init(sdk_path='[/path/to/sdk/directory/]')  # please insert the sdk file path


### Colelct a time-series sequences
1. Start collecting

		
		python3 main.py -D [dataset] -n [index]

2. Stop collecting

		Ctrl + C
