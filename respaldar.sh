#!/bin/bash
caspetaDEstino $2
carpetaARespaldar $1
fechahoy = (date +'%Y_%m_%d')
nombre="${carpetaARespaldar##*/}"
archivo="$fechahoy$archivo"
tar -cf $2/$archivo $1