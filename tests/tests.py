name: Python Tests

on:
  push:
    branches:
      - main  # Trigger the workflow on push to the main branch
  pull_request:
    branches:
      - main  # Trigger the workflow on pull requests targeting the main branch

jobs:
  test:
    runs-on: ubuntu-latest  # Use the latest Ubuntu runner

    steps:
      # Step 1: Checkout the code
      - name: Checkout code
        uses: actions/checkout@v2

      # Step 2: Set up Python (using the latest 3.x version)
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'  # Use the latest Python 3.x version

      # Step 3: Install dependencies from requirements.txt
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip  # Upgrade pip to the latest version
          pip install -r requirements.txt  # Install the dependencies from requirements.txt

      # Step 4: Run tests located in the /tests directory
      - name: Run tests
        run: |
          pytest tests/  # Run tests located in the /tests directory

