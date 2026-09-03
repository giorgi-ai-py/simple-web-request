# simple-web-request
on day 2 of learning python (learning it myself with the linux mint terminal) i made with simple python script that is cheesy and pretty funky but at least it teaches me something

# Day 2: My Web Scraper (that actually works now!)

## What is this?
So I built a Python script that can fetch websites and show you either:
- The raw HTML (pretty self explanatory but its a giant wall of code that looks scary)
- Just the page title (the clean, readable version)

## Why did I make this?
Because typing `curl https://google.com` and getting back 50,000 lines of HTML is not fun. I wanted something that could grab just the important stuff.

## What I learned today
- How to use `requests` to download websites
- How to use `BeautifulSoup` to parse HTML (it's like finding needles in a haystack)
- How to make a menu with `if/elif/else`
- That Linux doesn't want me installing packages system-wide (had to use a venv)
- That I accidentally tried to `cd` into my Cuphead game folder to install Python libraries (don't ask)

## The funny part
I spent 20 minutes debugging why my script kept crashing, only to realize I had a typo: `ApplWebKit` instead of `AppleWebKit`. Computers are dumb.

## How to run it
```bash
cd ~/ai-cyber-lab (laugh it up ik)
source venv/bin/activate
python3 web_request.py
