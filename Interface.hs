{-# LANGUAGE ForeignFunctionInterface, TemplateHaskell #-}

module Interface where

	import Foreign.HaPy
	import SchdgerEngine

	initHaPy

	pythonExport 'laplace
	pythonExport 'schrodinger
	pythonExport 'solve