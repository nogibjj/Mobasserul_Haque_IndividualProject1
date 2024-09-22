install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py mylib/*.py *.ipynb

lint:
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

generate_and_push:
	python main.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git add summary_report.md
	git commit -m "Summary_report.md" || true 
	git push

all: install format lint test