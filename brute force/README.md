# Brute Force PIN Demo

This folder contains a small Python script that demonstrates a brute-force search against a 4-digit PIN.

## What it does

The script in [Brute_force.py](Brute_force.py) loops through values from `0000` to `9999` until it finds the hard-coded secret PIN.
It also measures how long the search took and how many attempts were made.

## How to run

```bash
python3 Brute_force.py
```

## Notes

The current secret PIN is defined in the script as `4669`.
This is a learning example only and should not be used to protect real data.
