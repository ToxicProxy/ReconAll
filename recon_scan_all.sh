#!/bin/bash
echo ///////////////////////////
echo RECON_SCAN_ALL v0.0.1//////
echo ///////////////////////////
echo

read -p "Press any button to start the engines!"
echo Starting recon on $1!

python ~/RECON_STAGE/knock/knockpy/knockpy.py -j $1 -w ~/RECON_STAGE/list1.txt &

wait

python ~/RECON_STAGE/Sublist3r/sublist3r.py -v -d $1 -o rdp.txt &

wait

read -p "Ready for screenshots?"

python ~/RECON_STAGE/EyeWitness/EyeWitness.py -f rdp.txt --rdp &

wait

read -p "CRLF testing is next!"

python ~/RECON_STAGE/auto_CRLF.py rdp.txt < CRLF.txt
