<h1>AI Realtime Gym Coach</h1>
<h2>Overview</h2>
This is an AI Real-time Gym Coach that uses computer vision and AI voice feedback to guide workouts through live pose detection. This project showcases practical AI integration with modern web technologies to create an efficient and scalable solution for gyms and exercise centers.

<h2>Table of Contents</h2>
<li>Overview</li>
<li>Tech Stack</li> 
<li>Features</li>
<li>Installation</li>
<li>Usage</li>
<li>Deployment</li>
<li>License</li>
<h2>Tech Stack</h2>
<h3>Frontend</h3>
<li>HTML</li>
<li>CSS</li>
<h3>Database</h3>
<li>SQLite</li>
<h3>Deployment</h3>
<li>Streamlit</li>
<h3>Development Tools</h3>
<li>Visual Studio Code</li>
<li>Git</li>
<li>GitHub</li>
<h3>Features</h3>
<li>Real-time exercise tracking using computer vision</li>
<li>AI-powered workout coaching and feedback</li>
<li>Voice-based motivational guidance</li>
<li>Rep counting and set tracking</li>
<li>Multiple exercise support</li>
<li>Continuous deployment on Streamlit</li>
<h2>Installation</h2>
To run AI Realtime Gym Coach locally, follow these steps:

<h3>1. Clone the repository:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>git clone https://github.com/yourusername/Realtime-Voice-Video-AI-Gym-Trainer.git</code></pre>
</div>

<h3>2. Navigate to the project directory:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>cd AI-Realtime-Gym-Coach</code></pre>
</div>

<h3>3. Install the dependencies:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>pip install streamlit</code></pre>
</div>
<h3>4. Set up environment variables:</h3>

Create a .env file in the root directory and configure the following variables:

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>GROQ_API_KEY=&lt;your_groq_api_key&gt;</code></pre>
</div>

<h3>5. Run the development server:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>uv run streamlit run main.py</code></pre>
</div>
<h3>6. Open your browser and navigate to:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>http://localhost:8501</code></pre>
</div>
<h2>Usage</h2>
Once the application is running, you can:

<h3><li>Enter Name:</h3>Enter your name and click Start Session.</li>
<h3><li>Create Workout Plan:</h3>Select Exercise,Sets,Reps per Set in the Workout Plan and click Start Workout.</li>
<h3><li>Do Workout:</h3>Do exercise as per the workout plan.</li>
<h3><li>View Workout History:</h3> Check your workout history.</li>

<h2>Deployment</h2>
AI Realtime Gym Coach is deployed on Streamlit. For deployment, ensure you have the Streamlit CLI configured.
Ensure your Streamlit credentials and services are properly set up for deployment.

<h2>License</h2>
All rights reserved.
