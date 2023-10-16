import os
import sys

### Custom errors

# class NotSubtitleFile(ValueError):
#     """Raise when user tries to purches item more than 3 times."""


# class TooManyAttempts(Exception):
#     """Raise error when attempts are higher than 3"""


# def validate_attempts(attempt):
#     """Check number of attempts"""
#     if attempt >= 3:
#         raise TooManyAttempts("---Too many unsuccessful attempts. Try again later.---\n")


#%%
# file_path = "\\\\172.16.20.3\\pm\\quote\\QN18960-01\\Prm\\Notes"


# %%

### Validation functions
def validate_confirmation(user_input):
    """Check if y/n confirmation is valid and exit if n"""
    if user_input not in ['y', 'n']:
        raise ValueError("  Invalid input. Please type in 'y' or 'n'.\n")
    if user_input == 'n':
        sys.exit()


def validate_file_path(file_path):
    """Validate if path provided by user exists"""
    if not file_path:
        raise ValueError("You did not provide a path, please try again.")

    if not os.path.exists(file_path):
        raise ValueError(f"File or directory you provided does not exist:\n {file_path}")
    
    if not os.path.isdir(file_path):
        raise ValueError(f"this is not a valid directory\n{file_path}")

    return file_path

# validate_file_path()

# %

# %%
