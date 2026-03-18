# AI-Powered Mental Health Chatbot

## Overview
The AI-Powered Mental Health Chatbot is an innovative application designed to provide accessible mental health support through an AI-driven conversational interface. This project aims to offer empathetic interaction and valuable resources to users seeking mental health guidance. By leveraging modern web technologies, the chatbot creates a supportive environment where users can engage in meaningful conversations about their mental well-being.

The application is particularly beneficial for individuals looking for immediate mental health support, professionals seeking to integrate AI solutions into mental health services, and developers interested in exploring AI-driven web applications. With features like user profiles, resource recommendations, and a seamless chat interface, this project addresses the growing need for accessible mental health tools.

## Features
- **AI Chat Interface**: Engage with an AI-powered chatbot that provides empathetic responses to mental health inquiries.
- **User Profiles**: Manage personal information, including name, email, age, and mood, to tailor the chatbot experience.
- **Resource Recommendations**: Access a curated list of mental health resources, including guides and external links.
- **Dynamic Content Loading**: Utilize JavaScript to dynamically load user and resource data, enhancing user experience.
- **Responsive Design**: Enjoy a user-friendly interface that adapts to various screen sizes, ensuring accessibility on all devices.
- **Data Persistence**: Store user data, conversations, and resources in a SQLite database for reliable data management.
- **Seamless Navigation**: Navigate through different sections like Home, Chat, Profile, Resources, and About with ease.

## Tech Stack
| Component       | Technology       |
|-----------------|------------------|
| Backend         | FastAPI          |
| Frontend        | HTML, CSS, JavaScript |
| Database        | SQLite           |
| Templating      | Jinja2           |
| Web Server      | Uvicorn          |
| ORM             | SQLAlchemy       |

## Architecture
The project architecture is designed to efficiently serve the frontend through a robust backend API. The FastAPI framework handles all server-side logic, while the frontend is rendered using Jinja2 templates. The database models are defined using SQLAlchemy, ensuring seamless interaction with the SQLite database.

```plaintext
+-------------------+
| Frontend          |
| - HTML/CSS/JS     |
| - Jinja2 Templates|
+---------+---------+
          |
          |
+---------v---------+
| Backend (FastAPI) |
| - API Endpoints   |
| - Business Logic  |
+---------+---------+
          |
          |
+---------v---------+
| Database (SQLite) |
| - User Data       |
| - Conversations   |
| - Resources       |
+-------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-mental-health-chatbot.git
   cd ai-powered-mental-health-chatbot
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI application:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your web browser and visit:
   ```
   http://127.0.0.1:8000
   ```

## API Endpoints
| Method | Path                  | Description                                      |
|--------|-----------------------|--------------------------------------------------|
| GET    | `/`                   | Render the homepage.                             |
| GET    | `/chat`               | Render the chat interface.                       |
| GET    | `/profile`            | Render the user profile page.                    |
| GET    | `/resources`          | Render the resources page.                       |
| GET    | `/about`              | Render the about page.                           |
| POST   | `/api/chat`           | Send a message to the chatbot.                   |
| GET    | `/api/resources`      | Retrieve all mental health resources.            |
| GET    | `/api/users/{user_id}`| Retrieve user information by ID.                 |
| PUT    | `/api/users/{user_id}`| Update user information by ID.                   |

## Project Structure
```
.
├── Dockerfile          # Docker configuration file
├── app.py              # Main application logic with FastAPI
├── requirements.txt    # Project dependencies
├── start.sh            # Script to start the application
├── static              # Static files (CSS, JS)
│   ├── css
│   │   └── style.css   # Styling for the application
│   └── js
│       └── main.js     # JavaScript for dynamic content
├── templates           # HTML templates
│   ├── about.html      # About page template
│   ├── chat.html       # Chat interface template
│   ├── index.html      # Home page template
│   ├── profile.html    # User profile page template
│   └── resources.html  # Resources page template
└── mental_health_chatbot.db # SQLite database file
```

## Screenshots
*Screenshots of the application interfaces will be added here.*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t mental-health-chatbot .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 mental-health-chatbot
   ```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code adheres to the project's coding standards and includes relevant tests.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.