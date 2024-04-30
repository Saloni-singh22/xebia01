name: Generate QR Code

on:
  push:
    branches:
      - main

jobs:
  build:
    name: Generate QR Code
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: pip install qrcode[pil]

    - name: Run Python script
      run: python generate_qr_code.py

    - name: Commit changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add qrcode.png
        git commit -m "Add QR code image"
      
    - name: Push changes
      uses: ad-m/github-push-action@master
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
