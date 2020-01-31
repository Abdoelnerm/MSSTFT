apt update -y && apt upgrade -y
apt -y install python2
mv MSSTFT.py .MSSTFT.py && mv .MSSTFT.py $HOME
rm -rif $HOME/MSSTFT
