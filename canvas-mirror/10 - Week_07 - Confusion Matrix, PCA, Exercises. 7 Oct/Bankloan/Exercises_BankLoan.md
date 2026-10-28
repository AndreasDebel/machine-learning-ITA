# Exercises Week 7 - Bank Loan (ITA Machine Learning)

Source: Exercises_BankLoan.pdf, 3 pages, no author/date visible (pages 2-3 carry no extracted text; likely figures)

The exercises this week are a bit more "open-ended" than before; use the techniques introduced so far. Work in groups of 2-3.

## Exercise

A bank deals in home loans (urban, semi-urban, rural areas). Customers send information about Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this, the bank wants a program that identifies customer segments: those eligible for loans and those not. The bank provides a training dataset with loans given, and a test dataset where the program should decide (grant a loan or not) with the highest possible accuracy.

*[Page 2: "Dataset Description" table (image):]*

| Variable          | Description                              |
|-------------------|------------------------------------------|
| Loan_ID           | Unique Loan ID                           |
| Gender            | Male/ Female                             |
| Married           | Applicant married (Y/N)                  |
| Dependents        | Number of dependents                     |
| Education         | Applicant Education (Graduate/ Under Graduate) |
| Self_Employed     | Self employed (Y/N)                      |
| ApplicantIncome   | Applicant income                         |
| CoapplicantIncome | Coapplicant income                       |
| LoanAmount        | Loan amount in thousands                 |
| Loan_Amount_Term  | Term of loan in months                   |
| Credit_History    | credit history meets guidelines          |
| Property_Area     | Urban/ Semi Urban/ Rural                 |
| Loan_Status       | Loan approved (Y/N)                      |

Information given:
- Loan Approval Status: about 2/3 of applicants have been granted a loan.
- Education: about 5/6 of the population is Graduate; graduates have a higher proportion [sic: "propotion"] of approvals.
- Employment: 5/6 of the population is not self employed.
- Property Area: applicants from Semi-urban are more likely to be granted loans.
- Applicants with a credit history are far more likely to be accepted.

The original dataset is split into training and test sets (80/20). Using logistic regression, accuracy is measured with various thresholds. A threshold somewhere between 0.3 and 0.6 appears optimal.

*[Page 3: line plot, x = Decision Threshold (0.1 to 0.8), y = Score (about 0.55-0.80); two series, Training Accuracy (blue) and Test Accuracy (orange). Both rise from threshold 0.1 (train ~0.71, test ~0.62), plateau around 0.4-0.7 (train ~0.81, test ~0.78-0.79), then drop sharply at 0.8 (train ~0.56, test ~0.66).]*

Tasks:
- a) Verify that everyone in the group understands the code ("Loan Approval Prediction.ipynb").
- b) Make similar plots using sklearn:
  - decision tree or random forest,
  - neural net.

  Can you get similar results with a random forest classifier? What about the neural net? Is it possible to improve the results from the given logistic regression code? What are the best values for the random forest parameters (number of trees, tree depth) and the neural net parameters (number of hidden layers, neurons etc.)?

Data: see bank_loan_data.md.
