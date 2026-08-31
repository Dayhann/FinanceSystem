# Project 1 — Finance System

A finance organisation system managing clients, accounts, transactions and
branches, built with Python OOP concepts: encapsulation, validation,
getters/setters, association and aggregation.

## Design Notes

### Class responsibilities

- **Client** — manages the client's own information (contact details) and
  the client's relationships: the accounts it holds (aggregation) and its
  preferred branch (association).
- **Account** — manages account information and balance behaviour. The
  balance only changes through `add_funds()` and `withdraw()`.
- **Transaction** — manages transaction information and status. Status only
  changes through `process_transaction()` and `cancel_transaction()`, and
  processing applies the amount to a validated `Account`.
- **Branch** — manages branch information and opening state, which only
  changes through `open_branch()` and `close_branch()`.

### What works well

- **Single Responsibility Principle** — each class has one clear focus:
  client/relationships, account/balance, transaction/status,
  branch/opening state.
- **Protected aggregation** — `get_accounts()` returns a copy of the
  internal list, so outside code cannot modify the real aggregation;
  `add_account()`/`remove_account()` guard the relationship with
  `isinstance` checks and duplicate/membership checks.
- **Consistent validation** — constructors fall back to safe defaults,
  setters reject invalid values and keep the previous state, and all
  numeric checks exclude booleans (the bool-is-int trap).
- **Delegation** — behaviour methods that change an attribute (e.g.
  `update_phone_number()`) delegate to the validated setter, so the
  assignment and validation logic lives in one place.

### To reconsider as the project grows

- Behaviour methods print feedback instead of returning success/failure,
  so outside code cannot react programmatically to a rejected change.
- Money is `int`-only and dates are unvalidated strings; a real system
  would use `Decimal` and date types.
- `transaction.py` imports `Account` to validate `process_transaction()`
  (and `client.py` imports both `Account` and `Branch`) — module coupling
  is growing; concepts still to come (e.g. inheritance/polymorphism) may
  handle this more cleanly.
- Client holds no transactions; a Client–Transaction relationship may
  become useful when transaction history or reporting is introduced.

### S.O.L.I.D

Each class currently follows the Single Responsibility Principle. The
remaining principles (Open/Closed, Liskov Substitution, Interface
Segregation, Dependency Inversion) are not yet meaningfully applicable
without inheritance and interfaces, which arrive in later topics.
