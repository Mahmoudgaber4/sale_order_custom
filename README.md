# Sale Order Custom
## add new features into sale_order model
#### 1- Fields:
- Add check (Boolean) and unit_check (Date) to sale.order.
#### 2- State:
- Add a new state, unit_confirm, to the order workflow.
#### 3- Button:
- Add a change_unit button to update the state to unit_confirm.
#### 4- Visibility:
- Hide change_unit and unit_check if check is False.
#### 5- Validation:
- Show an error if unit_check > expiration_date.
