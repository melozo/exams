#!/bin/bash
clear
py.test intern_exam.py  --hosts=10.10.120.100 --connection=ssh -v
