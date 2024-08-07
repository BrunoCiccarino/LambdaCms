# Contribute

Thank you for considering contributing to our project! Below you will find information on how you can contribute efficiently and productively. Please follow these guidelines to ensure your contributions are well received and the onboarding process goes smoothly.

## Code of Conduct

To ensure a respectful and productive collaboration environment, we ask that all contributors follow our Code of Conduct. This code sets expectations for behavior and communication in our development community. If you notice any behavior that does not comply with our code of conduct, please contact the project maintainers.

## How to contribute

1. Review Before Committing

Before submitting a pull request, be sure to check the code carefully. Check that:

The code follows the style guidelines: Use the formatting and style established in the project.
Code is documented: Add comments and documentation where necessary to ensure the code is explained. No syntax or execution errors: Verify that the code compiles and runs without errors.

2. Run Tests

Before pushing your changes, run all tests to ensure your contribution doesn't break existing functionality. Follow the steps below to ensure the tests run correctly:

## Install Dependencies: Make sure all project dependencies are installed.

```pip install -r requirements.txt```

Run Tests: Run the tests to check that everything is working as expected.

```python manage.py test```

If new tests are completed, check that they are covering all necessary cases and pass successfully. If running your tests finds failures, fix the issues before submitting your pull request.

## Project Tree

```
/LambdaCms/
    manage.py
    /api/
        __init__.py
        settings.py
        urls.py
        middleware.py
        wsgi.py
    /posts/
        __init__.py
        admin.py
        apps.py
        models.py
        permissions.py
        post_owner.py
        serializers.py
        views.py
```