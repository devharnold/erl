# erl
A social-media related tool to help users within different regions share insights or items and bring happiness over the internet. All this is achieved because of the Django framework that is used to build the tool.

## Features

- **Create Blog Posts**: Users can write and publish blog posts.
- **Photo Sharing**: Users can upload and share photos within their posts.
- **User Authentication**: Secure login and registration system.
- **User Profiles**: Each user has a profile displaying their posts.
- **Future Feature - Chat**: A chat feature will be implemented to allow users to communicate, potentially as a premium feature.

## Tech Stack

- **Backend**: Django
- **Frontend**: React
- **Database**: SQLite (default, can be switched to PostgreSQL, MySQL, etc.)
- **Authentication**: Django's built-in authentication system

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- Node.js
- npm or yarn
- Pip

### Installation

#### Backend Setup

1. **Clone the repository**

    ```sh
    git clone https://github.com/yourusername/erl.git
    cd erl/backend
    ```

2. **Create a virtual environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**

    ```sh
    python manage.py runserver
    ```

#### Frontend Setup

1. **Navigate to the frontend directory**

    ```sh
    cd ../frontend
    ```

2. **Install dependencies**

    ```sh
    npm install
    # or
    yarn install
    ```

3. **Run the development server**

    ```sh
    npm start
    # or
    yarn start
    ```

4. **Access the application**

    Open your web browser and go to `http://localhost:3000/`

## Usage

- **Register and Login**: Create a new account or login with an existing one.
- **Create a Post**: Navigate to the 'Create Post' section to write a new blog post and upload photos.
- **View Posts**: Browse through the posts created by other users.
- **User Profiles**: Visit user profiles to see all posts made by a specific user.
- **Notifications**: Implement a notification system for user interactions.

## Future Plans

- **Chat Feature**: A real-time chat feature will be added to allow users to communicate. This might be offered as a premium feature.
- **Enhanced Photo Gallery**: Improve photo upload and display capabilities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, feel free to open an issue or contact us at [henryarnoldme@gmail.com](mailto:youremail@example.com).

---

Thank you for using erl.