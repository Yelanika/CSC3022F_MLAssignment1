#Yelanika Gunasekara
#GNSSEN002
#Assignment 1 ML

install: venv
	. venv/bin/activate; pip3 install -Ur requirements.txt

venv:
	test -d venv || python3 -m venv venv

run:
	python3 kmeans.py

clean:
	rm -rf venv
	find -iname "*.pyc" -delete