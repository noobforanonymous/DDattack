red='\033[1;31m'
clear='\033[0m'
green='\033[1;32m'
yellow='\033[1;33m'
clear
echo " "
echo " "
echo '
  ____, ____,__, _, ____,____,__, ,____, 
(-|__)(-|  (-|__| (-/_|(-/  ( |_/(-(__  
 _|  \,_|,  _|  |,_/  |,_\__,_| \,____) 
(     (    (     (     (    (    (    
                          
'|lolcat
echo " "
echo " "
sleep 6.0
clear
echo -e "$red                         <===================wait===============>$clear"
sleep 2.0
clear
echo -e "$red                          <===================we are checking===============>$clear"
sleep 2.0
clear
echo -e "$red                         <===================any updates===============>$clear"
sleep 2.0
clear
echo -e "$red                         <===================wait now it's===============>$clear"
sleep 2.0
clear
echo " "
echo " "
echo -e "$green               <=================== updating the DDattack please wait===============>$clear"
sleep 2.0
cd $HOME
rm -rf getsourcecode
git clone https://github.com/noobforanonymous/DDattack
clear
cho " "
echo -e "$green               <==================DDattack has been updated========================>$clear"
sleep 3.0
echo " "
cd DDattack
python ddattack.py
clear
