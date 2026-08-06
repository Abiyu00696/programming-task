# Login Lockout Demo

This folder contains a Python script that simulates a simple login system with limited attempts and a temporary lockout.

## What it does

The script in [login.py](login.py) checks a username and password against a small in-memory dictionary.
After too many failed attempts, it locks the system for a fixed time before allowing more tries.

## How to run

```bash
python3 login.py
```

## Default credentials

The demo includes these sample accounts:

| Username | Password |
| --- | --- |
| james | pa55w0rd |
| john | h3ll0 |
| robert | n07ing |
| admin | admin |

## Notes

The lockout delay is set in the script and is currently 60 seconds.
This is a basic educational example, not a production-ready authentication system.
