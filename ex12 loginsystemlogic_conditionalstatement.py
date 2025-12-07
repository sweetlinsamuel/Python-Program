"""
Login System Logic
Scenario 3: Secure Access
Create a simple authentication check using Conditional Statements.
Task:
1. Define saved_pass = "Secure123"
2. Ask user for input
3. If match--> Print "Access Granted"
4. Else --> Print "Access Denied"
"""

saved_pass = "Secure123"
password = input("Enter your password here:")

if password == saved_pass:
    print("Access Granted")
else:
    print("Access Denied")

