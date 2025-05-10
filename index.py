from app import app

# This is for Vercel serverless deployment
# Vercel looks for this handler in a file named index.py by default
handler = app
