{-# LANGUAGE CPP #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -fno-warn-implicit-prelude #-}
module Paths_SchdgerEngine (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,0,2,0] []
bindir, libdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/Users/David/Public/SchdgerEq/.cabal-sandbox/bin"
libdir     = "/Users/David/Public/SchdgerEq/.cabal-sandbox/lib/x86_64-osx-ghc-8.0.1/SchdgerEngine-0.0.2.0-58I1cgPrB4V6IbmSvo2Abe"
datadir    = "/Users/David/Public/SchdgerEq/.cabal-sandbox/share/x86_64-osx-ghc-8.0.1/SchdgerEngine-0.0.2.0"
libexecdir = "/Users/David/Public/SchdgerEq/.cabal-sandbox/libexec"
sysconfdir = "/Users/David/Public/SchdgerEq/.cabal-sandbox/etc"

getBinDir, getLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "SchdgerEngine_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "SchdgerEngine_libdir") (\_ -> return libdir)
getDataDir = catchIO (getEnv "SchdgerEngine_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "SchdgerEngine_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "SchdgerEngine_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
