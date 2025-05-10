# FSM Designer

A web-based Finite State Machine (FSM) designer for Theory of Computation visualizations. Build, edit, and export FSM diagrams in various formats.

## Features

- Create and edit FSM diagrams with an intuitive interface
- Export diagrams as PNG, SVG, or LaTeX
- Mobile-responsive design
- Multiple color themes (Dark, Light, Nord, Monokai)
- Example FSMs to get started

## Deployment on Vercel

This application is configured for deployment on Vercel. Follow these steps to deploy:

1. Install the Vercel CLI (if not already installed):
   ```
   npm install -g vercel
   ```

2. Log in to Vercel from the command line:
   ```
   vercel login
   ```

3. Navigate to your project directory and run:
   ```
   vercel
   ```

4. Follow the prompts from the Vercel CLI. You can use the default settings for most options.

5. Once deployed, Vercel will provide you with a URL where your application is hosted.

## Local Development

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open your browser and navigate to `http://localhost:8080`

## Technologies Used

- Frontend: HTML, CSS, JavaScript (Canvas API)
- Backend: Python Flask
- Deployment: Vercel
