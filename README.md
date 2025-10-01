# 📦 TrackWise  
**Inventory Management System (IMS) for Small Businesses**  

TrackWise is a web-based Inventory Management System built with **Python (Django)** and **MySQL**, designed to help small businesses efficiently monitor, organize, and optimize their stock. It provides real-time inventory tracking, automated reporting, role-based access, and analytical insights to improve decision-making and minimize errors.  

---

## 🚀 Features  

- **Account Management**  
  - User registration, secure login, and role-based access control.  
  - Admin, Manager, and Staff roles.  

- **Inventory Management**  
  - Add, update, and delete stock items.  
  - Real-time updates within 5 seconds of changes.  
  - Track item quantities and categories.  

- **Analytics & Reporting**  
  - Generate automated sales and stock reports.  
  - Interactive bar/line graphs for inventory insights.  
  - Profit and loss monitoring.  

- **User Interface & Experience**  
  - Minimalist, clean, and responsive design.  
  - Light/Dark mode toggle.  
  - Editable user profiles with image uploads.  

- **Integrations**  
  - Gmail & Facebook login.  
  - Export inventory data in multiple formats.  

---

## 🛠️ Tech Stack  

- **Frontend & Backend**: [Django (Python)](https://www.djangoproject.com/)  
- **Database**: [MySQL](https://www.mysql.com/) (optionally [Supabase](https://supabase.com/))  
- **Deployment**: AWS / Azure (planned)  
- **Version Control**: Git & GitHub  

---

## 📋 Project Objectives  

- Streamline stock monitoring and reduce manual tracking errors.  
- Achieve at least **80% positive usability feedback** from test users.  
- Reduce inventory-related errors by **30% in the first week of testing**.  
- Ensure system is fully operational by **November 2025**.  

---

## 📂 Folder Structure  

```bash
TrackWise/
│── backend/           # Django project files
│   ├── manage.py
│   ├── trackwise/     # Main Django app config
│   ├── inventory/     # Inventory management module
│   ├── accounts/      # User authentication & roles
│   ├── reports/       # Analytics & reporting
│
│── frontend/          # Templates & static files
│   ├── templates/     
│   ├── static/        
│
│── docs/              # Project documentation
│── requirements.txt   # Python dependencies
│── README.md          # Project overview
│── .gitignore         # Git ignore rules
