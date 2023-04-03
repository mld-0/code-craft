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
        self.loaders = loaders
    def loadFile(filePath: str) -> Dict:
        ext = os.path.splitext(filePath)[-1]
        if not ext in self.loaders.keys():
            raise Exception("ext=({ext}) not supported, supported=({self.loaders.keys()})")
        return self.loaders[ext].load(filePath)


#   9.4) Decorate existing behaviour


#   9.5) Use notification objects or event listeners for additional behaviour


#   9.6) Don't use inheritance to change an object's behaviour


#   9.7) Make classes as final be default

#   Python final class
#   {{{
#   }}}


#   9.8) Make methods and properties private by default


#   Summary


