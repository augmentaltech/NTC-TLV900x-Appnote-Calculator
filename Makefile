OUTDIR=out
TEXFILE=calculations
CSVFILE=curve

.PHONY: all clean

all: $(OUTDIR)/main.pdf

$(TEXFILE).tex $(CSVFILE).csv: calculate.py
	python calculate.py $(TEXFILE).tex $(CSVFILE).csv

curve.png: plt $(CSVFILE).csv
	gnuplot plt

$(OUTDIR)/main.pdf: main.tex $(TEXFILE).tex curve.png
	xelatex  --output-directory=$(OUTDIR)/ --halt-on-error main.tex > $(OUTDIR)/make.log

clean:
	rm $(OUTDIR)/*
