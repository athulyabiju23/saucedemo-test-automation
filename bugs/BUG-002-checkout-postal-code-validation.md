# BUG-002: Checkout Accepts Invalid Postal Codes Without Format Validation

## Summary
The saucedemo checkout form accepts any string in the postal code field, including non-numeric values, single characters, and overly long strings. There is no client-side or apparent server-side validation of postal code format.

## Severity
**Medium** — Data quality issue. Real e-commerce shipping would fail with invalid postal codes.

## Priority
**P2** — Should be fixed before a real launch.

## Environment
- **URL:** https://www.saucedemo.com/checkout-step-one.html
- **Browser:** Chrome 124+
- **OS:** macOS 14.4
- **User:** standard_user

## Steps to Reproduce
1. Log in as `standard_user` with password `secret_sauce`
2. Add any product to cart and proceed to checkout
3. Fill First Name: `Test`, Last Name: `User`
4. In Postal Code field, enter: `abc`
5. Click Continue

## Expected Result
Form should reject invalid postal codes with a clear error message such as "Please enter a valid postal code."

## Actual Result
Form accepts any non-empty string and proceeds to checkout overview page successfully.

## Test Data Tested
| Input | Result |
|-------|--------|
| `abc` | Accepted ❌ |
| `!` | Accepted ❌ |
| `00000` | Accepted ⚠️ |
| `123456789012345` | Accepted ❌ |
| Empty | Rejected ✅ |

## Impact
- Real shipping integrations would fail downstream
- Data quality issues in customer database
- Potential injection vector if backend doesn't sanitize

## Recommendation
Add client-side validation regex matching standard US postal codes (5-digit or 5+4 format). Backend should also validate and sanitize before database storage.

## Discovered During
Exploratory testing while building checkout automation in `tests/test_cart_and_checkout.py`