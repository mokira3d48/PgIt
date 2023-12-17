import os
import math
import time


class ProgressIter:
	""" Implementatation of a progressbar

	:param length: The length of the process.
	"""

	def __init__(self,
							 length: int,
							 bins: int = 20,
							 bchr: str = '-',
							 lchr: str = '[',
							 rchr: str = ']',
							 pchr: str = '>',
							 empt: str = ' '):

		self._length = length
		self._bins = bins
		self._bchr = bchr
		self._lchr = lchr
		self._rchr = rchr
		self._pchr = pchr
		self._empt = empt

		self._progress = 0
		self._starttime = 0
		self._log = ''

	@property
	def length(self) -> int:
		""" Returns the length of the JOB """
		return self._length

	@length.setter
	def length(self, value: int):
		self._length = value

	def _time_format(self, millis: int) -> str:
		""" Function to converte milliseconds to hh:mm:ss:millis """
		sec = millis // 1000
		millis = millis % 1000

		mins = sec // 60
		sec = sec % 60

		hours = mins // 60
		mins = mins % 60

		days = hours // 24
		hours = hours % 24
		# return "Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
		return f"{days}:{hours:02d}:{mins:02d}:{sec:02d}:{millis:03d}"

	def get_progress_purcent(self) -> float:
		""" Function to compute and returns the progress purcent """
		return self._progress * 100.0 / self._length

	def step(self, value: int):
		""" Function to perform one step

		:param value: The value of one step performed.
		"""
		self._progress += value
		if self._progress > self._length:
			self._progress = self._length

		# compute remaning
		if not self._starttime:
			self._starttime = time.time()

		rate = self._progress / (time.time() - self._starttime)
		str_rem = ""
		if rate != 0.0:
			remaining = (self._length - self._progress) / rate
			# convert to milisecond
			remaining = int(remaining*1000)
			str_rem = self._time_format(remaining)
		else:
			str_rem = '-:--:--:--:---'

		n_bins = math.floor(self._progress  * self._bins / self._length)
		purcent = self.get_progress_purcent()
		done = n_bins == self._bins
		pchr = self._pchr if not done else self._bchr
		# clear line and print the progress bar into terminal
		print("\033[2K", end='\r')
		print(
			(f"[ {purcent:6.2f}% - "
			 f"{str_rem} ] "
			 f"{self._lchr}{self._bchr * n_bins}{pchr}"
			 f"{self._empt*(self._bins - n_bins)}{self._rchr} "
			 f"{rate:.2f} its/sec "
			 f"{self._log}"
			),
			end=' ',
			flush=True
		)

	def get_duration(self) -> int:
		""" Returns the duration of the progress in seconds """
		return time.time() - self._starttime

	def log(self, message: str):
		""" Function of log printing """
		self._log = f"- {message}"

	def finalise(self, message: str):
		""" Function to finalise the progress counting with a message

		:param message: The resume message.
		"""
		# clear the progress bar, and print the message received by argument
		print("\033[2K", end='\r')
		print(message, flush=True)

	def reset(self):
		""" Function to reset the progress counter """
		self._progress = 0
		self._starttime = 0
		self._log = ''


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
