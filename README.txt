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