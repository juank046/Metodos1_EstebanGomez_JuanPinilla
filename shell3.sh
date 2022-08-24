let pass=0 

checkvalue(){
	if [ $1 -eq 0 ] | [ $1 -eq 1 ]; then 
		pass=1
	else
		echo "intente de nuevo"
	fi
}

while [[ $pass -eq 0 ]]
do 
	read -p '0 o 1:' n
	checkvalue $n
done
