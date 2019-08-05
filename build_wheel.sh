#!/usr/bin/env bash

#Variables
VERSION=$(python -W ignore -c "import redison; print(redison.__version__)")
WHL_NAME="redison-$VERSION-py3-none-any.whl";
WHL_NAME_NEW="redison-$VERSION-py36-none-any.whl";

##Build wheel
COMMAND="rm dist/*.whl"; echo $COMMAND;  $COMMAND
python setup.py  bdist_wheel --python-tag py35

##Clean
COMMAND="mv dist/*.whl $WHL_NAME_NEW"; echo $COMMAND;  $COMMAND
COMMAND="rm -r dist"; echo $COMMAND;  $COMMAND

#Upload
COMMAND="twine upload $WHL_NAME_NEW"; echo $COMMAND;  $COMMAND
