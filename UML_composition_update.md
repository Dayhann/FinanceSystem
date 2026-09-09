# Project 1: Finance System - UML Update (Workshop 4-2, Task 3)

Topic 4 update: Account now exposes properties (not shown in class
diagrams, as standard practice) and the Account-Transaction
relationship is now **composition**, because the account creates and
owns the transaction records made by its deposit and withdrawal
behaviour through a private helper method.

```mermaid
classDiagram
    class Client {
        -__client_no : int
        -__first_name : str
        -__last_name : str
        -__email : str
        -__address : str
        -__accounts : List~Account~
        -__preferred_branch : Branch
        +add_account(account)
        +remove_account(account)
        +set_preferred_branch(branch)
    }

    class Account {
        -__account_no : int
        -__account_type : str
        -__current_balance : int
        -__date_created : str
        -__transactions : List~Transaction~
        -__next_transaction_id : int
        +add_funds(amount)
        +withdraw(amount)
        +display_information()
        -__create_transaction(transaction_type, amount, resulting_balance) Transaction
    }

    class Transaction {
        -__transaction_id : int
        -__transaction_type : str
        -__amount : int
        -__description : str
        -__status : str
        -__resulting_balance : int
        +process_transaction(account)
        +cancel_transaction()
        +display_information()
    }

    class Branch {
        -__branch_number : int
        -__branch_name : str
        -__location : str
        -__phone_number : str
        -__is_open : bool
        +open_branch()
        +close_branch()
    }

    Client "1" o-- "0..*" Account : holds (aggregation)
    Client "1" --> "0..1" Branch : preferred branch (association)
    Account "1" *-- "0..*" Transaction : creates and owns (composition)
```

## What changed in Workshop 4-2

- **Account creates Transaction records** - the private helper
  `__create_transaction()` is reused by `add_funds()` and `withdraw()`,
  assigns each record a unique identifier, and records the transaction
  type, the amount, and the resulting balance.
- **Composition** - Transaction objects are created inside the Account
  (filled diamond) rather than independently in main.py. Invalid
  financial operations create no records.
- **Controlled read access** - the `transactions` property returns a
  copy of the private collection.
- **Properties** - `account_no`, `account_type` (read-write),
  `current_balance`, `date_created`, and `transactions` provide
  attribute-style access; identifiers and balances stay read-only and
  balance changes remain controlled by behaviour methods.
- Transaction itself gains a read-only `resulting_balance` field, set
  when the account records a completed movement of money.
