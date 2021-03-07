#!/bin/bash
Kirmizi='\033[31m'

if [[ $(echo $USER) != "root" ]] ; then
    echo -e   ${Kirmizi} " 

            Please Put Sudo Before Command!!!

             

            Example Usage: sudo main.py
             
             "
    exit
    fi

netcheck() {
    ping -q -w1 -c1 google.com &>/dev/null && netcheck="online" || netcheck="offline"
    case ${1} in
        print|PRINT|-p)
            echo "${netcheck}"
        ;;
    esac
}

function debian() {

  if [[ $(command -v proxychains) = "" ]] ; then 
    apt install -y proxychains
  fi

  if [[ $(command -v tor) = "" ]] ; then 
    apt install -y tor
  fi
  sudo python3 setconfig.py
}


function arch() {

  if [[ $(command -v proxychains) = "" ]] ; then 
    pacman -S proxychains-ng --noconfirm
  fi

  if [[ $(command -v tor) = "" ]] ; then 
    pacman -S tor --noconfirm
  fi
  sudo python3 setconfig.py
}


function rpm() {

  if [[ $(command -v proxychains) = "" ]] ; then 
    dnf install proxychains-ng
  fi

  if [[ $(command -v tor) = "" ]] ; then 
    dnf install tor
  fi
    sudo python3 setconfig.py
}

netcheck -p && { [[ ${netcheck} = "offline" ]] && exit 1 ; }

if [[ $(command -v apt >& /dev/null ; echo $?) == 0 ]] ; then
  debian
elif [[ $(command -v pacman >& /dev/null ; echo $?) == 0  ]] ; then
  arch
elif [[ $(command -v rpm >& /dev/null ; echo $?) == 0  ]] ; then
  rpm
fi

