#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
import sys
import os
import unittest
import abc
from typing import List, Dict
from dataclasses import dataclass
#   Notes:
#   {{{
#   2023-04-03T21:28:22AEST 'ParameterLoader' should have makeXmlLoader / makeJsonLoader factory functions(?)
#   2023-04-03T21:30:08AEST 'ParameterLoader' hierachy, who should be responsible for checking file exists?
#   2023-04-04T20:51:51AEST 'EnvParameterFileLoader' should be derived from 'FileLoader' / 'ParameterLoader' / nothing? [...] (why does 'EnvParameterFileLoader' / 'CachedParameterLoader' need to inherit anything ('ParameterLoader' does not) (besides being an example for decoration)) [...] (deriving from 'ParameterLoader' and calling 'super().load()' is what the book *meant* to do?) [...] (we could use composition and not derive from anything ... but that wouldn't be decoration?) [...] (chatgpt advises using composition not inheritance for decoration) ... (how do python '@myclass' official decorations do it?)
#   2023-04-04T20:58:19AEST use 'assert issubclass(v, FileLoader)' to verify we are using the correct interface since type hints are not enforced 
#   }}}

#   The nature of software projects is to change over time
#   Modifying classes comes with the danger of breaking some behaviour
#   In general, it is preferable to replace parts of an object rather than to change them

#   Service objects should be created all in one go, with all dependencies/configuration-value provided as ctor arguments

#   9.1) Introduce ctor arguments to make behaviour configurable
#   The prefered way to change the behaviour of a service should be to supply a different argument to the ctor

class FileLogger:
    def __init__(self, filePath):
        self.filePath = filePath
    def log(self, message):
        with open(filePath, 'a') as f:
            f.write(message)


#   9.2) Introduce ctor arguments to make behaviour replaceable

#   Example: behaviour of ParameterLoader can be configured by supplying different 'FileLoader' implementations to the ctor
class FileLoader(abc.ABC):
    def loadFile(filePath: str) -> Dict:
        raise NotImplementedError()

class JsonFileLoader(FileLoader):
    def loadFile(filePath: str) -> Dict:
        result = dict()
        #   ...
        return result

class XmlFileLoader(FileLoader):
    def loadFile(filePath: str) -> Dict:
        result = dict()
        #   ...
        return result

class ParameterLoader:
    def __init__(self, fileLoader: FileLoader):
        assert issubclass(fileLoader, FileLoader)
        self.fileLoader = fileLoader
    def load(self, filePath: str) -> Dict:
        if not os.path.isfile(filePath):
            raise FileNotFoundError(filePath)
        return self.fileLoader.loadFile(filePath)

#   9.3) Compose abstractions to achieve more complicated behaviour
#   <>

class SmartFileLoader(FileLoader):
    def new() -> SmartFileLoader:
        loaders = { 'json': JsonFileLoader, 'xml': XmlFileLoader, }
        return SmartFileLoader(loaders)
    def __init__(self, loaders):
        for (k,v) in loaders.items():
            assert issubclass(v, FileLoader)
            assert isinstance(k, str)
        self.loaders = loaders
    def loadFile(self, filePath: str) -> Dict:
        ext = os.path.splitext(filePath)[-1]
        if not ext in self.loaders.keys():
            raise Exception("ext=({ext}) not supported, supported=({self.loaders.keys()})")
        return self.loaders[ext].load(filePath)


#   9.4) Decorate existing behaviour
#   A decorator class wraps an existing class and extends/modifies its behaviour without requiring modification of the origional class

#   Example: replace certain values read by 'ParameterLoader'
class EnvParameterFileLoader(ParameterLoader):
    def __init__(self, fileLoader: FileLoader, envVar: Dict):
        self.envVar = envVar
        super().__init__(fileLoader)
    def load(self, filePath: str) -> Dict:
        params = super().load(filePath)
        self.updateParams(params)
        return params
    def updateParams(self, params):
        for (k,v) in params:
            if k in self.envVar.items():
                params[k] = self.envVar[k]

#   Example: cache results of 'ParameterLoader'
class CachedParameterLoader(ParameterLoader):
    def __init__(self, fileLoader: FileLoader):
        self.cache = dict()
        super().__init__(fileLoader)
    def load(self, filePath: str) -> Dict:
        if filePath in self.cache.keys():
            return self.cache[filePath]
        return super().load(filePath)


#   9.5) Use notification objects or event listeners for additional behaviour


#   9.6) Don't use inheritance to change an object's behaviour


#   9.7) Make classes as final be default

#   Python final class
#   {{{
#   }}}


#   9.8) Make methods and properties private by default


#   Summary


