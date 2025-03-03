# Todo List for Telegram Budget Tracking Bot

## 1. Project Setup

- [ ] **Create Project & Virtual Environment**
  - [ ] Initialize a Python virtual environment.
  - [ ] Install necessary libraries (e.g., `python-telegram-bot`, `pytest`).

- [ ] **Set Up Git**
  - [ ] Create a new Git repository.
  - [ ] Add a `.gitignore` to exclude unnecessary files (e.g., venv folders).

- [ ] **Basic "Hello World" Bot**
  - [ ] Create a minimal bot that responds to `/start` and `/help`.
  - [ ] Write and run minimal tests to confirm it works.

## 2. Firebase Connection

- [ ] **Create Firebase Project**
  - [ ] Generate service account credentials.
  - [ ] Configure Firestore rules if needed.

- [ ] **Integrate Firebase in Python**
  - [ ] Install `firebase-admin`.
  - [ ] Initialize Firebase with service account credentials.
  - [ ] Implement a test to read/write a sample document to Firestore.

## 3. Basic Expense Tracking

- [ ] **Expense Data Model**
  - [ ] Define structure (e.g., `{user_id, date, amount, category, description}`).
  - [ ] Create unit tests to validate correct initialization.

- [ ] **Firestore Write/Read Logic**
  - [ ] Implement `add_expense(user_id, amount, category, description)`.
  - [ ] Include date/time.
  - [ ] Unit test for successful writes and reads.

- [ ] **Commands**
  - [ ] `/expense <amount> <category> [optional description]`
    - [ ] Validate command parameters.
    - [ ] Store silently, no confirmation.
    - [ ] Error handling for incorrect usage.

- [ ] **Categories**
  - [ ] `/addcategory <category>`
  - [ ] `/removecategory <category>`
  - [ ] Store categories in Firestore.
  - [ ] Tests: handle duplicates, missing arguments, etc.

## 4. Delete Recent Expenses

- [ ] **Retrieve Recent Expenses**
  - [ ] Implement logic to query the last N expenses (default 5).
  - [ ] Display with inline buttons to delete each.

- [ ] **Deletion**
  - [ ] On button click, remove the chosen expense from Firestore.
  - [ ] Confirm successful deletion with a short message or silent success.

- [ ] **Configurable History**
  - [ ] `/setdeletehistory <number>` to store user preference.
  - [ ] Test with different values (e.g., 5, 10).

## 5. Income Tracking

- [ ] **Income Data Model**
  - [ ] Similar structure to expenses, stored separately or flagged.
  - [ ] Write tests to verify correct fields.

- [ ] **Commands**
  - [ ] `/income <amount> <category> [optional description]`
    - [ ] Validate and store in Firestore.
  - [ ] `/addincomecategory <category>`
  - [ ] `/removeincomecategory <category>`
  - [ ] Tests for each command.

## 6. Recurring Transactions

- [ ] **Recurring Data Structure**
  - [ ] `recurring_transactions` collection with:
    - [ ] `amount`, `category`, `dateOfMonth`, `status` (active/paused), etc.

- [ ] **Scheduling**
  - [ ] Bot checks daily if it’s time to prompt for confirmation of a recurring expense.
  - [ ] Upon confirmation, add the expense to Firestore.

- [ ] **Commands**
  - [ ] `/recurring <amount> <category> <date>`
    - [ ] Store in Firestore as pending.
    - [ ] Schedule confirmation.
  - [ ] `/pauserecurring <category>`
  - [ ] `/resumerecurring <category>`
  - [ ] `/deleterecurring <category>`
  - [ ] `/recurringlist`
  - [ ] Write tests for setting, pausing, resuming, and deleting.

## 7. Budget Limits & Alerts

- [ ] **Set Budget**
  - [ ] `/setbudget <category> <amount>`
  - [ ] Store or update budget in Firestore.

- [ ] **Tracking & Thresholds**
  - [ ] On each expense, compute if the user hits 75% or 100% of the budget.
  - [ ] Send alert if threshold is reached.
  - [ ] Ensure no duplicate alerts for the same threshold in the same budget cycle.

- [ ] **Tests**
  - [ ] Verify correct alerts at 75% and 100%.
  - [ ] Handle multiple budgets in different categories.

## 8. Reports & Summaries

- [ ] **Summaries**
  - [ ] `/summary <period>` (day, week, month).
  - [ ] `/breakdown <period>` for detailed listing.
  - [ ] `/category <category> <period>` for category-specific summary.
  - [ ] Include daily average spending logic.

- [ ] **Scheduled Reports**
  - [ ] Daily reports each morning (previous day’s data).
  - [ ] Weekly reports Sunday night (past week’s data).
  - [ ] Only send if there were expenses in that period.

- [ ] **User-Configurable Schedules**
  - [ ] `/setreport daily <time>`
  - [ ] `/setreport weekly <day> <time>`
  - [ ] `/disablereport daily` / `/disablereport weekly`
  - [ ] Store schedule in Firestore, use a scheduler to send.

- [ ] **Tests**
  - [ ] Ensure date filtering is correct (today, thisweek, thismonth, etc.).
  - [ ] Check scheduling logic.

## 9. Export & Migrate

- [ ] **Export Commands**
  - [ ] `/export csv`
  - [ ] `/export json`
  - [ ] Retrieve all user data and send as a file.

- [ ] **Migrate Command**
  - [ ] `/migrate`
  - [ ] Provide a JSON snapshot of all data for a user (expense, income, recurring, budgets).

- [ ] **Tests**
  - [ ] Validate CSV and JSON formats.
  - [ ] Confirm that the data is complete.

## 10. Error Handling & Input Correction

- [ ] **Error Detection**
  - [ ] Handle incorrect commands, missing arguments, etc.
  - [ ] Show suggestions for recognized partial commands.

- [ ] **Fuzzy Matching**
  - [ ] If a user types `/expeense`, suggest `/expense`.
  - [ ] Test with common typos.

- [ ] **Help Command**
  - [ ] `/help` lists all features, usage examples.
  - [ ] Keep updated as new commands are added.

## 11. Final Testing & Deployment

- [ ] **Run Full Test Suite**
  - [ ] Unit tests, functional tests, coverage checks.

- [ ] **Performance Testing**
  - [ ] Verify Firestore can handle rapid read/writes.
  - [ ] Confirm bot remains responsive under load.

- [ ] **Deployment**
  - [ ] Deploy to server or hosting platform (Heroku, AWS, etc.).
  - [ ] Update environment variables or config for production.

- [ ] **Post-Deployment Verification**
  - [ ] Check logs for errors.
  - [ ] Perform manual end-to-end tests of core commands.

## 12. Future Enhancements (Optional / V2)

- [ ] **Graph-based Summaries**
  - [ ] Chart generation (pie/bar) for category distribution, monthly trends, etc.

- [ ] **Natural Language Input**
  - [ ] Parse “I spent 10€ on Food” → `/expense 10 Food`.

- [ ] **Settings Menu with Buttons**
  - [ ] Replace or augment certain command flows with inline button menus.
