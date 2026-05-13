# BUG-001: Cart Badge Not Displayed for Empty Cart Edge Cases

## Summary
On saucedemo.com, after adding and then removing all items from the cart, the shopping cart badge is removed entirely from the DOM. This creates an ambiguous state for QA automation — the badge element exists in some states and is removed in others, requiring conditional checks.

## Severity
**Low** — Functional, not blocking. UX clarity concern.

## Priority
**P3** — Nice to fix in a future sprint.

## Environment
- **URL:** https://www.saucedemo.com/inventory.html
- **Browser:** Chrome 124+
- **OS:** macOS 14.4
- **User:** standard_user

## Steps to Reproduce
1. Log in as `standard_user` with password `secret_sauce`
2. On the inventory page, observe no cart badge is displayed (empty cart)
3. Click "Add to cart" on Sauce Labs Backpack
4. Observe cart badge appears showing "1"
5. Click "Remove" on the same product
6. Observe cart badge is removed entirely from DOM

## Expected Result
Cart badge should remain visible with "0" or transition consistently between states for predictable automation.

## Actual Result
Cart badge element is removed from the DOM when cart is empty, causing `NoSuchElementException` if automation assumes the badge always exists.

## Impact on Automation
Page Object Model `get_cart_count()` method must include conditional handling:

```python
def get_cart_count(self):
    if not self.is_displayed(self.CART_BADGE):
        return 0
    return int(self.get_text(self.CART_BADGE))
```

## Recommendation
Render the badge with "0" when cart is empty for predictable DOM state.

## Discovered During
Cart automation tests in `tests/test_cart_and_checkout.py::test_remove_item_from_cart`