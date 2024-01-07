#!/bin/bash

TOKEN="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"
today=`date -d "0 days" +"%Y-%m-%d"`
git clone ${REPO} /root/ipvps/ &> /dev/null
clear
echo -e "MASUKAN IP VPS YANG BELUM DI DAFTAR !"
echo -e ""
read -p "Input nama : " name
read -p "Input IP Address : " ip
CLIENT_EXISTS=$(grep -w $ip /root/ipvps/ip | wc -l)
if [[ ${CLIENT_EXISTS} == '1' ]]; then
echo "IP Already Exist !"
exit 0
fi
echo -e ""
#name=F6EPQtYeJ3DmRZaL`</dev/urandom tr -dc A-Z0-9 | head -c4`
echo -e ""
clear
read -p " Masukan Waktu Expired : " -e exp
exp2=`date -d "${exp} days" +"%Y-%m-%d"`
echo "### ${name} ${exp2} ${ip}" >> /root/ipvps/ip
cd /root/ipvps
git config --global user.email "andyyuda630@gmail.com" &> /dev/null
git config --global user.name "myvpn1" &> /dev/null
rm -rf .git &> /dev/null
git init &> /dev/null
git add . &> /dev/null
git commit -m register &> /dev/null
git branch -M main &> /dev/null
git remote add origin https://github.com/myvpn1/andy
git push -f https://${TOKEN}@github.com/myvpn1/andy.git &> /dev/null
rm -rf /root/ipvps
clear
sleep 1
echo "  Registering IP Address..."
sleep 1
echo "  Processing..."
sleep 1
echo "  Done!"
sleep 1
clear