
-----

### 1\. Adding an Expense

The `add` command records a new expense. It requires an amount and a category. The description and date are optional.

  * **Command:** `expense-tracker add 25.50 Food --description "Groceries from Albert Heijn"`

  * **Purpose:** Adds an expense of €25.50 to the "Food" category with a specific description.

  * **Output:** `Expense of 25.5 added successfully!`

  * **Command:** `expense-tracker add 120.00 Rent`

  * **Purpose:** Adds an expense of €120.00 for "Rent" without a description.

-----

### 2\. Viewing a Summary

The `summary` command shows a total of all expenses, grouped by category.

  * **Command:** `expense-tracker summary`
  * **Purpose:** Displays a quick overview of your spending habits across all categories.
  * **Output:**
    ```
    ┏━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
    ┃ Category  ┃ Total Amount ┃
    ┡━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
    │ Food      │ 76.0         │
    │ Rent      │ 120.0        │
    └───────────┴──────────────┘
    Total Expenses: 196.0
    ```

-----

### 3\. Showing Recent Expenses

The `show` command lists your most recent expenses. You can specify the number of expenses to display.

  * **Command:** `expense-tracker show --last 5`
  * **Purpose:** Lists the last 5 expenses you added, including their unique IDs, which are useful for the `remove` command.
  * **Output:**
    ```
    ┏━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ ID ┃ Date       ┃ Category  ┃ Amount ┃ Description                  ┃
    ┡━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
    │ 1  │ 2025-08-14 │ Food      │ 50.5   │ Lunch with a friend          │
    │ 2  │ 2025-08-14 │ Groceries │ 25.75  │ Weekly shopping              │
    │ 3  │ 2025-08-14 │ Transport │ 4.5    │ Train ticket                 │
    │ 4  │ 2025-08-14 │ Coffee    │ 3.25   │ Morning coffee               │
    │ 5  │ 2025-08-14 │ Food      │ 12.0   │ Dinner with family           │
    └────┴────────────┴───────────┴────────┴──────────────────────────────┘
    ```

-----

### 4\. Removing an Expense

You can remove a specific expense using its ID, which is shown by the `show` command.

  * **Command:** `expense-tracker remove 3`
  * **Purpose:** Deletes the expense with ID `3` (in this case, the train ticket) from your records.
  * **Output:** `Expense with ID 3 removed successfully.`

### 5\. Removing the Last Expense

The `remove_last` command provides a quick way to undo your last entry without needing to know its ID.

  * **Command:** `expense-tracker remove_last`
  * **Purpose:** Deletes the most recently added expense.
  * **Output:** `Last expense removed successfully.`

-----

### 6\. Checking Your Budget

The `budget_check` command helps you monitor your spending against a set monthly budget.

  * **Command:** `expense-tracker budget-check 1000`
  * **Purpose:** Compares your current spending for the month to a budget of €1000.
  * **Output:**
    ```
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
    ┃ Metric                      ┃ Value  ┃
    ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
    │ Monthly Budget              │ 1000.0 │
    │ Total Expenses This Month   │ 196.0  │
    │ Remaining Budget            │ 804.0  │
    └─────────────────────────────┴────────┘

    You are on track! 804.0 left for this month.
    ```