# Article Management System

A simple article management system built with Django for handling articles, creating new ones, and searching existing articles. This project is a **Server-Side Rendered (SSR)** application, meaning all content is rendered on the server before being sent to the client.

## Features

- **Create Articles**: Users can create new articles by providing a title, author, content, and publication date.
- **Search Articles**: Users can search for articles based on their title.
- **View Articles**: The system displays all articles or search results when queried.
- **Basic CRUD**: Allows basic operations for managing articles.

## Technologies Used

- **Django**: The backend framework used to handle the server-side logic and rendering of pages.
- **HTML**: Used for structuring the content of the pages.
- **CSS**: Provides styling and layout to the application.
- **SQLite**: Default database engine used in Django for storing article data.
  
## Getting Started

### Prerequisites

To run this project locally, you will need to have the following installed on your system:

- Python 3.x
- Django (can be installed via `pip`)
- SQLite (comes bundled with Python, so no additional installation needed)
- Pillow (for handling images)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/fabrixindex/SSR-Django-News-Portal.git
   cd article-management-system
