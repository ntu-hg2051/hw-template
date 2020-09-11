# GitHub Classroom Autograded Homework Template

This is a template for autograded homework assignments for GitHub
Classroom. This example is for Python coding assignments using Pytest for autograding.

## Instructions for Teachers

1. Create a new homework assignment using this as the template
   - It may be a private repository on GitHub

2. Clone the new assignment locally

3. Add skeleton code
   - Edit or replace `hw.py`
   - Modify `requirements.txt` as necessary
   - Edit `.github/workflows/classroom.yml` with any necessary build
     steps (e.g., downloading data). For instance:

     ```diff
               run: |
                 python -m pip install -r requirements.txt
     +           python -m nltk.downloader gutenberg
     ```

4. Add tests
   - Edit or replace `hw_test.py`; make sure the filename begins with
     `test_` or ends with `_test.py`
   - Edit `.github/classroom/autograding.json` and add the tests you want
     to run when students push submissions
     - Modify the test script parameters to select specific tests
     - Assign points to be awarded if the test passes

5. Edit this `README.md` file to contain only student instructions

6. Push to GitHub

## Example Instructions for Students

You are to edit `hw.py` and fix all the places with `TODO` comments so
the tests pass. Also answer the question at the bottom of this file.

When you are satisfied with your solution and answer, commit your
changes and push them to GitHub.

### Question

From the tests, you can see that the function works with integers as
well as strings. What are some other Python types that work with the
function, and what are some that do not? You might consider `float`,
`tuple`, `set`, `list`, or `bool` types, for example.

**Answer:**

Enter your answer here.
