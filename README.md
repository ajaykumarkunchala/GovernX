GovernX
│                                              
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── routes
│   └── risk_routes.py
│
├── services
│   ├── risk_engine.py
│   ├── financial_engine.py
│   └── validator.py
│
├── database
│   ├── database.py
│   └── governx.db
│
└── venv (ignored by .gitignore)

Step 7

In Postman

POST

http://127.0.0.1:5000/calculate-risk

GET

http://127.0.0.1:5000/risk-history

GET

http://127.0.0.1:5000/dashboard

GET

http://127.0.0.1:5000/filter-risk?level=Critical

PUT

http://127.0.0.1:5000/update-risk/1

DELETE

http://127.0.0.1:5000/delete-risk/1
