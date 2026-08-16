# CI/CD Pipeline for Web Application Using AWS

A complete **Continuous Integration/Continuous Deployment** pipeline demonstrating automated build, test, and deployment on AWS infrastructure.

## 🚀 Project Overview

This project implements an end-to-end CI/CD pipeline that:
- Automatically builds code when pushed to GitHub
- Runs automated tests via AWS CodeBuild
- Deploys to EC2 instances via AWS CodeDeploy
- Stores artifacts in S3 bucket
- Provides real-time status monitoring

## 📋 Features

✓ **Automated Build** - CodeBuild compiles and tests code
✓ **Automated Tests** - Pytest runs unit tests with coverage
✓ **Automated Deployment** - CodeDeploy pushes to EC2
✓ **Artifact Storage** - Built artifacts stored in S3
✓ **Health Checks** - Real-time application status monitoring
✓ **Error Handling** - Graceful failure and rollback
✓ **Containerization** - Docker support for consistency

## 🏗️ Architecture

## 📁 Folder Structure

CI-CD-Pipeline-AWS/
├── app/ # Flask application
│ ├── app.py # Main Flask app
│ ├── templates/
│ │ └── index.html # Web interface
│ └── static/
│ ├── css/style.css # Styling
│ └── js/script.js # JavaScript
│
├── tests/ # Unit tests
│ └── test_app.py # Flask app tests
│
├── scripts/ # Deployment scripts
│ ├── before_install.sh # Pre-deployment setup
│ ├── after_install.sh # Dependency installation
│ ├── application_start.sh # Start Flask
│ └── application_stop.sh # Stop Flask
│
├── buildspec.yml # CodeBuild configuration
├── appspec.yml # CodeDeploy configuration
├── Dockerfile # Container configuration
├── requirements.txt # Python dependencies
├── .env # Environment variables
├── .gitignore # Git ignore rules
└── README.md # This file

## 🛠️ Tech Stack

- **Language:** Python 3.9
- **Framework:** Flask 2.3.0
- **Testing:** Pytest 7.3.1
- **CI/CD:** AWS CodePipeline, CodeBuild, CodeDeploy
- **Storage:** AWS S3
- **Compute:** AWS EC2
- **Containerization:** Docker
- **Frontend:** HTML, CSS, JavaScript

## 📦 Dependencies

All dependencies listed in `requirements.txt`:
- Flask - Web framework
- Pytest - Testing framework
- Python-dotenv - Environment variables

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- AWS Account with appropriate permissions
- GitHub repository
- Git installed locally

### Local Installation

1. **Clone repository:**
```bash
git clone https://github.com/yourusername/CI-CD-Pipeline-AWS.git
cd CI-CD-Pipeline-AWS
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set environment variables:**
```bash
cp .env .env.local
# Edit .env.local with your settings
```

5. **Run tests:**
```bash
pytest tests/ -v --cov=app
```

6. **Run application locally:**
```bash
python app/app.py
```

Application runs on: `http://localhost:5000`

## 🔄 CI/CD Pipeline Workflow

### Step 1: Developer Push
- Developer commits and pushes code to GitHub

### Step 2: Pipeline Trigger
- GitHub webhook triggers AWS CodePipeline

### Step 3: Build Phase
- CodeBuild executes buildspec.yml:
  - Installs dependencies from requirements.txt
  - Runs pytest tests
  - Creates app.zip artifact

### Step 4: Deploy Phase
- CodeDeploy executes appspec.yml:
  - Runs scripts/before_install.sh (cleanup)
  - Copies files to /home/ec2-user/app
  - Runs scripts/after_install.sh (install dependencies)
  - Runs scripts/application_start.sh (start app)

### Step 5: Verification
- Application runs on EC2
- Health checks monitor status

## 📊 Testing

Run tests locally:

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app

# Run specific test
pytest tests/test_app.py::test_home_page -v
```

## 🐳 Docker Support

Build and run with Docker:

```bash
# Build image
docker build -t cicd-pipeline .

# Run container
docker run -p 5000:5000 cicd-pipeline

# Access application
curl http://localhost:5000
```

## 📝 Configuration Files

### buildspec.yml
Tells CodeBuild HOW to build your application:
- Install dependencies
- Run tests
- Create artifacts

### appspec.yml
Tells CodeDeploy HOW to deploy your application:
- When to run scripts
- Which files to copy
- Set file permissions

### .env
Stores sensitive configuration:
- Flask secret key
- AWS credentials
- Database URLs
- API keys

## 🔐 Security Notes

⚠️ **Important:**
- Never commit .env to Git (included in .gitignore)
- Change SECRET_KEY in production
- Use AWS Secrets Manager for sensitive data
- Enable EC2 security groups properly
- Use IAM roles for EC2 permissions

## 📈 Monitoring & Logs

### View Application Logs
```bash
ssh -i your-key.pem ec2-user@your-instance-ip
tail -f /tmp/flask_app.log
```

### AWS CodeBuild Logs
- View in AWS Console > CodeBuild > Build projects

### AWS CodeDeploy Logs
- View in AWS Console > CodeDeploy > Applications

## 🚨 Troubleshooting

### Build Fails
1. Check buildspec.yml syntax
2. Verify requirements.txt is valid
3. Check CodeBuild IAM permissions

### Deploy Fails
1. Check appspec.yml syntax
2. Verify EC2 security groups
3. Check CodeDeploy agent status on EC2

### Application Won't Start
1. Check Flask app.py for errors
2. Verify port 5000 is available
3. Check /tmp/flask_app.log for errors

## 📚 Resources

- [AWS CodePipeline Documentation](https://docs.aws.amazon.com/codepipeline/)
- [AWS CodeBuild Documentation](https://docs.aws.amazon.com/codebuild/)
- [AWS CodeDeploy Documentation](https://docs.aws.amazon.com/codedeploy/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pytest Documentation](https://docs.pytest.org/)

## 🤝 Contributing

1. Create feature branch
2. Make changes
3. Run tests locally
4. Push to GitHub
5. Create Pull Request

## 📄 License

This project is licensed under MIT License - see LICENSE file for details.

## 👤 Author

D.Madhav Reddy

## 📞 +91 9392211630

For issues and questions, create an issue in GitHub repository.

---

**Last Updated:** 2024
**Version:** 1.0.0