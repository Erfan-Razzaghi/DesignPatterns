# MkDocs Cheat Sheet

This is a comprehensive reference guide for writing documentation using MkDocs with Material theme.

## Best Practices

1. **File Organization**: Use clear, descriptive filenames and organize content in logical folders
2. **Cross-References**: Use relative links for internal pages: `[Link](../other-section/page.md)`
3. **Images**: Store images in an `img/` folder within each section
4. **Consistency**: Use consistent formatting and structure across all documentation
5. **TOC**: Use proper heading hierarchy (H1 → H2 → H3) for automatic table of contents generation


## Basic Markdown Syntax

### Headers
```markdown
# H1 Header
## H2 Header
### H3 Header
#### H4 Header
##### H5 Header
###### H6 Header
```

### Text Formatting
```markdown
**Bold text**
*Italic text*
***Bold and italic***
~~Strikethrough~~
`Inline code`
```

### Lists
```markdown
- Unordered list item 1
- Unordered list item 2
  - Nested item
  - Another nested item

1. Ordered list item 1
2. Ordered list item 2
   1. Nested numbered item
   2. Another nested numbered item
```

### Links and Images
```markdown
[Link text](https://example.com)
[Internal link](../other-page.md)
![Alt text](path/to/image.png)
![Alt text](path/to/image.png "Optional title")

<figure markdown="span">![Alt text](path/to/img.jpg){ width="500" }<figcaption>Optional caption</figcaption></figure>
```

### Tables
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

## Code Blocks

### Basic Code Block
````markdown
```
Plain code block
```
````

### Language-Specific Code Blocks
````markdown
```python
def hello_world():
    print("Hello, World!")
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-config
```

```bash
#!/bin/bash
echo "Hello, World!"
```
````

### Code Block with Title
````markdown
```python title="main.py"
def main():
    print("Hello from main!")
```
````

```python title="main.py"
def main():
    print("Hello from main!")
```

### Code Block with Line Numbers
````markdown
```python linenums="1"
def calculate_sum(a, b):
    return a + b

result = calculate_sum(5, 3)
print(f"Result: {result}")
```
````

```python linenums="1"
def calculate_sum(a, b):
    return a + b

result = calculate_sum(5, 3)
print(f"Result: {result}")
```

### Code Block with Highlighting
````markdown
```python hl_lines="2 3"
def example_function():
```
````
```python hl_lines="2 3"
def example_function():
    important_line = "This line is highlighted"
    another_important_line = "This too"
    regular_line = "This is not highlighted"
```


## Admonitions (Callout Boxes)

### Basic Admonitions
```markdown
!!! note
    This is a note admonition.

!!! note "Custom Title"
    This is a note with a custom title.
```

### All Admonition Types

!!! note "Note Example"
    This is a general note with important information. (`!!! note`)

!!! tip "Helpful Tip"
    This provides helpful tips and suggestions for better implementation.  (`!!! tip`)

!!! info "Information"
    This contains informational content without a custom title.  (`!!! info`)

!!! warning "Warning Message"
    This warns about potential issues or important considerations.  (`!!! warning`)

!!! danger "Critical Alert"
    This indicates dangerous situations or critical errors.  (`!!! danger`)

!!! success "Success Message"
    This indicates successful operations or positive outcomes.  (`!!! success`)

!!! failure "Failure Notice"
    This indicates failed operations or negative outcomes.  (`!!! failure`)

!!! bug "Bug Report"
    This highlights known bugs or issues in the system.  (`!!! bug`)

!!! example "Code Example"
    (`!!! exmaple`)
    ```json
    {
      "rsname": "admin-resource",
      "scopes": ["READ", "WRITE"]
    }
    ```

!!! quote "Important Quote"
    "One resource must appear in only one Resource-based permission."  (`!!! quote`)

!!! abstract "Summary"
    This provides a brief summary or abstract of key concepts.  (`!!! abstract`)

!!! todo "To-Do Item"
    - (`!!! todo`)
    - Implement additional validation
    - Update documentation
    - Test with multiple clients

!!! question "Frequently Asked Question"
    (`!!! question`)
    **Q:** Can I mix Resource-based and Scope-based permissions?
    **A:** No, choose one model per resource to avoid conflicts.

### Collapsible Admonitions
```markdown
??? note "Collapsible Note"
    This content is hidden by default and can be expanded.
```

??? note "Collapsible Note"
    This content is hidden by default and can be expanded.

```markdown
???+ tip "Expanded by Default"
    This content is expanded by default but can be collapsed.
```

???+ tip "Expanded by Default"
    This content is expanded by default but can be collapsed.

## Content Tabs

### Syntax
```markdown
=== "Tab 1"
    Content for tab 1

=== "Tab 2"
    Content for tab 2

=== "Tab 3"
    Content for tab 3
```

### Example
=== "Production"
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: api-server
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: api-server
    ```

=== "Staging"
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: api-server
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: api-server
    ```

=== "Development"
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: api-server
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: api-server
    ```

## Keyboard Keys

```markdown
++ctrl+alt+delete++
++cmd+c++
++enter++
++tab++
```

Result: ++ctrl+alt+delete++ ++cmd+c++ ++enter++ ++tab++

## Footnotes

### Syntax
```markdown
Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

### Example
MkDocs supports many extensions[^mkdocs] and is highly customizable[^material]. The Material theme[^material-theme] provides additional features for documentation.

[^mkdocs]: MkDocs is a fast, simple static site generator for documentation.
[^material]: Material for MkDocs extends the base theme with many useful features.
[^material-theme]: Available at https://squidfunk.github.io/mkdocs-material/

## Task Lists

### Syntax
```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another incomplete task
```

### Example
#### Project Setup Checklist
- [x] Initialize repository
- [x] Set up CI/CD pipeline
- [x] Configure development environment
- [ ] Write unit tests
- [ ] Add integration tests

## Metadata (Front Matter)

```yaml
---
title: Page Title
description: Page description for SEO
tags:
  - tag1
  - tag2
hide:
  - navigation
  - toc
---
```

## Advanced Features

### HTML in Markdown

You can embed HTML directly in your markdown:

```html
<div style="background-color: #af6e6eff; padding: 10px; border-radius: 5px;">
  <strong>Custom styled content</strong>
  <p>This content uses custom HTML styling.</p>
</div>
```

Result:
<div style="background-color: #af7474ff; padding: 10px; border-radius: 5px;">
  <strong>Custom styled content</strong>
  <p>This content uses custom HTML styling.</p>
</div>

### Progress Bars

```markdown
<div style="background-color: #e0e0e0; border-radius: 10px; overflow: hidden;">
  <div style="background-color: #4caf50; height: 20px; width: 75%; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">
    75% Complete
  </div>
</div>
```

<div style="background-color: #e0e0e0; border-radius: 10px; overflow: hidden;">
  <div style="background-color: #4caf50; height: 20px; width: 75%; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">
    75% Complete
  </div>
</div>

### Badges

```markdown
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)
```

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)

## Quick Reference Table

| Element | Syntax | Example |
|---------|--------|---------|
| Bold | `**text**` | **bold text** |
| Italic | `*text*` | *italic text* |
| Code | `` `code` `` | `inline code` |
| Link | `[text](url)` | [link example](https://example.com) |
| Image | `![alt](url)` | ![alt text](https://via.placeholder.com/50) |
| Header | `## Header` | ## Sample Header |
| List | `- item` | • Bullet point |
| Checkbox | `- [x] done` | ☑ Completed task |
| Quote | `> quote` | > Blockquote text |