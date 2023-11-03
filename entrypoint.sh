#!/bin/bash

if [ -f .envconfig ]
then
  export $(cat .envconfig | sed 's/#.*//g' | xargs)
fi