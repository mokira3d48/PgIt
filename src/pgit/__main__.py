import os
import time
from pgit import ProgressIter


def main():
	""" Main function """
	pbar_format = ("{logger:18s} {pbar}"
	               " [\033[91m{purcent:6.2f}\033[0m - {time_rem}]")
	time_format = "{mins:02d}:{secs:02d}"
	progressbar = ProgressIter(
		2000, 80,
		barf=pbar_format,
		pchr='#',
		bchr='=',
		empt='-',
		time_format=time_format,
	)
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
	import os
	main()
	os.sys.exit(0)

