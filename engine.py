import contextlib
import io

def run_user_code(code: str) -> str:
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})
    except Exception as e:
        return str(e)
    return output.getvalue().strip()

def check_output(actual: str, expected: str) -> bool:
    return actual.strip().lower() == expected.strip().lower()

def award_tracker(score: int) -> int:
    # One star for every 5 correct answers
    return score // 5

def get_next_challenge(index: int, challenges: list):
    if index < len(challenges):
        return challenges[index]
    return None
