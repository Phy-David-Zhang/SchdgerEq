# Makefile for Schrodinger equation solve engine

# Copyright (C) 2017 Zhang Changkai
# Contact via phy.zhangck@gmail.com
# All rights reserved.

# extended python environment
# change to python if necessary
python = ~/.anaconda3/bin/python

# haskell configuration
cmplr = ghc
gflag = --make
optmz = -O2
proff = -rtsopts
cmpfg = -fforce-recomp

exepf = +RTS -sstderr

target = Generator.hs
exefile = Generator

# generate data
data:
	@echo === Compiling Schrodinger Equation Solve Engine ===
	@$(cmplr) $(gflag) $(optmz) $(proff) $(cmpfg) $(target)
	@echo === Generating Solution ===
	@./$(exefile) $(exepf)
	@echo === Cleaning Temporary Files
	@rm -f *.o *.hi
	@echo === Solution Generation Complete

# visualization
visual:
	@echo === Generating Visualization ===
	@$(python) Visualizer.py

clean:
	@echo === Cleaning Haskell Build ===
	rm -f cabal.sandbox.config
	rm -rf .cabal-sandbox
	rm -rf dist
