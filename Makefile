install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py myLib/*.py *.ipynb

lint:
	ruff check *.py myLib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

test:
	python -m pytest -vv --nbval -cov=myLib -cov=main test_*.py *.ipynb

generate_and_push:
	python main.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git add README.md summary_report.md
	git commit -m "Summary_report.md" || true 
	git push

all: install format lint test