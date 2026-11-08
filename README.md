## Han Sun's resume

markdown -> html -> pdf

**https://cv.sunhanice.com**

------

### Installation

```
git clone git@github.com:HaniceSun/hanicesun.github.io.git
cd hanicesun.github.io
pip install .
```

### Usage

```
cd docs
mdcv                                  # build index.html + Resume_HanSun.pdf from resume.md
mdcv --resume resume.md               # same, explicit input
mdcv --letter cover_letter.md         # build cover_letter.pdf
mdcv --resume --letter                # build both
```

### Author and License

**Author:** Han Sun

**Email:** hansun@stanford.edu

**License:** [MIT License](LICENSE)
