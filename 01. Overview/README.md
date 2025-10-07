# Objects are Passed by Reference

## Overview

This example demonstrates the fundamental concept that **objects in Python are passed by reference**.

## What This Means

When you pass an object to a function, you're not passing a copy of the object. Instead, you're passing a reference to the same object in memory. This means that any modifications made to the object inside the function will affect the original object.

## Example Demonstration

The `example_objects_passed_by_ref.py` file shows this concept by:

1. Creating a `Person` object with initial values
2. Passing it to a function that modifies its attributes
3. Showing that the original object is changed after the function call

## Key Takeaway

Objects are **mutable** and when passed to functions, changes made inside the function persist outside the function because both variables point to the same object in memory.