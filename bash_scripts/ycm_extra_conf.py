# This file is NOT licensed under the GPLv3, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core

# These are the compilation flags that will be used in case there's no
# compilation database set (by default, one is not set).
# CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
flags = [
'-Wall',
'-Wextra',
#'-Werror',
'-Wc++98-compat',
'-Wno-long-long',
'-Wno-variadic-macros',
'-fexceptions',
'-DNDEBUG',
# You 100% do NOT need -DUSE_CLANG_COMPLETER in your flags; only the YCM
# source code needs it.
'-DUSE_CLANG_COMPLETER',
# THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't know which
# language to use when compiling headers. So it will guess. Badly. So C++
# headers will be compiled as C headers. You don't want that so ALWAYS specify
# a "-std=<something>".
# For a C project, you would set this to something like 'c99' instead of
# 'c++11'.
'-std=c++11',
# ...and the same thing goes for the magic -x option which specifies the
# language that the files to be compiled are written in. This is mostly
# relevant for c++ headers.
# For a C project, you would set this to 'c' instead of 'c++'.
'-x',
'c++',
'-isystem',
'/usr/include',
'-isystem',
'/usr/local/include',
'-I/usr/local/Qt-5.3.1/include',
'-I/usr/local/Qt-5.3.1/include/QtNfc',
'-I/usr/local/Qt-5.3.1/include/QtNfc/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtNfc/5.3.1/QtNfc',
'-I/usr/local/Qt-5.3.1/include/QtNfc/5.3.1/QtNfc/private',
'-I/usr/local/Qt-5.3.1/include/QtCLucene',
'-I/usr/local/Qt-5.3.1/include/QtCLucene/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtCLucene/5.3.1/QtCLucene',
'-I/usr/local/Qt-5.3.1/include/QtCLucene/5.3.1/QtCLucene/private',
'-I/usr/local/Qt-5.3.1/include/QtPrintSupport',
'-I/usr/local/Qt-5.3.1/include/QtPrintSupport/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtPrintSupport/5.3.1/QtPrintSupport',
'-I/usr/local/Qt-5.3.1/include/QtPrintSupport/5.3.1/QtPrintSupport/private',
'-I/usr/local/Qt-5.3.1/include/QtPrintSupport/5.3.1/QtPrintSupport/qpa',
'-I/usr/local/Qt-5.3.1/include/QtQuick',
'-I/usr/local/Qt-5.3.1/include/QtQuick/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtQuick/5.3.1/QtQuick',
'-I/usr/local/Qt-5.3.1/include/QtQuick/5.3.1/QtQuick/private',
'-I/usr/local/Qt-5.3.1/include/QtQuick/5.3.0',
'-I/usr/local/Qt-5.3.1/include/QtQuick/5.3.0/QtQuick',
'-I/usr/local/Qt-5.3.1/include/QtQuick/5.3.0/QtQuick/private',
'-I/usr/local/Qt-5.3.1/include/QtSerialPort',
'-I/usr/local/Qt-5.3.1/include/QtSerialPort/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtSerialPort/5.3.1/QtSerialPort',
'-I/usr/local/Qt-5.3.1/include/QtSerialPort/5.3.1/QtSerialPort/private',
'-I/usr/local/Qt-5.3.1/include/QtSensors',
'-I/usr/local/Qt-5.3.1/include/QtSensors/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtSensors/5.3.1/QtSensors',
'-I/usr/local/Qt-5.3.1/include/QtSensors/5.3.1/QtSensors/private',
'-I/usr/local/Qt-5.3.1/include/QtWidgets',
'-I/usr/local/Qt-5.3.1/include/QtWidgets/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtWidgets/5.3.1/QtWidgets',
'-I/usr/local/Qt-5.3.1/include/QtWidgets/5.3.1/QtWidgets/private',
'-I/usr/local/Qt-5.3.1/include/QtBluetooth',
'-I/usr/local/Qt-5.3.1/include/QtBluetooth/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtBluetooth/5.3.1/QtBluetooth',
'-I/usr/local/Qt-5.3.1/include/QtBluetooth/5.3.1/QtBluetooth/private',
'-I/usr/local/Qt-5.3.1/include/QtSvg',
'-I/usr/local/Qt-5.3.1/include/QtSvg/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtSvg/5.3.1/QtSvg',
'-I/usr/local/Qt-5.3.1/include/QtSvg/5.3.1/QtSvg/private',
'-I/usr/local/Qt-5.3.1/include/QtDesigner',
'-I/usr/local/Qt-5.3.1/include/QtDesigner/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtDesigner/5.3.1/QtDesigner',
'-I/usr/local/Qt-5.3.1/include/QtDesigner/5.3.1/QtDesigner/private',
'-I/usr/local/Qt-5.3.1/include/QtWebKitWidgets',
'-I/usr/local/Qt-5.3.1/include/QtWebKitWidgets/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtWebKitWidgets/5.3.1/QtWebKitWidgets',
'-I/usr/local/Qt-5.3.1/include/QtWebKitWidgets/5.3.1/QtWebKitWidgets/private',
'-I/usr/local/Qt-5.3.1/include/QtNetwork',
'-I/usr/local/Qt-5.3.1/include/QtNetwork/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtNetwork/5.3.1/QtNetwork',
'-I/usr/local/Qt-5.3.1/include/QtNetwork/5.3.1/QtNetwork/private',
'-I/usr/local/Qt-5.3.1/include/QtSql',
'-I/usr/local/Qt-5.3.1/include/QtSql/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtSql/5.3.1/QtSql',
'-I/usr/local/Qt-5.3.1/include/QtSql/5.3.1/QtSql/private',
'-I/usr/local/Qt-5.3.1/include/QtTest',
'-I/usr/local/Qt-5.3.1/include/QtTest/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtTest/5.3.1/QtTest',
'-I/usr/local/Qt-5.3.1/include/QtTest/5.3.1/QtTest/private',
'-I/usr/local/Qt-5.3.1/include/QtGui',
'-I/usr/local/Qt-5.3.1/include/QtGui/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtGui/5.3.1/QtGui',
'-I/usr/local/Qt-5.3.1/include/QtGui/5.3.1/QtGui/private',
'-I/usr/local/Qt-5.3.1/include/QtGui/5.3.1/QtGui/qpa',
'-I/usr/local/Qt-5.3.1/include/QtX11Extras',
'-I/usr/local/Qt-5.3.1/include/QtDBus',
'-I/usr/local/Qt-5.3.1/include/QtDBus/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtDBus/5.3.1/QtDBus',
'-I/usr/local/Qt-5.3.1/include/QtDBus/5.3.1/QtDBus/private',
'-I/usr/local/Qt-5.3.1/include/QtOpenGLExtensions',
'-I/usr/local/Qt-5.3.1/include/QtConcurrent',
'-I/usr/local/Qt-5.3.1/include/QtDocGallery',
'-I/usr/local/Qt-5.3.1/include/QtDocGallery/5.0.0',
'-I/usr/local/Qt-5.3.1/include/QtDocGallery/5.0.0/QtDocGallery',
'-I/usr/local/Qt-5.3.1/include/QtDocGallery/5.0.0/QtDocGallery/private',
'-I/usr/local/Qt-5.3.1/include/QtMultimedia',
'-I/usr/local/Qt-5.3.1/include/QtMultimedia/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtMultimedia/5.3.1/QtMultimedia',
'-I/usr/local/Qt-5.3.1/include/QtMultimedia/5.3.1/QtMultimedia/private',
'-I/usr/local/Qt-5.3.1/include/QtOpenGL',
'-I/usr/local/Qt-5.3.1/include/QtOpenGL/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtOpenGL/5.3.1/QtOpenGL',
'-I/usr/local/Qt-5.3.1/include/QtOpenGL/5.3.1/QtOpenGL/private',
'-I/usr/local/Qt-5.3.1/include/QtXml',
'-I/usr/local/Qt-5.3.1/include/QtMultimediaWidgets',
'-I/usr/local/Qt-5.3.1/include/QtMultimediaWidgets/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtMultimediaWidgets/5.3.1/QtMultimediaWidgets',
'-I/usr/local/Qt-5.3.1/include/QtMultimediaWidgets/5.3.1/QtMultimediaWidgets/private',
'-I/usr/local/Qt-5.3.1/include/QtCore',
'-I/usr/local/Qt-5.3.1/include/QtCore/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtCore/5.3.1/QtCore',
'-I/usr/local/Qt-5.3.1/include/QtCore/5.3.1/QtCore/private',
'-I/usr/local/Qt-5.3.1/include/QtScript',
'-I/usr/local/Qt-5.3.1/include/QtScript/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtScript/5.3.1/QtScript',
'-I/usr/local/Qt-5.3.1/include/QtScript/5.3.1/QtScript/private',
'-I/usr/local/Qt-5.3.1/include/QtDesignerComponents',
'-I/usr/local/Qt-5.3.1/include/QtDesignerComponents/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtDesignerComponents/5.3.1/QtDesignerComponents',
'-I/usr/local/Qt-5.3.1/include/QtDesignerComponents/5.3.1/QtDesignerComponents/private',
'-I/usr/local/Qt-5.3.1/include/QtUiTools',
'-I/usr/local/Qt-5.3.1/include/QtUiTools/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtUiTools/5.3.1/QtUiTools',
'-I/usr/local/Qt-5.3.1/include/QtUiTools/5.3.1/QtUiTools/private',
'-I/usr/local/Qt-5.3.1/include/QtXmlPatterns',
'-I/usr/local/Qt-5.3.1/include/QtXmlPatterns/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtXmlPatterns/5.3.1/QtXmlPatterns',
'-I/usr/local/Qt-5.3.1/include/QtXmlPatterns/5.3.1/QtXmlPatterns/private',
'-I/usr/local/Qt-5.3.1/include/QtWebSockets',
'-I/usr/local/Qt-5.3.1/include/QtWebSockets/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtWebSockets/5.3.1/QtWebSockets',
'-I/usr/local/Qt-5.3.1/include/QtWebSockets/5.3.1/QtWebSockets/private',
'-I/usr/local/Qt-5.3.1/include/QtQuickWidgets',
'-I/usr/local/Qt-5.3.1/include/QtQuickWidgets/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtQuickWidgets/5.3.1/QtQuickWidgets',
'-I/usr/local/Qt-5.3.1/include/QtQuickWidgets/5.3.1/QtQuickWidgets/private',
'-I/usr/local/Qt-5.3.1/include/QtQuickWidgets/5.3.0',
'-I/usr/local/Qt-5.3.1/include/QtQuickWidgets/5.3.0/QtQuickWidgets',
'-I/usr/local/Qt-5.3.1/include/QtQuickWidgets/5.3.0/QtQuickWidgets/private',
'-I/usr/local/Qt-5.3.1/include/QtScriptTools',
'-I/usr/local/Qt-5.3.1/include/QtScriptTools/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtScriptTools/5.3.1/QtScriptTools',
'-I/usr/local/Qt-5.3.1/include/QtScriptTools/5.3.1/QtScriptTools/private',
'-I/usr/local/Qt-5.3.1/include/QtQuickParticles',
'-I/usr/local/Qt-5.3.1/include/QtQuickParticles/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtQuickParticles/5.3.1/QtQuickParticles',
'-I/usr/local/Qt-5.3.1/include/QtQuickParticles/5.3.1/QtQuickParticles/private',
'-I/usr/local/Qt-5.3.1/include/QtQuickParticles/5.3.0',
'-I/usr/local/Qt-5.3.1/include/QtQuickParticles/5.3.0/QtQuickParticles',
'-I/usr/local/Qt-5.3.1/include/QtQuickParticles/5.3.0/QtQuickParticles/private',
'-I/usr/local/Qt-5.3.1/include/QtQuickTest',
'-I/usr/local/Qt-5.3.1/include/QtQuickTest/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtQuickTest/5.3.1/QtQuickTest',
'-I/usr/local/Qt-5.3.1/include/QtQuickTest/5.3.1/QtQuickTest/private',
'-I/usr/local/Qt-5.3.1/include/QtQuickTest/5.3.0',
'-I/usr/local/Qt-5.3.1/include/QtQuickTest/5.3.0/QtQuickTest',
'-I/usr/local/Qt-5.3.1/include/QtQuickTest/5.3.0/QtQuickTest/private',
'-I/usr/local/Qt-5.3.1/include/QtMultimediaQuick_p',
'-I/usr/local/Qt-5.3.1/include/QtMultimediaQuick_p/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtMultimediaQuick_p/5.3.1/QtMultimediaQuick_p',
'-I/usr/local/Qt-5.3.1/include/QtMultimediaQuick_p/5.3.1/QtMultimediaQuick_p/private',
'-I/usr/local/Qt-5.3.1/include/QtQml',
'-I/usr/local/Qt-5.3.1/include/QtQml/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtQml/5.3.1/QtQml',
'-I/usr/local/Qt-5.3.1/include/QtQml/5.3.1/QtQml/private',
'-I/usr/local/Qt-5.3.1/include/QtQml/5.3.0',
'-I/usr/local/Qt-5.3.1/include/QtQml/5.3.0/QtQml',
'-I/usr/local/Qt-5.3.1/include/QtQml/5.3.0/QtQml/private',
'-I/usr/local/Qt-5.3.1/include/QtWebKit',
'-I/usr/local/Qt-5.3.1/include/QtWebKit/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtWebKit/5.3.1/QtWebKit',
'-I/usr/local/Qt-5.3.1/include/QtWebKit/5.3.1/QtWebKit/private',
'-I/usr/local/Qt-5.3.1/include/QtWebKit/5.3.0',
'-I/usr/local/Qt-5.3.1/include/QtWebKit/5.3.0/QtWebKit',
'-I/usr/local/Qt-5.3.1/include/QtWebKit/5.3.0/QtWebKit/private',
'-I/usr/local/Qt-5.3.1/include/QtPlatformSupport',
'-I/usr/local/Qt-5.3.1/include/QtPlatformSupport/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtPlatformSupport/5.3.1/QtPlatformSupport',
'-I/usr/local/Qt-5.3.1/include/QtPlatformSupport/5.3.1/QtPlatformSupport/private',
'-I/usr/local/Qt-5.3.1/include/QtPositioning',
'-I/usr/local/Qt-5.3.1/include/QtPositioning/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtPositioning/5.3.1/QtPositioning',
'-I/usr/local/Qt-5.3.1/include/QtPositioning/5.3.1/QtPositioning/private',
'-I/usr/local/Qt-5.3.1/include/QtDeclarative',
'-I/usr/local/Qt-5.3.1/include/QtDeclarative/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtDeclarative/5.3.1/QtDeclarative',
'-I/usr/local/Qt-5.3.1/include/QtDeclarative/5.3.1/QtDeclarative/private',
'-I/usr/local/Qt-5.3.1/include/QtHelp',
'-I/usr/local/Qt-5.3.1/include/QtHelp/5.3.1',
'-I/usr/local/Qt-5.3.1/include/QtHelp/5.3.1/QtHelp',
'-I/usr/local/Qt-5.3.1/include/QtHelp/5.3.1/QtHelp/private',
]


# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# You can get CMake to generate this file for you by adding:
#   set( CMAKE_EXPORT_COMPILE_COMMANDS 1 )
# to your CMakeLists.txt file.
#
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.
compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.h', '.hxx', '.hpp', '.hh' ]


def GetCompilationInfoForFile( filename ):
  # The compilation_commands.json file generated by CMake does not have entries
  # for header files. So we do our best by asking the db for flags for a
  # corresponding source file, if any. If one exists, the flags for that file
  # should be good enough.
  if IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        compilation_info = database.GetCompilationInfoForFile(
          replacement_file )
        if compilation_info.compiler_flags_:
          return compilation_info
    return None
  return database.GetCompilationInfoForFile( filename )


def FlagsForFile( filename, **kwargs ):
  if database:
    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object
    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )

    # NOTE: This is just for YouCompleteMe; it's highly likely that your project
    # does NOT need to remove the stdlib flag. DO NOT USE THIS IN YOUR
    # ycm_extra_conf IF YOU'RE NOT 100% SURE YOU NEED IT.
    try:
      final_flags.remove( '-stdlib=libc++' )
    except ValueError:
      pass
  else:
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }
