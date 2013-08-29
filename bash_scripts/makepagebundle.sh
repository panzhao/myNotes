# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is a simple script.
#
# The Initial Developer of the Original Code is
# Alice Nodelman.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Alice Nodelman <alice@mozilla.com>
#   Clint Talbert <cmtalbert@gmail.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

#!/bin/bash
set -x

usage()
{
cat << EOF
usage: $0 -d <directory to create> < -u <url to download> | -f <file of url list> >
EOF
}

DIR=
URL=
INPUT_FILE=
while getopts "hd:u:f:" OPTION
do
  case $OPTION in
    h)
      usage
      exit 1
      ;;
    d)
      DIR=$OPTARG
      ;;
    u)
      URL=$OPTARG
      ;;
    f)
      INPUT_FILE=$OPTARG
      ;;
  esac
done

if [[ -z $DIR ]]
then
  usage
  exit 1
fi
if [[ -z $URL ]] && [[ -z $INPUT_FILE ]]
then
  usage
  exit 1
fi
echo saved directory: $DIR
echo download url: $URL
echo download url list-from file: $INPUT_FILE

# create directory
if [[ -f $DIR ]]
then
  usage
  exit 1
fi
if [[ ! -d $DIR ]]
then
  mkdir $DIR
fi

# download from file of url lists
cd $DIR
if [[ ! -z $INPUT_FILE ]] && [[ -f $INPUT_FILE ]]
then
  while read url_line
  do
    if [[ ! -z $url_line ]]
    then
      echo downloading ... $url_line
      mkdir $DIR/$url_line
      cd $DIR/$url_line
      wget -p -k -H -E -r -np -l 1 -erobots=off --no-check-certificate -U "Mozilla/5.0 (firefox)" --force-directories --restrict-file-names=unix --restrict-file-names=nocontrol $url_line -o outputlog.txt
      cd ..
    fi
  done < $INPUT_FILE
fi

# download from command parameter of -u
if [[ ! -z $URL ]]
then
  echo downloading ... $URL
  mkdir -p $DIR/$URL
  cd $DIR/$URL
  wget -p -k -H -E -r -np -l 1 -erobots=off --no-check-certificate -U "Mozilla/5.0 (firefox)" --force-directories --restrict-file-names=unix --restrict-file-names=nocontrol $URL -o outputlog.txt
  cd ..
fi
