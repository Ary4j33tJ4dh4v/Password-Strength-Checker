# 🔐 Password Strength Checker

A simple Python command-line tool that analyzes a password and tells you how strong it is — with a percentage score, a visual strength meter, and personalized tips to make it stronger.

## Features

- **Percentage-based strength score** (0–100%) based on a 7-point rule check
- **Visual strength meter** — a text progress bar right in the terminal
- **Strength labels** — Weak / Medium / Strong / Very Strong
- **Actionable recommendations** — tells you exactly what's missing (length, uppercase, digits, special characters, etc.)
- **Common password detection** — flags predictable passwords like `password`, `123456`, `qwerty`
- **Interactive loop** — check as many passwords as you like in one session

## How It's Scored

Each password is checked against 7 criteria, and the final score is converted to a percentage:

| # | Criterion |
|---|-----------|
| 1 | At least 8 characters long |
| 2 | At least 12 characters long (bonus for extra length) |
| 3 | Contains at least one digit |
| 4 | Contains at least one uppercase letter |
| 5 | Contains at least one lowercase letter |
| 6 | Contains at least one special character (`!@#$%^&*` etc.) |
| 7 | Avoids common/predictable words or patterns |

**Strength labels:**

| Percentage | Label |
|---|---|
| Below 40% | Weak |
| 40% – 69% | Medium |
| 70% – 99% | Strong |
| 100% | Very Strong |

## Requirements

- Python 3.6+
- No external dependencies (uses only Python's built-in `re` module)

## Installation

```bash
git clone https://github.com/your-username/password-strength-checker.git
cd password-strength-checker
```

## Usage

Run the script:

```bash
python password_strength_checker.py
```

You'll be prompted to enter a password. The tool will show:

```
Enter your password (or type 'exit' to quit): weak

Strength: Weak (29%)
[████████----------------------] 29%

Recommendations to improve your password:
  - Use at least 8 characters.
  - Use 12+ characters for stronger protection.
  - Add at least one number (0-9).
  - Add at least one uppercase letter (A-Z).
  - Add at least one special character (!@#$%^&* etc).
```

Type `exit` at any time to quit the program.

## Example

```
Welcome! TO THE PASSWORD STRENGTH CHECKER <3

Enter your password (or type 'exit' to quit): P@ssw0rd123!

Strength: Very Strong (100%)
[██████████████████████████████] 100%

Great job! Your password meets all strength criteria.
```

## Project Structure

```
password-strength-checker/
├── password_strength_checker.py   # Main script
└── README.md                      # Project documentation
```

## Possible Future Enhancements

- Entropy-based scoring and estimated crack time
- Hidden password input (no echo to terminal)
- Built-in strong password generator
- "Have I Been Pwned" breach check integration
- Graphical (Tkinter/web) interface

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Made with ❤️ by [Your Name]
