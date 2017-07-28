#!/bin/bash


export DEST=172.16.120.130
export BASE=flask_hello
export ARTIFACT="$BASE.tar.gz"
export DEST_FOLDER=/tmp

case "$1" in
  build)
	tar -czvf $ARTIFACT flask_hello
	;;
  test_connection)
	ssh root@$DEST exit
	if [[ $? == 0 ]]; then
		echo "Connection OK"
		exit 0
	else
		echo "Connection FAIL"
		exit 255
	fi
	;;
  copy)
	scp $ARTIFACT root@$DEST:$DEST_FOLDER/
	;;

  extract)
	ssh $DEST "rm -fr $DEST_FOLDER/$BASE"
	ssh $DEST "tar -zxvf $DEST_FOLDER/$ARTIFACT -C $DEST_FOLDER/"
	;;
  setup)
	ssh $DEST "/usr/local/bin/pip3 install venv"
	;;
esac

