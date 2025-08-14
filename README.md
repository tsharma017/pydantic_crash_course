# Pydantic Examples

This repository contains Python examples demonstrating how to use **Pydantic** for data validation, serialization, and nested model handling.

## Files Overview

### 1. **Basic Model with Validation** (`pydantic_test.py`)
- Defines a `Patient` model with multiple field types (`str`, `EmailStr`, `AnyUrl`, `int`, `float`, `bool`, `list`, `dict`).
- Key features:
  - **Field constraints** (`max_length`, `gt`, `lt`, `strict`, `max_items`).
  - **Field validators** with `@field_validator` for domain-specific checks (e.g., restricting email domain, transforming names to uppercase, validating age range).
  - **Model-level validators** with `@model_validator` for cross-field validation (e.g., requiring an emergency contact if age > 60).
  - **Computed fields** (`@computed_field`) to calculate BMI from `weight` and `height`.
- Demonstrates **type coercion** and **automatic validation** when creating model instances.

---

### 2. **Nested Models** (`nested_models.py`)
- Shows how to embed one Pydantic model inside another.
- Example:
  ```python
  class Address(BaseModel):
      city: str
      state: str
      pin: str

  class Patient(BaseModel):
      name: str
      gender: str
      age: int
      address: Address
  ```
- Pydantic automatically parses nested dictionaries into model instances.

---

### 3. **Serialization** (`serialization.py`)
- Demonstrates converting Pydantic models to:
  - **Dictionaries** (`model_dump()`)
  - **JSON strings** (`model_dump_json()`)
- Useful for APIs, file storage, or database operations.

---

## 🚀 Key Pydantic Features Covered
- Type validation and coercion
- Field constraints (`gt`, `lt`, `max_length`, etc.)
- Built-in types (`EmailStr`, `AnyUrl`)
- Nested models
- Field and model validators
- Computed fields
- Serialization to dict/JSON

---


## Requirements
- Python 3.10+
- Pydantic v2+
- Install dependencies:
```bash
pip install 'pydantic[email]'
```

---

## **Basic Concepts**

**Q:** What is Pydantic and why is it used?  
**A:** Pydantic is a Python library for data validation and settings management using Python type hints. It ensures data integrity by validating input against type annotations.

**Q:** How does Pydantic perform data validation?  
**A:** It uses Python type hints and validators to parse and validate data before creating model instances.

**Q:** How does Pydantic differ from `dataclasses`?  
**A:** `dataclasses` provide structure only, while Pydantic adds automatic type conversion, validation, and error handling.

---

## **Field Validation**

**Q:** How do you enforce constraints like `max_length` or `gt`?  
**A:** Use `Field()` with parameters, e.g., `Field(gt=0, max_length=50)`.

**Q:** Difference between `@field_validator` and `@model_validator`?  
**A:** `@field_validator` validates a single field; `@model_validator` validates the whole model or multiple fields together.

**Q:** How do you validate multiple fields together?  
**A:** Use `@model_validator` (v2) or `@root_validator` (v1).

---

## **Type Handling**

**Q:** What happens if you pass a string instead of an integer?  
**A:** Pydantic will attempt type coercion; if it fails, it raises a `ValidationError`.

**Q:** How does Pydantic handle optional fields?  
**A:** Use `Optional[type]` or `Field(default=None)`.

---

## **Advanced Features**

**Q:** How do nested models work?  
**A:** You can declare a model as a field type in another model; Pydantic auto-parses nested dicts into model instances.

**Q:** What is a computed field?  
**A:** A read-only field calculated from other fields in the model using `@computed_field`.

**Q:** How do you create custom validators?  
**A:** Use `@field_validator` or `@model_validator` to write custom logic.

---

## **Serialization**

**Q:** How do you convert a Pydantic model to JSON?  
**A:** Use `.model_dump_json()` in v2 or `.json()` in v1.

**Q:** Difference between `.model_dump()` and `.model_dump_json()`?  
**A:** `.model_dump()` returns a Python dict; `.model_dump_json()` returns a JSON string.

---

## **Performance and Versioning**

**Q:** Performance considerations?  
**A:** Pydantic is fast but validation adds overhead; avoid excessive nested validations for performance-critical paths.

**Q:** Key differences between v1 and v2?  
**A:** v2 uses `pydantic-core` for speed, changes validators (`validator` → `field_validator`, `root_validator` → `model_validator`), and adds `@computed_field`.
