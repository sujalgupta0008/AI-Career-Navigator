# 🎯 AI Career Navigator

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)](https://streamlit.io/)
[![Groq API](https://img.shields.io/badge/Groq-API-FF6B35)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)

</div>

**AI Career Navigator** is an intelligent career guidance platform powered by Groq API. It helps students and early-career professionals analyze their career readiness, identify skill gaps, match their profile with job descriptions, and follow a personalized 30-day preparation roadmap.

---

## 📋 Table of Contents

- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Groq API Integration](#-groq-api-integration)
- [Contributing](#-contributing)
- [License](#license)

---

## Problem Statement

Many students and early-career professionals face challenges:
- 🤔 Uncertainty about suitable career paths
- ❌ Unaware of missing technical and soft skills
- 📊 Lack of structured preparation guidance
- 🎯 No personalized roadmap for career development
- 📄 Limited resources for resume and interview prep

---

## Solution

AI Career Navigator leverages **Groq API** to provide:
- **Personalized Career Analysis** based on student profile, skills, and goals
- **Skill Gap Identification** highlighting missing technical and soft skills
- **Job Match Analysis** comparing profile with job descriptions
- **30-Day Roadmap** with actionable learning tasks
- **Improvement Suggestions** for resume, LinkedIn, and GitHub
- **Interview Preparation** with curated questions
- **Professional Reports** ready for download

---

## ✨ Features

### Core Features
- ✅ **Student Profile Input** - Comprehensive profile creation
- ✅ **Target Role Selection** - Choose desired career paths
- ✅ **AI-Powered Analysis** - Gemini-generated career insights
- ✅ **Skill Readiness Score** - Quantified assessment of readiness
- ✅ **Skill Gap Analysis** - Detailed missing skills report
- ✅ **Job Match Analyzer** - Compare profile with job descriptions
- ✅ **30-Day Roadmap Tracker** - Step-by-step learning plan
- ✅ **Downloadable Reports** - Professional PDF export
- ✅ **Demo Profile** - Quick start with sample data

### Advanced Capabilities
- 📈 Resume optimization suggestions
- 🔗 LinkedIn profile enhancement tips
- 💻 GitHub portfolio recommendations
- 🎤 Interview preparation questions
- 🗺️ Personalized learning roadmap

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3.8+ |
| **Frontend** | Streamlit |
| **AI Engine** | Groq API |
| **Data Processing** | Pandas |
| **Visualization** | Matplotlib |
| **Environment** | python-dotenv |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Groq API key ([Get one here](https://console.groq.com/))

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sujalgupta0008/AI-Career-Navigator.git
   cd AI-Career-Navigator
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

1. **Create `.env` file** in the project root
   ```bash
   cp .env.example .env
   ```

2. **Add your Groq API key**
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

   > **Note:** Get your free API key from [Groq Console](https://console.groq.com/)

3. **Verify setup**
   ```bash
   python app.py
   ```

---

## 🚀 Usage

### Start the Application
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Platform

1. **Enter Your Profile**
   - Name and contact details
   - Current degree and graduation date
   - Technical skills and proficiency levels
   - Projects and achievements
   - Career aspirations

2. **Select Target Role**
   - Choose desired job role
   - Input job description (optional)

3. **Generate Analysis**
   - Click "Analyze" to get AI insights
   - Review career readiness score
   - Check skill gaps and recommendations

4. **Follow Your Roadmap**
   - Track 30-day learning milestones
   - Complete suggested tasks
   - Monitor progress

5. **Download Report**
   - Export professional career report
   - Share with mentors or recruiters

---

## 📂 Project Structure

```text
AI-Career-Navigator/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
│
└── utils/
    ├── gemini_helper.py       # Gemini API integration
    ├── scoring.py             # Skill scoring algorithms
    ├── report_generator.py    # Report generation logic
    └── theme.py               # UI theme customization
```

---

## 🧠 Groq API Integration

The platform utilizes Groq API for:

| Feature | AI Task |
|---------|---------|
| Career Analysis | Personalized insights based on profile |
| Job Matching | Compare skills with job requirements |
| Skill Gap | Identify missing technical skills |
| Soft Skills | Recommend behavioral improvements |
| Resume Tips | Enhance resume content |
| LinkedIn Optimization | Profile enhancement suggestions |
| GitHub Portfolio | Project and repo recommendations |
| Learning Roadmap | 30-day structured learning plan |
| Interview Prep | Curated technical & HR questions |

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Guidelines
- Write clean, readable code
- Add comments for complex logic
- Update documentation as needed
- Test your changes before submitting PR

---

## 📝 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 👨‍💻 Author

**Sujal Gupta**
- GitHub: [@sujalgupta0008](https://github.com/sujalgupta0008)
- Portfolio: [Your Portfolio]

---

## 🙏 Acknowledgments

- Groq API for AI capabilities
- Streamlit for the web framework
- Open-source community

---

## 📞 Support

For questions or issues, please:
- Open an [Issue](https://github.com/sujalgupta0008/AI-Career-Navigator/issues)
- Reach out via GitHub

---

**Last Updated:** August 2026