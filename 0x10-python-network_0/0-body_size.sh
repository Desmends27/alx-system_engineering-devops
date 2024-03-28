#!/usr/bin/bash
 #takes a url and sendsa url request
curl -sI "$1" | grep content-length
