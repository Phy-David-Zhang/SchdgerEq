# Makefile for Schrodinger equation solve engine

# Copyright (C) 2017 Zhang Changkai
# Contact via phy.zhangck@gmail.com
# All rights reserved.

cmplr = ghc
gflag = --make
optmz = -O2
proff = -rtsopts
cmpfg = -fforce-recomp

exepf = +RTS -sstderr

target = Main.hs
exefile = Main

data:
	@echo === Compiling Schrodinger Equation Solve Engine ===
	@$(cmplr) $(gflag) $(optmz) $(proff) $(cmpfg) $(target)
	@echo === Generating Solution ===
	@./$(exefile) $(exepf)
	@echo === Cleaning Temporary Files
	@rm -f *.o *.hi
	@echo === Solution Generation Complete

pack:
	@echo === Building Haskell Solving Engine ===
	@echo '>>> cabal sandbox init'
	@cabal sandbox init
	@echo
	@echo '>>> cabal install --enable-shared'
	@cabal install --enable-shared
	@echo
	@echo '>>> cp dist/dist-sandbox-*/build/*.dylib .'
	@cp dist/dist-sandbox-*/build/*.dylib .

clean:
	@echo === Cleaning Haskell Build ===
	rm -f cabal.sandbox.config
	rm -rf .cabal-sandbox
	rm -rf dist
