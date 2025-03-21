# Microservices Project Make File
# author: umer mansoor

.PHONY: install test run clean

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest tests/

run-movies:
	python3 -m services.movies

run-showtimes:
	python3 -m services.showtimes

run-bookings:
	python3 -m services.bookings

run-users:
	python3 -m services.users

run-all:
	python3 -m services.movies & \
	python3 -m services.showtimes & \
	python3 -m services.bookings & \
	python3 -m services.users

stop-all:
	pkill -f "python3 -m services"

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +

format:
	black services/ tests/

lint:
	flake8 services/ tests/

