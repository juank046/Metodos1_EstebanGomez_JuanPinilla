#!/bin/bash
  
funcion_help(){

echo "Debe incluir la posición inicial, la velocidad inicial y el tiempo total"
}
if [ "$#" -eq "3" ]
then
        echo "corriendo programa"
else
        funcion_help
fi
