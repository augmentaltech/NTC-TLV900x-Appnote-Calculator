OUTDIR=out
TEXFILE=calculations
CSVFILE=curve

.PHONY: all clean

all: calculate pdf

all:
calculate:
	python calculate.py $(TEXFILE).tex $(CSVFILE).csv
pdf:
	gnuplot plt
	xelatex  --output-directory=$(OUTDIR)/ --halt-on-error main.tex > $(OUTDIR)/make.log
clean:
	rm $(OUTDIR)/
