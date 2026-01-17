# AI Code Review Assignment (Python)

## Candidate
- Name:Dagim Assefa
- Approximate time spent: 40 min

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Cancelled orders are skipped when summing amounts, but the denominator still includes them, so the calculated average is incorrect.
- An empty input list will cause a division-by-zero error.
- Missing status or amount keys are not handled and can cause runtime failures.

### Edge cases & risks
- When all orders are cancelled, the function still performs a division and returns a misleading average instead of handling the case explicitly.
- Non-numeric amount values are not handled and can lead to exceptions or incorrect calculations.

### Code quality / design issues
- The function assumes a specific input structure without validating it, which makes it fragile when faced with unexpected or malformed data.
- The comparison against the hard-coded "cancelled" string will not handle if given with a diffrent casing

## 2) Proposed Fixes / Improvements
### Summary of changes
- Only include non-cancelled orders with a numeric amount when calculating the average.
- Handle missing fields or bad data without crashing.
- Return 0.0 when there are no valid orders instead of dividing by zero.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
- If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty list ([]) → should not throw and should return 0.0.
- A mix of cancelled and non-cancelled orders → the average should only be based on non-cancelled orders.
- All orders cancelled → should return 0.0 instead of a misleading value.
- Orders missing status or amount → should be handled without raising errors.
- Non-numeric amounts ("10", "abc", None) → only values that can be converted to numbers should be included.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- It says cancelled orders are excluded from the calculation, but in practice the denominator still includes them.
- The explanation doesn’t mention the risk of division by zero or the assumptions being made about the input structure.
### Rewritten explanation
- This function calculates the average order value using only non-cancelled orders with numeric amounts.
- Cancelled or malformed orders are skipped, and the function returns 0.0 when there are no valid orders to average.
## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

- Decision: Request Changes
- Justification: The current logic gives the wrong average (bad denominator) and it can break on common cases like an empty list or missing fields.
- Confidence & unknowns: Pretty high confidence. The only question is what the expected behavior should be for messy data (missing/invalid amounts) — skip vs raise, depends on requirements.
---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The validation error prone anything with an "@" gets counted as valid (even clearly invalid emails).
- It can crash with a TypeError if an entry isn’t a string (like None or an int).
### Edge cases & risks
- invalid emails like "@", "a@", "@b", or "a@@b" are still counted as valid.
- Email values with leading or trailing whitespace (e.g. " test@example.com ") aren’t handled correctly.
- There’s no basic check on the domain part, so emails without a dot are treated as valid.

### Code quality / design issues
- The code doesn’t check input types or normalize values before validating.
- What counts as a valid email is not clearly defined and needs at least some basic structural rules.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Only treat strings as candidates and trim whitespace first.
- Require a single "@" with both local and domain parts present.
- Add a simple domain check (has a dot and doesn’t start or end with one).
- Safely skip malformed or non-string values.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
Empty input ([]) → returns 0.
- Non-string entries (None, 123, objects) → ignored safely.
- Valid examples: a@b.com, test.user@sub.domain.com, " test@ex.com ".
- Invalid examples: "@", "a@", "@b", "a@@b.com", "a@b", "a@.com", "a@b.".
- Mixed list with valid + invalid → count matches only valid ones.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- It says validation is correct but checking for "@" alone doesn’t mean an email is valid.
- It is not safe for non-string inputs — it can throw runtime errors.
- Saying it ignores invalid entries is misleading, since many invalid formats still get counted.

### Rewritten explanation
- This function counts emails that meet some basic structure checks: the value has to be a string, contain exactly one "@", have both local and domain parts, and use a minimally valid domain. Non-string or malformed entries are skipped.

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

- Decision: Request Changes
- Justification: The original function treats many invalid email formats as valid and can fail when the input contains non-string values.
- Confidence & unknowns: High confidence.
---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function divides by `len(values)` even though `None` values are skipped, which leads to an incorrect average.
- An empty input list can cause a division-by-zero error.
- Converting values using `float(v)` can raise `TypeError` or `ValueError` for non-numeric inputs.

### Edge cases & risks
- If all values are `None`, the function still attempts a division, which either produces a misleading result or fails when the list is empty.
- Mixed inputs (numbers, numeric strings, invalid strings) aren’t handled safely and can cause runtime errors, despite what the explanation suggests.
- Special float values like `NaN` or `inf` may silently propagate into the result, depending on how strictly this needs to be handled.

### Code quality / design issues
- The code doesn’t clearly validate whether values can actually be converted to numbers.
- What counts as a “valid” measurement is unclear — it only checks for `None` and ignores other invalid, non-numeric inputs.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Only include values that can actually be converted to floats in the average.
- Skip `None` and any values that can’t be converted without throwing.
- Return `0.0` when there are no valid measurements to avoid division-by-zero issues.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
Empty list → returns 0.0.
- Empty list → should return `0.0` without throwing.
- All values are `None` → should return `0.0`.
- A mix of numeric values and `None` → only numeric values should be included in the denominator.
- Numeric strings (e.g. `"1.5"`) should be included, while invalid strings (e.g. `"abc"`) should be ignored.
- Mixed types (`1`, `2.0`, `"3"`, `None`, `"bad"`) → should not crash and should average only the valid numeric values.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- It says the function averages only the remaining values, but the denominator still includes `None`, so the result can be wrong.
- It claims mixed types are handled safely, but `float(v)` can still raise on invalid inputs.
- It doesn’t mention the division-by-zero case for empty input or when no valid values exist.

### Rewritten explanation
- This function computes the average using only numeric values, skipping `None` and ignoring anything that can’t be converted to a float. If there are no valid measurements, it returns `0.0` to avoid division errors.

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

- Decision: Request Changes
- Justification: The original implementation can produce incorrect averages and may fail on common cases like empty input or non-numeric values.
- Confidence & unknowns: High confidence. How to handle special float values such as `NaN` or `inf` may depend on domain-specific requirements.