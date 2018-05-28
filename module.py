# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:53:31 2017

@author: mustafa
"""
'''prepare the input for the interpreter and running it with that file as input instead.
 This is known as creating a script.
 
 You may also want to use a handy function that you’ve written in several programs 
 without copying its definition into each program.
 
To support this, Python has a way to put definitions in a file and use them in a script
 or in an interactive instance of the interpreter. Such a file is called a module; 
 definitions from a module can be imported into other modules or into the main module 
 (the collection of variables that you have access to in a script executed at the top level and in calculator mode).
 
 A module is a file containing Python definitions and statements. 
 The file name is the module name with the suffix .py appended.
 Within a module, the module’s name (as a string) is available as the value of the
 global variable __name__. For instance, use your favorite text editor to 
 create a file called fibo.py in the current directory with the following contents:'''
 
def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end = '')
        a, b = b, a+b
print ()

def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
        return result
    
import math
content = dir(math) #dir() returns a sorted list of string containing the names defined by a module
print (content)

#Standard Modules
'''Some modules are built into the interpreter; these provide access to operations
 that are not part of the core of the language but are nevertheless built in, 
 either for efficiency or to provide access to operating system primitives 
 such as system calls. The set of such modules is a configuration option which also
 depends on the underlying platform. For example, the winreg module is only provided
 on Windows systems. One particular module deserves some attention: sys, which is 
 built into every Python interpreter. The variables sys.ps1 and sys.ps2 define the
 strings used as primary and secondary prompts'''
 
import sys #These two variables are only defined if the interpreter is in interactive mode
sys.ps1
sys.ps2
sys.ps1 = 'C> '

''' The variable sys.path is a list of strings that determines the interpreter’s search
 path for modules. It is initialized to a default path taken from the environment 
 variable PYTHONPATH, or from a built-in default if PYTHONPATH is not set. 
 You can modify it using standard list operations:
     
import sys
sys.path.append('/ufs/guido/lib/python')'''

#packages
'''Packages are a way of structuring Python’s module namespace by using 
“dotted module names”. For example, the module name A.B designates a submodule named
 B in a package named A. Just like the use of modules saves the authors of different
 modules from having to worry about each other’s global variable names, the use of 
 dotted module names saves the authors of multi-module packages like NumPy or the 
 Python Imaging Library from having to worry about each other’s module names.'''

'''Suppose you want to design a collection of modules (a “package”) for the uniform 
handling of sound files and sound data. There are many different sound file formats 
(usually recognized by their extension, for example: .wav, .aiff, .au), so you may 
need to create and maintain a growing collection of modules for the conversion 
between the various file formats. There are also many different operations you 
might want to perform on sound data (such as mixing, adding echo, applying an equalizer 
function, creating an artificial stereo effect), so in addition you will be writing
 a never-ending stream of modules to perform these operations. Here’s a possible 
 structure for your package (expressed in terms of a hierarchical filesystem) '''
 
#sound/                          #Top-level package
      __init__.py               #Initialize the sound package
      formats/                  #Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  #Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  #Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
 
'''When importing the package, Python searches through the directories on sys.path 
looking for the package subdirectory.

The __init__.py files are required to make Python treat the directories as containing 
packages; this is done to prevent directories with a common name, such as string, 
from unintentionally hiding valid modules that occur later on the module search path. 
In the simplest case, __init__.py can just be an empty file, but it can also execute 
initialization code for the package or set the __all__ variable, described later.

Users of the package can import individual modules from the package, for example:'''
 
#import sound.effects.echo
 
 '''Note that when using from package import item, the item can be either a submodule
 (or subpackage) of the package, or some other name defined in the package, like a 
 function, class or variable. The import statement first tests whether the item is 
 defined in the package; if not, it assumes it is a module and attempts to load it.
 If it fails to find it, an ImportError exception is raised.

Contrarily, when using syntax like import item.subitem.subsubitem, each item except
 for the last must be a package; the last item can be a module or a package but can’t 
 be a class or function or variable defined in the previous item.'''
 
 #Importing * From a Package
'''Now what happens when the user writes from sound.effects import *? 
Ideally, one would hope that this somehow goes out to the filesystem, finds which 
submodules are present in the package, and imports them all. This could take a long 
time and importing sub-modules might have unwanted side-effects that should only 
happen when the sub-module is explicitly imported.
 
The only solution is for the package author to provide an explicit index of the 
package. The import statement uses the following convention: if a package’s 
__init__.py code defines a list named __all__, it is taken to be the list of module 
names that should be imported when from package import * is encountered. It is up 
to the package author to keep this list up-to-date when a new version of the package 
is released. Package authors may also decide not to support it, if they don’t see 
a use for importing * from their package. 
For example, the file sound/effects/__init__.py could contain the following code'''

#__all__ = ["echo", "surround", "reverse"]

'''This would mean that from sound.effects import * would import the three named 
submodules of the sound package.

If __all__ is not defined, the statement from sound.effects import * does not 
import all submodules from the package sound.effects into the current namespace; 
it only ensures that the package sound.effects has been imported 
(possibly running any initialization code in __init__.py) and then imports whatever 
names are defined in the package.'''

#Intra-package References
'''When packages are structured into subpackages (as with the sound package in the 
example), you can use absolute imports to refer to submodules of siblings packages.
For example, if the module sound.filters.vocoder needs to use the echo module in 
the sound.effects package, it can use from sound.effects import echo.

You can also write relative imports, with the from module import name form of 
import statement. These imports use leading dots to indicate the current and parent 
packages involved in the relative import. From the surround module for example, 
you might use
 
 from . import echo
 from .. import formats
 from ..filters import equalizer'''
 
#Packages in Multiple Directories
'''Packages support one more special attribute, __path__. This is initialized to 
be a list containing the name of the directory holding the package’s __init__.py 
before the code in that file is executed. This variable can be modified; doing so 
affects future searches for modules and subpackages contained in the package.

While this feature is not often needed, it can be used to extend the set of modules 
found in a package.'''
 
 
 
 
 
 
 
 
 
 
 
 
 
 