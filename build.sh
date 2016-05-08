#!/usr/bin/env bash

    # Check if venv is created or not
        if [ ! -d "venv" ]; then
            virtualenv -p python2.7 venv
        fi
    sudo venv/bin/pip install  --no-cache-dir -r requirements.txt

        if [ ! -d /etc/luigi ];
            then
                sudo pip install luigi
                sudo mkdir /etc/luigi
            else
                echo "Luigi Dir exists !"
        fi

        sudo cp -f client.cfg /etc/luigi/

        if  pgrep "luigid" > /dev/null
           then
                echo "Luigi Central Scheduler Already Running..."
                #echo "Killing Luigi Central Scheduler..."
                #sudo kill luigid
                #echo "Luigi Central Scheduler Re-Starting...."

           else
                echo "Luigi Central Scheduler Starting...."
                sudo luigid --background --pidfile /etc/luigi/pid --logdir /etc/luigi/log --state-path /etc/luigi/state
         fi
