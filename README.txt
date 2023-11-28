1. Start with blank Flask app, from Flask Quickstart
2. Install Bootstrap
3. Flask Jinja templates: base.html
4. Static files: Make `static_url` utility processor
5. Create local in-memory `db` variable

6. Create Posts route, render posts
7. Render comments with nested queries: `{% set comment = comments | selectattr("id", "==", comment_id) | list | first %}`
8. Macros: `render_comment`
9. Put db in utility_processor for global access
10. Put active_nav in utility_processor to toggle nav active class

11. Install HTMX and make `edit_post` route.
12. "Edit Post" buttons should update post contents to a form
13. Complete functionality and API route for "Cancel" button in Edit Post form

14. Complete functionality and API route for "Edit Post" > "Submit".

15. Partially complete functionality for "Delete Post" (pending delete confirmation)

16. New Post functionality
17. HX-Trigger headers: Reset new form after submit
18. Inline validation

Todo:
- MongoDB
- Flask Auth (with Protected Routes, sessions, etc)
- Flask Blueprints
- Flask forms?

Snippets:
```
{% macro render_comment(db, comment_id) %}
  {% set comment = db['comments'] | selectattr("id", "==", comment_id) | list | first %}
  <p class="fs-6 mb-0">{{comment.text}}</p>
{% endmacro %}
```