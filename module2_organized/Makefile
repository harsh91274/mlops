.PHONY: run install clean check runner
.DEFAULT_GOAL:=runner

run: install
	pushd src && poetry run python runner.py && popd

install: pyproject.toml
	poetry install

clean:
	for /r %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

check:
	poetry run flake8 src/

runner: check run clean
