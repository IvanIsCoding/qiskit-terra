.PHONY: env env-dev lint test run

# Virtual environment creation and deps install.
env:
	conda create -y -n QISKitenv python=3 pip
	bash -c "source activate QISKitenv;pip install -r requires.txt"

env-dev:
	bash -c "source activate QISKitenv;pip install pylint matplotlib"

lint:
	bash -c "source activate QISKitenv;pylint qiskit test tools tutorial"

test:
	bash -c "source activate QISKitenv;python test/QISKit-tests.py"

run:
	bash -c "source activate QISKitenv;cd scripts;jupyter notebook"

