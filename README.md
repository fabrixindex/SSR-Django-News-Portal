<p align="center">
      <img src="https://imgur.com/IdvTlVe.jpg" alt="TruethLine" width="150">
</p>

# TruethLine - Article Management System

A simple article management system built with Django for handling articles, creating new ones, and searching existing articles. This project is a **Server-Side Rendered (SSR)** application, meaning all content is rendered on the server before being sent to the client.


## Features

- **Create Articles**: Users can create new articles by providing a title, author, content, and publication date.
- **Search Articles**: Users can search for articles based on their title.
- **View Articles**: The system displays all articles or search results when queried.
- **Basic CRUD**: Allows basic operations for managing articles.

## Technologies Used

<p align="center">

   <img src="https://camo.githubusercontent.com/0d0779a129f1dcf6c31613b701fe0646fd4e4d2ed2a7cbd61b27fd5514baa938/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534" alt="Python" width="100">
   <img src="https://camo.githubusercontent.com/13b219a55add1b06da0738bf43724acbd63e642faf01035506f20554f068fe0e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d2532333039324532302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465" alt="Django" width="110">
   <img src="https://camo.githubusercontent.com/e37ddb78355265ccd69b7d3c30dbaa5bc04855958c4ae320090d4f945616ad6c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d2532333037343035652e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d7768697465" alt="SQLite" width="100"> 
   <img src="https://camo.githubusercontent.com/d4d9d935f85b68223a3514c6a889ea3ed6a77afb5f560c05baa1a1b168077830/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f68746d6c352d2532334533344632362e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d68746d6c35266c6f676f436f6c6f723d7768697465" alt="Html" width="90">
   <img src="https://camo.githubusercontent.com/29d02b3669d6450d67e043cf5909e740dcb94c1e2306d88ac48b15b4ec55dc65/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a6176617363726970742d2532333332333333302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6a617661736372697074266c6f676f436f6c6f723d253233463744463145" alt="Js" width="130" />
</p>

- **Django**: The backend framework used to handle the server-side logic and rendering of pages.
- **HTML**: Used for structuring the content of the pages.
- **CSS**: Provides styling and layout to the application.
- **SQLite**: Default database engine used in Django for storing article data.
- **Pillow**: For handling images.

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

2. **Create and activate a virtual environment**:

   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install dependencies**:

   pip3 install -r requirements.txt

4. **Apply Migrations**:

   python3 manage.py makemigrations
   python3 manage.py migrate

5. **Create superuser**:

   python3 manage.py createsuperuser

6. **Start the development server**:

   python3 manage.py runserver

### Contributing
If you wish to contribute to this project, follow these steps:

1. **Fork this repository.**

2. **Clone your fork**:

   ```bash
   git clone https://github.com/fabrixindex/SSR-Django-News-Portal.git
   cd SSR-Django-News-Portal

3. **Create a new branch for your feature or fix**:
   
   ```bash
   git checkout -b branch-name

4. **Make your changes and commit them**:
   
   ```bash
   git commit -m "Description of changes"

5. **Push your changes to your fork**:

   ```bash
   git push origin branch-name

6. **Open a Pull Request on GitHub.**


### CONTACT

📫 How to reach me [fabriciopapetti1121@gmail.com](mailto:fabriciopapetti1121@gmail.com)

