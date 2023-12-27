### Step 1: Install Homebrew

Homebrew is a package manager for macOS that makes it easy to install software from the command line.

1. Open the Terminal app.
2. Run the following command to install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Follow the on-screen instructions to complete the installation.
4. After installation, run `brew doctor` to make sure Homebrew is set up correctly.

### Step 2: Install Git with Homebrew

1. In the Terminal, run:

```bash
brew install git
```

2. Verify the installation with `git --version`.

### Step 3: Clone the Project Repository

1. Navigate to the directory where you want to clone the repository using `cd`.
2. Clone the repository:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of your Git repository.

3. Change to the project directory:

```bash
cd <repository-directory>
```

Replace `<repository-directory>` with the name of the directory that was created when you cloned the repository.

### Step 4: Checkout the Development Setup Branch

1. Check out the specific branch for setting up the development environment:

```bash
git checkout dev/setup
```

### Step 5: Create a New Branch for Development

1. Create a new branch to work on:

```bash
git checkout -b <your-new-branch-name>
```

Replace `<your-new-branch-name>` with the name you want for your new branch.

### Step 6: Install MySQL

1. Install MySQL with Homebrew:

```bash
brew install mysql
```


Certainly! Here is the updated Step 7 with the additional MySQL setup instructions:

### Step 7: Install MySQL Client and Set Up MySQL Database

1. Install `mysqlclient`, a Python package that allows your Django application to interact with MySQL databases:

```bash
pip install mysqlclient
```

2. Start MySQL 

```bash
mysql.server start
```

3. Access the MySQL command line interface with the root user:

```bash
mysql -u root -p
```

Press Enter when prompted for a password if you haven't set one yet.

4. Secure your MySQL installation (especially if you haven't set a root password):

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
```

Replace `new_password` with a secure password.

5. Create a database for your Django project:

```sql
CREATE DATABASE mobi_db;
```

Replace `mobi_db` with the desired database name.

6. Create a dedicated database user for your Django application:

```sql
CREATE USER 'mobi_user'@'localhost' IDENTIFIED BY 'user_password';
```

Replace `mobi_user` with the desired username and `user_password` with a secure password.

7. Grant the necessary permissions to the new user:

```sql
GRANT ALL PRIVILEGES ON mobi_db.* TO 'mobi_user'@'localhost';
```

8. Apply the privilege changes:

```sql
FLUSH PRIVILEGES;
```

9. Exit the MySQL command line:

```sql
EXIT;
```

10. Update your Django `settings.py` to use the new MySQL database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mobi_db',  # Your database name
        'USER': 'mobi_user',  # Your database user
        'PASSWORD': 'user_password',  # Your database password
        'HOST': 'localhost',  # Your database host
        'PORT': '3306',  # Your database port
    }
}
```


### Step 8: Install Project Dependencies

1. Navigate to the project's root directory.
2. Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 9: Configure and Run the Django Server

1. Set up your `settings.py` file with the correct database configuration.
2. Run migrations to create the database schema:

```bash
python manage.py migrate
```

3. Create a superuser account:

```bash
python manage.py createsuperuser
```

4. Start the Django development server:

```bash
python manage.py runserver
```

5. Open a web browser and navigate to `http://127.0.0.1:8000/` to see if the server is running without issues.


