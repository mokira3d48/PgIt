# Progress Iterator (PgIt)
![](https://img.shields.io/badge/LICENSE-MIT-%2300557f)
![](https://img.shields.io/badge/lastest-2024--07--23-success)
![](https://img.shields.io/badge/contact-dr.mokira%40gmail.com-blueviolet)

## Installation
Just copy and past this module into your project source code.

## Usage

```python
from pgit import PBM, ProgressBar


def main():
    """Main function"""
    pbm = PBM(" | ")
    pb1 = ProgressBar()
    pb2 = ProgressBar()
    pb1.name = "progress1"
    pb2.name = "progress2"
    pbm.append(pb2)
    pbm.add(pb1)

    pb1.length = 300
    pb2.length = 5
    pb1.bins = 100
    pb2.bins = 5
    pb2.bchr = '='
    pb2.pchr = '>'
    pb2.empt = '.'
    pb2.lchr = '{'
    pb2.rchr = '}'
    pb2.format = "{logger} {progressbar} {percent}"
    pb2.log_format("code: {k:05d} / {num}", k=0, num=pb1.length)

    for i in range(2):
        for j in range(pb1.length):
            pb1.step(1)
            if j % 2 == 0:
                pb2.step(1)
            pb1.log(f"index: {j}")
            pb2.log(k=j)
            sleep(0.05)
            if pb2.full():
                pb2.reset()

        pbm.resume(
            f"End of step {i} session in " + "{progress1_duration}.")
        pbm.reset()

    pbm.resume(
        "End of all progress session"
        " in {progress1_duration} - {progress2_duration}.")
    pbm.reset()


if __name__ == '__main__':
    main()
```

```
End of step 0 session in 000:00:00:15.119.
End of step 1 session in 000:00:00:15.124.
End of all progress session in 000:00:00:15.124 - 000:00:00:00.000.
```
