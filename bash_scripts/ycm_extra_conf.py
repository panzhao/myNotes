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
'-I/usr/local/Qt-5.5.1/include',
'-I/usr/local/Qt-5.5.1/include/QtNfc',
'-I/usr/local/Qt-5.5.1/include/QtNfc/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtNfc/5.5.1/QtNfc',
'-I/usr/local/Qt-5.5.1/include/QtNfc/5.5.1/QtNfc/private',
'-I/usr/local/Qt-5.5.1/include/QtCLucene',
'-I/usr/local/Qt-5.5.1/include/QtCLucene/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtCLucene/5.5.1/QtCLucene',
'-I/usr/local/Qt-5.5.1/include/QtCLucene/5.5.1/QtCLucene/private',
'-I/usr/local/Qt-5.5.1/include/QtPrintSupport',
'-I/usr/local/Qt-5.5.1/include/QtPrintSupport/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtPrintSupport/5.5.1/QtPrintSupport',
'-I/usr/local/Qt-5.5.1/include/QtPrintSupport/5.5.1/QtPrintSupport/private',
'-I/usr/local/Qt-5.5.1/include/QtPrintSupport/5.5.1/QtPrintSupport/qpa',
'-I/usr/local/Qt-5.5.1/include/QtQuick',
'-I/usr/local/Qt-5.5.1/include/QtQuick/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtQuick/5.5.1/QtQuick',
'-I/usr/local/Qt-5.5.1/include/QtQuick/5.5.1/QtQuick/private',
'-I/usr/local/Qt-5.5.1/include/QtQuick/5.3.0',
'-I/usr/local/Qt-5.5.1/include/QtQuick/5.3.0/QtQuick',
'-I/usr/local/Qt-5.5.1/include/QtQuick/5.3.0/QtQuick/private',
'-I/usr/local/Qt-5.5.1/include/QtSerialPort',
'-I/usr/local/Qt-5.5.1/include/QtSerialPort/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtSerialPort/5.5.1/QtSerialPort',
'-I/usr/local/Qt-5.5.1/include/QtSerialPort/5.5.1/QtSerialPort/private',
'-I/usr/local/Qt-5.5.1/include/QtSensors',
'-I/usr/local/Qt-5.5.1/include/QtSensors/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtSensors/5.5.1/QtSensors',
'-I/usr/local/Qt-5.5.1/include/QtSensors/5.5.1/QtSensors/private',
'-I/usr/local/Qt-5.5.1/include/QtWidgets',
'-I/usr/local/Qt-5.5.1/include/QtWidgets/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtWidgets/5.5.1/QtWidgets',
'-I/usr/local/Qt-5.5.1/include/QtWidgets/5.5.1/QtWidgets/private',
'-I/usr/local/Qt-5.5.1/include/QtBluetooth',
'-I/usr/local/Qt-5.5.1/include/QtBluetooth/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtBluetooth/5.5.1/QtBluetooth',
'-I/usr/local/Qt-5.5.1/include/QtBluetooth/5.5.1/QtBluetooth/private',
'-I/usr/local/Qt-5.5.1/include/QtSvg',
'-I/usr/local/Qt-5.5.1/include/QtSvg/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtSvg/5.5.1/QtSvg',
'-I/usr/local/Qt-5.5.1/include/QtSvg/5.5.1/QtSvg/private',
'-I/usr/local/Qt-5.5.1/include/QtDesigner',
'-I/usr/local/Qt-5.5.1/include/QtDesigner/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtDesigner/5.5.1/QtDesigner',
'-I/usr/local/Qt-5.5.1/include/QtDesigner/5.5.1/QtDesigner/private',
'-I/usr/local/Qt-5.5.1/include/QtWebKitWidgets',
'-I/usr/local/Qt-5.5.1/include/QtWebKitWidgets/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtWebKitWidgets/5.5.1/QtWebKitWidgets',
'-I/usr/local/Qt-5.5.1/include/QtWebKitWidgets/5.5.1/QtWebKitWidgets/private',
'-I/usr/local/Qt-5.5.1/include/QtNetwork',
'-I/usr/local/Qt-5.5.1/include/QtNetwork/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtNetwork/5.5.1/QtNetwork',
'-I/usr/local/Qt-5.5.1/include/QtNetwork/5.5.1/QtNetwork/private',
'-I/usr/local/Qt-5.5.1/include/QtSql',
'-I/usr/local/Qt-5.5.1/include/QtSql/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtSql/5.5.1/QtSql',
'-I/usr/local/Qt-5.5.1/include/QtSql/5.5.1/QtSql/private',
'-I/usr/local/Qt-5.5.1/include/QtTest',
'-I/usr/local/Qt-5.5.1/include/QtTest/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtTest/5.5.1/QtTest',
'-I/usr/local/Qt-5.5.1/include/QtTest/5.5.1/QtTest/private',
'-I/usr/local/Qt-5.5.1/include/QtGui',
'-I/usr/local/Qt-5.5.1/include/QtGui/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtGui/5.5.1/QtGui',
'-I/usr/local/Qt-5.5.1/include/QtGui/5.5.1/QtGui/private',
'-I/usr/local/Qt-5.5.1/include/QtGui/5.5.1/QtGui/qpa',
'-I/usr/local/Qt-5.5.1/include/QtX11Extras',
'-I/usr/local/Qt-5.5.1/include/QtDBus',
'-I/usr/local/Qt-5.5.1/include/QtDBus/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtDBus/5.5.1/QtDBus',
'-I/usr/local/Qt-5.5.1/include/QtDBus/5.5.1/QtDBus/private',
'-I/usr/local/Qt-5.5.1/include/QtOpenGLExtensions',
'-I/usr/local/Qt-5.5.1/include/QtConcurrent',
'-I/usr/local/Qt-5.5.1/include/QtDocGallery',
'-I/usr/local/Qt-5.5.1/include/QtDocGallery/5.0.0',
'-I/usr/local/Qt-5.5.1/include/QtDocGallery/5.0.0/QtDocGallery',
'-I/usr/local/Qt-5.5.1/include/QtDocGallery/5.0.0/QtDocGallery/private',
'-I/usr/local/Qt-5.5.1/include/QtMultimedia',
'-I/usr/local/Qt-5.5.1/include/QtMultimedia/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtMultimedia/5.5.1/QtMultimedia',
'-I/usr/local/Qt-5.5.1/include/QtMultimedia/5.5.1/QtMultimedia/private',
'-I/usr/local/Qt-5.5.1/include/QtOpenGL',
'-I/usr/local/Qt-5.5.1/include/QtOpenGL/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtOpenGL/5.5.1/QtOpenGL',
'-I/usr/local/Qt-5.5.1/include/QtOpenGL/5.5.1/QtOpenGL/private',
'-I/usr/local/Qt-5.5.1/include/QtXml',
'-I/usr/local/Qt-5.5.1/include/QtMultimediaWidgets',
'-I/usr/local/Qt-5.5.1/include/QtMultimediaWidgets/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtMultimediaWidgets/5.5.1/QtMultimediaWidgets',
'-I/usr/local/Qt-5.5.1/include/QtMultimediaWidgets/5.5.1/QtMultimediaWidgets/private',
'-I/usr/local/Qt-5.5.1/include/QtCore',
'-I/usr/local/Qt-5.5.1/include/QtCore/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtCore/5.5.1/QtCore',
'-I/usr/local/Qt-5.5.1/include/QtCore/5.5.1/QtCore/private',
'-I/usr/local/Qt-5.5.1/include/QtScript',
'-I/usr/local/Qt-5.5.1/include/QtScript/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtScript/5.5.1/QtScript',
'-I/usr/local/Qt-5.5.1/include/QtScript/5.5.1/QtScript/private',
'-I/usr/local/Qt-5.5.1/include/QtDesignerComponents',
'-I/usr/local/Qt-5.5.1/include/QtDesignerComponents/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtDesignerComponents/5.5.1/QtDesignerComponents',
'-I/usr/local/Qt-5.5.1/include/QtDesignerComponents/5.5.1/QtDesignerComponents/private',
'-I/usr/local/Qt-5.5.1/include/QtUiTools',
'-I/usr/local/Qt-5.5.1/include/QtUiTools/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtUiTools/5.5.1/QtUiTools',
'-I/usr/local/Qt-5.5.1/include/QtUiTools/5.5.1/QtUiTools/private',
'-I/usr/local/Qt-5.5.1/include/QtXmlPatterns',
'-I/usr/local/Qt-5.5.1/include/QtXmlPatterns/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtXmlPatterns/5.5.1/QtXmlPatterns',
'-I/usr/local/Qt-5.5.1/include/QtXmlPatterns/5.5.1/QtXmlPatterns/private',
'-I/usr/local/Qt-5.5.1/include/QtWebSockets',
'-I/usr/local/Qt-5.5.1/include/QtWebSockets/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtWebSockets/5.5.1/QtWebSockets',
'-I/usr/local/Qt-5.5.1/include/QtWebSockets/5.5.1/QtWebSockets/private',
'-I/usr/local/Qt-5.5.1/include/QtQuickWidgets',
'-I/usr/local/Qt-5.5.1/include/QtQuickWidgets/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtQuickWidgets/5.5.1/QtQuickWidgets',
'-I/usr/local/Qt-5.5.1/include/QtQuickWidgets/5.5.1/QtQuickWidgets/private',
'-I/usr/local/Qt-5.5.1/include/QtQuickWidgets/5.3.0',
'-I/usr/local/Qt-5.5.1/include/QtQuickWidgets/5.3.0/QtQuickWidgets',
'-I/usr/local/Qt-5.5.1/include/QtQuickWidgets/5.3.0/QtQuickWidgets/private',
'-I/usr/local/Qt-5.5.1/include/QtScriptTools',
'-I/usr/local/Qt-5.5.1/include/QtScriptTools/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtScriptTools/5.5.1/QtScriptTools',
'-I/usr/local/Qt-5.5.1/include/QtScriptTools/5.5.1/QtScriptTools/private',
'-I/usr/local/Qt-5.5.1/include/QtQuickParticles',
'-I/usr/local/Qt-5.5.1/include/QtQuickParticles/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtQuickParticles/5.5.1/QtQuickParticles',
'-I/usr/local/Qt-5.5.1/include/QtQuickParticles/5.5.1/QtQuickParticles/private',
'-I/usr/local/Qt-5.5.1/include/QtQuickParticles/5.3.0',
'-I/usr/local/Qt-5.5.1/include/QtQuickParticles/5.3.0/QtQuickParticles',
'-I/usr/local/Qt-5.5.1/include/QtQuickParticles/5.3.0/QtQuickParticles/private',
'-I/usr/local/Qt-5.5.1/include/QtQuickTest',
'-I/usr/local/Qt-5.5.1/include/QtQuickTest/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtQuickTest/5.5.1/QtQuickTest',
'-I/usr/local/Qt-5.5.1/include/QtQuickTest/5.5.1/QtQuickTest/private',
'-I/usr/local/Qt-5.5.1/include/QtQuickTest/5.3.0',
'-I/usr/local/Qt-5.5.1/include/QtQuickTest/5.3.0/QtQuickTest',
'-I/usr/local/Qt-5.5.1/include/QtQuickTest/5.3.0/QtQuickTest/private',
'-I/usr/local/Qt-5.5.1/include/QtMultimediaQuick_p',
'-I/usr/local/Qt-5.5.1/include/QtMultimediaQuick_p/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtMultimediaQuick_p/5.5.1/QtMultimediaQuick_p',
'-I/usr/local/Qt-5.5.1/include/QtMultimediaQuick_p/5.5.1/QtMultimediaQuick_p/private',
'-I/usr/local/Qt-5.5.1/include/QtQml',
'-I/usr/local/Qt-5.5.1/include/QtQml/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtQml/5.5.1/QtQml',
'-I/usr/local/Qt-5.5.1/include/QtQml/5.5.1/QtQml/private',
'-I/usr/local/Qt-5.5.1/include/QtQml/5.3.0',
'-I/usr/local/Qt-5.5.1/include/QtQml/5.3.0/QtQml',
'-I/usr/local/Qt-5.5.1/include/QtQml/5.3.0/QtQml/private',
'-I/usr/local/Qt-5.5.1/include/QtWebKit',
'-I/usr/local/Qt-5.5.1/include/QtWebKit/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtWebKit/5.5.1/QtWebKit',
'-I/usr/local/Qt-5.5.1/include/QtWebKit/5.5.1/QtWebKit/private',
'-I/usr/local/Qt-5.5.1/include/QtWebKit/5.3.0',
'-I/usr/local/Qt-5.5.1/include/QtWebKit/5.3.0/QtWebKit',
'-I/usr/local/Qt-5.5.1/include/QtWebKit/5.3.0/QtWebKit/private',
'-I/usr/local/Qt-5.5.1/include/QtPlatformSupport',
'-I/usr/local/Qt-5.5.1/include/QtPlatformSupport/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtPlatformSupport/5.5.1/QtPlatformSupport',
'-I/usr/local/Qt-5.5.1/include/QtPlatformSupport/5.5.1/QtPlatformSupport/private',
'-I/usr/local/Qt-5.5.1/include/QtPositioning',
'-I/usr/local/Qt-5.5.1/include/QtPositioning/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtPositioning/5.5.1/QtPositioning',
'-I/usr/local/Qt-5.5.1/include/QtPositioning/5.5.1/QtPositioning/private',
'-I/usr/local/Qt-5.5.1/include/QtDeclarative',
'-I/usr/local/Qt-5.5.1/include/QtDeclarative/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtDeclarative/5.5.1/QtDeclarative',
'-I/usr/local/Qt-5.5.1/include/QtDeclarative/5.5.1/QtDeclarative/private',
'-I/usr/local/Qt-5.5.1/include/QtHelp',
'-I/usr/local/Qt-5.5.1/include/QtHelp/5.5.1',
'-I/usr/local/Qt-5.5.1/include/QtHelp/5.5.1/QtHelp',
'-I/usr/local/Qt-5.5.1/include/QtHelp/5.5.1/QtHelp/private',
"-I/usr/include",
"-I/usr/include/libpng12",
"-I/usr/include/KHR",
"-I/usr/include/video",
"-I/usr/include/libxslt",
"-I/usr/include/gtk-unix-print-2.0",
"-I/usr/include/gtk-unix-print-2.0/gtk",
"-I/usr/include/p11-kit-1",
"-I/usr/include/p11-kit-1/p11-kit",
"-I/usr/include/gssapi",
"-I/usr/include/fcitx",
"-I/usr/include/fcitx/module",
"-I/usr/include/fcitx/module/autoeng-ng",
"-I/usr/include/fcitx/module/punc-ng",
"-I/usr/include/gnutls",
"-I/usr/include/netax25",
"-I/usr/include/netatalk",
"-I/usr/include/layout",
"-I/usr/include/netash",
"-I/usr/include/cmos",
"-I/usr/include/cmos/packagemanager-qt5",
"-I/usr/include/pci",
"-I/usr/include/netiucv",
"-I/usr/include/gtk-2.0",
"-I/usr/include/gtk-2.0/gdk",
"-I/usr/include/gtk-2.0/gtk",
"-I/usr/include/net",
"-I/usr/include/netpacket",
"-I/usr/include/python2.7",
"-I/usr/include/pixman-1",
"-I/usr/include/c++",
"-I/usr/include/c++/4.6",
"-I/usr/include/c++/4.6/backward",
"-I/usr/include/c++/4.6/decimal",
"-I/usr/include/c++/4.6/tr1",
"-I/usr/include/c++/4.6/parallel",
"-I/usr/include/c++/4.6/ext",
"-I/usr/include/c++/4.6/ext/pb_ds",
"-I/usr/include/c++/4.6/ext/pb_ds/detail",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/bin_search_tree_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/eq_fn",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/binomial_heap_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/thin_heap_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/gp_hash_table_map_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/list_update_map_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/left_child_next_sibling_heap_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/cc_hash_table_map_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/hash_fn",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/resize_policy",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/unordered_iterator",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/basic_tree_policy",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/pat_trie_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/rc_binomial_heap_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/binary_heap_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/splay_tree_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/trie_policy",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/tree_policy",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/binomial_heap_base_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/list_update_policy",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/pairing_heap_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/ov_tree_map_",
"-I/usr/include/c++/4.6/ext/pb_ds/detail/rb_tree_map_",
"-I/usr/include/c++/4.6/profile",
"-I/usr/include/c++/4.6/profile/impl",
"-I/usr/include/c++/4.6/debug",
"-I/usr/include/c++/4.6/x86_64-linux-gnu",
"-I/usr/include/c++/4.6/x86_64-linux-gnu/32",
"-I/usr/include/c++/4.6/x86_64-linux-gnu/32/bits",
"-I/usr/include/c++/4.6/x86_64-linux-gnu/bits",
"-I/usr/include/c++/4.6/bits",
"-I/usr/include/gstreamer-0.10",
"-I/usr/include/gstreamer-0.10/gst",
"-I/usr/include/GLES2",
"-I/usr/include/unistring",
"-I/usr/include/krb5",
"-I/usr/include/dbus-1.0",
"-I/usr/include/dbus-1.0/dbus",
"-I/usr/include/clang",
"-I/usr/include/clang/3.0",
"-I/usr/include/clang/3.0/include",
"-I/usr/include/exempi-2.0",
"-I/usr/include/exempi-2.0/exempi",
"-I/usr/include/nautilus-sendto",
"-I/usr/include/gdk-pixbuf-2.0",
"-I/usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib",
"-I/usr/include/gdk-pixbuf-2.0/gdk-pixbuf",
"-I/usr/include/alsa",
"-I/usr/include/alsa/sound",
"-I/usr/include/nouveau",
"-I/usr/include/nspr",
"-I/usr/include/nspr/obsolete",
"-I/usr/include/nspr/private",
"-I/usr/include/nspr/md",
"-I/usr/include/unicode",
"-I/usr/include/netinet",
"-I/usr/include/uuid",
"-I/usr/include/libxml2",
"-I/usr/include/libxml2/libxml",
"-I/usr/include/drm",
"-I/usr/include/kadm5",
"-I/usr/include/nss",
"-I/usr/include/rdma",
"-I/usr/include/pango-1.0",
"-I/usr/include/pango-1.0/pango",
"-I/usr/include/gio-unix-2.0",
"-I/usr/include/gio-unix-2.0/gio",
"-I/usr/include/cups",
"-I/usr/include/cups/i18n.h",
"-I/usr/include/neteconet",
"-I/usr/include/sys",
"-I/usr/include/mm",
"-I/usr/include/libiptcdata",
"-I/usr/include/avahi-client",
"-I/usr/include/xcb",
"-I/usr/include/mtd",
"-I/usr/include/sound",
"-I/usr/include/xorg",
"-I/usr/include/openssl",
"-I/usr/include/gobject-introspection-1.0",
"-I/usr/include/libsoup-2.4",
"-I/usr/include/libsoup-2.4/libsoup",
"-I/usr/include/nfs",
"-I/usr/include/fontconfig",
"-I/usr/include/GL",
"-I/usr/include/GL/internal",
"-I/usr/include/libdrm",
"-I/usr/include/glib-2.0",
"-I/usr/include/glib-2.0/gio",
"-I/usr/include/glib-2.0/gobject",
"-I/usr/include/glib-2.0/glib",
"-I/usr/include/glib-2.0/glib/deprecated",
"-I/usr/include/rpcsvc",
"-I/usr/include/netrose",
"-I/usr/include/libexif",
"-I/usr/include/GLES",
"-I/usr/include/atk-1.0",
"-I/usr/include/atk-1.0/atk",
"-I/usr/include/gudev-1.0",
"-I/usr/include/gudev-1.0/gudev",
"-I/usr/include/libltdl",
"-I/usr/include/protocols",
"-I/usr/include/pulse",
"-I/usr/include/bsd",
"-I/usr/include/bsd/netinet",
"-I/usr/include/bsd/sys",
"-I/usr/include/linux",
"-I/usr/include/linux/netfilter_arp",
"-I/usr/include/linux/netfilter_ipv4",
"-I/usr/include/linux/spi",
"-I/usr/include/linux/netfilter",
"-I/usr/include/linux/netfilter/ipset",
"-I/usr/include/linux/byteorder",
"-I/usr/include/linux/mmc",
"-I/usr/include/linux/tc_act",
"-I/usr/include/linux/isdn",
"-I/usr/include/linux/wimax",
"-I/usr/include/linux/hdlc",
"-I/usr/include/linux/netfilter_bridge",
"-I/usr/include/linux/raid",
"-I/usr/include/linux/caif",
"-I/usr/include/linux/sunrpc",
"-I/usr/include/linux/netfilter_ipv6",
"-I/usr/include/linux/tc_ematch",
"-I/usr/include/linux/nfsd",
"-I/usr/include/linux/dvb",
"-I/usr/include/linux/can",
"-I/usr/include/linux/usb",
"-I/usr/include/rpc",
"-I/usr/include/et",
"-I/usr/include/libexslt",
"-I/usr/include/gssrpc",
"-I/usr/include/qt4",
"-I/usr/include/qt4/QtSvg",
"-I/usr/include/qt4/QtDesigner",
"-I/usr/include/qt4/QtNetwork",
"-I/usr/include/qt4/QtSql",
"-I/usr/include/qt4/QtTest",
"-I/usr/include/qt4/QtGui",
"-I/usr/include/qt4/QtDBus",
"-I/usr/include/qt4/Qt3Support",
"-I/usr/include/qt4/QtOpenGL",
"-I/usr/include/qt4/QtXml",
"-I/usr/include/qt4/QtCore",
"-I/usr/include/qt4/QtScript",
"-I/usr/include/qt4/QtUiTools",
"-I/usr/include/qt4/Qt",
"-I/usr/include/qt4/QtXmlPatterns",
"-I/usr/include/qt4/QtScriptTools",
"-I/usr/include/qt4/QtWebKit",
"-I/usr/include/qt4/QtDeclarative",
"-I/usr/include/qt4/QtHelp",
"-I/usr/include/scsi",
"-I/usr/include/x86_64-linux-gnu",
"-I/usr/include/x86_64-linux-gnu/gnu",
"-I/usr/include/x86_64-linux-gnu/sys",
"-I/usr/include/x86_64-linux-gnu/asm",
"-I/usr/include/x86_64-linux-gnu/bits",
"-I/usr/include/X11",
"-I/usr/include/X11/dri",
"-I/usr/include/X11/Xft",
"-I/usr/include/X11/Xtrans",
"-I/usr/include/X11/ICE",
"-I/usr/include/X11/Xcursor",
"-I/usr/include/X11/fonts",
"-I/usr/include/X11/SM",
"-I/usr/include/X11/extensions",
"-I/usr/include/X11/bitmaps",
"-I/usr/include/arpa",
"-I/usr/include/cairo",
"-I/usr/include/netipx",
"-I/usr/include/crypto++",
"-I/usr/include/asm-generic",
"-I/usr/include/xen",
"-I/usr/include/EGL",
"-I/usr/include/phonon",
"-I/usr/include/phonon/Phonon",
"-I/usr/include/netrom",
"-I/usr/include/avahi-common",
"-I/usr/include/mit-krb5",
"-I/usr/include/mit-krb5/gssapi",
"-I/usr/include/mit-krb5/krb5",
"-I/usr/include/mit-krb5/kadm5",
"-I/usr/include/mit-krb5/gssrpc",
"-I/usr/include/freetype2",
"-I/usr/include/freetype2/freetype",
"-I/usr/include/freetype2/freetype/config",
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
