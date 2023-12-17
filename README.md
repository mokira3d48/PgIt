# PGIT
This package allows you to put a progress bar in your Python program.


## Installation and Configuration

```sh
pip install https://github.com/mokira3d48/pgit
```


## Usage
To use this package, you must import `ProgressIter` from `pgit` package. You instanciate with
several arguments and call function `step()` in progress loop.

```python
import os
from pgit import ProgressIter


def main():
	""" Main function """
	progressbar = ProgressIter(2000, 80, pchr='#', bchr='=', empt='-')
	for i in range(2000):
		progressbar.step(1)
		time.sleep(0.1)
		progressbar.log("First step: " + str(i))

	time.sleep(10)
	progressbar.finalise("The current job is done.")
	progressbar.reset()

	for i in range(2000):
		progressbar.step(1)
		time.sleep(0.1)
		progressbar.log("Second step: " + str(i))

	progressbar.finalise("The current job is done.")


if __name__ == '__main__':
	main()
	os.sys.exit(0)
```
